---
name: rung
description: Govern tasks whose primary accepted outcome designs, creates, changes, assesses, verifies, or releases a software codebase or an artifact whose correctness and lifecycle are coupled to it. Repository presence, location, tools, and incidental code do not establish scope.
---

# Rung

Govern only the next decision; keep work light.

## Scope gate

Before references, establish a positive codebase relationship for the accepted outcome:

- **Codebase:** the outcome concerns the codebase or an artifact coupled to it in correctness and maintenance. Continue.
- **Outside:** no relationship. Load no Rung reference or artifact; continue with the Host.
- **Mixed:** govern the qualifying codebase portion; leave the rest with its owner.

Repository, path/type, tool use, and incidental code are insufficient. Read [Development scope](references/development-scope.md) only if materially ambiguous.

## Core prompts

- **Outcome:** Desired observation?
- **Context:** Relevant facts, constraints, and user changes?
- **Approach:** Smallest coherent direction?
- **Evidence:** Proof for the claim?
- **Handoff:** Delivery ready?

Keep these internal unless useful.

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
