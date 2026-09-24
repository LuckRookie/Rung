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
STATE_SCHEMA_VERSION = 2


class StateCaptureError(ValueError):
    """The helper cannot reliably identify the requested source state."""


def _run_git(root: Path, *arguments: str) -> subprocess.CompletedProcess[bytes] | None:
    try:
        return subprocess.run(
            ["git", "--no-optional-locks", "-C", str(root), *arguments],
            check=False,
            capture_output=True,
            timeout=10,
        )
    except FileNotFoundError:
        return None
    except subprocess.TimeoutExpired as exc:
        raise StateCaptureError("Git timed out while identifying project state") from exc


def git_repository_root(project: Path) -> Path | None:
    result = _run_git(project, "rev-parse", "--show-toplevel")
    if result is not None and result.returncode == 0:
        return Path(os.fsdecode(result.stdout.rstrip(b"\n"))).resolve()
    # A broken/unavailable Git command must not silently downgrade a repository
    # to a filesystem snapshot with different coverage and exclusions.
    if any((parent / ".git").exists() for parent in (project, *project.parents)):
        raise StateCaptureError("Cannot identify the Git repository root")
    return None


def _project_relative(root: Path, path: Path) -> str | None:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return None


def normalize_exclusions(
    root: Path, paths: Iterable[Path | str], *, project: Path | None = None
) -> list[str]:
    project = project or root
    exclusions = set(DEFAULT_EXCLUDED_PREFIXES)
    # Default run locations are lexical paths. Resolving a run-directory link
    # here could silently exclude an unrelated source directory that it targets.
    exclusions.update(
        (project / prefix).relative_to(root).as_posix()
        for prefix in DEFAULT_EXCLUDED_PREFIXES
    )
    for value in paths:
        path = Path(value).expanduser()
        if not path.is_absolute():
            path = project / path
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


def _path_snapshot(root: Path, relative: str, *, missing_allowed: bool = False) -> bytes:
    path = root / relative
    try:
        metadata = path.lstat()
    except FileNotFoundError as exc:
        if missing_allowed:
            return b"missing"
        raise StateCaptureError(f"State path unexpectedly missing: {relative}") from exc
    except OSError as exc:
        raise StateCaptureError(f"Cannot inspect state path {relative}: {exc}") from exc

    mode = stat.S_IMODE(metadata.st_mode)
    prefix = f"{mode:o}\0".encode()
    if stat.S_ISLNK(metadata.st_mode):
        try:
            return prefix + b"symlink\0" + os.readlink(path).encode(errors="surrogateescape")
        except OSError as exc:
            raise StateCaptureError(f"Cannot read symbolic link {relative}: {exc}") from exc
    if not stat.S_ISREG(metadata.st_mode):
        raise StateCaptureError(
            f"Unsupported state path (directory, nested repository, or special file): {relative}"
        )

    content = hashlib.sha256()
    try:
        with path.open("rb") as source:
            for chunk in iter(lambda: source.read(1024 * 1024), b""):
                content.update(chunk)
    except OSError as exc:
        raise StateCaptureError(f"Cannot read state file {relative}: {exc}") from exc
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
            raise StateCaptureError("Git returned malformed porcelain status")
        status_code = entry[:2].decode("ascii", errors="replace")
        paths = [entry[3:].decode(errors="surrogateescape")]
        if status_code[0] in {"R", "C"} or status_code[1] in {"R", "C"}:
            if index >= len(entries) or not entries[index]:
                raise StateCaptureError("Git returned an incomplete rename status")
            paths.append(entries[index].decode(errors="surrogateescape"))
            index += 1
        parsed.append((status_code, paths))
    return parsed


