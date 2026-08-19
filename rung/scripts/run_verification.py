#!/usr/bin/env python3
"""Run an explicit JSON verification plan without invoking a shell."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


def utc_now() -> str:
    return datetime.now(UTC).isoformat()


def truncate(text: str | bytes | None, limit: int) -> tuple[str, bool]:
    if text is None:
        return "", False
    if isinstance(text, bytes):
        text = text.decode(errors="replace")
    if len(text) <= limit:
        return text, False
    half = max(1, limit // 2)
    marker = "\n... output truncated by Rung ...\n"
    return text[:half] + marker + text[-half:], True


def git_revision(root: Path) -> str | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None
    return result.stdout.strip() if result.returncode == 0 else None


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
    return plan


def resolve_working_directory(project: Path, raw_cwd: str) -> Path:
    candidate = (project / raw_cwd).resolve()
    try:
        candidate.relative_to(project)
    except ValueError as exc:
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
    if not isinstance(command, list) or not command or not all(isinstance(v, str) for v in command):
        raise ValueError(f"Check {index} command must be a non-empty string array")
    if any("{{" in value for value in command):
        raise ValueError(f"Check {index} command contains an unresolved placeholder")

    timeout = raw.get("timeout_seconds", 300)
    if not isinstance(timeout, int) or not 1 <= timeout <= 86_400:
        raise ValueError(f"Check {index} timeout_seconds must be between 1 and 86400")
    cwd = raw.get("cwd", ".")
    if not isinstance(cwd, str):
        raise ValueError(f"Check {index} cwd must be a string")

    return {
        "name": name.strip(),
        "claim": raw.get("claim"),
        "tier": raw.get("tier"),
        "command": command,
        "cwd": resolve_working_directory(project, cwd),
        "cwd_display": cwd,
        "timeout_seconds": timeout,
    }


def execute_check(check: dict[str, Any], max_output_chars: int) -> dict[str, Any]:
    started_at = utc_now()
    started = time.monotonic()
    try:
        result = subprocess.run(
            check["command"],
            cwd=check["cwd"],
            check=False,
            capture_output=True,
            text=True,
            timeout=check["timeout_seconds"],
        )
        status = "pass" if result.returncode == 0 else "fail"
        return_code: int | None = result.returncode
        stdout, stdout_truncated = truncate(result.stdout, max_output_chars)
        stderr, stderr_truncated = truncate(result.stderr, max_output_chars)
        message = None
    except FileNotFoundError as exc:
        status = "blocked"
        return_code = None
        stdout, stdout_truncated = "", False
        stderr, stderr_truncated = "", False
        message = str(exc)
    except subprocess.TimeoutExpired as exc:
        status = "blocked"
        return_code = None
        stdout, stdout_truncated = truncate(exc.stdout, max_output_chars)
        stderr, stderr_truncated = truncate(exc.stderr, max_output_chars)
        message = f"Timed out after {check['timeout_seconds']} seconds"

    return {
        "name": check["name"],
        "claim": check["claim"],
        "tier": check["tier"],
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
    parser.add_argument("--max-output-chars", type=int, default=20_000)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project = Path(args.project).expanduser().resolve()
    if not project.is_dir():
        print(json.dumps({"status": "error", "message": f"Project directory not found: {project}"}))
        return 2
    if args.max_output_chars < 100:
        print(json.dumps({"status": "error", "message": "--max-output-chars must be at least 100"}))
        return 2

    try:
        plan_path = Path(args.plan).expanduser().resolve()
        plan = load_plan(plan_path)
        checks = [
            validate_check(raw, index, project)
            for index, raw in enumerate(plan["checks"], 1)
        ]
    except ValueError as exc:
        print(json.dumps({"status": "error", "message": str(exc)}, ensure_ascii=False))
        return 2

    started_at = utc_now()
    results = [execute_check(check, args.max_output_chars) for check in checks]
    statuses = {result["status"] for result in results}
    overall = "fail" if "fail" in statuses else "blocked" if "blocked" in statuses else "pass"
    evidence = {
        "schema_version": 1,
        "run_id": plan.get("run_id"),
        "project_root": str(project),
        "plan": str(plan_path),
        "planned_revision": plan.get("revision"),
        "observed_revision": git_revision(project),
        "started_at": started_at,
        "finished_at": utc_now(),
        "status": overall,
        "checks": results,
    }
    payload = json.dumps(evidence, ensure_ascii=False, indent=2) + "\n"
    if args.output == "-":
        sys.stdout.write(payload)
    else:
        output = Path(args.output).expanduser().resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload, encoding="utf-8")

    return {"pass": 0, "fail": 1, "blocked": 2}[overall]


if __name__ == "__main__":
    raise SystemExit(main())
