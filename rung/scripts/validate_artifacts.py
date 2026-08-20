#!/usr/bin/env python3
"""Validate selected or discovered Artifacts for a Rung DevelopmentRun."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ARTIFACT_FILES = [
    "brief.md",
    "context.md",
    "design.md",
    "plan.md",
    "harness-change.md",
    "verification-harness.md",
    "verification-plan.json",
    "verification.md",
    "review.md",
    "evidence.json",
    "release.yaml",
]

PLACEHOLDER = re.compile(r"\{\{[^{}]+\}\}")


def inspect_file(path: Path) -> list[str]:
    problems: list[str] = []
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        problems.append("file is not UTF-8 text")
        return problems
    except OSError as exc:
        problems.append(f"cannot read file: {exc}")
        return problems

    if not content.strip():
        problems.append("file is empty")
        return problems
    placeholders = sorted(set(PLACEHOLDER.findall(content)))
    if placeholders:
        preview = ", ".join(placeholders[:5])
        suffix = " ..." if len(placeholders) > 5 else ""
        problems.append(f"unresolved template placeholders: {preview}{suffix}")

    if path.suffix == ".json":
        try:
            json.loads(content)
        except json.JSONDecodeError as exc:
            problems.append(f"invalid JSON: {exc}")
    return problems


def select_artifacts(run_dir: Path, explicit: list[str]) -> tuple[list[str], str]:
    if explicit:
        selected = explicit
        selection = "explicit"
    else:
        selected = [name for name in ARTIFACT_FILES if (run_dir / name).is_file()]
        selection = "discovered"

    return list(dict.fromkeys(selected)), selection


def validate(run_dir: Path, selected: list[str], selection: str) -> dict[str, Any]:
    files: list[dict[str, Any]] = []
    for relative in selected:
        path = run_dir / relative
        if not path.is_file():
            files.append(
                {
                    "path": relative,
                    "status": "missing",
                    "problems": ["required file missing"],
                }
            )
            continue
        problems = inspect_file(path)
        files.append(
            {
                "path": relative,
                "status": "fail" if problems else "pass",
                "problems": problems,
            }
        )

    problems = [] if files else ["no supported artifacts selected or found"]
    status = (
        "pass"
        if files and all(item["status"] == "pass" for item in files)
        else "fail"
    )
    return {
        "schema_version": 1,
        "run_dir": str(run_dir),
        "selection": selection,
        "status": status,
        "problems": problems,
        "files": files,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True)
    parser.add_argument(
        "--require",
        action="append",
        default=[],
        choices=ARTIFACT_FILES,
        metavar="ARTIFACT",
        help="Require one known Artifact; repeat for multiple files",
    )
    parser.add_argument("--output", default="-", help="JSON output path, or - for stdout")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    run_dir = Path(args.run_dir).expanduser().resolve()
    if not run_dir.is_dir():
        print(json.dumps({"status": "error", "message": f"Run directory not found: {run_dir}"}))
        return 2

    selected, selection = select_artifacts(run_dir, args.require)
    report = validate(run_dir, selected, selection)
    payload = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output == "-":
        sys.stdout.write(payload)
    else:
        output = Path(args.output).expanduser().resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload, encoding="utf-8")
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
