# Work Type, Risk, and Depth

Read when work type, risk, or evidence scope can materially change the next decision.

## Work cues

| Type | Distinct focus |
|---|---|
| Greenfield | first value, minimum runnable slice, known boundaries, first release |
| Feature | observable behavior, interface/data impact, regression |
| Bugfix | expected versus actual, reproduction, root cause, regression evidence |
| Refactor | preserved behavior, characterization, structural gain |
| Migration | current/target state, compatibility window, order, recovery |
| Dependency | API change, advisory, lock state, build compatibility |
| Docs/Config | agreement with actual behavior |
| Release-only | revision, evidence, artifact, version, notes |

Types are routing hints and may overlap.

## Depth hints

- **[Lite](../profiles/lite.md):** local, reversible, understood impact; conversational context and targeted checks.
- **[Standard](../profiles/standard.md):** multiple files/modules, new module, coordination, or recovery; selective plan and broader evidence.
- **[Strict](../profiles/strict.md):** public contract, security/privacy, persistent data, migration, core architecture, or release chain; explicit design, recovery, and stronger evidence.

Apply depth locally. Increase attention for public APIs or schemas; auth, secrets, or sensitive data; new top-level modules, shared state, core dependencies, or direction changes; migration or rollback; build/package/signing changes; major dependency upgrades; uncertain impact; weak compatibility evidence; overlapping user work; or cross-session coordination.

Harness maintenance can stay Lite. Shared fixtures, authority, or execution often merit Standard depth. Framework, architecture-rule, required-CI, or release-policy evolution may merit Strict attention at that boundary.

Governance depth and evidence scope are independent. Evidence may range from Tier 0 target/syntax checks, through Tier 1 local behavior and Tier 2 integration/contract/build checks, to Tier 3 release matrices and packaging. Claims and risk select the scope.
