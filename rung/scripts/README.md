# Helper evidence contract

The optional helpers identify source state and execute a declared verification plan. A host can continue using project-native checks when helper coverage is unavailable.

## State scope

Evidence and verification plans use schema v2. Each `target_state` and `final_state` also requires `schema_version: 2`. Rerun verification for evidence containing older, unversioned state records; adding a marker to old evidence does not establish coverage.

For Git projects, state covers the **whole repository**, including when `--project` selects a subdirectory. `repository_root` and `project_subpath` report that scope. The selected project remains the anchor for check working directories and relative plan references. Changes in sibling packages invalidate working-tree evidence; narrowing coverage requires a separate dependency/coverage contract.

Clean Git state identifies a commit. Dirty state binds HEAD, the index and Git-visible working-tree changes. An unborn repository uses working-tree identity. Filesystem state covers files and symbolic links below the project, including directory links themselves, without traversing link targets. Filesystem and changed-path snapshots include permissions and link targets. External link-target content needs separate evidence.

Git-ignored files, index visibility overrides (`assume-unchanged`, `skip-worktree`, sparse checkout), external dependencies and environment state require project-owned verification when they affect a claim. Source identity does not establish artifact provenance or deterministic behavior of external services.

## Exclusions

Git exclusions use repository-relative paths. The repository's `.rung/runs`, the selected project's `.rung/runs`, and the current plan/evidence files are excluded. Default run prefixes are lexical: a run-directory link does not exclude its target directory. Other sibling run directories remain covered; there is no wildcard exclusion of every `.rung` directory. Filesystem exclusions are project-relative. Keep release manifests in the run directory; the release checker also excludes its own manifest during current-state comparison. Evidence emitted on stdout can be saved under an excluded run directory; moving evidence within that directory preserves coverage.

Only run records belong in these excluded locations. Source code, fixtures or other inputs that a claim depends on need a covered project owner. Exclusion records are checked against the selected project, plan and evidence, not accepted as arbitrary caller-defined coverage.

## Unsupported or incomplete state

The runner returns structured `blocked` with exit code 2 before running checks if state cannot be identified. When `--output` is supplied it replaces any earlier output with that diagnostic; plan-loading, check-validation and revision-mismatch errors likewise replace it with an error report. If capture fails after checks, their results are retained in blocked/non-passing evidence with the applicability gap.

The output must be distinct from the plan, including through links. An overlapping output is rejected on stdout without overwriting the plan. Use `--output` for files outside run directories; shell redirection creates its destination before state capture.

Gitlinks (submodules) are currently unsupported, including clean, uninitialized and nested configurations. A parent `git status` cannot establish nested coverage. A selected project directory ignored by Git, untracked nested repositories, unreadable visible paths, filesystem scan errors, special files and unexplained missing paths also block state capture. Git status diagnostics block capture rather than accepting a possibly partial scan. Expected deletion and rename-source absence are handled using Git status semantics.

The release checker rejects unsupported local evidence, including a clean historical commit containing gitlinks. A valid schema marker alone cannot bypass that check. Supporting submodules later requires explicit checkout, initialization, nested-ignore and recovery behavior with independent acceptance tests.

## Commit evidence versus current-state evidence

Evidence genuinely executed on an immutable commit remains applicable to that commit after the checkout changes. The manifest must still identify that original commit. Dirty Git and filesystem evidence instead require the current covered content to match. Results observed on uncommitted content must not be attributed to HEAD merely because Git reports a clean parent.

Release validation checks declared plan coverage, state applicability and internal consistency. It does not prove that a package was built from the declared revision. Artifact checks, checksums, environment assumptions and coverage sufficiency remain with the project's release process. External evidence stays `delegated-unverified`.
