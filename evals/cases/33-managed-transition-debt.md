# Case 33: Managed transition debt

## Purpose

Test whether an intentionally temporary compatibility path is treated as a bounded engineering obligation with protected behavior, propagation limits, ownership, and retirement evidence.

## Fixture

Use an authentication service migrating opaque session identifiers from version 1 to version 2. Current web and mobile releases write and read v1. The accepted target uses v2, while mobile clients can take up to ninety days to update. A single session boundary owns parsing, issuance, lookup, and error translation. The project has migration telemetry, feature flags, a release calendar, tests, and a normal issue tracker.

The requested first release needs dual-read and v2-write behavior. New modules can accidentally call the legacy decoder directly unless the transition is contained. Production deployment and traffic changes remain outside the fixture; the code, configuration, telemetry contract, tests, and Release Handoff are in scope.

## Initial prompt

```text
实现 session ID 的第一阶段迁移：新会话写 v2，迁移窗口内继续读取 v1 和 v2，公共认证行为和现有客户端保持兼容。把临时兼容义务控制在 session 边界，补齐验证、回退、观测和清理条件，并准备 Release Handoff。
```

## Hidden follow-up

Reveal only after the initial task reaches handoff:

```text
项目记录显示 v1 使用量已经连续十四天为零，九十天兼容窗口结束，支持版本均已升级。按既定条件移除 v1 路径并验证债务已经退役。
```

## Acceptable routing range

- Design, Plan, Implement, Verify, Review, Release, Software Quality, and Technical Debt are relevant as their signals become current.
- Project Harness or Verification Harness is relevant only when telemetry, shared test support, or release protection itself requires change.
- The project's issue tracker is the preferred durable home for the transition obligation.
- Deployment execution, traffic control, and live production mutation retain their external owners and authorization.

## Correctness gate

- New sessions use v2 and supported v1 sessions remain readable during the window.
- Callers receive stable authentication results and error semantics.
- Direct legacy knowledge does not spread beyond the session boundary.
- Relevant success, malformed input, expired session, lookup, rollback, and mixed-version behavior has integrated evidence.
- Telemetry distinguishes v1 reads without exposing session secrets.
- The hidden follow-up removes v1 code, flags, tests, configuration, documentation, and exceptions made obsolete by the accepted retirement evidence.

## Debt contract gate

- Borrowed value is the bounded client migration window.
- The debt-bearing construct, allowed consumers, protected behavior, time and usage triggers, exposure, spread limit, owner, rollback, and cleanup condition are explicit.
- Carrying the compatibility path is an accepted strategy during the window; new direct consumers fail the propagation limit.
- The durable item uses the project issue and has a concrete revisit or expiry condition rather than a vague TODO.
- Retirement checks the agreed telemetry window and supported-client fact, preserves v2 behavior, closes the issue or equivalent owner state, and leaves no ownerless compatibility residue.

## Observations

Record loaded References, quality goals, Debt Contract fields, project owner, compatibility callers, legacy references, telemetry contract, propagation controls, rollback, verification layers, Release state, retirement evidence, removed surfaces, residual debt, external actions, and context cost.
