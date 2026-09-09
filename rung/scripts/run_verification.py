#!/usr/bin/env python3
"""Run an explicit JSON verification plan without invoking a shell."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import signal
import subprocess
import sys
import threading
import time
from contextlib import suppress
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from project_state import capture_project_state, revision_matches_state


def utc_now() -> str:
    return datetime.now(UTC).isoformat()


class BoundedCapture:
    """Keep bounded head and tail bytes while draining a process stream."""

    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.head_limit = max(1, limit // 2)
        self.tail_limit = max(1, limit - self.head_limit)
        self.head = bytearray()
        self.tail = bytearray()
        self.total = 0

    def append(self, chunk: bytes) -> None:
        self.total += len(chunk)
        head_remaining = self.head_limit - len(self.head)
        if head_remaining > 0:
            self.head.extend(chunk[:head_remaining])
            chunk = chunk[head_remaining:]
        if chunk:
            self.tail.extend(chunk)
            if len(self.tail) > self.tail_limit:
                del self.tail[: len(self.tail) - self.tail_limit]

    def render(self) -> tuple[str, bool]:
        truncated = self.total > self.limit
        if truncated:
            captured = bytes(self.head) + b"\n... output truncated by Rung ...\n" + bytes(
                self.tail
            )
        else:
            captured = bytes(self.head) + bytes(self.tail)
        return captured.decode(errors="replace"), truncated


def drain_stream(stream: Any, capture: BoundedCapture) -> None:
    try:
        for chunk in iter(lambda: stream.read(8192), b""):
            capture.append(chunk)
    finally:
        stream.close()


def terminate_process_tree(process: subprocess.Popen[bytes]) -> None:
    if os.name == "posix":
        try:
            os.killpg(process.pid, signal.SIGTERM)
        except ProcessLookupError:
            return
        with suppress(subprocess.TimeoutExpired):
            process.wait(timeout=2)
        with suppress(ProcessLookupError):
            os.killpg(process.pid, signal.SIGKILL)
        if process.poll() is None:
            process.wait()
        return

    if process.poll() is None:
        process.terminate()
        try:
            process.wait(timeout=2)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait()


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return f"sha256:{digest.hexdigest()}"


def display_path(project: Path, path: Path) -> str:
    try:
        return path.relative_to(project).as_posix()
    except ValueError:
        return str(path)


def load_plan(path: Path) -> dict[str, Any]:
    try:
        plan = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ValueError(f"Cannot read verification plan: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid verification plan JSON: {exc}") from exc
    if not isinstance(plan, dict) or not isinstance(plan.get("checks"), list):
        raise ValueError("Verification plan must contain a checks array")
    if not plan["checks"]:
        raise ValueError("Verification plan contains no checks")
    if "{{" in json.dumps(plan, ensure_ascii=False):
        raise ValueError("Verification plan contains unresolved template placeholders")
    if plan.get("schema_version") != 2:
        raise ValueError("Verification plan schema_version must be 2")
    if "run_id" in plan and (
        not isinstance(plan["run_id"], str) or not plan["run_id"].strip()
    ):
        raise ValueError("Verification plan run_id must be a non-empty string")
    if "revision" in plan and (
        not isinstance(plan["revision"], str) or not plan["revision"].strip()
    ):
        raise ValueError("Verification plan revision must be a non-empty string")
    return plan


def resolve_working_directory(project: Path, raw_cwd: str) -> Path:
    candidate = (project / raw_cwd).resolve()
    try:
        candidate.relative_to(project)
    except (OSError, ValueError) as exc:
        raise ValueError(f"Check working directory escapes project root: {raw_cwd}") from exc
    if not candidate.is_dir():
        raise ValueError(f"Check working directory not found: {raw_cwd}")
    return candidate


def validate_check(raw: Any, index: int, project: Path) -> dict[str, Any]:
    if not isinstance(raw, dict):
        raise ValueError(f"Check {index} must be an object")
    name = raw.get("name")
    command = raw.get("command")
    if not isinstance(name, str) or not name.strip():
        raise ValueError(f"Check {index} requires a non-empty name")
    if (
        not isinstance(command, list)
        or not command
        or not all(isinstance(value, str) and value for value in command)
    ):
        raise ValueError(f"Check {index} command must be a non-empty string array")
    if any("{{" in value for value in command):
        raise ValueError(f"Check {index} command contains an unresolved placeholder")

    claim = raw.get("claim")
    if not isinstance(claim, str) or not claim.strip():
        raise ValueError(f"Check {index} requires a non-empty claim")

    tier = raw.get("tier")
    if isinstance(tier, bool) or not isinstance(tier, int) or not 0 <= tier <= 3:
        raise ValueError(f"Check {index} tier must be an integer between 0 and 3")
    required_for_release = raw.get("required_for_release")
    if not isinstance(required_for_release, bool):
        raise ValueError(f"Check {index} required_for_release must be a boolean")

    timeout = raw.get("timeout_seconds", 300)
    if isinstance(timeout, bool) or not isinstance(timeout, int) or not 1 <= timeout <= 86_400:
        raise ValueError(f"Check {index} timeout_seconds must be between 1 and 86400")
    cwd = raw.get("cwd", ".")
    if not isinstance(cwd, str):
        raise ValueError(f"Check {index} cwd must be a string")

    return {
        "name": name.strip(),
        "claim": claim.strip(),
        "tier": tier,
        "required_for_release": required_for_release,
        "command": command,
        "cwd": resolve_working_directory(project, cwd),
        "cwd_display": cwd,
        "timeout_seconds": timeout,
    }


def execute_check(check: dict[str, Any], max_output_bytes: int) -> dict[str, Any]:
    started_at = utc_now()
    started = time.monotonic()
    stdout_capture = BoundedCapture(max_output_bytes)
    stderr_capture = BoundedCapture(max_output_bytes)
    process: subprocess.Popen[bytes] | None = None
    output_threads: list[threading.Thread] = []
    try:
        process = subprocess.Popen(
            check["command"],
            cwd=check["cwd"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            start_new_session=os.name == "posix",
        )
        assert process.stdout is not None
        assert process.stderr is not None
        output_threads = [
            threading.Thread(
                target=drain_stream, args=(process.stdout, stdout_capture), daemon=True
            ),
            threading.Thread(
                target=drain_stream, args=(process.stderr, stderr_capture), daemon=True
            ),
        ]
        for thread in output_threads:
            thread.start()
        process.wait(timeout=check["timeout_seconds"])
        for thread in output_threads:
            thread.join(timeout=2)
        if any(thread.is_alive() for thread in output_threads):
            terminate_process_tree(process)
            for thread in output_threads:
                thread.join(timeout=2)
            status = "blocked"
            return_code = None
            message = "Output streams remained open after the command exited"
        else:
            status = "pass" if process.returncode == 0 else "fail"
            return_code = process.returncode
            message = None
    except FileNotFoundError as exc:
        status = "blocked"
        return_code = None
        message = str(exc)
    except subprocess.TimeoutExpired:
        assert process is not None
        terminate_process_tree(process)
        for thread in output_threads:
            thread.join(timeout=2)
        status = "blocked"
        return_code = None
        message = f"Timed out after {check['timeout_seconds']} seconds"
    except OSError as exc:
        if process is not None:
            terminate_process_tree(process)
        for thread in output_threads:
            thread.join(timeout=2)
        status = "blocked"
        return_code = None
        message = str(exc)

    stdout, stdout_truncated = stdout_capture.render()
    stderr, stderr_truncated = stderr_capture.render()

    return {
        "name": check["name"],
        "claim": check["claim"],
        "tier": check["tier"],
        "required_for_release": check["required_for_release"],
        "command": check["command"],
        "cwd": check["cwd_display"],
        "status": status,
        "return_code": return_code,
        "started_at": started_at,
        "duration_seconds": round(time.monotonic() - started, 6),
        "stdout": stdout,
        "stderr": stderr,
        "stdout_truncated": stdout_truncated,
        "stderr_truncated": stderr_truncated,
        "message": message,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", default=".", help="Project root")
    parser.add_argument("--plan", required=True, help="Verification plan JSON")
    parser.add_argument("--output", default="-", help="Evidence JSON path, or - for stdout")
    parser.add_argument(
        "--max-tier",
        type=int,
        default=3,
        help="Execute checks at or below this verification tier (0-3)",
    )
    parser.add_argument(
        "--max-output-bytes",
        "--max-output-chars",
        dest="max_output_bytes",
        type=int,
        default=20_000,
        help="Maximum captured bytes per output stream",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project = Path(args.project).expanduser().resolve()
    if not project.is_dir():
        print(json.dumps({"status": "error", "message": f"Project directory not found: {project}"}))
        return 2
    if args.max_output_bytes < 100:
        print(json.dumps({"status": "error", "message": "--max-output-bytes must be at least 100"}))
        return 2
    if not 0 <= args.max_tier <= 3:
        print(json.dumps({"status": "error", "message": "--max-tier must be between 0 and 3"}))
        return 2

    try:
        plan_path = Path(args.plan).expanduser().resolve()
        plan = load_plan(plan_path)
        checks = [
            validate_check(raw, index, project)
            for index, raw in enumerate(plan["checks"], 1)
        ]
        names = [check["name"] for check in checks]
        if len(names) != len(set(names)):
            raise ValueError("Verification plan check names must be unique")
        selected_checks = [check for check in checks if check["tier"] <= args.max_tier]
        skipped_checks = [check for check in checks if check["tier"] > args.max_tier]
        if not selected_checks:
            raise ValueError(
                f"Verification plan has no checks at or below tier {args.max_tier}"
            )
        output_path = (
            None if args.output == "-" else Path(args.output).expanduser().resolve()
        )
        state_exclusions: list[Path] = [plan_path]
        if output_path is not None:
            state_exclusions.append(output_path)
        target_state = capture_project_state(
            project, excluded_paths=state_exclusions
        )
        planned_revision = plan.get("revision")
        planned_revision_match = (
            None
            if planned_revision is None
            else revision_matches_state(project, planned_revision, target_state)
        )
        if planned_revision_match is False:
            raise ValueError(
                "Verification plan revision does not identify the current project state: "
                f"expected {planned_revision}, observed {target_state['identity']}"
            )
        initial_plan_sha256 = file_sha256(plan_path)
    except (OSError, ValueError) as exc:
        print(json.dumps({"status": "error", "message": str(exc)}, ensure_ascii=False))
        return 2

    started_at = utc_now()
    results = [execute_check(check, args.max_output_bytes) for check in selected_checks]
    try:
        final_state = capture_project_state(project, excluded_paths=state_exclusions)
        final_plan_sha256 = file_sha256(plan_path)
    except (OSError, ValueError) as exc:
        print(
            json.dumps(
                {"status": "error", "message": f"Cannot capture final project state: {exc}"},
                ensure_ascii=False,
            )
        )
        return 2
    state_stable = (
        target_state["identity"] == final_state["identity"]
        and initial_plan_sha256 == final_plan_sha256
    )
    applicability_reasons: list[str] = []
    if target_state["identity"] != final_state["identity"]:
        applicability_reasons.append("project state changed while verification was running")
    if initial_plan_sha256 != final_plan_sha256:
        applicability_reasons.append("verification plan changed while verification was running")
    statuses = {result["status"] for result in results}
    overall = (
        "fail"
        if "fail" in statuses
        else "blocked"
        if "blocked" in statuses or not state_stable
        else "pass"
    )
    evidence = {
        "schema_version": 2,
        "run_id": plan.get("run_id"),
        "project_root": str(project),
        "plan": display_path(project, plan_path),
        "plan_sha256": initial_plan_sha256,
        "planned_revision": planned_revision,
        "planned_revision_match": planned_revision_match,
        "target_state": target_state,
        "final_state": final_state,
        "state_stable": state_stable,
        "applicability": {
            "status": "pass" if state_stable else "blocked",
            "reasons": applicability_reasons,
        },
        "requested_max_tier": args.max_tier,
        "max_output_bytes": args.max_output_bytes,
        "planned_check_count": len(checks),
        "selected_check_count": len(selected_checks),
        "skipped_checks": [
            {
                "name": check["name"],
                "claim": check["claim"],
                "tier": check["tier"],
                "required_for_release": check["required_for_release"],
                "reason": f"tier exceeds requested maximum {args.max_tier}",
            }
            for check in skipped_checks
        ],
        "started_at": started_at,
        "finished_at": utc_now(),
        "status": overall,
        "checks": results,
    }
    payload = json.dumps(evidence, ensure_ascii=False, indent=2) + "\n"
    if args.output == "-":
        sys.stdout.write(payload)
    else:
        assert output_path is not None
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(payload, encoding="utf-8")

    return {"pass": 0, "fail": 1, "blocked": 2}[overall]


if __name__ == "__main__":
    raise SystemExit(main())
