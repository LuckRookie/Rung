# Case 16: Project model supports intentional product evolution

## Purpose

Test whether the Agent can revise a previously coherent Project Model when the user deliberately changes product direction, while making the resulting contracts, migration, and architecture consequences explicit.

## Fixture

Use the same kind of established fruit-catalog application as Case 14, with fruit-specific public names, attributes, inventory behavior, clients, and tests. Include a credible business decision, supplied only in the prompt, to expand the product into a fresh-produce catalog covering fruit and vegetables while preserving existing clients.

## Initial prompt

```text
我们决定把这个水果目录发展成生鲜农产品目录，第一步加入蔬菜，同时现有水果客户必须继续工作。请先更新项目画像，说明哪些核心概念、边界和兼容责任会变化，再给出可渐进实施的方案；先不要改代码。
```

## Hidden follow-up

Reveal only after the proposal reaches handoff:

```text
实施第一步：让现有水果行为保持兼容，并加入一个具有保鲜方式属性的蔬菜品种。完成集成验证和交接。
```

## Acceptable routing range

- Clarify, Inspect, Project Model, Design, Engineering Structure, and Plan are relevant to accepted direction, current contracts, concept migration, compatibility, and slices.
- Architecture Assessment is relevant only if the Agent needs a broader existing-system assessment to choose the first slice.
- Project Harness and Verification become relevant to public compatibility and shared contract evidence.
- The initial request authorizes model and design work; implementation begins with the follow-up.

## Correctness gate

- The Agent accepts the user's authorized product evolution and revises the central model toward fresh produce.
- Existing fruit contracts, names, data, and clients are mapped as compatibility obligations rather than discarded for conceptual symmetry.
- The proposed first slice introduces a coherent produce or category owner with an explicit transition path and avoids a flag-day rewrite.
- The hidden follow-up adds the vegetable capability, preserves fruit behavior, and verifies the integrated state.

## Model quality gate

- The prior model, accepted direction change, revised semantic center, stable behaviors, and open migration questions are distinguishable.
- The model guides actual data, interface, ownership, naming, and test decisions.
- Current-image fit checks remain advisory evidence and do not override an authorized product-direction change.

## Observations

Record model delta, user authority, retained contracts, renamed or generalized concepts, migration slices, new abstractions and consumers, fruit compatibility evidence, hidden follow-up locality, residual fruit-specific knowledge, persistence, context cost, and any unjustified resistance or unbounded generalization.
