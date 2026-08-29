---
name: rung
description: Govern active software development whose outcome is a durable codebase change, a decision directing one, or readiness to release one. A codebase relationship alone does not activate this skill.
---

# Rung

## Scope gate

Before references, require a **codebase relationship** and an **active development claim**: the outcome concerns a maintained codebase or coupled artifact and changes it durably, directs a concrete change, or proves a current change or release.

- **Development:** both hold; continue.
- **Understanding only:** codebase facts are the endpoint; load no Rung reference or artifact.
- **Outside:** no relationship; load no Rung reference or artifact.
- **Mixed:** govern the active development portion only.

Relationship, repository, path/type, tool, or incidental code alone is insufficient. For material claim or ownership ambiguity, read [Development scope](references/development-scope.md).

## Core prompts

- **Outcome:** Desired observation?
- **Context:** Relevant facts, constraints, and user changes?
- **Approach:** Smallest coherent direction?
- **Evidence:** Proof for the claim?
- **Handoff:** Delivery ready?

Keep these internal unless useful.

## Operating spine

One Primary Agent owns the run and handoff; one session by default. For radius, persistence, recovery, or delegation, read [Execution model](references/execution-model.md).

## Signal routing

Pass the gate. Use one current reference by default; do not preload future phases. Combine only interacting concerns.

- Direction, identity, authority: [Clarify](references/clarify.md)
- Missing facts/user work: [Inspect](references/inspect.md)
- Behavior, UX, ownership, data, errors: [Design](references/design.md)
- Migration, collaboration, recovery: [Plan](references/plan.md)
- Editing, overlap, integration: [Implement](references/implement.md)
- Behavior, compatibility, release proof: [Verify](references/verify.md)
- Diff, structure, risk, delivery: [Review](references/review.md)
- Revision, artifact, publication: [Release](references/release.md)

Unresolved paths: [Design Exploration](references/design-exploration.md). Quality: [Software Quality](references/software-quality.md). Debt: [Technical Debt](references/technical-debt.md). Structure: [Engineering Structure](references/engineering-structure.md). Architecture: [Architecture Assessment](references/architecture-assessment.md). Harness: [Project Harness](references/project-harness.md).

Interaction: [Workflow](references/workflow.md). Depth: [Risk signals](references/risk-signals.md). State: [Artifacts](references/artifacts.md).

## Handoff

Preserve facts/user work. No default `.rung/` workspace. External writes need authorization. Report result, evidence, risk, and release state.