def _git_state(root: Path, project: Path, exclusions: list[str]) -> dict[str, Any]:
    subpath = project.relative_to(root).as_posix()
    if subpath != ".":
        ignored = _run_git(root, "check-ignore", "--quiet", "--", f"{subpath}/")
        if ignored is None or ignored.returncode not in {0, 1}:
            raise StateCaptureError("Cannot establish the selected project's Git visibility")
        if ignored.returncode == 0:
            raise StateCaptureError(f"Selected project directory is ignored by Git: {subpath}")
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
        "--ignore-submodules=none",
    )
    if (
        index_result is None
        or index_result.returncode != 0
        or status_result is None
        or status_result.returncode != 0
    ):
        raise StateCaptureError("Cannot capture the Git index and working-tree state")
    if status_result.stderr.strip():
        diagnostic = status_result.stderr.decode(errors="replace").strip()[:2000]
        raise StateCaptureError(
            f"Git status emitted diagnostics; coverage is incomplete: {diagnostic}"
        )

    digest = hashlib.sha256()
    _add_field(digest, b"kind", b"git")
    _add_field(digest, b"state-schema", str(STATE_SCHEMA_VERSION).encode())
    _add_field(digest, b"head", (head or "unborn").encode())

    for record in sorted(item for item in index_result.stdout.split(b"\0") if item):
        metadata, separator, raw_path = record.partition(b"\t")
        if not separator:
            raise StateCaptureError("Git returned malformed index data")
        relative = raw_path.decode(errors="surrogateescape")
        if metadata.split()[0] == b"160000":
            raise StateCaptureError(
                f"Git submodules are not supported by state evidence: {relative}"
            )
        if not _is_excluded(relative, exclusions):
            _add_field(digest, b"index", record)

    relevant_status: list[tuple[str, list[str], set[str]]] = []
    for status_code, paths in _parse_status(status_result.stdout):
        included_paths = [path for path in paths if not _is_excluded(path, exclusions)]
        if not included_paths:
            continue
        # The second porcelain path is a rename/copy source, which can have
        # disappeared. A D in the working tree (including AD) is also expected.
        missing_allowed = set(paths[1:])
        if status_code[1] == "D" or status_code == "D ":
            missing_allowed.add(paths[0])
        relevant_status.append((status_code, included_paths, missing_allowed))

    tracked_change_count = 0
    untracked_count = 0
    for status_code, paths, missing_allowed in sorted(relevant_status):
        if status_code == "??":
            untracked_count += 1
        else:
            tracked_change_count += 1
        _add_field(digest, b"status", status_code.encode())
        for relative in sorted(paths):
            encoded_path = relative.encode(errors="surrogateescape")
            _add_field(digest, b"path", encoded_path)
            _add_field(
                digest, b"content",
                _path_snapshot(root, relative, missing_allowed=relative in missing_allowed),
            )

    fingerprint = digest.hexdigest()
    dirty = head is None or bool(relevant_status)
    identity = head if head and not dirty else f"git-worktree:sha256:{fingerprint}"
    return {
        "schema_version": STATE_SCHEMA_VERSION,
        "kind": "git",
        "repository_root": str(root),
        "project_subpath": subpath,
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
    _add_field(digest, b"state-schema", str(STATE_SCHEMA_VERSION).encode())
    file_count = 0

    def scan_error(error: OSError) -> None:
        raise StateCaptureError(f"Cannot scan project state: {error}") from error

    for current, directories, files in os.walk(root, followlinks=False, onerror=scan_error):
        current_path = Path(current)
        if ".git" in directories or ".git" in files:
            raise StateCaptureError(f"Nested Git repositories are not supported: {current_path}")
        directories[:] = [
            name
            for name in sorted(directories)
            if name not in {".git", ".hg"}
            and not _is_excluded(
                (current_path / name).relative_to(root).as_posix(), exclusions
            )
        ]
        directory_links = [name for name in directories if (current_path / name).is_symlink()]
        directories[:] = [name for name in directories if name not in directory_links]
        for name in sorted(files + directory_links):
            path = current_path / name
            relative = path.relative_to(root).as_posix()
            if _is_excluded(relative, exclusions):
                continue
            _add_field(digest, b"path", relative.encode(errors="surrogateescape"))
            _add_field(digest, b"content", _path_snapshot(root, relative))
            file_count += 1

    fingerprint = digest.hexdigest()
    return {
        "schema_version": STATE_SCHEMA_VERSION,
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
    repository = git_repository_root(project)
    scope_root = repository or project
    exclusions = normalize_exclusions(scope_root, excluded_paths, project=project)
    if repository is not None:
        return _git_state(repository, project, exclusions)
    return _filesystem_state(project, exclusions)


def validate_commit_coverage(project: Path, revision: str, subpath: str = ".") -> None:
    """Apply the same gitlink boundary to historical clean-commit evidence."""
    result = _run_git(project, "ls-tree", "-r", "-z", "--full-tree", revision)
    if result is None or result.returncode != 0:
        raise StateCaptureError("Cannot inspect the commit covered by verification evidence")
    has_project = subpath == "."
    for record in result.stdout.split(b"\0"):
        path = os.fsdecode(record.partition(b"\t")[2])
        if record.startswith(b"160000 "):
            raise StateCaptureError(f"Git submodules are not supported by state evidence: {path}")
        if path.startswith(f"{subpath}/"):
            has_project = True
    if not has_project:
        raise StateCaptureError("The evidence commit does not contain the selected project subtree")


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
