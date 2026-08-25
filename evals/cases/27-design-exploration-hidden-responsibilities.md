# Case 27: Design exploration discovers hidden responsibilities

## Purpose

Test whether Rung expands a consequential but under-supported design space through representative behavior before choosing modules and abstractions, then hands a coherent direction to implementation.

## Fixture

Use an existing literature application where search and metadata acquisition are stable. A small rule-based component can download open PDF URLs. The project has no browser automation, login-state model, fallback coordinator, or durable acquisition-attempt state. Preserve current project facts, tests, and an unrelated user edit across variants.

## Initial prompt

```text
我要为这个项目设计 PDF acquisition 子系统，先不要实现。

已经确定：上游会提供文献 metadata；常规规则式下载先执行；失败后可以使用 AI browser 尝试从站点获得 PDF；
AI browser 是 fallback。登录态、人工介入、重试、失败分类、状态、模块边界和接口还没有确定。

请先把这项重要设计想清楚。用户需要决定的内容用通俗结果说明，其余专业选择你可以作为项目设计师决定。
```

## Hidden follow-up

After the design handoff, reveal:

```text
首个版本必须支持浏览器在需要登录时暂停同一次 acquisition，等待用户完成登录后继续；
用户也可以取消，取消或重试都不能产生重复 PDF 记录。常规下载路径仍应保持无浏览器依赖。
按照前面接受的方向实现最小可运行切片并验证。
```

## Acceptable routing range

- The request has an active subsystem-design Claim and is eligible for Rung.
- Inspect and Design Exploration are relevant. Clarify is relevant for consequential human choices; Project Model loads only if project identity, subsystem fit, or semantic center can change the decision.
- Design and Engineering Structure consume the accepted exploration. Plan, persistent artifacts, Workers, and independent Review remain signal-driven.

## Correctness gate

- The initial run leaves implementation unchanged and states the exact decision and uncertainty boundary.
- Representative scenarios expose ordinary success, fallback activation, access denial or login, interruption, cancellation, retry, duplicate prevention, and observable acquisition results only to the extent needed to distinguish directions.
- Accepted, evidenced, inferred, contested, and unknown statements remain distinguishable where consequential.
- Candidate directions differ in ownership, state, contracts, dependencies, UX, failure semantics, or recovery; cosmetic class arrangements do not inflate the option count.
- The recommendation identifies assumptions, trade-offs, evidence needs, owned Unknowns, and revisit signals, then stops when Design can proceed.
- The hidden follow-up fits the discovered responsibilities and state model without spreading browser knowledge into the ordinary rule-based path or duplicating PDF records.

## Exploration quality gate

- The Agent does not commit to module boundaries before behavior exposes their responsibilities.
- User questions are limited to choices that change product meaning, material UX, durable data, accepted risk, or authority.
- No fixed scenario count, fixed alternative count, generic plugin platform, browser abstraction family, Discovery document, or `.rung/` workspace appears without a current reason.
- Verification covers pause/resume/cancel/idempotency behavior at the lowest reliable boundaries and the integrated slice.

## Observations

Record loaded References and order, decision boundary, scenarios, discovered responsibilities and states, failure semantics, questions, candidate consequences, premature convergence, unsupported abstractions, stop point, persistence, hidden follow-up locality, checks, user-work preservation, and context cost.
