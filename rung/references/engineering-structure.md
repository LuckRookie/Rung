# Engineering Structure

Read when a change or review can alter concept ownership, module boundaries, public surface, dependency knowledge, shared state, data or error semantics, an external-detail boundary, or an abstraction with more than local effect. Keep a local edit on the ordinary path when its owner and impact are already clear.

For an explicit review of an existing architecture, modularity, structural debt, or framework fit, also read [Architecture Assessment](architecture-assessment.md).

If project identity, semantic center, or feature fit is unclear, read [Project Model](project-model.md) before assigning durable owners or boundaries.

## Governing outcome

Keep the knowledge and change required for a coherent behavior bounded and explainable. Judge structure by the current product, repository, credible variation, and important quality goals. Source code and executable configuration are the implemented design; diagrams and prose are useful claims to verify against them.

Consider both scale and significance. A one-line schema, dependency, or public-contract choice can be architectural. A large private implementation can remain well contained. File length, class count, directory depth, pattern names, and visual symmetry are discovery signals rather than design verdicts.

## Ownership and change locality

- Locate the stable concept changed by the requirement and the component that currently owns its rules, state, and invariants.
- Keep code that changes for the same conceptual reason together when doing so reduces duplicated authority or caller knowledge.
- Treat a small requirement spreading through unrelated components as evidence to inspect ownership, public surface, shared state, or a missing domain concept.
- Allow several valid decompositions when each has a coherent owner and explainable dependency shape.

Names such as `common`, `shared`, `utils`, `manager`, or `helpers` warrant a question about ownership; their names alone do not establish a defect. Duplication warrants structural action when it duplicates policy or unstable knowledge. Incidental repetition can be cheaper than a premature shared abstraction.

## Information hiding and public surface

- Expose the smallest caller knowledge needed to use a capability: behavior, stable data, and meaningful failures.
- Contain storage formats, SDK types, cache strategy, internal sequencing, temporary state, and replaceable algorithms unless a current contract requires them outside.
- Check whether an internal change forces callers to change. Repeated propagation can reveal information leakage or a shallow boundary.
- Keep public configuration and extension points tied to a current consumer, real variant, unstable boundary, or stable contract.

A simple interface is not automatically valuable. Judge the complexity hidden, the knowledge required to use it correctly, and the cost it transfers into implementations or callers.

## Dependencies and external details

- Every material dependency should have a current business, data, control, or boundary reason.
- Inspect what knowledge crosses the edge, not only the import arrow. Types, errors, lifecycle, retries, ordering, and configuration can couple modules without a direct import.
- Contain unstable infrastructure or vendor details when current variation, testability, migration, or core-policy independence justifies a boundary.
- Revisit responsibility before using registries, late imports, global lookup, callbacks, or other indirection to hide a cycle.
- Include generated code, build configuration, schemas, queue payloads, and persistence when they carry the effective contract.

Core logic need not follow a universal inward-dependency diagram. The project must be able to explain why stable policy knows a concrete detail and what future change that choice optimizes.

## Data, state, behavior, and errors

- Model important states, valid transitions, invariants, ownership, and lifecycle explicitly enough that invalid combinations fail visibly.
- Repeated conditionals, correlated booleans, magic values, and caller-known sequencing can indicate a missing state or domain model; verify the pattern before introducing one.
- Prefer explicit inputs, outputs, and side effects when hidden mutable state expands the reasoning radius.
- Handle an error where its meaning is understood. Translate implementation failures at a boundary when callers need stable semantics; retain useful cause and context for diagnosis.
- Keep durable data and compatibility semantics separate from a convenient in-memory representation when migration or independent evolution is real.

## Abstraction evidence

Create or retain an abstraction when current evidence shows at least one useful role: a stable concept, multiple real behaviors, an unstable dependency, a public contract, or repeated knowledge that should have one owner. Record the evidence in the design or review reasoning.

Before adding a base type, factory, provider, handler layer, option, plugin point, wrapper, or generic framework, ask which present consumer or variation uses it. Prefer a direct implementation while the shape is uncertain. Before removing an existing abstraction, inspect its consumers, compatibility role, and history; unfamiliarity is not evidence of waste.

Composition, delegation, inheritance, functions, traits, protocols, packages, and services are possible mechanisms. Choose the mechanism that contains relevant knowledge with the least new coordination burden for this project.

## Tests as structural evidence

- Tests should protect behavior, contracts, invariants, and meaningful failures at the boundary that owns them.
- Excessive test churn during an internal refactor can reveal leaked implementation details in tests or an unstable contract.
- A module that cannot be exercised without constructing unrelated infrastructure can reveal shared state or dependency entanglement; it can also reflect a deliberate integration boundary, so inspect the intended verification layer.
- Keep project-native format, lint, type, dependency, test, and build rules in the Project Harness. Read [Project Harness](project-harness.md) when those controls conflict or become change targets.

## Working with existing code

Extend a sound current owner when it can absorb the behavior coherently. When the existing boundary creates the problem, separate the structural move from behavior change as far as useful evidence and project risk allow. Preserve public behavior, persistent data, user work, and compatibility through small checkable slices.

Use recent changes, issue history, co-change patterns, callers, dependency paths, and tests when a claim concerns frequency or propagation. Use them only when available and relevant; do not manufacture historical certainty from the current tree.

When actual code reveals a structural decision with durable consumers, route it back to Design. When a structure rule, dependency check, generated boundary, or test policy must change, route to Project Harness. Broad or risky changes may need Plan, migration, recovery, and independent Review.

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
