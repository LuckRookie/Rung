# Case 15: Existing project model is recovered from conflicting evidence

## Purpose

Test whether the Agent reconstructs a mature project's current semantic model from human intent and repository reality without treating one stale source or accidental implementation as complete authority.

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

## Acceptable routing range

- Inspect and Project Model are relevant to declared boundary, sources, public behavior, vocabulary, history, tests, dormant code, and protected work.
- Clarify is relevant only for authority conflicts that change the product conclusion or implementation direction.
- Design, Engineering Structure, Verify, and Review become relevant for the follow-up.
- Project Harness is relevant if fact-source authority or tests conflict in a way that changes project governance.

## Correctness gate

- The model identifies shared on-call coordination as the supported current center and marks the general-calendar README claim as stale or contested with concrete evidence.
- Dormant room-booking code is evidence of an experiment, not proof of an active product capability.
- Facts, inference, conflicts, unknowns, uninspected surfaces, and confidence remain visible.
- The working-tree localization change is preserved byte-for-byte.
- Temporary substitution enters the rotation owner, preserves coverage invariants, and passes relevant integrated checks.

## Model quality gate

- Evidence authority follows current user-visible behavior, accepted requirements, releases, contracts, tests, history, and code in context rather than a universal source order.
- The model remains compact enough to guide the follow-up and does not become a repository inventory.
- The follow-up uses the recovered language and invariants; it does not revive dormant calendar abstractions without current evidence.

## Observations

Record inspection radius, sources and revisions, conflict handling, model claims by status, dormant-code treatment, user-work protection, follow-up owner and files, invariants tested, Project Harness routing, persistence, context cost, and remaining uncertainty.
