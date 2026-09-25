# Structural bugfix guidance smoke — 2026-09-25

This targeted check tests the bugfix guidance with a plain defect report and a
hidden extension. One control run and one candidate run both produced a coherent
repair. It does **not** establish that the candidate outperforms the control.

## Setup

Three independent Codex task agents received fresh isolated Git projects and
task-specific available Rung metadata. They chose whether to load Rung. They did
not receive the evaluator protocol, expected repair, hidden follow-up, parent
discussion or other agents' output. The model was inherited without an override;
exact runtime model/sampling settings and independent host read traces were not
captured. Resource reads below are agent reports.

Control used repository commit `17cb1ba`; candidate used a frozen working-tree
skill snapshot. Exact skill and fixture hashes, the full control revision, and
the local-control fixture sources are in [manifests](2026-09-25-structural-bugfix/manifests.json).
The structural fixture and prompts are maintained in
[Case 39](../cases/39-bugfix-structural-cause.md). Each project included a local
user-note edit whose bytes were independently checked after both phases.

After the snapshot, four runtime files received final refinements: the entrypoint
restored explicit durable-change wording and adjusted its repair/evolution
sentence; Inspect retained dependencies; Implement retained outcome linkage and
made its repair instruction conditional on fixes; Review restored the existing
`independent reviewer` term required by a repository check. Final hashes are
recorded separately. Behavioral observations apply to the frozen snapshot;
repository validation covers the final runtime files.

## Observed behavior

| Condition | Initial repair | Hidden on_hold extension | Reported Rung reads |
|---|---|---|---|
| Control | `Order.cancel()` owns eligibility and mutation; both adapters delegate | Policy changes only in `orders.py`; adapters unchanged | SKILL, Design |
| Candidate | `Order.cancel()` owns eligibility and mutation; both adapters delegate | Policy changes only in `orders.py`; adapters unchanged | SKILL, Design |
| Candidate local control | One-line cart-total floor, no abstraction | Not requested | None |

The parent inspected actual code and diffs. Both structural runs retired the
adapter eligibility predicates, retained transport-specific response translation,
preserved order and rejected-state behavior, and added no framework or registry.
Follow-ups also changed tests and documentation, but only one production rule.
The local control changed only the existing calculation line.

## Independent checks

- Original structural fixture: the public-behavior oracle reproduces the shipped
  batch failure despite all four original tests passing.
- Initial control and candidate: each passes nine public-behavior checks covering
  all four released states through both entry points and a mixed batch. Configured
  suites pass with six and eight tests respectively.
- Each agent's initial regression suite fails when run against a fresh copy of
  the original production code, confirming sensitivity to the defect.
- Follow-up control and candidate: each passes eleven checks, including on_hold
  through both entry points; configured suites pass with seven and ten tests.
- Local control: 36 combinations of nonnegative subtotal and credit agree with
  the floor contract. The agent reported the configured two-test suite passing.
- A deliberately constructed symptom-only patch passes all nine initial behavior
  checks while leaving two eligibility predicates. Its structural gate fails by
  code inspection. Behavioral tests alone do not establish unified ownership.
- All user notes remain byte-identical to their pre-agent state.

The oracle source, inputs, expected and observed results, suite outputs and
regression-on-original failures are in
[independent checks](2026-09-25-structural-bugfix/independent-checks.json).
[Forward observations](2026-09-25-structural-bugfix/forward-results.json) record
prompts, permissions, reported reads, conclusions and limits. Initial and follow-up
patches for both variants, plus the local patch, are retained beside those files.
These use zero context to avoid whitespace-only context lines in tracked evidence;
replay with `git apply --unidiff-zero` against the corresponding baseline. All five
patches were independently replayed and matched their recorded target files.

Final repository validation passed: 81 unit tests, Ruff, contract validation,
scope evaluation, skill-creator validation and whitespace checks. Context limits
remain unchanged: entrypoint 2,393 bytes, changed cards at most 1,295 bytes, and
Engineering Structure 8,982 bytes.

This small smoke supports the intended repair and local-bypass behavior on these
fixtures. It does not measure a general reliability gain, production architecture
benefit, cross-model performance or context savings. Repeated host-baseline,
control and candidate comparisons with captured host traces remain unperformed.
