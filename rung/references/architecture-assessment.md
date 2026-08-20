# Architecture Assessment

Read for an explicit assessment of an existing project's architecture, code organization, modularity, structural debt, dependency shape, framework fit, or proposed architecture improvement. Also read [Engineering Structure](engineering-structure.md) for the shared design lenses.

Use an accepted [Project Model](project-model.md) when available; recover one when product identity, semantic center, or feature fit can change the assessment.

An assessment request authorizes inspection and recommendations. Edit the project only when the user also requests change or delegates that next action.

## Assessment contract

Architecture quality is relative to what the project must do and what it must be able to change, preserve, or withstand. Establish the smallest useful assessment contract from repository facts and the user's request:

- the system or subsystem boundary included;
- current product or business drivers;
- credible upcoming changes and known pain;
- the quality goals that can change the judgment, such as modifiability, correctness, data integrity, reliability, performance, security, privacy, compatibility, usability, build or delivery behavior;
- applicable project constraints, user-owned work, and authority to recommend or implement;
- important surfaces left uninspected.

Use a declared System inspection radius for a broad audit. "Review the repository" does not prove complete coverage. If drivers are missing and the user delegates judgment, infer cautiously from requirements, issues, public contracts, tests, history, and release shape; expose assumptions that affect priority.

Do not evaluate every quality attribute by default. Select the ones supported by the request and project evidence. A structure that improves one goal may trade against another, so preserve relevant performance, compatibility, security, operational, and organizational constraints.

## Select evidence around scenarios

Use concrete scenarios to make architecture claims testable. A useful scenario identifies a stimulus or change, the affected environment or boundary, the expected response, and the consequence that matters. Prefer current work, recurring changes, incidents, planned features, required failures, or high-impact quality goals over invented futures.

Possible probes include:

- add or alter one representative capability;
- replace or add an external system;
- change a public contract or durable data rule;
- trace a critical request, job, event, or failure path;
- isolate or recover from a relevant failure;
- satisfy a measured performance, security, compatibility, or release constraint.

Choose only enough probes to expose the highest-value tensions. Use issue and change history when the judgment depends on change frequency or co-change. Use benchmarks, incident evidence, runtime configuration, or delivery controls when they determine the trade-off. More context can dilute the review; retrieve evidence for the current hypothesis and expand when it changes the judgment.

## Recover the implemented structure

Treat project documentation as a map and set of claims. Confirm material claims against code, schemas, dependency manifests, generated sources, configuration, build and delivery paths, and tests.

Recover only the views needed for the assessment:

- entry points and caller-visible capabilities;
- stable product concepts and their current owners;
- public and inter-module contracts;
- important data, state, error, and control flow;
- dependency knowledge, including types and semantics crossing boundaries;
- external systems and persistent formats;
- verification and Project Harness boundaries when they affect change confidence;
- team or maintainer ownership when repository evidence provides it.

Trace representative vertical paths into implementation. Architecture is realized in code, yet every local detail need not become an architecture finding. Raise a detail when it changes structural significance: ownership, public surface, dependency knowledge, shared state, durable semantics, an important quality goal, irreversibility, or future change propagation.

## Diagnose mechanisms, not labels

Generate candidate explanations from observed symptoms, then verify how each mechanism creates cost or risk. Examples of mechanisms include:

- one rule or invariant has several authoritative owners;
- callers must know an internal format, lifecycle, ordering, or vendor semantic;
- shared mutable state creates hidden coordination;
- a missing state or domain model produces invalid combinations and repeated branches;
- a public surface exposes speculative options or unstable implementation details;
- a dependency cycle reflects misplaced responsibility;
- a local change crosses unrelated components because ownership and concept boundaries differ;
- generated, documented, tested, and executed contracts have drifted;
- the architecture cannot demonstrate a required quality scenario within its current Harness.

Terms such as coupling, cohesion, layering, technical debt, god object, or framework leakage summarize a mechanism; they do not establish it. A large file, repeated code, unusual pattern, direct dependency, or flat directory is a lead to inspect. Verify who changes, who knows, and what consequence follows.

For each material finding, form an evidence chain:

```text
driver or change scenario
  -> repository evidence
  -> structural mechanism
  -> observable cost or risk
  -> smallest coherent intervention
  -> independent verification
```

