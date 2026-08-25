# Design Exploration

Read when the next consequential design decision lacks sufficient support because several materially different interpretations or behavior paths remain plausible, and their consequences can change ownership, contracts, state, UX, risk, or implementation direction.

A useful trigger has three parts: an active codebase development decision, more than one credible path, and consequences that matter to that decision. Clear bounded changes stay on their current card. Repository understanding without an active development claim exits at the Scope Gate.

## Bound the decision

State the single decision this exploration must support and the uncertainty that prevents a responsible choice. Record:

- accepted behavior, constraints, delegated authority, and relevant project facts;
- the user-visible or project-visible consequence of getting the decision wrong;
- which ownership, contract, state, UX, data, dependency, compatibility, security, recovery, or verification differences could change the direction;
- the next consumer of the result.

Use [Project Model](project-model.md) when project identity, semantic center, feature fit, or intended evolution is uncertain. Use [Inspect](inspect.md) to obtain only facts that can distinguish credible paths. Broad inventory does not improve a bounded design decision.

## Choose discriminating scenarios

Select the smallest set of representative scenarios able to separate meaningful directions. Start with concrete use; draw a component diagram only when it helps the decision. Useful coverage may include:

- a primary success path and its observable result;
- a materially different user, caller, input, or operating condition;
- a failure, interruption, denial, timeout, partial result, or recovery path;
- a state transition, retry, cancellation, concurrency, or lifecycle boundary;
- compatibility, migration, rollout, rollback, or downstream-consumer behavior.

There is no required scenario count. Add a scenario only when it can reveal a different responsibility, state, contract, failure meaning, quality trade-off, or choice.

## Walk behavior before structure

For each selected scenario, follow the behavior far enough to expose:

- actor or caller, trigger, preconditions, and desired observation;
- important state before, during, and after the interaction;
- durable data, side effects, external dependencies, and authorization;
- failure semantics, visibility, retry ownership, cancellation, compensation, and recovery;
- the concept responsible for each decision and invariant;
- evidence that could verify the behavior independently of one implementation.

Hidden responsibilities often appear where a scenario needs policy selection, state ownership, fallback, coordination, translation, trust, or recovery. Keep them attached to the behavior that revealed them. Delay module and interface choices until their responsibilities are visible.

Classify consequential statements as **Accepted**, **Evidenced**, **Inferred**, or **Unknown**. Preserve **Contested** evidence when credible sources disagree. Inspect or ask only when an Unknown can change the current direction. A plausible detail remains a hypothesis until its authority is clear.

## Form and compare directions

Retain only directions whose consequences differ materially. Equivalent names, class layouts, or minor implementation variants do not create separate design options. There is no fixed number of alternatives, and one direction is valid when the scenarios and evidence genuinely converge.

Compare surviving directions against the same scenarios and current decision criteria:

- user flow, defaults, feedback, failure prevention, recovery, accessibility, and trust;
- concept ownership, public contracts, state and data semantics, dependency knowledge, and change locality;
- correctness, security, compatibility, performance, operability, and verification feasibility where relevant;
- migration, rollback, reversibility, delivery cost, and credible evolution;
- unsupported assumptions and the evidence that would reverse the choice.

Prefer the smallest coherent direction that explains all important scenarios. Simplicity follows removal of unsupported paths and responsibilities; it does not justify ignoring a scenario that changes the decision.

## Resolve and hand off

When a choice requires the user, pass it to [Clarify](clarify.md) in plain language: recommendation, immediate consequence, credible development impact, reversibility, and the smallest decision needed. When the user delegates the in-scope choice, the Primary Agent acts as project designer and gives human-facing consequences full UX attention.

Pass the accepted direction to [Design](design.md) with:

- behavior and scenarios the direction must support;
- discovered responsibilities, state, contracts, failures, and evidence needs;
- the material alternatives considered and why their consequences were weaker;
- assumptions, owned Unknowns, trade-offs, and revisit signals.

[Engineering Structure](engineering-structure.md) maps the accepted responsibilities and knowledge to code boundaries. [Architecture Assessment](architecture-assessment.md) evaluates whether an existing system can support the direction when a decision-ready assessment is active.

## Stop and persist proportionally

Stop when representative scenarios distinguish the important directions, hidden responsibilities and failure semantics are clear enough for the current decision, direction-changing Unknowns have an owner or revisit signal, and Design can proceed without critical invention. Continuing after only low-value detail remains is context waste.

Keep the exploration in the session by default. Persist it in an existing product, design, issue, or architecture fact when cross-session recovery, multiple executors, formal review, or recurring decisions create a consumer. Use `assets/solution-design.template.md` only when the project has no better temporary owner. Do not create a default Discovery document or `.rung/` artifact.
