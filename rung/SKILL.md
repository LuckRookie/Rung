---
name: rung
description: Govern project-scoped software development to verified release. Use for code, tests, architecture, migrations, dependencies, docs, and build/release artifacts. Skip deployment-only operations, service administration, monitoring, and incidents.
---

# Rung

Add governance only for the next decision; keep work light.

## Scope gate

Before references, classify the outcome:

- **Project:** design, change, assessment, verification, or release readiness of project behavior/artifacts. Continue.
- **Runtime only:** machine/service/environment/incident state. Use host instructions; load no Rung reference or artifact.
- **Mixed:** govern project work to release handoff; separate authorization-gated runtime execution.

Use outcome/ownership; files/commands are clues. If unclear or mixed, read [Development scope](references/development-scope.md).

## Core prompts

- **Outcome:** Desired observation?
- **Context:** Relevant facts, constraints, and user changes?
- **Approach:** Smallest coherent direction?
- **Evidence:** Proof for the claim?
- **Handoff:** Delivery ready?

Keep these internal unless useful to the user.

## Operating spine

One Primary Agent owns facts, decisions, integration, verification, review, and handoff; one session by default. Read [Execution model](references/execution-model.md) for radius, persistence, recovery, delegation, or ownership.

## Signal routing

Pass the gate. Use one current reference by default; do not preload future phases. Combine only interacting concerns.

- Direction, identity, or authority: [Clarify](references/clarify.md)
- Unknown project facts/user work: [Inspect](references/inspect.md)
- Behavior, UX, ownership, boundary, data, dependencies, or errors: [Design](references/design.md)
- Dependencies, migration, collaboration, or recovery: [Plan](references/plan.md)
- Editing scope, overlap, integration, or fact sources: [Implement](references/implement.md)
- Behavior, compatibility, build, artifact, or release proof: [Verify](references/verify.md)
- Diff, structure, risk, or delivery judgment: [Review](references/review.md)
- Revision, artifact, version, note, or publication: [Release](references/release.md)

Structure: [Engineering Structure](references/engineering-structure.md). Architecture assessment: [guide](references/architecture-assessment.md). Harness changes: [Project Harness](references/project-harness.md).

Interaction: [Workflow](references/workflow.md). Depth: [Risk signals](references/risk-signals.md). State: [Artifacts](references/artifacts.md).

## Handoff

Preserve repository facts and user work. No default `.rung/` workspace. External writes need authorization. Report result, checks, uncovered scope, risk, and release state.
