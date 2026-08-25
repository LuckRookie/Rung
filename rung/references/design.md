# Design Card

Read when behavior, UX, ownership, boundaries, interfaces, data, state, errors, compatibility, or recovery need design.

## Operate

- Build from facts and accepted/delegated decisions.
- Place behavior with its owner; contain caller knowledge, SDKs, storage formats, shared state, and sequence.
- Base modules, surfaces, dependencies, and abstractions on a need, variant, unstable boundary, or stable contract.
- For human-facing surfaces, design flow, hierarchy, defaults, feedback, error prevention, recovery, consistency, accessibility, and trust.
- Prefer the smallest revisable direction supporting a runnable slice and failure checks. Read [Design Exploration](design-exploration.md) when materially different paths leave the direction under-supported.

[Project Model](project-model.md) informs uncertain identity or fit; [Engineering Structure](engineering-structure.md) informs nonlocal choices.

Stop when ownership, behavior, data, state, errors, and verification support change. Output direction, trade-offs and revisit signals.

Keep reversible choices in code, tests, or session. Persist lasting contracts, data, ownership, UX, migration, recovery, or multi-session design in its owner or `assets/solution-design.template.md`. See [Execution Model](execution-model.md).
