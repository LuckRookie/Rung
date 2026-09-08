# Design Card

Read when behavior, UX, ownership, interfaces, data, state, errors, compatibility, or recovery need design.

## Operate

- Use facts and accepted/delegated decisions.
- Place behavior with its owner; contain caller, SDK, format, state, and sequence knowledge.
- Base modules, surfaces, dependencies, and abstractions on a need, variant, unstable boundary, or stable contract.
- For material quality trade-offs, read [Software Quality](software-quality.md).
- For human-facing surfaces, design flow, hierarchy, defaults, feedback, error prevention, recovery, consistency, accessibility, and trust.
- Prefer a runnable slice and failure checks. Read [Design Exploration](design-exploration.md) when paths remain unresolved.

[Architecture Design](architecture-design.md) for new system boundaries; [Project Model](project-model.md) for fit; [Engineering Structure](engineering-structure.md) informs nonlocal choices; [Technical Debt](technical-debt.md) governs future obligations.

Stop when ownership, behavior, state, errors, and verification support change. Output direction, trade-offs, and revisit signals.

Keep reversible choices local; persist lasting design in its owner or `assets/solution-design.template.md`. See [Execution Model](execution-model.md).
