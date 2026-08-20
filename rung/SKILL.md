---
name: rung
description: Guide software work from intent through a verified release with progressive governance. Use for projects, features, fixes, refactors, migrations, dependency or configuration changes, and release preparation.
---

# Rung

Add governance only when it improves the next decision. Keep ordinary work lightweight.

## Core prompts

- **Outcome:** What result should the user observe?
- **Context:** Which facts, constraints, and existing changes matter?
- **Approach:** What is the smallest coherent direction?
- **Evidence:** Which observations support completion?
- **Handoff:** Are code, docs, version, and risks ready for this delivery?

Handle these internally when possible. Surface only useful decisions and evidence.

## Operating spine

One Primary Agent owns each DevelopmentRun. Ground the outcome and target facts, resolve consequential decisions, coordinate when useful, integrate, verify and review the combined state, then hand off. Default to one session.

Read [Execution model](references/execution-model.md) for inspection radius, durable design, recovery, delegation, review, or ownership.

## Signal routing

Read the most relevant reference; add another only when evidence creates a new need.

- Direction needs user collaboration or delegated authority: [Clarify](references/clarify.md)
- Relevant code, rules, commands, interfaces, dependencies, facts, or user work are unknown: [Inspect](references/inspect.md)
- Behavior, UX, skeleton, ownership, boundaries, data, dependencies, or errors need design: [Design](references/design.md)
- Dependent units, migration, collaboration, or recovery need coordination: [Plan](references/plan.md)
- Editing raises scope, overlap, integration, or fact-source concerns: [Implement](references/implement.md)
- Behavior, compatibility, build, artifact, or release claims need evidence: [Verify](references/verify.md)
- The integrated diff, structure, risk, or delivery deserves another look: [Review](references/review.md)
- A revision, artifact, version, note, or publication is being prepared: [Release](references/release.md)

If instructions, docs, checks, build, CI, or release rules may change, read [Project Harness](references/project-harness.md).

For interacting concerns read [Workflow](references/workflow.md), for depth [Risk signals](references/risk-signals.md), and for durable state [Artifacts](references/artifacts.md).

## Handoff

Repository facts lead. Preserve user work. Create no `.rung/` workspace by default. Use assets, helpers, sessions, and workers only when useful. External writes require authorization and host permission.

Report the result, checks run, uncovered scope, residual risk, and release state proportionally.
