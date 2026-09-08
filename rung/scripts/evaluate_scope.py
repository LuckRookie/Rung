#!/usr/bin/env python3
"""Classify development scope and governance activation from host-supplied judgments."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ALLOWED_STATES = {"present", "absent", "mixed", "uncertain"}


def load_input(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ValueError(f"Cannot read scope input: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid scope input JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError("Scope input must be an object")
    return value


def evaluate_scope(data: dict[str, Any]) -> dict[str, Any]:
    relationship = data.get("codebase_relationship")
    claim = data.get("development_claim")
    materiality = data.get("materiality", "uncertain")
    mode = data.get("invocation_mode", "implicit")
    problems: list[str] = []
    fields = {
        "codebase_relationship": (relationship, ALLOWED_STATES),
        "development_claim": (claim, ALLOWED_STATES),
        "materiality": (materiality, {"present", "absent", "uncertain"}),
        "invocation_mode": (mode, {"implicit", "explicit"}),
    }
    for field, (value, allowed) in fields.items():
        if not isinstance(value, str) or value not in allowed:
            problems.append(f"{field} must be one of: {', '.join(sorted(allowed))}")
    if problems:
        return {"schema_version": 2, "status": "error", "problems": problems}

    if relationship == "absent":
        scope = "outside"
    elif claim == "absent":
        scope = "understanding-only"
    elif relationship == "uncertain" or claim == "uncertain":
        scope = "uncertain"
    elif relationship == "mixed" or claim == "mixed":
        scope = "mixed"
    else:
        scope = "development"

    if scope in {"outside", "understanding-only"}:
        activation, reason = "bypass", "No active codebase development portion qualifies."
    elif scope == "uncertain":
        activation, reason = "defer", "Resolve scope through minimal host inspection."
    elif mode == "explicit":
        activation, reason = "enter", "Governance was requested for in-scope development."
    elif materiality == "present":
        activation, reason = "enter", "A consequential engineering decision warrants governance."
    elif materiality == "absent":
        activation, reason = "bypass", "Routine development continues on the host path."
    else:
        activation, reason = "defer", "Materiality is unknown; inspect on the host and reassess."

    return {
        "schema_version": 2,
        "status": "pass",
        "scope": scope,
        "activation": activation,
        # This is a recommendation, not evidence that the host actually exited.
        "exited_before_references": activation != "enter",
        "codebase_relationship": relationship,
        "development_claim": claim,
        "materiality": materiality,
        "invocation_mode": mode,
        "reason": reason,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Scope classification JSON")
    parser.add_argument("--output", default="-", help="JSON report path, or - for stdout")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        result = evaluate_scope(load_input(Path(args.input).expanduser().resolve()))
    except ValueError as exc:
        result = {"schema_version": 2, "status": "error", "problems": [str(exc)]}

    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output == "-":
        sys.stdout.write(payload)
    else:
        output = Path(args.output).expanduser().resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload, encoding="utf-8")
    return 0 if result["status"] == "pass" else 2


if __name__ == "__main__":
    raise SystemExit(main())
