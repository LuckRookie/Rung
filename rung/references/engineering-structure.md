# Engineering Structure

Read when inspection, a change or review exposes a structural cause or affects ownership, module boundaries, public surface, dependency knowledge, shared state, data or error semantics. Keep clear local implementation defects on the ordinary path.

For a decision-ready review of an existing architecture, modularity, structural debt, or framework fit, also read [Architecture Assessment](architecture-assessment.md).

If project identity, semantic center, or feature fit is unclear, read [Project Model](project-model.md) before assigning durable owners or boundaries.

Read [Software Quality](software-quality.md) when the active concern is current touched-code fitness without a material structural mechanism. Read [Technical Debt](technical-debt.md) when a structure must be judged as a future obligation with a trigger, interest, or repayment decision.

## Governing outcome

Keep knowledge and change for a coherent behavior bounded and explainable. Judge structure by current needs, repository evidence and credible variation. Code and executable configuration implement the design; verify diagrams and prose against them.

A one-line schema or contract choice can be architectural; a large private implementation can remain contained. File length, class count, directory depth and pattern names are investigation signals.

## Ownership and change locality

- Locate the stable concept changed by the requirement and the component that currently owns its rules, state, and invariants.
- Keep code that changes for the same conceptual reason together when doing so reduces duplicated authority or caller knowledge.
- Treat a small requirement spreading through unrelated components as evidence to inspect ownership, public surface, shared state, or a missing domain concept.
- Allow several valid decompositions when each has a coherent owner and explainable dependency shape.

Names such as `utils` or `manager` invite ownership questions, not a defect verdict. Consolidate duplicated policy or unstable knowledge when justified; incidental repetition can be cheaper than a shared abstraction.

## Information hiding and public surface

- Expose the smallest caller knowledge needed to use a capability: behavior, stable data, and meaningful failures.
- Contain storage formats, SDK types, cache strategy, internal sequencing, temporary state, and replaceable algorithms unless a current contract requires them outside.
- Check whether an internal change forces callers to change. Repeated propagation can reveal information leakage or a shallow boundary.
- Keep public configuration and extension points tied to a current consumer, real variant, unstable boundary, or stable contract.

Judge an interface by complexity hidden, caller knowledge required and cost transferred.

## Dependencies and external details

- Every material dependency should have a current business, data, control, or boundary reason.
- Inspect what knowledge crosses the edge, not only the import arrow. Types, errors, lifecycle, retries, ordering, and configuration can couple modules without a direct import.
- Contain unstable infrastructure or vendor details when current variation, testability, migration, or core-policy independence justifies a boundary.
- Revisit responsibility before using registries, late imports, global lookup, callbacks, or other indirection to hide a cycle.
- Include generated code, build configuration, schemas, queue payloads, and persistence when they carry the effective contract.

Explain why stable policy knows a concrete detail and which changes that dependency serves.

## Data, state, behavior, and errors

- Model important states, valid transitions, invariants, ownership, and lifecycle explicitly enough that invalid combinations fail visibly.
- Repeated conditionals, correlated booleans, magic values, and caller-known sequencing can indicate a missing state or domain model; verify the pattern before introducing one.
- Prefer explicit inputs, outputs, and side effects when hidden mutable state expands the reasoning radius.
- Handle an error where its meaning is understood. Translate implementation failures at a boundary when callers need stable semantics; retain useful cause and context for diagnosis.
- Keep durable data and compatibility semantics separate from a convenient in-memory representation when migration or independent evolution is real.

## Abstraction evidence

Create or retain an abstraction when current evidence shows at least one useful role: a stable concept, multiple real behaviors, an unstable dependency, a public contract, or repeated knowledge that should have one owner. Record the evidence in the design or review reasoning.

Before adding a base type, factory, provider, handler layer, option, plugin point, wrapper, or generic framework, ask which present consumer or variation uses it. Prefer a direct implementation while the shape is uncertain. Before removing an existing abstraction, inspect its consumers, compatibility role, and history; unfamiliarity is not evidence of waste.

Choose functions, composition, types, packages or services by knowledge contained and coordination cost.

For a nonlocal boundary, make a small design record covering owner, caller-visible contract, hidden knowledge, state and errors, dependency direction, verification seam, and the next change it should contain. If one of these remains unknown, keep the choice provisional and name the evidence that would resolve it.

## Tests as structural evidence

- Tests should protect behavior, contracts, invariants, and meaningful failures at the boundary that owns them.
- Excessive test churn during an internal refactor can reveal leaked implementation details in tests or an unstable contract.
- A module that cannot be exercised without constructing unrelated infrastructure can reveal shared state or dependency entanglement; it can also reflect a deliberate integration boundary, so inspect the intended verification layer.
- Keep project-native format, lint, type, dependency, test, and build rules in the Project Harness. Read [Project Harness](project-harness.md) when those controls conflict or become change targets.

## Working with existing code

For a bug fix, follow the failing behavior to its rule, state or lifecycle owner and inspect relevant sibling paths. Repeated special cases, divergent copies of a rule, invalid state combinations, caller sequencing and leaked infrastructure knowledge are signals to explain the cause. Do not assume the reported location is the repair boundary.

Compare a local correction with a bounded structural repair when evidence supports both. Extend a sound owner for a local defect. If existing responsibilities, boundaries or state modeling cause the failure, include the necessary abstraction, modularization or responsibility move in the fix without waiting for an explicit refactor request. Minimize the coherent repair, including compatibility and verification cost; changed-line count alone cannot choose it.

Preserve public behavior, data and user work through checkable slices; separate structural moves from behavior changes when useful. Remove replaced policy and obsolete workarounds once consumers are accounted for. If only containment is currently safe, explain the remaining mechanism and a concrete follow-up owner or condition; do not claim the cause is removed.

Verify the reported failure, relevant sibling paths and preserved contracts at their owning boundaries. Inspect whether a credible next change would still require duplicated edits or caller knowledge; no speculative feature or framework is required. Use history only when available and relevant.

Return durable boundary decisions to Design and changed structural controls to Project Harness. Broad or risky repairs may need Plan, migration, recovery and independent Review.

## Review discipline

Elevate a local observation into a structural finding when it affects ownership, public contracts, dependency direction or knowledge, shared state, durable data, important quality goals, irreversibility, or the likely spread of future change. Keep other observations at their local priority.

Ground a material judgment in this chain:

```text
current need or credible variation
  -> repository evidence
  -> structural mechanism
  -> change cost or product risk
```

Look for counterevidence such as measured performance, compatibility, generation ownership, deployment constraints, or intentionally coupled lifecycle. Distinguish facts, risks, and hypotheses. A review may reasonably find that the inspected structure is fit for its current purpose.

Output only decisions or findings that can change the work. State the owner or boundary involved, evidence, impact, smallest coherent response, trade-offs, confidence, and a revisit signal. Keep local reversible judgments in code, tests, or the session; persist lasting contracts and architecture in their project owner.
