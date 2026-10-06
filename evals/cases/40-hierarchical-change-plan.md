# Case 40: Complete hierarchical change planning

## Purpose

Test whether a request for a complete implementation plan yields outcome-based decomposition, executable tasks throughout the scope, real dependencies and integrated acceptance. Distinguish planning quality from document length, file count and template compliance.

## Fixture and isolation

Copy only `../fixtures/content-review/roster/` into a fresh temporary Git repository. Commit the initial files, append a user-owned line to `USER-NOTE.md`, and record the resulting bytes. The released surface is `rota.owner_at`; room code is an unrelated experiment. The task introduces persistence and a CLI rather than assuming either already exists.

Use identical project copies and prompts for host baseline, the declared pre-change Skill snapshot and candidate. Record snapshot digests when the Skill includes uncommitted changes. Give agents only their project, prompt and variant's normal Skill exposure; hide this protocol, expectations and successor prompt. Do not supply the requested decomposition as an extra instruction.

## Initial prompt

```text
Write a complete implementation plan under docs/plans/schedule-files for adding
schedule files and a command-line interface to this repository. Another developer
will implement it later; do not change code or tests now. Preserve my local note.

The accepted scope is: read legacy JSON arrays of {start, end, owner} slots;
read and write a v2 envelope {"version": 2, "slots": [...]}; preserve owner_at,
half-open intervals, adjacency and invalid/overlapping interval rejection.
Reject malformed input and unsupported versions without modifying existing files.
Add CLI commands for lookup and migration. Migration writes v2 atomically to a
specified destination, refuses an existing destination unless --replace is set,
and supports --dry-run that validates and reports without writing. Retain the
source file. Reuse the domain validation rather than maintaining a second policy
in the CLI. Use Python's standard library and the repository's test convention.
Include compatibility checks, failure recovery, end-to-end CLI verification and
documentation updates. Choose reasonable internal details from repository facts
and state them in the plan. No commits, pushes or external service operations.
```

## Plan delivery gate

- The plan covers every accepted outcome, including migration failure, overwrite protection, dry-run, CLI integration and documentation; later work is not reduced to generic headings.
- Overall direction is decomposed into verifiable results and executable tasks. Blocks follow output and dependency boundaries rather than mechanically assigning one file, agent or lifecycle stage per block.
- Tasks have stable references, actual or explicitly proposed locations, concrete changes, prerequisites and observable completion conditions. Shared checks are referenced precisely; implementation and its direct verification can remain one coherent task.
- The chosen file and CLI contracts are clear enough to implement. Existing behavior, new decisions and unresolved facts remain distinguishable. Blocking uncertainty has bounded investigation and explicit dependent refinement rather than invented certainty.
- The decomposition covers the parent outcomes; task-level dependencies and cross-block integration are explicit where needed. No circular handoff or dependency on an unrelated completed block is introduced.
- Local success does not imply integrated completion. The plan distinguishes its own readiness from implementation status and records the next executable task and recovery state.
- The requested directory contains a navigable overview and result detail, or a justified compact equivalent with the same logical structure. File count, task count and word count earn no points.
- Source, tests, existing documents and the user note remain intact. No implementation or external action occurs during planning.

## Independent execution follow-up

After saving the plan and its evidence, start a fresh executor with only the project and delivered plan. Do not pass the planning conversation, this case, or the original prompt:

```text
Implement the plan under docs/plans/schedule-files. Reconcile it with the current
repository, preserve existing user edits, verify each meaningful unit and the
integrated behavior, and update progress with actual evidence. Do not commit,
push or operate external services. Report missing decisions instead of silently
replacing the plan's scope or contracts.
```

Independently check legacy/v2 round trips, all released lookup semantics, malformed/unsupported input, CLI lookup, destination protection, replacement, dry-run, source preservation and injected write failure. Check the final documentation and preserved user bytes. Record consequential decisions the executor had to reconstruct, unsupported plan assumptions, changed dependencies and tasks too broad to track. A passing implementation alone cannot establish plan sufficiency if the executor redesigned it.

## Proportionality and uncertainty controls

- In a separate fresh run, request only a plan for one local documentation correction. A brief task and direct check suffice; extra result files or a hierarchy without meaningful outputs are overhead.
- In another fresh run, withhold an external file-format contract needed for implementation. Expect a bounded investigation task and explicit readiness limits, with the rest of the known scope retained. Do not reward fabricated schema details or indefinite investigation.
- Interrupt a separate plan-writing run after its overview and initial block exist. While required blocks remain unwritten, the saved overview must remain Draft and identify the remaining planning work. A ready first task cannot establish whole-plan readiness. Resume writing in a fresh session and check all referenced blocks before accepting the final plan.

## Evidence and limits

Record model, Host, variant and fixture identities, resources actually read, plan artifacts, requirement coverage, task and dependency findings, protected bytes, checks, successor questions and changes, and context cost. Compare matched variants and repeat before claiming a general improvement. A planning-only smoke can establish observed plan shape and content; it does not establish successful execution, recovery or implicit Skill discovery. Static checks cannot prove executability.
