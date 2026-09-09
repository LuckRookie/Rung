#!/usr/bin/env python3
"""Identify the project state covered by verification evidence."""

from __future__ import annotations

import hashlib
import os
import stat
import subprocess
from collections.abc import Iterable
from pathlib import Path
from typing import Any

DEFAULT_EXCLUDED_PREFIXES = (".rung/runs",)


def _run_git(root: Path, *arguments: str) -> subprocess.CompletedProcess[bytes] | None:
    try:
        return subprocess.run(
            ["git", "-C", str(root), *arguments],
            check=False,
            capture_output=True,
            timeout=10,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None


def _project_relative(root: Path, path: Path) -> str | None:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return None


def normalize_exclusions(root: Path, paths: Iterable[Path | str]) -> list[str]:
    exclusions = set(DEFAULT_EXCLUDED_PREFIXES)
    for value in paths:
        path = Path(value).expanduser()
        if not path.is_absolute():
            path = root / path
        relative = _project_relative(root, path)
        if relative and relative != ".":
            exclusions.add(relative.rstrip("/"))
    return sorted(exclusions)


def _is_excluded(relative: str, exclusions: list[str]) -> bool:
    normalized = relative.replace(os.sep, "/").strip("/")
    return any(
        normalized == excluded or normalized.startswith(f"{excluded}/")
        for excluded in exclusions
    )


def _add_field(digest: Any, label: bytes, value: bytes) -> None:
    digest.update(label)
    digest.update(len(value).to_bytes(8, "big"))
    digest.update(value)


def _path_snapshot(root: Path, relative: str) -> bytes:
    path = root / relative
    try:
        metadata = path.lstat()
    except OSError:
        return b"missing"

    mode = stat.S_IMODE(metadata.st_mode)
    prefix = f"{mode:o}\0".encode()
    if path.is_symlink():
        try:
            return prefix + b"symlink\0" + os.readlink(path).encode(errors="surrogateescape")
        except OSError:
            return prefix + b"unreadable-symlink"
    if not path.is_file():
        return prefix + b"non-regular"

    content = hashlib.sha256()
    try:
        with path.open("rb") as source:
            for chunk in iter(lambda: source.read(1024 * 1024), b""):
                content.update(chunk)
    except OSError:
        return prefix + b"unreadable"
    return prefix + b"file\0" + content.hexdigest().encode()


def _parse_status(data: bytes) -> list[tuple[str, list[str]]]:
    entries = data.split(b"\0")
    parsed: list[tuple[str, list[str]]] = []
    index = 0
    while index < len(entries):
        entry = entries[index]
        index += 1
        if not entry:
            continue
        if len(entry) < 4:
            raise ValueError("Git returned malformed porcelain status")
        status_code = entry[:2].decode("ascii", errors="replace")
        paths = [entry[3:].decode(errors="surrogateescape")]
        if status_code[0] in {"R", "C"} or status_code[1] in {"R", "C"}:
            if index >= len(entries) or not entries[index]:
                raise ValueError("Git returned an incomplete rename status")
            paths.append(entries[index].decode(errors="surrogateescape"))
            index += 1
        parsed.append((status_code, paths))
    return parsed


def _git_state(root: Path, exclusions: list[str]) -> dict[str, Any] | None:
    inside = _run_git(root, "rev-parse", "--is-inside-work-tree")
    if inside is None or inside.returncode != 0 or inside.stdout.strip() != b"true":
        return None

    head_result = _run_git(root, "rev-parse", "HEAD")
    head = (
        head_result.stdout.decode(errors="replace").strip()
        if head_result is not None and head_result.returncode == 0
        else None
    )
    index_result = _run_git(root, "ls-files", "--stage", "-z")
    status_result = _run_git(
        root,
        "status",
        "--porcelain=v1",
        "-z",
        "--untracked-files=all",
    )
    if (
        index_result is None
        or index_result.returncode != 0
        or status_result is None
        or status_result.returncode != 0
    ):
        raise ValueError("Cannot capture the Git index and working-tree state")

    digest = hashlib.sha256()
    _add_field(digest, b"kind", b"git")
    _add_field(digest, b"head", (head or "unborn").encode())

    for record in sorted(item for item in index_result.stdout.split(b"\0") if item):
        _, separator, raw_path = record.partition(b"\t")
        if not separator:
            raise ValueError("Git returned malformed index data")
        relative = raw_path.decode(errors="surrogateescape")
        if not _is_excluded(relative, exclusions):
            _add_field(digest, b"index", record)

    relevant_status: list[tuple[str, list[str]]] = []
    for status_code, paths in _parse_status(status_result.stdout):
        included_paths = [path for path in paths if not _is_excluded(path, exclusions)]
        if not included_paths:
            continue
        relevant_status.append((status_code, included_paths))

    tracked_change_count = 0
    untracked_count = 0
    for status_code, paths in sorted(relevant_status):
        if status_code == "??":
            untracked_count += 1
        else:
            tracked_change_count += 1
        _add_field(digest, b"status", status_code.encode())
        for relative in sorted(paths):
            encoded_path = relative.encode(errors="surrogateescape")
            _add_field(digest, b"path", encoded_path)
            _add_field(digest, b"content", _path_snapshot(root, relative))

    fingerprint = digest.hexdigest()
    dirty = bool(relevant_status)
    identity = head if head and not dirty else f"git-worktree:sha256:{fingerprint}"
    return {
        "kind": "git",
        "identity": identity,
        "head_revision": head,
        "dirty": dirty,
        "fingerprint": f"sha256:{fingerprint}",
        "tracked_change_count": tracked_change_count,
        "untracked_count": untracked_count,
        "excluded_paths": exclusions,
    }


def _filesystem_state(root: Path, exclusions: list[str]) -> dict[str, Any]:
    digest = hashlib.sha256()
    _add_field(digest, b"kind", b"filesystem")
    file_count = 0
    for current, directories, files in os.walk(root, followlinks=False):
        current_path = Path(current)
        directories[:] = [
            name
            for name in sorted(directories)
            if name not in {".git", ".hg"}
            and not _is_excluded(
                (current_path / name).relative_to(root).as_posix(), exclusions
            )
        ]
        for name in sorted(files):
            path = current_path / name
            relative = path.relative_to(root).as_posix()
            if _is_excluded(relative, exclusions):
                continue
            _add_field(digest, b"path", relative.encode(errors="surrogateescape"))
            _add_field(digest, b"content", _path_snapshot(root, relative))
            file_count += 1

    fingerprint = digest.hexdigest()
    return {
        "kind": "filesystem",
        "identity": f"filesystem:sha256:{fingerprint}",
        "head_revision": None,
        "dirty": None,
        "fingerprint": f"sha256:{fingerprint}",
        "file_count": file_count,
        "excluded_paths": exclusions,
    }


def capture_project_state(
    root: Path, *, excluded_paths: Iterable[Path | str] = ()
) -> dict[str, Any]:
    project = root.resolve()
    exclusions = normalize_exclusions(project, excluded_paths)
    return _git_state(project, exclusions) or _filesystem_state(project, exclusions)


def resolve_git_commit(root: Path, revision: str) -> str | None:
    result = _run_git(root, "rev-parse", "--verify", f"{revision}^{{commit}}")
    if result is None or result.returncode != 0:
        return None
    return result.stdout.decode(errors="replace").strip() or None


def revision_matches_state(root: Path, revision: str, state: dict[str, Any]) -> bool:
    if revision == state.get("identity"):
        return True
    if state.get("kind") != "git" or state.get("dirty") is not False:
        return False
    resolved = resolve_git_commit(root, revision)
    return resolved is not None and resolved == state.get("head_revision")
