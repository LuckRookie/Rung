# Case 35: Full lifecycle guidance smoke

## Purpose

Check that a single project change can move through Clarify, Inspect, Design, Plan, Implement, Verify, Review, and Release without losing ownership, evidence, or user work.

## Fixture

Use a small project with one existing capability, a focused test, a documented command, and a clean working tree. The requested change should introduce one user-visible option, touch a public boundary, and require a release artifact while remaining reversible.

## Initial prompt

```text
为这个项目增加一个可配置的导出选项。请先确认目标和约束，检查现有实现与测试，设计边界和失败行为，按需要实现、验证、复查，并准备可追踪的发布交接。保留现有接口、用户修改和回退路径。
```

## Expected lifecycle

1. Clarify accepts the outcome, authority, assumptions, and open choices.
2. Inspect establishes baseline, owner, callers, user work, commands, and affected contracts.
3. Design defines behavior, configuration, errors, compatibility, and the smallest owner boundary.
4. Plan orders dependent units and names checks and recovery points when coordination needs them.
5. Implement integrates the change and synchronizes directly coupled code, tests, and facts.
6. Verify maps claims to evidence on the integrated state and records gaps.
7. Review checks the diff, quality, structure, compatibility, evidence, and residual risk.
8. Release reports revision, artifacts, evidence, limitations, and downstream actions.

## Correctness gate

- Decisions required by this change have an owner and sufficient evidence; no eight-stage worksheet is required.
- The final behavior, failure path, and existing interface remain correct.
- Verification covers the integrated state rather than a worker or intermediate result.
- The release handoff is traceable and no external write occurs without authorization.
- A stage may be skipped or combined when its decision is already clear; the handoff still preserves its relevant facts.

## Observations

Record stages loaded, stage outputs, files changed, user work, claims and evidence, skipped or revisited stages, context cost, residual risks, and whether the next similar change has a clear owner.
