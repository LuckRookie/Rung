# Case 31: High-quality code carries active technical debt

## Purpose

Test whether current software quality and future engineering burden remain independent when clean, correct, well-tested code depends on an expiring platform.

## Fixture

Use a maintained payment service with a cohesive `LegacyPay` adapter. The adapter has a stable project-owned interface, clear names and errors, complete contract tests, reliable diagnostics, and no known current defect. Four callers depend only on that interface.

Repository facts include a vendor notice that API v1 becomes unsupported in sixty days, an accepted roadmap item for recurring mandates available only in v2, and measured integration evidence showing that v2 changes idempotency keys, pagination, and declined-payment error semantics. The current release remains supported today. No migration issue, owner, or compatibility plan exists.

## Initial prompt

```text
请评估 LegacyPay 这部分是否需要进入近期改造，并形成能够指导实际迁移的决定。当前支付行为必须继续可靠，六十天后的供应商停止支持和下一版 recurring mandates 也要进入判断。先不要修改代码。
```

## Hidden follow-up

Reveal only after the decision reaches handoff:

```text
按已接受方案实施第一个可交付迁移切片：建立并验证 v2 路径，同时让现有调用方继续通过项目自己的支付契约工作。保留清楚的回退和旧路径清理条件。
```

## Acceptable routing range

- The initial result is a concrete development decision and enters Rung without authorizing edits.
- Inspect, Design, Technical Debt, Plan, and Verify may be relevant according to the current decision.
- Software Quality may confirm current fitness but should not absorb the EOL obligation.
- Engineering Structure is relevant only for a real adapter, contract, or dependency-knowledge change.
- A durable item should use the project's issue or migration owner when one is established; `.rung/` and a parallel debt register remain optional.

## Correctness gate

- The initial assessment leaves the working tree unchanged.
- It acknowledges the adapter's current correctness, clarity, verifiability, and operability.
- It identifies v1 support expiry and the accepted v2-only capability as credible triggers.
- The follow-up preserves the project-owned caller contract and current payment behavior, verifies materially changed v2 semantics, and provides a bounded rollback.
- Old v1 code remains only under an explicit compatibility or cleanup condition.

## Debt qualification gate

- The qualified item identifies the current v1 dependency, affected boundary and consumers, time-driven exposure, support and option-loss interest, likely propagation, principal, and repayment risk.
- Borrowed value or current compatibility value is visible without lowering the urgency created by the deadline.
- The strategy compares deliberate carrying with a staged migration and selects an action from evidence rather than a universal score.
- Current quality does not erase the debt finding, and the debt label does not invent a current product defect.
- Owner, revisit or activation point, compatibility window, and retirement evidence are clear enough for a future consumer.

## Observations

Record loaded References, current-quality result, debt confidence state, trigger, exposure, interest type, propagation, option loss, principal range, strategy, owner, persistence location, protected claims, migration slices, rollback, cleanup condition, follow-up diff, integrated evidence, and context cost.
