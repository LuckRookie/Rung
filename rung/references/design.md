# Design Card

Read when behavior, UX, ownership, boundaries, interfaces, data, state, dependencies, errors, compatibility, or recovery need design.

## Operate

- Build from inspected facts, user decisions, and delegated scope.
- Place behavior with its owning concept; contain caller knowledge, SDKs, storage formats, shared state, and sequence.
- Give modules, public surfaces, dependencies, and abstractions current evidence from a need, variant, unstable boundary, or stable contract.
- For human-facing surfaces, design flow, hierarchy, defaults, feedback, error prevention, recovery, consistency, accessibility, and trust.
- Prefer the smallest revisable direction supporting a runnable slice and failure checks.

Read [Project Model](project-model.md) when identity or feature fit is uncertain, and [Engineering Structure](engineering-structure.md) for nonlocal choices.

Stop when ownership, behavior, data, state, errors, and verification support safe change. Output the direction, trade-offs, and revisit signals.

Keep reversible choices in code, tests, or session. Persist lasting contracts, data, ownership, UX, migration, recovery, or multi-session design in its owner or `assets/solution-design.template.md`. Read [Execution Model](execution-model.md) for authority and persistence.
