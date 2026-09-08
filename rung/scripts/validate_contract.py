#!/usr/bin/env python3
"""Validate Rung's machine-readable core and routing contract."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

CONTRACT_NAME = "contracts/rung-contract.json"
REQUIRED_PACKAGE_KEYS = {"name", "stable_ref", "candidate_version"}
ALLOWED_KINDS = {"card", "guide"}


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ValueError(f"Cannot read contract: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid contract JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError("Contract root must be an object")
    return value


def validate_contract(skill_root: Path, contract: dict[str, Any]) -> list[str]:
    problems: list[str] = []

    if contract.get("schema_version") != 2:
        problems.append("schema_version must be 2")
    package = contract.get("package")
    if not isinstance(package, dict):
        problems.append("package must be an object")
    else:
        missing = sorted(REQUIRED_PACKAGE_KEYS - package.keys())
        if missing:
            problems.append("package missing keys: " + ", ".join(missing))
        if package.get("name") != "rung":
            problems.append("package.name must be rung")
        for key in ("stable_ref", "candidate_version"):
            if not isinstance(package.get(key), str) or not package[key].strip():
                problems.append(f"package.{key} must be a non-empty string")

        repository_root = skill_root.parent
        stable_ref = package.get("stable_ref")
        candidate_version = package.get("candidate_version")
        if isinstance(stable_ref, str) and isinstance(candidate_version, str):
            for document_name in ("README.md", "INSTALL.md"):
                document = repository_root / document_name
                if not document.is_file():
                    continue
                try:
                    content = document.read_text(encoding="utf-8")
                except OSError as exc:
                    problems.append(f"cannot read {document_name}: {exc}")
                    continue
                if stable_ref not in content:
                    problems.append(f"{document_name} does not mention stable ref {stable_ref}")
                if document_name == "README.md" and candidate_version not in content:
                    problems.append(
                        f"{document_name} does not mention candidate version {candidate_version}"
                    )

    entrypoint = contract.get("entrypoint")
    if not isinstance(entrypoint, str) or not entrypoint.strip():
        problems.append("entrypoint must be a non-empty string")
    elif entrypoint != "SKILL.md":
        problems.append("entrypoint must be SKILL.md")
    elif not (skill_root / entrypoint).is_file():
        problems.append(f"entrypoint not found: {entrypoint}")

    scope_gate = contract.get("scope_gate")
    if not isinstance(scope_gate, dict):
        problems.append("scope_gate must be an object")
    else:
        predicates = scope_gate.get("required_predicates")
        if predicates != ["codebase_relationship", "active_development_claim"]:
            problems.append(
                "scope_gate.required_predicates must require codebase relationship "
                "and active development claim"
            )
        outcomes = scope_gate.get("development_outcomes")
        if not isinstance(outcomes, list) or not outcomes:
            problems.append("scope_gate.development_outcomes must be a non-empty list")
        if scope_gate.get("understanding_only_exits_before_references") is not True:
            problems.append("understanding-only work must exit before references")

    concerns = contract.get("concerns")
    if not isinstance(concerns, list) or not concerns:
        problems.append("concerns must be a non-empty list")
        return problems

    ids: set[str] = set()
    entries: set[str] = set()
    for index, concern in enumerate(concerns, 1):
        label = f"concern {index}"
        if not isinstance(concern, dict):
            problems.append(f"{label} must be an object")
            continue
        concern_id = concern.get("id")
        if not isinstance(concern_id, str) or not concern_id.strip():
            problems.append(f"{label}.id must be a non-empty string")
        elif concern_id in ids:
            problems.append(f"duplicate concern id: {concern_id}")
        else:
            ids.add(concern_id)

        entry = concern.get("entry")
        if not isinstance(entry, str) or not entry.strip():
            problems.append(f"{label}.entry must be a non-empty string")
        else:
            if Path(entry).is_absolute() or ".." in Path(entry).parts:
                problems.append(f"{label}.entry must stay below the Skill root: {entry}")
            elif entry in entries:
                problems.append(f"duplicate concern entry: {entry}")
            else:
                entries.add(entry)
            target = (skill_root / entry).resolve()
            try:
                target.relative_to(skill_root.resolve())
            except ValueError:
                problems.append(f"{label}.entry escapes the Skill root: {entry}")
            else:
                if not target.is_file():
                    problems.append(f"{label}.entry not found: {entry}")

        if not isinstance(concern.get("kind"), str) or concern["kind"] not in ALLOWED_KINDS:
            problems.append(f"{label}.kind must be card or guide")
        max_bytes = concern.get("max_bytes")
        if isinstance(max_bytes, bool) or not isinstance(max_bytes, int) or max_bytes < 1:
            problems.append(f"{label}.max_bytes must be a positive integer")
        elif isinstance(entry, str) and (skill_root / entry).is_file():
            size = (skill_root / entry).stat().st_size
            if size > max_bytes:
                problems.append(f"{entry} exceeds {max_bytes} bytes ({size})")

        signals = concern.get("signals")
        if (
            not isinstance(signals, list)
            or not signals
            or not all(isinstance(signal, str) and signal.strip() for signal in signals)
        ):
            problems.append(f"{label}.signals must be a non-empty string list")

    activation = contract.get("activation")
    expected_activation = {
        "implicit_requires_materiality": True,
        "explicit_overrides_materiality_only": True,
        "routine_activation": "bypass",
        "uncertain_activation": "defer",
    }
    if not isinstance(activation, dict) or any(
        type(activation.get(key)) is not type(value) or activation.get(key) != value
        for key, value in expected_activation.items()
    ):
        problems.append("activation must preserve implicit materiality and explicit scope limits")

    budget = contract.get("entrypoint_max_bytes")
    if type(budget) is not int or not 0 < budget <= 2400:
        problems.append("entrypoint_max_bytes must be an integer from 1 to 2400")
    elif (
        entrypoint == "SKILL.md"
        and (skill_root / entrypoint).is_file()
        and (skill_root / entrypoint).stat().st_size > budget
    ):
        problems.append(f"entrypoint exceeds {budget} bytes")

    # Check discoverability after pruning the root router, without requiring
    # guides to be direct links or rewarding repeated wording in every card.
    if entrypoint == "SKILL.md":
        visited: set[Path] = set()
        pending = [skill_root / entrypoint]
        while pending:
            document = pending.pop().resolve()
            if document in visited or not document.is_relative_to(skill_root.resolve()):
                continue
            visited.add(document)
            if not document.is_file():
                problems.append(f"linked document not found: {document.name}")
                continue
            content = document.read_text(encoding="utf-8")
            for link in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", content):
                if not re.match(r"^[a-z][a-z0-9+.-]*:", link, re.IGNORECASE):
                    target = (document.parent / link).resolve()
                    if target.suffix == ".md":
                        pending.append(target)
        for entry in entries:
            if (skill_root / entry).resolve() not in visited:
                problems.append(f"unreachable concern: {entry}")

    lifecycle = contract.get("lifecycle")
    expected_lifecycle = [
        "clarify",
        "inspect",
        "design",
        "plan",
        "implement",
        "verify",
        "review",
        "release",
    ]
    if not isinstance(lifecycle, list) or not lifecycle:
        problems.append("lifecycle must be a non-empty list")
    else:
        actual_lifecycle = [
            stage.get("id") if isinstance(stage, dict) else None for stage in lifecycle
        ]
        if len(actual_lifecycle) != len(expected_lifecycle) or any(
            actual_lifecycle.count(item) != 1 for item in expected_lifecycle
        ):
            problems.append("lifecycle must cover each of the eight composable concerns once")
        concern_by_id = {
            concern.get("id"): concern
            for concern in concerns
            if isinstance(concern, dict) and isinstance(concern.get("id"), str)
        }
        for index, stage in enumerate(lifecycle, 1):
            label = f"lifecycle stage {index}"
            if not isinstance(stage, dict):
                problems.append(f"{label} must be an object")
                continue
            stage_id = stage.get("id")
            concern_id = stage.get("concern")
            if (
                not isinstance(concern_id, str)
                or stage_id != concern_id
                or concern_id not in concern_by_id
            ):
                problems.append(f"{label} must reference its matching concern")
                continue

    return problems


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-root", default=".", help="Skill root containing contracts/")
    parser.add_argument(
        "--contract",
        default=CONTRACT_NAME,
        help="Contract path relative to Skill root",
    )
    parser.add_argument("--output", default="-", help="JSON report path, or - for stdout")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    skill_root = Path(args.skill_root).expanduser().resolve()
    contract_path = Path(args.contract).expanduser()
    if not contract_path.is_absolute():
        contract_path = skill_root / contract_path
    contract_path = contract_path.resolve()
    try:
        contract = load_json(contract_path)
        problems = validate_contract(skill_root, contract)
    except ValueError as exc:
        problems = [str(exc)]

    report = {
        "schema_version": 1,
        "status": "pass" if not problems else "fail",
        "skill_root": str(skill_root),
        "contract": str(contract_path),
        "problems": problems,
    }
    payload = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output == "-":
        sys.stdout.write(payload)
    else:
        output = Path(args.output).expanduser().resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload, encoding="utf-8")
    return 0 if not problems else 1


if __name__ == "__main__":
    raise SystemExit(main())
