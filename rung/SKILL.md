---
name: rung
description: "Software-development harness for engineering decisions, change planning, verification and delivery. Inspect bug causes and reconcile project rules when needed."
---

# Rung

Rung supplies reusable engineering guidance through a Skill, integrated with the project's own facts, tools and controls.

Use for changes, decisions or evidence about maintained software when an engineering judgment is needed. Size alone does not qualify. Pure explanations and clear local work stay with the host; explicit Rung requests can include small software tasks. If impact is unclear, inspect first. Read [scope details](references/development-scope.md) only if needed.

An applicable project instruction requiring Rung is an explicit request within its stated scope; an informational mention is not. Reapply standing instructions to each task without expanding their scope or authority.

## Engineering judgment

- Recover intended behavior and invariants from requirements, code and tests; existing structure may need to change.
- Trace failures to rule, state or resource owners and sibling paths. Fix sound owners directly; if their boundary causes the defect, include necessary responsibility or abstraction changes without waiting for a refactor request.
- Unify rules that must agree, such as CLI and API validation of the same account ID. Similar loops with different business meanings may remain independent.
- Preserve behavior, data and user edits; retire replaced rules after checking consumers. Verify the failure, affected paths and compatibility on the final integrated state; disclose gaps or temporary containment.

One agent owns the integrated result. Use the smallest coherent change. Documents, helpers and delegation need a concrete benefit; no fixed stages are required.

## Read when it helps the next decision

- Intent or authority: [Clarify](references/clarify.md)
- Missing facts: [Inspect](references/inspect.md)
- Behavior or boundaries: [Design](references/design.md)
- Plan deliverables, decomposition or dependencies: [Plan](references/plan.md)
- Editing or integration: [Implement](references/implement.md)
- Evidence: [Verify](references/verify.md)
- Diff or architecture: [Review](references/review.md)
- Delivery: [Release](references/release.md)
- Project adoption or rule conflicts: [Project Harness](references/project-harness.md)

Read what the current decision needs and reuse loaded guidance. Allow sufficient context and verification for reliable results; avoid redundant work. [Workflow](references/workflow.md) covers interacting concerns.

Implement only when authorized; decisions and reviews can finish without edits. Report results, evidence and limits; distinguish verified work from actual publication. For blockers, name recovery and the next owner. External actions follow user authority and host policy.
