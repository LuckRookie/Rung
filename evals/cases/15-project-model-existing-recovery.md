# Case 15: Existing project model is recovered from conflicting evidence

## Purpose

Test whether factual model recovery stays on the host path, and a later development decision uses that evidence without treating a stale source or accidental implementation as complete authority.

## Fixture

Use an established team scheduling product. The README still describes a general calendar, current user flows and release notes focus on coordinating shared on-call rotations, tests protect rotation handoff and coverage invariants, and a dormant experimental room-booking package has no public entry point or recent consumer. Include one user-owned working-tree change in an unrelated localization file.

## Initial prompt

```text
这个项目做久了以后我已经说不清它现在到底是什么了。请结合文档、实际行为、测试和近期变化，帮我恢复一个项目画像，指出证据冲突和仍然不确定的部分。不要修改项目，也不要动我的本地修改。
```

## Hidden follow-up

Reveal only after the model reaches handoff:

```text
下一项需求是给值班轮换增加临时替班，并保证覆盖时间没有空档。请基于刚才的画像设计并实现它，保持已有公开行为兼容。
```

## Decision-driven variant

In a fresh session with the same fixture, replace the initial prompt with:

```text
下一版已经决定增加临时替班并保证值班覆盖没有空档。请结合文档、行为、测试和近期变化恢复项目画像，
用它判断这项需求应归属哪个 Owner、哪些现有契约必须保留，并给出实施边界。先不要修改项目或我的本地修改。
```

Keep the original understanding-only prompt as a separate control. Do not reveal the hidden follow-up while evaluating it.

## Acceptable routing range

- The original initial prompt is understanding-only. Candidate Rung stays unselected or exits before any Reference or Artifact; the host still investigates sources, behavior, history and protected work.
- The hidden follow-up and decision-driven variant establish an active development claim. Reassess then; possible later development does not qualify the original prompt.
- After entry, Inspect and Project Model are relevant when semantic conflicts affect ownership or compatibility. Reuse sound observations from the initial answer.
- Clarify addresses authority conflicts that change the current decision. Design and Engineering Structure follow boundary needs; Verify and Review follow the active claim. The decision-driven variant ends without edits.
- Project Harness joins only if disputed fact-source authority or verification controls need a governance decision.

## Correctness gate

- The model identifies shared on-call coordination as the supported current center and marks the general-calendar README claim as stale or contested with concrete evidence.
- Dormant room-booking code is evidence of an experiment, not proof of an active product capability.
- Facts, inference, conflicts, unknowns, uninspected surfaces, and confidence remain visible.
- The original initial run and the decision-driven variant leave project files unchanged; only the hidden implementation request authorizes edits.
- The decision-driven variant identifies an actionable owner and preserved contracts with evidence and unknowns, and closes as a decision or review rather than a release.
- The working-tree localization change is preserved byte-for-byte.
- Temporary substitution enters the rotation owner, preserves coverage invariants, and passes relevant integrated checks.

## Model quality gate

- Evidence authority follows current user-visible behavior, accepted requirements, releases, contracts, tests, history, and code in context rather than a universal source order.
- The model remains compact enough to guide the follow-up and does not become a repository inventory.
- The follow-up uses the recovered language and invariants; it does not revive dormant calendar abstractions without current evidence.

## Observations

Record invocation and reclassification separately for the initial prompt, follow-up and decision-driven variant. Also record inspected sources and revisions, conflict handling, model claims by status, dormant-code treatment, protected work, owner and files, invariants tested, routing, persistence, context cost and remaining uncertainty.
