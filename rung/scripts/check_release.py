#!/usr/bin/env python3
"""Validate Rung's Release Manifest and the applicability of its evidence."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import subprocess
import sys
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlparse

from project_state import capture_project_state, revision_matches_state

REQUIRED_KEYS = {
    "schema_version",
    "run_id",
    "version",
    "revision",
    "status",
    "artifacts",
    "acceptance",
    "verification",
    "documentation",
    "known_limitations",
    "unverified_risks",
    "publish_actions",
}

LIST_KEYS = {"artifacts", "known_limitations", "unverified_risks", "publish_actions"}
ALLOWED_STATUS = {"blocked", "ready", "published"}
EVIDENCE_STATUS = {"pass", "fail", "blocked"}
EVIDENCE_REQUIRED_KEYS = {
    "schema_version",
    "run_id",
    "project_root",
    "plan",
    "plan_sha256",
    "planned_revision",
    "planned_revision_match",
    "target_state",
    "final_state",
    "state_stable",
    "applicability",
    "requested_max_tier",
    "max_output_bytes",
    "planned_check_count",
    "selected_check_count",
    "skipped_checks",
    "started_at",
    "finished_at",
    "status",
    "checks",
}
CHECK_REQUIRED_KEYS = {
    "name",
    "claim",
    "tier",
    "required_for_release",
    "command",
    "cwd",
    "status",
    "return_code",
    "started_at",
    "duration_seconds",
    "stdout",
    "stderr",
    "stdout_truncated",
    "stderr_truncated",
    "message",
}
STATE_REQUIRED_KEYS = {
    "kind",
    "identity",
    "head_revision",
    "dirty",
    "fingerprint",
    "excluded_paths",
}
URI_PATTERN = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")
SHA256_PATTERN = re.compile(r"^sha256:[0-9a-f]{64}$")
PLACEHOLDER_PATTERN = re.compile(r"\{\{[^{}]+\}\}")
TOP_LEVEL_PATTERN = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?$")
LIST_ITEM_PATTERN = re.compile(r"^\s+-\s*(.*)$")


def parse_scalar(raw: str) -> Any:
    value = raw.strip()
    if value == "":
        return None
    if value in {"[]", "{}"}:
        return [] if value == "[]" else {}
    if value in {"true", "false", "null"}:
        return {"true": True, "false": False, "null": None}[value]
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    if value.startswith(('"', "'")) and value.endswith(value[0]):
        if value[0] == '"':
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return value[1:-1]
        return value[1:-1].replace("''", "'")
    return value


def parse_manifest(path: Path) -> dict[str, Any]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise ValueError(f"Cannot read manifest: {exc}") from exc

    result: dict[str, Any] = {}
    active_list: str | None = None
    for number, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped == "---":
            continue
        top_level = TOP_LEVEL_PATTERN.match(line)
        if top_level:
            key, raw = top_level.groups()
            if key in result:
                raise ValueError(f"Duplicate top-level key {key!r} at line {number}")
            parsed = parse_scalar(raw or "")
            if key in LIST_KEYS and parsed is None:
                parsed = []
                active_list = key
            else:
                active_list = None
            result[key] = parsed
            continue

        list_item = LIST_ITEM_PATTERN.match(line)
        if list_item and active_list:
            result[active_list].append(parse_scalar(list_item.group(1)))
            continue
        raise ValueError(f"Unsupported manifest syntax at line {number}: {line}")
    return result


def contains_placeholder(value: Any) -> bool:
    if isinstance(value, str):
        return bool(PLACEHOLDER_PATTERN.search(value))
    if isinstance(value, list):
        return any(contains_placeholder(item) for item in value)
    if isinstance(value, dict):
        return any(contains_placeholder(item) for item in value.values())
    return False


def git_revision_exists(project: Path, revision: str) -> bool | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(project), "cat-file", "-e", f"{revision}^{{commit}}"],
            check=False,
            capture_output=True,
            timeout=10,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None
    if result.returncode == 0:
        return True
    try:
        inside = subprocess.run(
            ["git", "-C", str(project), "rev-parse", "--is-inside-work-tree"],
            check=False,
            capture_output=True,
            timeout=10,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None
    return False if inside.returncode == 0 else None


def resolve_reference(
    project: Path, value: Any, label: str, problems: list[str]
) -> tuple[str, Path | None]:
    if not isinstance(value, str) or not value.strip():
        problems.append(f"{label} must be a non-empty string")
        return "invalid", None
    if value.startswith("file:"):
        path = Path(unquote(urlparse(value).path)).resolve()
    elif URI_PATTERN.match(value) and not Path(value).is_absolute():
        return "external", None
    else:
        raw_path = Path(value).expanduser()
        path = raw_path.resolve() if raw_path.is_absolute() else (project / raw_path).resolve()
    if not path.exists():
        problems.append(f"{label} not found: {value}")
        return "invalid", None
    return "local", path


def _is_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return f"sha256:{digest.hexdigest()}"


def project_relative(project: Path, path: Path) -> str | None:
    try:
        return path.resolve().relative_to(project.resolve()).as_posix()
    except ValueError:
        return None


def validate_state(value: Any, label: str, problems: list[str]) -> dict[str, Any] | None:
    if not isinstance(value, dict):
        problems.append(f"{label} must be an object")
        return None
    missing = sorted(STATE_REQUIRED_KEYS - value.keys())
    if missing:
        problems.append(f"{label} missing keys: {', '.join(missing)}")
    kind = value.get("kind")
    if not isinstance(kind, str) or kind not in {"git", "filesystem"}:
        problems.append(f"{label}.kind must be git or filesystem")
    identity = value.get("identity")
    if not isinstance(identity, str) or not identity.strip():
        problems.append(f"{label}.identity must be a non-empty string")
    fingerprint = value.get("fingerprint")
    if not isinstance(fingerprint, str) or not SHA256_PATTERN.fullmatch(fingerprint):
        problems.append(f"{label}.fingerprint must be a sha256 digest")
    exclusions = value.get("excluded_paths")
    if not isinstance(exclusions, list) or not all(
        isinstance(item, str)
        and item
        and not Path(item).is_absolute()
        and ".." not in Path(item).parts
        for item in exclusions
    ):
        problems.append(f"{label}.excluded_paths must contain safe relative paths")
    if kind == "git":
        head = value.get("head_revision")
        if head is not None and (not isinstance(head, str) or not head.strip()):
            problems.append(f"{label}.head_revision must be null or a non-empty string")
        if not isinstance(value.get("dirty"), bool):
            problems.append(f"{label}.dirty must be a boolean for Git state")
        elif value.get("dirty") is False and identity != head:
            problems.append(f"{label} clean Git identity must equal head_revision")
        elif value.get("dirty") is True and identity != f"git-worktree:{fingerprint}":
            problems.append(f"{label} dirty Git identity must match its fingerprint")
    elif kind == "filesystem":
        if value.get("head_revision") is not None or value.get("dirty") is not None:
            problems.append(
                f"{label} filesystem state must use null head_revision and dirty fields"
            )
        if identity != f"filesystem:{fingerprint}":
            problems.append(f"{label} filesystem identity must match its fingerprint")
    return value


def validate_check_result(value: Any, index: int, problems: list[str]) -> str | None:
    label = f"verification check {index}"
    if not isinstance(value, dict):
        problems.append(f"{label} must be an object")
        return None
    missing = sorted(CHECK_REQUIRED_KEYS - value.keys())
    if missing:
        problems.append(f"{label} missing keys: {', '.join(missing)}")
    name = value.get("name")
    claim = value.get("claim")
    status = value.get("status")
    return_code = value.get("return_code")
    if not isinstance(name, str) or not name.strip():
        problems.append(f"{label}.name must be a non-empty string")
    if not isinstance(claim, str) or not claim.strip():
        problems.append(f"{label}.claim must be a non-empty string")
    tier = value.get("tier")
    if not _is_int(tier) or not 0 <= tier <= 3:
        problems.append(f"{label}.tier must be an integer between 0 and 3")
    if not isinstance(value.get("required_for_release"), bool):
        problems.append(f"{label}.required_for_release must be a boolean")
    command = value.get("command")
    if not isinstance(command, list) or not command or not all(
        isinstance(item, str) for item in command
    ):
        problems.append(f"{label}.command must be a non-empty string array")
    if not isinstance(status, str) or status not in EVIDENCE_STATUS:
        problems.append(f"{label}.status must be pass, fail, or blocked")
        return None
    if status == "pass" and (not _is_int(return_code) or return_code != 0):
        problems.append(f"{label} pass status requires return_code 0")
    if status == "fail" and (
        not _is_int(return_code) or return_code == 0
    ):
        problems.append(f"{label} fail status requires a non-zero integer return_code")
    if status == "blocked" and return_code is not None:
        problems.append(f"{label} blocked status requires a null return_code")
    duration = value.get("duration_seconds")
    if (
        isinstance(duration, bool)
        or not isinstance(duration, (int, float))
        or not math.isfinite(duration)
        or duration < 0
    ):
        problems.append(f"{label}.duration_seconds must be a non-negative number")
    for field in ("cwd", "started_at"):
        if not isinstance(value.get(field), str) or not value[field].strip():
            problems.append(f"{label}.{field} must be a non-empty string")
    for field in ("stdout", "stderr"):
        if not isinstance(value.get(field), str):
            problems.append(f"{label}.{field} must be a string")
    for field in ("stdout_truncated", "stderr_truncated"):
        if not isinstance(value.get(field), bool):
            problems.append(f"{label}.{field} must be a boolean")
    if value.get("message") is not None and not isinstance(value.get("message"), str):
        problems.append(f"{label}.message must be a string or null")
    return status


def validate_verification_evidence(
    path: Path,
    project: Path,
    manifest_path: Path,
    manifest: dict[str, Any],
    problems: list[str],
) -> str:
    if path.suffix.lower() != ".json":
        problems.append("local verification evidence must be a JSON file")
        return "invalid"
    try:
        evidence = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        problems.append(f"cannot read verification evidence: {exc}")
        return "invalid"
    except json.JSONDecodeError as exc:
        problems.append(f"invalid verification evidence JSON: {exc}")
        return "invalid"
    if not isinstance(evidence, dict):
        problems.append("verification evidence must be a JSON object")
        return "invalid"
    missing = sorted(EVIDENCE_REQUIRED_KEYS - evidence.keys())
    if missing:
        problems.append("verification evidence missing keys: " + ", ".join(missing))
    if evidence.get("schema_version") != 2:
        problems.append("verification evidence schema_version must be 2")

    evidence_run_id = evidence.get("run_id")
    if not isinstance(evidence_run_id, str) or not evidence_run_id.strip():
        problems.append("verification evidence run_id must be a non-empty string")
    elif evidence_run_id != manifest.get("run_id"):
        problems.append("verification evidence run_id does not match the manifest")
    if not isinstance(evidence.get("project_root"), str) or not evidence[
        "project_root"
    ].strip():
        problems.append("verification evidence project_root must be a non-empty string")

    plan_path: Path | None = None
    plan_data: dict[str, Any] | None = None
    if not isinstance(evidence.get("plan"), str) or not evidence["plan"].strip():
        problems.append("verification evidence plan must be a non-empty string")
    else:
        raw_plan = Path(evidence["plan"]).expanduser()
        plan_path = (
            raw_plan.resolve()
            if raw_plan.is_absolute()
            else (project / raw_plan).resolve()
        )
        if not plan_path.is_file():
            problems.append("verification evidence plan file was not found")
        else:
            try:
                loaded_plan = json.loads(plan_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc:
                problems.append(f"cannot parse verification evidence plan: {exc}")
            else:
                if not isinstance(loaded_plan, dict):
                    problems.append("verification evidence plan must contain a JSON object")
                else:
                    plan_data = loaded_plan
    plan_digest = evidence.get("plan_sha256")
    if not isinstance(plan_digest, str) or not SHA256_PATTERN.fullmatch(plan_digest):
        problems.append("verification evidence plan_sha256 must be a sha256 digest")
    elif plan_path is not None and plan_path.is_file():
        try:
            observed_plan_digest = file_sha256(plan_path)
        except OSError as exc:
            problems.append(f"cannot read verification evidence plan: {exc}")
        else:
            if observed_plan_digest != plan_digest:
                problems.append("verification evidence plan digest does not match its file")

    for field in ("started_at", "finished_at"):
        if not isinstance(evidence.get(field), str) or not evidence[field].strip():
            problems.append(f"verification evidence {field} must be a non-empty string")

    checks = evidence.get("checks")
    check_statuses: list[str] = []
    check_names: list[str] = []
    if not isinstance(checks, list) or not checks:
        problems.append("verification evidence checks must be a non-empty array")
        checks = []
    for index, check in enumerate(checks, 1):
        status = validate_check_result(check, index, problems)
        if status:
            check_statuses.append(status)
        if isinstance(check, dict) and isinstance(check.get("name"), str):
            check_names.append(check["name"])
    if len(check_names) != len(set(check_names)):
        problems.append("verification evidence check names must be unique")

    evidence_status = evidence.get("status")
    evidence_status_valid = (
        isinstance(evidence_status, str) and evidence_status in EVIDENCE_STATUS
    )
    if not evidence_status_valid:
        problems.append("verification evidence status must be pass, fail, or blocked")
    expected_status = (
        "fail"
        if "fail" in check_statuses
        else "blocked"
        if "blocked" in check_statuses or not checks
        else "pass"
    )
    if evidence_status_valid and evidence_status != expected_status:
        problems.append(
            "verification evidence status is inconsistent with its check results"
        )
    if evidence_status != "pass":
        problems.append("verification evidence status must be pass for release readiness")

    selected_count = evidence.get("selected_check_count")
    planned_count = evidence.get("planned_check_count")
    skipped_checks = evidence.get("skipped_checks")
    if not _is_int(selected_count) or selected_count != len(checks):
        problems.append("verification evidence selected_check_count must match checks")
    if not isinstance(skipped_checks, list):
        problems.append("verification evidence skipped_checks must be an array")
        skipped_checks = []
    if not _is_int(planned_count) or planned_count != len(checks) + len(skipped_checks):
        problems.append(
            "verification evidence planned_check_count must equal selected and skipped checks"
        )
    requested_tier = evidence.get("requested_max_tier")
    if not _is_int(requested_tier) or not 0 <= requested_tier <= 3:
        problems.append(
            "verification evidence requested_max_tier must be an integer between 0 and 3"
        )
    max_output_bytes = evidence.get("max_output_bytes")
    if not _is_int(max_output_bytes) or max_output_bytes < 100:
        problems.append("verification evidence max_output_bytes must be at least 100")

    if plan_data is not None:
        if plan_data.get("schema_version") != 2:
            problems.append("verification evidence plan schema_version must be 2")
        if plan_data.get("run_id") != evidence_run_id:
            problems.append("verification evidence run_id does not match its plan")
        plan_checks = plan_data.get("checks")
        if not isinstance(plan_checks, list) or not plan_checks:
            problems.append("verification evidence plan checks must be a non-empty array")
        elif _is_int(requested_tier) and 0 <= requested_tier <= 3:
            valid_plan_checks = all(
                isinstance(check, dict)
                and _is_int(check.get("tier"))
                and 0 <= check["tier"] <= 3
                and isinstance(check.get("required_for_release"), bool)
                for check in plan_checks
            )
            if not valid_plan_checks:
                problems.append("verification evidence plan contains an invalid check")
            else:
                expected_selected = [
                    check for check in plan_checks if check["tier"] <= requested_tier
                ]
                expected_skipped = [
                    check for check in plan_checks if check["tier"] > requested_tier
                ]

                def plan_signature(check: dict[str, Any]) -> tuple[Any, ...]:
                    return (
                        check.get("name"),
                        check.get("claim"),
                        check.get("tier"),
                        check.get("required_for_release"),
                        check.get("command"),
                        check.get("cwd", "."),
                    )

                def evidence_signature(check: Any) -> tuple[Any, ...] | None:
                    if not isinstance(check, dict):
                        return None
                    return (
                        check.get("name"),
                        check.get("claim"),
                        check.get("tier"),
                        check.get("required_for_release"),
                        check.get("command"),
                        check.get("cwd"),
                    )

                if [evidence_signature(check) for check in checks] != [
                    plan_signature(check) for check in expected_selected
                ]:
                    problems.append(
                        "verification evidence executed checks do not match its plan"
                    )
                expected_skipped_signatures = [
                    (
                        check.get("name"),
                        check.get("claim"),
                        check.get("tier"),
                        check.get("required_for_release"),
                    )
                    for check in expected_skipped
                ]
                observed_skipped_signatures = [
                    (
                        check.get("name"),
                        check.get("claim"),
                        check.get("tier"),
                        check.get("required_for_release"),
                    )
                    if isinstance(check, dict)
                    else None
                    for check in skipped_checks
                ]
                if observed_skipped_signatures != expected_skipped_signatures:
                    problems.append(
                        "verification evidence skipped checks do not match its plan"
                    )
                if _is_int(planned_count) and planned_count != len(plan_checks):
                    problems.append(
                        "verification evidence planned_check_count does not match its plan"
                    )
                skipped_required = [
                    check.get("name")
                    for check in expected_skipped
                    if check.get("required_for_release") is True
                ]
                if skipped_required:
                    problems.append(
                        "release evidence skipped required checks: "
                        + ", ".join(str(name) for name in skipped_required)
                    )

    planned_revision = evidence.get("planned_revision")
    planned_match = evidence.get("planned_revision_match")
    if planned_revision is not None and (
        not isinstance(planned_revision, str) or not planned_revision.strip()
    ):
        problems.append("verification evidence planned_revision must be null or a string")
    if planned_match is not None and not isinstance(planned_match, bool):
        problems.append("verification evidence planned_revision_match must be boolean or null")
    if planned_revision is not None and planned_match is not True:
        problems.append("verification evidence does not match its planned revision")
    if plan_data is not None and plan_data.get("revision") != planned_revision:
        problems.append("verification evidence planned_revision does not match its plan")

    target_state = validate_state(evidence.get("target_state"), "target_state", problems)
    final_state = validate_state(evidence.get("final_state"), "final_state", problems)
    if evidence.get("state_stable") is not True:
        problems.append("verification evidence state_stable must be true")
    if target_state and final_state and target_state.get("identity") != final_state.get(
        "identity"
    ):
        problems.append("verification target and final project states do not match")
    if target_state and final_state and target_state.get("kind") != final_state.get("kind"):
        problems.append("verification target and final project state kinds do not match")
    if target_state and final_state and target_state.get(
        "excluded_paths"
    ) != final_state.get("excluded_paths"):
        problems.append("verification target and final state exclusions do not match")

    if target_state and isinstance(target_state.get("excluded_paths"), list):
        allowed_exclusions = {".rung/runs"}
        evidence_relative = project_relative(project, path)
        plan_relative = project_relative(project, plan_path) if plan_path else None
        if evidence_relative:
            allowed_exclusions.add(evidence_relative)
        if plan_relative:
            allowed_exclusions.add(plan_relative)
        for exclusion in target_state["excluded_paths"]:
            if (
                isinstance(exclusion, str)
                and exclusion not in allowed_exclusions
                and not exclusion.startswith(".rung/runs/")
            ):
                problems.append(
                    f"verification state excludes an unrelated project path: {exclusion}"
                )

    applicability = evidence.get("applicability")
    if not isinstance(applicability, dict):
        problems.append("verification evidence applicability must be an object")
    else:
        if applicability.get("status") != "pass":
            problems.append("verification evidence applicability status must be pass")
        if applicability.get("reasons") != []:
            problems.append("passing verification evidence must have no applicability reasons")

    revision = manifest.get("revision")
    if target_state and isinstance(revision, str) and revision.strip():
        if not revision_matches_state(project, revision, target_state):
            problems.append(
                "manifest revision does not identify the state covered by verification evidence"
            )
        if target_state.get("kind") != "git" or target_state.get("dirty") is not False:
            exclusions = list(target_state.get("excluded_paths") or [])
            exclusions.extend([path, manifest_path])
            try:
                current_state = capture_project_state(
                    project, excluded_paths=exclusions
                )
            except ValueError as exc:
                problems.append(f"cannot capture current project state: {exc}")
            else:
                if current_state["identity"] != target_state.get("identity"):
                    problems.append(
                        "verification evidence no longer applies to the current project state"
                    )
    return "verified" if not problems else "invalid"


def validate_manifest(
    data: dict[str, Any], project: Path, manifest_path: Path
) -> dict[str, Any]:
    problems: list[str] = []
    warnings: list[str] = []
    verification_applicability = "not-checked"
    missing = sorted(REQUIRED_KEYS - data.keys())
    if missing:
        problems.append("missing required keys: " + ", ".join(missing))
    if contains_placeholder(data):
        problems.append("manifest contains unresolved template placeholders")
    if data.get("schema_version") != 1:
        problems.append("schema_version must be 1")

    status = data.get("status")
    status_valid = isinstance(status, str) and status in ALLOWED_STATUS
    if not status_valid:
        problems.append("status must be blocked, ready, or published")

    for key in ("run_id", "version", "revision"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            problems.append(f"{key} must be a non-empty string")
    for key in LIST_KEYS:
        if key in data and not isinstance(data[key], list):
            problems.append(f"{key} must be a list")

    if status_valid and status in {"ready", "published"}:
        if data.get("acceptance") != "pass":
            problems.append("acceptance must be pass for a ready or published release")
        documentation = data.get("documentation")
        if not isinstance(documentation, str) or documentation not in {
            "complete",
            "pass",
            "updated",
            "unchanged",
            "not-applicable",
        }:
            problems.append(
                "documentation must be complete, pass, updated, unchanged, or not-applicable"
            )

        artifacts = data.get("artifacts")
        if isinstance(artifacts, list):
            for index, artifact in enumerate(artifacts, 1):
                resolve_reference(project, artifact, f"artifact {index}", problems)

        reference_kind, verification_path = resolve_reference(
            project, data.get("verification"), "verification", problems
        )
        if reference_kind == "local" and verification_path is not None:
            verification_applicability = validate_verification_evidence(
                verification_path,
                project,
                manifest_path,
                data,
                problems,
            )
        elif reference_kind == "external":
            verification_applicability = "delegated-unverified"
            warnings.append(
                "external verification evidence applicability was delegated and not checked locally"
            )

        revision = data.get("revision")
        if (
            reference_kind != "local"
            and isinstance(revision, str)
            and revision.strip()
        ):
            exists = git_revision_exists(project, revision)
            if exists is False:
                problems.append(
                    f"revision is not a commit in the project repository: {revision}"
                )

    if status == "published" and not data.get("publish_actions"):
        problems.append("published status requires at least one recorded publish action")

    if problems:
        result_status = "fail"
    elif status == "blocked":
        result_status = "blocked"
    else:
        result_status = "pass"
    return {
        "schema_version": 2,
        "status": result_status,
        "release_status": status,
        "verification_applicability": verification_applicability,
        "problems": problems,
        "warnings": warnings,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--project", default=".")
    parser.add_argument("--output", default="-", help="JSON output path, or - for stdout")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest = Path(args.manifest).expanduser().resolve()
    project = Path(args.project).expanduser().resolve()
    if not project.is_dir():
        print(json.dumps({"status": "error", "message": f"Project directory not found: {project}"}))
        return 2
    try:
        data = parse_manifest(manifest)
    except ValueError as exc:
        print(json.dumps({"status": "error", "message": str(exc)}, ensure_ascii=False))
        return 2

    report = validate_manifest(data, project, manifest)
    report["manifest"] = str(manifest)
    report["project_root"] = str(project)
    payload = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output == "-":
        sys.stdout.write(payload)
    else:
        output = Path(args.output).expanduser().resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload, encoding="utf-8")
    return {"pass": 0, "fail": 1, "blocked": 2}[report["status"]]


if __name__ == "__main__":
    raise SystemExit(main())
