#!/usr/bin/env python3
"""Collect read-only project facts for a Rung ProjectContext."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

IGNORED_DIRECTORIES = {
    ".git",
    ".hg",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".rung",
    ".tox",
    ".venv",
    "__pycache__",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "target",
    "vendor",
    "venv",
}

INSTRUCTION_NAMES = {
    "AGENTS.md",
    "CLAUDE.md",
    "COPILOT.md",
    ".cursorrules",
}

CONFIG_NAMES = {
    ".editorconfig",
    ".eslintrc",
    ".eslintrc.js",
    ".eslintrc.json",
    ".pre-commit-config.yaml",
    "Cargo.toml",
    "Dockerfile",
    "Gemfile",
    "Makefile",
    "Package.swift",
    "build.gradle",
    "build.gradle.kts",
    "composer.json",
    "go.mod",
    "justfile",
    "package.json",
    "pnpm-workspace.yaml",
    "pom.xml",
    "pyproject.toml",
    "pytest.ini",
    "requirements.txt",
    "setup.cfg",
    "setup.py",
    "tsconfig.json",
}

LANGUAGE_BY_SUFFIX = {
    ".c": "C",
    ".cc": "C++",
    ".cpp": "C++",
    ".cs": "C#",
    ".css": "CSS",
    ".dart": "Dart",
    ".ex": "Elixir",
    ".exs": "Elixir",
    ".go": "Go",
    ".h": "C/C++ header",
    ".hpp": "C++ header",
    ".html": "HTML",
    ".java": "Java",
    ".js": "JavaScript",
    ".jsx": "JavaScript",
    ".kt": "Kotlin",
    ".kts": "Kotlin",
    ".lua": "Lua",
    ".php": "PHP",
    ".py": "Python",
    ".rb": "Ruby",
    ".rs": "Rust",
    ".scala": "Scala",
    ".sh": "Shell",
    ".sql": "SQL",
    ".swift": "Swift",
    ".ts": "TypeScript",
    ".tsx": "TypeScript",
    ".vue": "Vue",
}


def utc_now() -> str:
    return datetime.now(UTC).isoformat()


def run_git(root: Path, *args: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(root), *args],
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None
    if result.returncode != 0:
        return None
    return result.stdout.strip()


def infer_commands(root: Path, relative_files: set[str]) -> list[dict[str, Any]]:
    commands: list[dict[str, Any]] = []

    def add(purpose: str, command: list[str], source: str) -> None:
        entry = {"purpose": purpose, "command": command, "source": source}
        if entry not in commands:
            commands.append(entry)

    def mentions_pytest(value: Any) -> bool:
        if isinstance(value, str):
            normalized = value.strip().lower()
            return normalized == "pytest" or normalized.startswith(
                (
                    "pytest-",
                    "pytest[",
                    "pytest<",
                    "pytest>",
                    "pytest=",
                    "pytest!",
                    "pytest~",
                )
            )
        if isinstance(value, list):
            return any(mentions_pytest(item) for item in value)
        if isinstance(value, dict):
            return any(mentions_pytest(key) or mentions_pytest(item) for key, item in value.items())
        return False

    package_json = root / "package.json"
    if package_json.is_file():
        try:
            package_data = json.loads(package_json.read_text(encoding="utf-8"))
            if not isinstance(package_data, dict):
                raise ValueError("package.json root must be an object")
            scripts = package_data.get("scripts", {})
            declared_manager = package_data.get("packageManager", "")
            if not isinstance(declared_manager, str):
                declared_manager = ""
            elif "@" in declared_manager:
                declared_manager = declared_manager.split("@", 1)[0]
            if declared_manager not in {"npm", "pnpm", "yarn", "bun"}:
                if "pnpm-lock.yaml" in relative_files:
                    declared_manager = "pnpm"
                elif "yarn.lock" in relative_files:
                    declared_manager = "yarn"
                elif "bun.lock" in relative_files or "bun.lockb" in relative_files:
                    declared_manager = "bun"
                else:
                    declared_manager = "npm"
            if isinstance(scripts, dict):
                for name in ("lint", "typecheck", "test", "build", "pack"):
                    if isinstance(scripts.get(name), str):
                        add(name, [declared_manager, "run", name], "package.json")
        except (OSError, ValueError):
            pass

    python_tests = any(path.startswith("tests/") for path in relative_files)
    if "pyproject.toml" in relative_files:
        pyproject: dict[str, Any] = {}
        try:
            import tomllib

            pyproject = tomllib.loads((root / "pyproject.toml").read_text(encoding="utf-8"))
        except (OSError, ValueError):
            pass

        tool_config = pyproject.get("tool", {})
        if not isinstance(tool_config, dict):
            tool_config = {}
        project_config = pyproject.get("project", {})
        if not isinstance(project_config, dict):
            project_config = {}
        dependency_sources = [
            project_config.get("dependencies"),
            project_config.get("optional-dependencies"),
            pyproject.get("dependency-groups"),
            tool_config.get("poetry"),
        ]
        uses_pytest = (
            "pytest.ini" in relative_files
            or "pytest" in tool_config
            or any(mentions_pytest(source) for source in dependency_sources)
        )
        if uses_pytest:
            add("test", ["python", "-m", "pytest"], "pyproject.toml or pytest.ini")
        elif python_tests:
            add(
                "test",
                ["python", "-m", "unittest", "discover", "-s", "tests", "-v"],
                "Python tests/ directory",
            )
        if isinstance(tool_config.get("ruff"), dict):
            add("lint", ["ruff", "check", "."], "pyproject.toml")
        if "build-system" in pyproject:
            add("build", ["python", "-m", "build"], "pyproject.toml")
    elif "pytest.ini" in relative_files:
        add("test", ["python", "-m", "pytest"], "pytest.ini or tests/")
    elif python_tests:
        add(
            "test",
            ["python", "-m", "unittest", "discover", "-s", "tests", "-v"],
            "Python tests/ directory",
        )

    if "Cargo.toml" in relative_files:
        add("test", ["cargo", "test"], "Cargo.toml")
        add("build", ["cargo", "build", "--release"], "Cargo.toml")
    if "go.mod" in relative_files:
        add("test", ["go", "test", "./..."], "go.mod")
        add("build", ["go", "build", "./..."], "go.mod")
    if "Makefile" in relative_files:
        try:
            makefile = (root / "Makefile").read_text(encoding="utf-8")
            targets = {
                match.group(1)
                for line in makefile.splitlines()
                if (match := re.match(r"^([A-Za-z0-9_.-]+):(?:\s|$)", line))
            }
            for target in ("lint", "test", "build", "package", "release", "help"):
                if target in targets:
                    purpose = "project tasks" if target == "help" else target
                    add(purpose, ["make", target], "Makefile")
        except OSError:
            pass

    return commands


def collect_git_facts(root: Path) -> dict[str, Any]:
    inside = run_git(root, "rev-parse", "--is-inside-work-tree") == "true"
    if not inside:
        return {"is_repository": False}

    status_text = run_git(root, "status", "--short") or ""
    return {
        "is_repository": True,
        "branch": run_git(root, "branch", "--show-current") or None,
        "revision": run_git(root, "rev-parse", "HEAD") or None,
        "dirty": bool(status_text),
        "status": status_text.splitlines(),
    }


def inspect_project(root: Path, max_files: int, extra_excludes: set[str]) -> dict[str, Any]:
    ignored = IGNORED_DIRECTORIES | extra_excludes
    file_count = 0
    code_file_count = 0
    truncated = False
    languages: Counter[str] = Counter()
    instruction_files: list[str] = []
    config_files: list[str] = []
    test_files: list[str] = []
    relative_files: set[str] = set()

    for current, directories, files in os.walk(root, followlinks=False):
        directories[:] = sorted(
            name
            for name in directories
            if name not in ignored and not (Path(current) / name).is_symlink()
        )
        for name in sorted(files):
            path = Path(current) / name
            if path.is_symlink():
                continue
            relative = path.relative_to(root).as_posix()
            relative_files.add(relative)
            file_count += 1

            language = LANGUAGE_BY_SUFFIX.get(path.suffix.lower())
            if language:
                languages[language] += 1
                code_file_count += 1
            if name in INSTRUCTION_NAMES:
                instruction_files.append(relative)
            if name in CONFIG_NAMES:
                config_files.append(relative)
            if "tests" in path.relative_to(root).parts or name.startswith(("test_", "spec.")):
                test_files.append(relative)

            if file_count >= max_files:
                truncated = True
                break
        if truncated:
            break

    has_build_config = any(Path(path).name in CONFIG_NAMES for path in config_files)
    if code_file_count == 0:
        project_state = "New"
    elif instruction_files and test_files and has_build_config:
        project_state = "Governed"
    else:
        project_state = "Existing"

    top_level_entries = sorted(
        entry.name for entry in root.iterdir() if entry.name not in ignored
    )

    return {
        "schema_version": 1,
        "generated_at": utc_now(),
        "project_root": str(root),
        "project_state": project_state,
        "scan": {
            "file_count": file_count,
            "code_file_count": code_file_count,
            "truncated": truncated,
            "max_files": max_files,
            "excluded_directories": sorted(ignored),
        },
        "git": collect_git_facts(root),
        "top_level_entries": top_level_entries,
        "languages": dict(languages.most_common()),
        "instruction_files": sorted(instruction_files),
        "config_files": sorted(config_files),
        "test_files": sorted(test_files),
        "candidate_commands": infer_commands(root, relative_files),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", default=".", help="Project root to inspect")
    parser.add_argument("--output", default="-", help="JSON output path, or - for stdout")
    parser.add_argument("--max-files", type=int, default=20_000)
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="Additional directory name to exclude; may be repeated",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.project).expanduser().resolve()
    if not root.is_dir():
        print(json.dumps({"status": "error", "message": f"Project directory not found: {root}"}))
        return 2
    if args.max_files < 1:
        print(json.dumps({"status": "error", "message": "--max-files must be positive"}))
        return 2

    report = inspect_project(root, args.max_files, set(args.exclude))
    payload = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output == "-":
        sys.stdout.write(payload)
    else:
        output = Path(args.output).expanduser().resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
