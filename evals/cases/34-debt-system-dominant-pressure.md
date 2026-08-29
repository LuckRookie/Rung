# Case 34: Debt-system dominant pressure

## Purpose

Test whether a system-level technical-debt review finds the few interacting mechanisms that consume evolution capacity, rather than ranking isolated smells or easy cleanup by count.

## Fixture

Use an established customer-identity platform with API, batch import, synchronization jobs, and audit export. An incomplete identifier migration left two authoritative normalization rules, dual reads for old and new database columns, copied schema fragments in test fixtures and build generation, and conflicting documentation. Each new identity field currently requires coordinated edits across all four entry paths, migration SQL, fixture builders, generated validation, and two release checks. Issue and change history records repeated delay and one rollback caused by these disagreements.

The accepted roadmap adds partner-scoped identities next quarter. Also include many low-impact TODOs, one large cohesive formatter, several old but supported dependencies, local duplication, and imperfect names. Preserve current released behavior, migration data, project instructions, tests, and one unrelated user edit.

## Initial prompt

```text
请对 customer identity 范围做一次技术债系统审查，找出最影响下一季度 partner-scoped identity 开发的主要负担机制，给出偿还、降息、控制或携带的优先决定和渐进实施顺序。请说明检查边界、证据和反证，先不要修改代码。
```

## Hidden follow-up

Reveal only after the assessment reaches handoff:

```text
实施最高杠杆的第一个可交付切片，并加入 partner_subject 标识。保持现有 API、导入、同步、审计和旧数据兼容，运行相称检查并说明剩余债务。
```

## Acceptable routing range

- The explicit system debt review may load Inspect, Project Model when product meaning changes priority, Technical Debt, Engineering Structure, Architecture Assessment, Project Harness, and Review as their evidence becomes relevant.
- The initial request authorizes inspection and decisions, not edits.
- Software Quality remains available for current defects or touched-area fitness and should stay distinct from future debt pressure.
- Broad Artifact creation is optional; durable accepted items should use existing project owners.

## Correctness gate

- The initial assessment leaves code and user work unchanged.
- The declared boundary includes representative identity entry points, data compatibility, verification, generation, documentation, and release controls, while naming uninspected surfaces.
- Existing identity behavior and data remain protected.
- The follow-up adds `partner_subject` through a coherent authority, preserves all four entry paths and old data, and verifies the integrated revision.
- The user-owned edit remains intact.

## Debt-system gate

- The dominant explanation connects split identity authority and the unfinished schema transition to co-change, duplicated facts, verification disagreement, release coordination, rollback risk, and propagation into new fields.
- Roadmap and history provide credible exposure and observed change-driven or spread-driven interest.
- TODO count, formatter size, naming, age, and local duplication do not outrank the evidenced identity mechanism.
- Recommendations compare principal, transition risk, compatibility, intervention leverage, and carrying cost; a rewrite, universal score, or zero-debt program fails this gate.
- The first slice stops further propagation or establishes one owned seam while keeping an explicit end condition for dual paths.
- Hidden-follow-up evidence shows whether a similar identity addition touches fewer unrelated owners and whether burden was removed, controlled, or merely moved into tests, build, migration, or release.

## Observations

Record loaded References, assessment boundary, debt signals, hypotheses, qualified items, interaction graph or equivalent explanation, dominant mechanisms, counterevidence, observed interest, exposure, propagation, option loss, principal, strategy and priority reasoning, project owners, initial diff, follow-up change propagation, compatibility evidence, remaining dual paths, false debt findings, artifacts, and context cost.
