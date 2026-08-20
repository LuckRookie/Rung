# Case 14: Project model governs feature fit

## Purpose

Test whether a Project Model gives the Agent a practical boundary for accepting, isolating, escalating, or declining a superficially related feature.

## Fixture

Use an established fruit-catalog application for small produce shops. Its accepted product document, user flows, public API, data model, and tests center on fruit variety, season, origin, availability, and fruit inventory. The repository has no generic merchandise contract. Preserve the exact project facts and history across variants.

## Initial prompt

```text
请先根据这个项目的文档、实际行为和代码，给我一个通俗、简短的项目画像。然后判断“把蔬菜加入目录”是否适合这个项目；先给判断和影响，不要修改代码。
```

## Hidden follow-up

Reveal only after the judgment reaches handoff:

```text
我们继续保持水果目录这个定位。现在增加“水果礼盒”，礼盒可以包含多个现有水果品种，并保持原有库存和查询行为。完成实现和相关验证。
```

## Acceptable routing range

- Inspect, Clarify, and Project Model are relevant to accepted purpose, observed behavior, vocabulary, users, boundaries, and authority.
- Design and Engineering Structure become relevant when judging or implementing concept ownership, data relationships, public surface, and compatibility.
- Architecture Assessment is unnecessary unless the user broadens the request into a system assessment or the repository reveals a material structural problem.
- The initial request authorizes inspection and advice only.

## Correctness gate

- The Project Model is grounded in named repository sources and describes the fruit catalog in plain language.
- Adding vegetables is recognized as changing the current semantic center toward a broader produce catalog; the response explains direct user, data, API, naming, and ownership consequences.
- The Agent does not create an unsupported generic product hierarchy solely to make vegetables fit.
- The fruit-basket follow-up is recognized as a current-model extension, implemented through coherent fruit and inventory ownership, and verified without breaking existing behavior.

## Model quality gate

- Canonical capabilities, adjacent extensions, and identity-changing probes are used as decision evidence rather than category slogans.
- A user can understand the recommendation, reversibility, and product-direction decision before reading technical details.
- The hidden follow-up demonstrates that the model can admit a new concept when it reinforces the current users and semantic center.

## Observations

Record sources inspected, accepted and inferred model statements, vegetable classification and rationale, clarification requested, abstractions proposed, basket owner and dependencies, public and data changes, tests, follow-up locality, context cost, and whether the Agent used the model to justify incompatible overgeneralization.
