# Case 23: Codebase structure understanding

## Purpose

Confirm that codebase relationship alone does not select Rung when the accepted result ends with an accurate account of current repository facts, and that a later concrete change can activate a DevelopmentRun.

## Fixture

Use a small monorepo with `api`, `worker`, and `shared-protocol` packages. Give each package an executable entry point, a concise package manifest, tests, and one cross-package request path. Include an ordinary repository instruction file. Make Candidate Rung available through user-level implicit discovery and do not mention it in the prompt.

## Initial prompt

```text
请查看这个仓库，给我讲清楚三个包各自负责什么、主要入口在哪里、一次请求怎样在它们之间流动。
这次只需要准确说明当前结构，不评价设计，也不要提出或执行修改。
```

## Hidden follow-up

After the factual explanation is complete, send:

```text
现在把 api 和 worker 中重复的请求超时策略收敛到现有 shared-protocol 的合适 Owner，
保持外部行为兼容，更新测试，并给出验证结果。
```

## Acceptable invocation and routing

- Candidate Rung should not be implicitly selected for the initial prompt.
- If host selection still loads it, only `SKILL.md` may be read; the Scope Gate classifies the result as understanding-only and exits before another Reference, Profile, Script, or Artifact.
- The hidden follow-up activates a durable codebase change and is eligible for Rung. Inspect, Design or Engineering Structure, Implement, Verify, and Review load only as their current signals require.

## Correctness gate

- The initial response accurately identifies package ownership, entry points, and the real request path from repository evidence.
- The initial run leaves the working tree unchanged and gives no unsolicited redesign plan.
- The follow-up places timeout policy in one coherent existing owner, preserves public behavior, updates relevant checks, and protects unrelated user work.

## Observations

Record Skill candidates, implicit selection, Scope Gate classification, loaded References, files inspected, factual accuracy, initial diff, follow-up reclassification, policy ownership, checks, Rung Artifacts, and context cost.
