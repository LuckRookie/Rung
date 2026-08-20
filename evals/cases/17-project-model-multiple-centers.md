# Case 17: Project model preserves multiple semantic centers

## Purpose

Test whether the Agent chooses a useful model boundary in a repository that contains several related products, instead of forcing every package into one vague identity.

## Fixture

Use a monorepo owned by one company with three products: a customer support inbox, an internal analytics pipeline, and a shared identity library. They share build tooling, authentication contracts, and release infrastructure. Each product has distinct users, workflows, domain concepts, data, and release cadence. The root README describes the company platform broadly; package documentation and public entry points are current.

## Initial prompt

```text
请给这个仓库建立项目画像，并用它指导后续模块划分。先说明画像边界、共享部分和仍然独立的产品中心，不要修改代码。
```

## Hidden follow-up

Reveal only after the assessment reaches handoff:

```text
客户支持产品现在需要按团队查看首次响应时间。设计并实现这个功能，复用真正共享的能力，同时避免把支持领域逻辑放进分析流水线或身份库。
```

## Acceptable routing range

- Inspect and Project Model are relevant to repository boundary, products, public entry points, users, shared contracts, tooling, and ownership.
- Architecture Assessment is relevant if the user expects a repository-level structural judgment; Engineering Structure and Design are relevant for the follow-up.
- A durable model is reasonable when several maintainers or future decisions consume it. A single universal domain ontology has no support from the fixture.

## Correctness gate

- The Agent identifies three semantic centers and distinguishes shared identity contracts and infrastructure from product-domain ownership.
- The root platform description is treated at its useful organizational level without erasing package-level product models.
- The response states the model boundary and uninspected surfaces.
- First-response-time behavior enters the support product's concepts and interfaces; analytics may consume a stable event or result but does not become the rule owner.
- Existing identity and build contracts remain compatible and the integrated checks pass.

## Model quality gate

- The model supports hierarchy or composition where repository evidence warrants it.
- Shared tooling, repository location, or organizational ownership does not independently establish one product identity.
- The hidden follow-up demonstrates coherent ownership and limited cross-product knowledge.

## Observations

Record models and scopes formed, shared facts, forced generalizations, architecture inventory size, support-rule owner, events or APIs added, dependency edges, files changed across products, test location, persistence choice, context cost, and model revisions after implementation evidence.
