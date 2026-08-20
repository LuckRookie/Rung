# Project Model

Read when a project or subsystem needs a shared semantic model before product, UX, scope, ownership, architecture, or feature-fit decisions can be made coherently. Useful signals include sparse greenfield intent, several plausible product interpretations, a proposed capability near the current boundary, conflicting descriptions of an existing product, deliberate product evolution, or several semantic centers in one repository.

Keep ordinary work on its current path when the user outcome, product meaning, owner, and impact are already clear. A Project Model is a compact decision aid, not a required stage or document.

## Governing outcome

Build the best current evidence-backed account of what the project is for, whom it serves, which concepts form its semantic center, which qualities shape it, what changes fit, and what evidence would revise the account. The model should be understandable to the user, correctable, useful for a real next decision, and explicit about material uncertainty.

The latent human picture will always be richer than its specification. Do not fill gaps with an apparently complete product story. Preserve several candidate models when available evidence supports materially different interpretations.

## Set a useful model boundary

Name the surface being modeled: a whole product, one subsystem, a library, a workflow, or another coherent capability. A repository, organization, deployment unit, or shared toolchain can contain several product models. Use a hierarchy or composition when evidence shows shared platform facts and distinct users, workflows, language, data, or release direction.

State included evidence, uninspected surfaces, the current decision the model must support, and the authority for product-direction choices. A request to assess or model authorizes inspection and recommendations; editing still follows the user's requested scope.

## Gather two evidence streams

Use **human meaning** to learn:

- people, situations, pain, desired outcome, and unacceptable failure;
- words, examples, comparisons, prototypes, and boundary cases the user uses;
- accepted direction, intended evolution, priorities, and delegated design scope;
- choices whose consequences the user wants to retain.

Use **project reality** to recover:

- observable behavior, public interfaces, primary flows, releases, and current users;
- requirements, README, product notes, domain glossary, ADRs, API, and schema;
- concepts, invariants, ownership, data, errors, and dependencies realized in code;
- tests and Harness claims that protect behavior;
- issues, incidents, change history, active consumers, and dormant experiments when relevant.

No universal source order resolves every conflict. Judge authority from user decisions, accepted requirements, caller-visible behavior, durable contracts, current consumers, history, and project governance. Code can reveal implemented meaning and accidental structure. Documentation can express accepted intent and become stale. Expose conflicts that can change the next decision.

Classify material model statements so their status remains visible:

- **Accepted:** confirmed by the user or an authorized project fact;
- **Evidenced:** directly supported by current observable repository behavior or contract;
- **Inferred:** the best explanation of available evidence;
- **Contested:** credible sources disagree;
- **Unknown:** missing information could change the model or decision.

Use sources and confidence proportionally. A short session model may label only consequential inferences; a durable model should make important evidence and authority traceable.

## Synthesize the smallest useful picture

A useful model may contain:

- a plain-language sentence connecting people, core situation, observable outcome, and central capability;
- the product shape and primary interaction surfaces;
- a small semantic center: core concepts, relationships, invariants, and shared vocabulary;
- decision priorities such as UX, correctness, compatibility, data integrity, security, performance, explainability, delivery cost, or change locality;
- canonical capabilities that strongly represent the project;
- adjacent extensions and examples that would change product identity;
- credible evolution, stable commitments, unknowns, and revisit signals.

Select only fields that affect the current or recurring decision. A Project Model is semantic compression, not a repository inventory, architecture diagram, exhaustive domain ontology, backlog, or feature catalogue.

Concrete exemplars and boundary probes often communicate meaning better than a long category definition. Use examples such as "a new fruit variety," "a fruit basket," and "vegetables as a core catalogue category" to expose whether a capability reinforces the current center, extends an edge, or changes the product identity.

When interpretations differ, present at most a few meaningful candidates in plain language. Explain their immediate user-visible consequence, credible development impact, and reversibility. Ask only about differences that change product meaning, material scope, accepted risk, durable data, or authority. When the user delegates an in-scope choice, select from evidence as project designer and give human-facing consequences full UX attention.

## Judge feature fit

Use the model to form a reasoned fit decision:

- **Core fit:** serves current people and outcome through the existing semantic center;
- **Adjacent extension:** serves a related situation while adding a meaningful concept, workflow, or boundary;
- **Identity change:** changes primary people, outcome, product shape, shared language, or semantic center.

Useful probes include:

- Does the capability serve the current people, situation, and observable outcome?
- Which existing concept owns it, and which invariant or workflow does it reinforce?
- Does it introduce another semantic center, public language, durable model, or primary interaction?
- Can it remain at an edge with a stable translation boundary?
- Which quality priorities and compatibility commitments change?
- Can the project still be explained coherently after the addition?
- Is this a credible planned evolution or an unsupported hypothetical expansion?
- Has the user authorized any product-identity change the capability requires?

Fit is evidence for a decision rather than a permanent gate. When the user deliberately expands the product, revise the model first, preserve applicable compatibility, expose migration consequences, and let Design establish the new coherent boundary. Do not force a new direction into old names and assumptions, or use the old model to resist an authorized evolution.

## Apply the model

Use the Project Model to reduce arbitrary choices while retaining technical judgment:

- map central concepts and invariants to coherent owners, data, state, and tests;
- shape primary interfaces and UX around the important people and tasks;
- contain concepts that belong to distinct product centers;
- let decision priorities select relevant quality scenarios and trade-offs;
- give seams and abstractions current evidence from credible evolution;
- name code, contracts, and artifacts with the accepted project language;
- detect semantic drift when a diff introduces an unowned concept or second product center.

The model supplies direction to [Design](design.md) and [Engineering Structure](engineering-structure.md). [Architecture Assessment](architecture-assessment.md) uses it as evidence for drivers, scenarios, dominant tensions, and intervention value. Architecture also depends on actual load, data, security, deployment, compatibility, organization, and Harness evidence; include or inspect these when they can change the decision.

Review the model when implementation evidence contradicts it, a hidden follow-up lands poorly, users or product direction change, previously adjacent behavior becomes central, or a new semantic center emerges. Revision under new evidence is a successful outcome when the model's prior status and accepted change remain visible.

## Persist only for a consumer

Keep a local, reversible model in the conversation or design reasoning. Use an existing README, product definition, requirements document, domain glossary, architecture overview, or other owning project fact when the accepted model will guide future work. For cross-session recovery, multiple executors, formal review, or temporary comparison, `.rung/runs/<run-id>/project-model.md` may use `assets/project-model.template.md`.

Do not create a second fact source when the project already has a maintained owner. Promote accepted durable meaning into that owner and retain or clean temporary state by an explicit condition. A persisted Project Model participates in the Project Harness as an intent and fact source; read [Project Harness](project-harness.md) when authority or synchronization conflicts affect project decisions.

## Handoff

Stop when the next consequential decision has a model boundary, a plain-language picture, enough semantic and quality information, visible uncertainty, and an owner for any required user choice. Output only the model elements and fit consequences that help the user or next action. Record the model's sources, status, home, and revisit signals when persistence has a real consumer.