If a link is unknown, label the result as a risk or hypothesis and state what evidence would resolve it. Avoid filling the gap with an unstated requirement or a generic best practice.

## Find the dominant tensions

Prioritize findings by judgment rather than a universal numeric score:

- **Relevance:** current work, observed history, or credible direction activates the issue;
- **Impact:** correctness, security, data, UX, delivery, or change cost is materially affected;
- **Propagation:** knowledge or edits spread across owners and are likely to keep spreading;
- **Irreversibility:** public contracts, persistent data, core dependencies, or cross-team commitments make delay costly;
- **Evidence strength:** several independent facts support the mechanism and counterevidence has been considered;
- **Intervention value:** a proportionate change can reduce the mechanism without greater collateral cost;
- **Trade-offs:** the recommendation respects quality goals that the current design intentionally optimizes.

Report the few findings that explain the largest current cost or risk. Supporting observations and local code findings can remain subordinate. Do not create a finding quota; a well-supported judgment that the inspected boundary is fit is useful.

## Falsify before recommending

Actively inspect reasons the candidate finding may be wrong:

- measured performance or resource constraints;
- required compatibility or external protocol semantics;
- generated-code ownership and authoritative schemas;
- security, reliability, deployment, or transaction boundaries;
- deliberately shared lifecycle;
- organizational ownership or policy;
- a stable facade that already contains the apparent complexity;
- rare or obsolete history that does not support the claimed future cost.

Compare the candidate intervention with leaving the current design in place. Check whether it moves complexity into callers, adds unsupported abstraction, expands the public surface, creates migration risk, or optimizes an unlikely future. An unfamiliar or unfashionable design can be appropriate.

For core architecture, high-impact migration, security or privacy boundaries, persistent data, or contested evidence, an independent reviewer can provide a second falsification pass. The Primary Agent still owns finding resolution and handoff; read [Execution Model](execution-model.md).

## Shape a useful modification

Recommend the smallest coherent change that addresses the causal mechanism. Explain:

- the concept, contract, state, or dependency knowledge that gains a clear owner;
- what moves or becomes internal, and what caller-visible behavior remains stable;
- directly enabling refactoring and the boundary of unrelated cleanup;
- transition slices, compatibility, data migration, activation, rollback, and cleanup when relevant;
- risks introduced by the new structure;
- alternative directions and the evidence that would choose among them.

Prefer reversible improvement over a flag-day rewrite in an established project. Before moving behavior, establish enough evidence to preserve it. Characterization checks, contract tests, a seam around an unstable detail, parallel compatibility, or a strangled slice may be useful when they match the project. The current Harness remains authoritative only where it is reliable. Read [Project Harness](project-harness.md) when facts or controls conflict, and [Harness Evolution](harness-evolution.md) when shared protection itself needs material repair.

A pattern, framework, interface, or service boundary needs current evidence. Framework-fit assessment should compare present capability, migration and lock-in cost, project expertise, required quality goals, and the actual pain of staying; framework fashion carries no weight.

## Verify architecture improvement

Turn the original scenario into a counterfactual check for the recommendation:

- Would the next similar change enter one coherent owner and touch fewer unrelated components?
- Does a caller need less unstable knowledge?
- Are state, data, errors, and side effects more explicit at the responsible boundary?
- Can current behavior and important failures be protected independently of the moved implementation?
- Does the new abstraction have a current consumer or variation?
- Are performance, security, compatibility, deployment, and recovery evidence preserved?
- Can the old path be removed under a visible condition?

Tests and static rules can support these claims, but a modified check cannot be its own sole evidence. For recommendations not yet implemented, state the expected observable delta and the evidence needed after implementation.

## Assessment handoff

Communicate in a form the user can judge. Lead with the assessment boundary, current drivers, and the dominant tension in plain language. For each material finding provide concrete evidence, mechanism, consequence, priority, confidence, counterevidence, and the smallest useful response. Separate local observations, uncertain hypotheses, and out-of-scope surfaces.

Keep diagrams and inventories only when they make relationships easier to verify. Preserve a durable assessment or Architecture Impact record only when implementation, collaboration, recovery, or future governance has a real consumer. End with the recommended next decision, implementation authority required, and the checks that would establish improvement.
