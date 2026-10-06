# Change Planning

Read when producing or reviewing a change plan, selecting its next task, or coordinating work across result blocks.

## Plan responsibility

Translate agreed outcomes and evidenced design into executable work. Inspect relevant code, consumers, contracts and check entry points. Reference owning requirements and design; revise them when decisions change. Distinguish existing paths, proposed additions and unverified assumptions.

A complete implementation plan covers the agreed scope with task detail throughout. Concision and progressive loading do not permit scope reduction or vague later blocks. For long plans, establish the full outline, write blocks in batches, check coverage, then summarize. Keep Draft while required blocks are unwritten or unchecked; record remaining writing work for recovery.

## Decompose by result

Use these levels for complex work; add depth when a result still contains separately executable outcomes:

| Level | Responsibility |
|---|---|
| Overall plan | Goal, accepted direction and fact sources, scope, shared invariants, result-block index, dependencies, integration acceptance, status and next action |
| Result block | A verifiable, handoff-ready outcome; entry conditions, owned and affected boundaries, tasks, local checks, exit conditions and recovery |
| Executable task | Stable ID, prerequisites, concrete action at identified locations, output, observable completion check and status |

Split by verifiable results, not mechanically by file, module, person or lifecycle phase. A block may cross modules; a task may combine implementation and its tests. Investigation, documentation, migration and cleanup belong to the result they enable unless they have independent outputs and dependencies.

Split tasks whose outputs, prerequisites or acceptance conditions need separate progress or recovery. Stop when an executor can locate the work, understand the change and preserved behavior, produce and verify a bounded result, and report status without reconstructing major design decisions. Leave ordinary implementation judgment to the executor; fixed file, task, tool-call counts or hierarchy depths do not define this boundary.

For example, replace "implement cancellation" with the identified policy owner, adapter changes, preserved responses, and assertions for allowed, idempotent and rejected states. Split adapter work only when its dependencies or outputs need independent tracking.

## Coverage and dependencies

Map every agreed outcome and acceptance condition to blocks or task IDs. Children plus integration must satisfy their parent. Check later blocks as carefully as initial ones, including relevant callers, configuration, data compatibility, documentation, retirement and delivery. Add work required by the outcome.

Record actual prerequisite outputs and task IDs; block numbering alone does not prescribe order. Resolve circular dependencies through a shared contract or integration task. If block-level dependencies conceal independent work, refine them before acting; do not silently waive entry conditions or a user-prescribed sequence.

Attach checks and expected assertions to each task or reference shared checks precisely. Include relevant failures and boundaries, block exit conditions and integrated checks at joins. "Run tests" is insufficient. Use discovered entry points; label proposed tests and commands, missing environments and evidence.

## Uncertainty and readiness

Represent unknowns as investigation tasks with a question, evidence, expected decision or artifact, exit condition and dependent tasks. Keep affected outcomes visible but mark their implementation awaiting refinement; identify who resolves material choices and when. Do not fabricate detail or classify unresolved implementation as ready.

Before delivery, review coverage, granularity, references, dependencies, local and integrated checks, and recovery for risky actions. An executor without the planning conversation must have enough linked context to start ready tasks. State gaps and impact. Mark the plan Ready only after required blocks exist and this review passes; one ready task is insufficient. Distinguish drafted, ready, partly implemented and verified complete.

## Document structure

Honor the user's location and established project conventions. For a large persisted plan without an existing shape, use an overview and numbered result-block files:

```text
docs/plans/<change>/
  README.md
  01-<outcome>.md
  02-<outcome>.md
```

Keep directories flat unless navigation warrants nesting. Smaller plans may use these sections in one document; immediate local work may use a short host plan. No fixed file or block count is required.

Use [Change Plan](../assets/change-plan.template.md) for the overview and [Result Block](../assets/plan-result-block.template.md) for blocks or inline sections. Adapt optional fields; retain outcomes, dependencies, tasks and checks. Keep global decisions and integration state in the overview, task details and evidence in their block, and enduring facts with their project owner. Link rather than duplicate.

## Execution order and focus

Default to advancing one current result block toward its exit conditions. A later task being ready does not by itself justify switching. Cross-block work can resolve a blocker, test an important integration assumption early, or produce a bounded independent result with a concrete benefit. Authorized workers may advance independent tasks while the Primary Agent retains the integration focus.

Before crossing blocks, record in the existing plan or session note: target task, reason, prerequisite outputs and evidence, bounded deliverable, and return condition. Return to the main block when that condition holds, or explicitly revise priorities and remaining work. Routine reordering within authorized scope needs no new user approval; scope and authority changes retain their own boundaries.

Match prerequisites to the action. A stable contract may permit adapter preparation or fixture tests before its provider is implemented. Production integration and acceptance require the corresponding implementation and verification evidence. Keep preparatory work distinct from delivered behavior; a mocked success cannot satisfy an unmet prerequisite.

Limit unfinished work. When several blocks remain Partial, reconcile their remaining exit conditions and blockers before opening more. Split oversized tasks, close verified sub-results, and retain responsibility for deferred work rather than repeatedly extending later blocks. A shared evidence log must map results to owning task IDs; its file location does not determine which block progressed.

## Progress and recovery

After meaningful units, record checks, results, revision or patch, evidence and gaps against stable task IDs. Task completion requires its verified output; block completion requires its exit conditions; plan completion requires all agreed outcomes and integrated acceptance.

When facts invalidate a decision, revise its owner, affected tasks, dependencies and checks. Record superseded work explicitly. On recovery, read the overview and current block, reconcile repository state and user edits, revalidate affected evidence, and restore the recorded focus and return conditions. Planning does not expand implementation, delegation or external-action authority.
