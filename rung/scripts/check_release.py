#!/usr/bin/env python3
"""Validate Rung's dependency-free Release Manifest contract and local evidence."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlparse

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
URI_PATTERN = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")
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
            text=True,
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
            text=True,
            timeout=10,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None
    return False if inside.returncode == 0 else None


def validate_local_reference(
    project: Path, value: Any, label: str, problems: list[str]
) -> Path | None:
    if not isinstance(value, str) or not value.strip():
        problems.append(f"{label} must be a non-empty string")
        return None
    if value.startswith("file:"):
        path = Path(unquote(urlparse(value).path)).resolve()
    elif URI_PATTERN.match(value) and not Path(value).is_absolute():
        return None
    else:
        raw_path = Path(value).expanduser()
        path = raw_path.resolve() if raw_path.is_absolute() else (project / raw_path).resolve()
    if not path.exists():
        problems.append(f"{label} not found: {value}")
        return None
    return path


def validate_verification_evidence(path: Path, problems: list[str]) -> None:
    if path.suffix.lower() != ".json":
        problems.append("local verification evidence must be a JSON file")
        return
    try:
        evidence = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        problems.append(f"cannot read verification evidence: {exc}")
        return
    except json.JSONDecodeError as exc:
        problems.append(f"invalid verification evidence JSON: {exc}")
        return
    if not isinstance(evidence, dict):
        problems.append("verification evidence must be a JSON object")
        return
    if evidence.get("status") != "pass":
        problems.append("verification evidence status must be pass")


def validate_manifest(data: dict[str, Any], project: Path) -> dict[str, Any]:
    problems: list[str] = []
    missing = sorted(REQUIRED_KEYS - data.keys())
    if missing:
        problems.append("missing required keys: " + ", ".join(missing))
    if contains_placeholder(data):
        problems.append("manifest contains unresolved template placeholders")
    if data.get("schema_version") != 1:
        problems.append("schema_version must be 1")

    status = data.get("status")
    if status not in ALLOWED_STATUS:
        problems.append("status must be blocked, ready, or published")

    for key in ("run_id", "version", "revision"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            problems.append(f"{key} must be a non-empty string")
    for key in LIST_KEYS:
        if key in data and not isinstance(data[key], list):
            problems.append(f"{key} must be a list")

    if status in {"ready", "published"}:
        if data.get("acceptance") != "pass":
            problems.append("acceptance must be pass for a ready or published release")
        if data.get("documentation") not in {
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
                validate_local_reference(project, artifact, f"artifact {index}", problems)

        verification_path = validate_local_reference(
            project, data.get("verification"), "verification", problems
        )
        if verification_path is not None:
            validate_verification_evidence(verification_path, problems)
        revision = data.get("revision")
        if isinstance(revision, str) and revision.strip():
            exists = git_revision_exists(project, revision)
            if exists is False:
                problems.append(f"revision is not a commit in the project repository: {revision}")

    if status == "published" and not data.get("publish_actions"):
        problems.append("published status requires at least one recorded publish action")

    if problems:
        result_status = "fail"
    elif status == "blocked":
        result_status = "blocked"
    else:
        result_status = "pass"
    return {
        "schema_version": 1,
        "status": result_status,
        "release_status": status,
        "problems": problems,
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

    report = validate_manifest(data, project)
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
