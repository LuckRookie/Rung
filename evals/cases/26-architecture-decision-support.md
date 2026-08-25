# Case 26: Architecture assessment supports a development decision

## Purpose

Ensure that narrowing automatic invocation still admits an evidence-driven assessment whose accepted result must decide whether and how to change an existing system.

## Fixture

Use a mature field-service application that currently assumes continuous connectivity in scheduling, form submission, and attachment upload. The next accepted product capability is bounded offline work for one active job. Include current contracts, state transitions, synchronization tests, production constraints, a stable API facade, and several visible local code smells unrelated to offline behavior.

## Initial prompt

```text
下个版本要支持技术员在断网时完成一个正在处理的工单，并在恢复连接后安全同步。
请审查当前架构是否能承受这项变化，找出主要结构矛盾，并建议我们在开发前应采用的最小改造方向。
先不要修改代码；这份结论将用于决定本次重构范围。
```

## Hidden follow-up

After the assessment reaches a decision-ready handoff, accept its smallest supported direction and ask the Agent to implement the first reversible slice with integrated verification.

## Acceptable invocation and routing

- Candidate Rung is eligible for implicit selection because the assessment directly governs an active versioned capability and refactoring decision.
- Inspect, Project Model when product boundaries require it, Architecture Assessment, Engineering Structure, and Review are relevant. Design Exploration loads only if several materially different paths remain credible after current constraints and scenarios are inspected.
- The initial assessment authorizes inspection and recommendations; editing starts only in the hidden follow-up.

## Correctness gate

- The assessment declares its boundary and driver, traces representative offline and recovery scenarios through actual state, data, contracts, dependencies, and verification, and identifies causal structural mechanisms.
- Visible local smells do not displace the dominant offline-data and synchronization tension without evidence.
- Recommendations state stable behavior, migration and rollback concerns, introduced risks, and evidence that would establish improvement.
- The hidden slice follows the accepted direction, remains reversible, and preserves current online behavior.

## Observations

Record metadata selection, Scope Gate predicates, loaded References, assessment boundary, primary tension, counterevidence, unsupported findings, alternatives, intervention size, hidden follow-up locality, integrated checks, and context cost.
