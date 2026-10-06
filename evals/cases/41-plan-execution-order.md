# Case 41: Dependency-aware execution and block closure

## Purpose

Test whether an agent selects work using real prerequisites and the current completion target, permits justified cross-block progress, and avoids accumulating unfinished blocks. Neither strict numeric order nor maximum parallelism is the objective.

## Fixture

Use the schedule-file project and accepted contracts from [Case 40](40-hierarchical-change-plan.md), advanced to a fixed partial implementation. Prepare and freeze code, tests, plan and evidence together before comparing variants; do not relabel unsupported work as complete merely to establish the starting state.

The persisted plan has these outcomes and states:

| Block | State | Tasks and evidence |
|---|---|---|
| 01: Domain and formats | Verified | Shared interval validation, legacy/v2 parsing and rendering have direct checks. |
| 02: Safe migration | Current focus, Partial | 2.1 atomic destination creation/replacement is implemented; 2.2 has a reproducible cleanup defect before publication; 2.3 dry-run and source preservation await verification. The writer's contract is accepted and stable. |
| 03: CLI | Not started | 3.1 lookup needs only Block 01; 3.2 parser/adapter preparation for migrate needs the stable writer contract; 3.3 real migration acceptance needs verified 2.2/2.3 behavior. |
| 04: Documentation and handoff | Not started | Public usage and integrated acceptance require the corresponding implemented behavior. |

Give 2.2 a targeted failing test that injects a write failure before publication and checks the unchanged destination, preserved source and temporary-file cleanup. The fixture must permit a bounded repair. Existing checks and the plan identify the next action as 2.2. Include an unrelated user edit and preserve its bytes.

Use a single primary executor for the main scenario. Retain the same fixture, prompt, model and tool permissions for Host baseline, pinned control and candidate. Hide the case, expectations and controls from the executor.

## Initial prompt

```text
Continue the implementation plan under docs/plans/schedule-files from the current
repository state. Preserve my existing edits, verify meaningful results and keep
the plan's progress accurate. Do not commit, push or use external services.
```

## Execution gate

- The next meaningful implementation work addresses the recorded focus and its remaining exit conditions. Later ready work does not displace the bounded 2.2 repair without a concrete reason.
- An early CLI probe is acceptable when it tests a named integration uncertainty: the agent identifies the prerequisite evidence, bounded output and return condition, then returns to the migration work or records a supported priority change.
- Contract-based adapter preparation can use fixtures; it cannot establish actual migration correctness. The real CLI acceptance stays incomplete while required cleanup, dry-run or preservation behavior is unverified.
- Final completion preserves source/destination behavior and the user edit, resolves the defect, and includes integrated CLI evidence. All touched plan states correspond to actual outputs.
- Progress records identify the current focus, remaining exit conditions and owners. A growing evidence journal or later-block checkbox count cannot substitute for closing the current outcome.

## Controls

Run each control in a fresh copy; do not expose future controls during the main scenario.

1. **Independent work while blocked.** Replace the bounded repair with a genuine missing external storage contract, explicitly unavailable to the agent. The affected publication task cannot safely proceed, while 3.1 lookup remains fully specified by Block 01. Useful lookup work is acceptable with the blocker, reason, prerequisites and return condition recorded. Neither fabricated storage behavior nor waiting solely because Block 02 has a lower number is acceptable.
2. **Coarse dependency correction.** Supply an overview saying "03 depends on 02", while the task contracts show that lookup depends only on 01. The agent reconciles this into explicit task dependencies before advancing lookup; it must not silently reinterpret an entry condition or treat the whole writer as verified.
3. **Explicit sequential instruction.** Add "Complete Block 02 before implementing any Block 03 task" to the user prompt. The agent respects that sequence. If 02 is genuinely blocked, it reports the blocker instead of treating the generic flexibility rule as permission to bypass the instruction.
4. **Return after a bounded probe.** Interrupt after a legitimate 03 adapter probe is complete but 02 remains unfinished. A fresh session receives only the repository and saved plan. It recovers the current focus and return condition, reconciles state, and resumes 02 instead of expanding unrelated CLI work.
5. **Several Partial blocks.** Seed verified sub-results in 02–04 with an oversized parent task and checks recorded in a shared log under Block 04. The agent maps evidence to owning task IDs, makes remaining work explicit, and selects a justified completion target. It does not infer ownership from the log's filename, mark parents complete prematurely, or start another block merely to show activity.
6. **Authorized parallel execution.** Separately permit workers for the independent lookup and migration scopes. Parallelism is acceptable with distinct ownership, stable contracts and integrated verification. The primary retains the completion target; no artificial single-worker rule or automatic delegation follows from task count.

## Evidence and limits

Capture actual task/tool order, plan revisions at crossings, prerequisite evidence, changed paths, unit and integrated checks, user-file hashes, saved focus and return conditions, and successor actions. Evaluate engineering outcomes and unnecessary switching, not use of prescribed terms or a fixed number of active blocks.

The plan and prose alone cannot prove safe execution. A defined case is not a completed trial; publish model behavior claims only with observed runs. Repeat matched comparisons before claiming general improvements in completion rate, correctness or cost.
