# Software Quality

Read when an active change or review needs an explicit judgment about the software's current fitness beyond reliable project-native checks. Useful signals include touched code becoming harder to understand, inconsistent placement or semantics, material reliability, performance, security, observability, or resource concerns, and a quality trade-off that can change Design or delivery.

Keep an ordinary clear edit on its normal Concern Card. Do not turn every change into a repository-wide quality audit. For a current construct whose main consequence is avoidable future burden under credible evolution, read [Technical Debt](technical-debt.md).

## Governing outcome

Leave the changed and materially affected software fit for its current users, maintainers, environment, and accepted direction. Judge quality relative to the [Project Model](project-model.md), observable behavior, project constraints, credible load and change, and the evidence available. A style ideal or tool score has no independent authority.

Use the smallest set of quality attributes that can change the decision:

- **Correctness:** behavior, contracts, invariants, boundaries, data, and meaningful failures agree with accepted intent.
- **Understandability:** a maintainer can recover purpose, ownership, control and data flow, state, side effects, and failure meaning from a bounded context.
- **Changeability:** a credible change enters a coherent owner without unnecessary knowledge or edits spreading elsewhere.
- **Verifiability:** important behavior and failure claims can be distinguished from relevant incorrect behavior at a proportionate boundary.
- **Operability:** the software exposes and contains relevant failure, load, concurrency, timeout, retry, cancellation, recovery, and resource behavior.
- **Consistency:** comparable behavior, code, tests, configuration, errors, diagnostics, and durable facts follow a project-supported way.
- **Predictability:** maintainers can anticipate placement, behavior, change effects, and failure meaning without hidden project knowledge.

Security, privacy, performance, accessibility, portability, compatibility, and other qualities join only when current requirements, evidence, risk, or credible use makes them consequential. Qualities interact; state the trade-off when improving one transfers cost or risk to another.

## Work within the touched ownership boundary

Inspect the owner being changed and the smallest surrounding context needed to keep it coherent:

- Place new behavior with the concept, policy, state, or boundary that owns it; follow a sound project layout.
- Keep files, types, functions, and tests organized around explainable responsibilities. Split or combine only when it reduces mixed authority, hidden knowledge, or reasoning cost.
- Use names that communicate project concepts and behavior. Keep control flow, data flow, side effects, and lifecycle visible enough for the risk.
- Model meaningful state and errors explicitly. Preserve diagnostic cause and context while exposing stable caller semantics.
- Remove duplication when it repeats policy or unstable knowledge in the touched path. Incidental repetition can remain cheaper than a shared abstraction.
- Remove code, parameters, branches, comments, flags, and compatibility paths made obsolete by the accepted change when their consumers and removal safety are known.
- Keep comments focused on purpose, constraints, provenance, or surprising reasoning. Synchronize public docs, configuration, generated sources, schemas, and examples that the change makes stale.
- Keep tests understandable and owned near the behavior or contract they protect. Avoid coupling them to incidental call sequences or representation.

Apply directly enabling or newly required cleanup with the change when it is coherent, authorized, and verifiable. Keep broad restyling, speculative abstraction, and unrelated cleanup outside the diff; report a material nearby finding with its owner and consequence.

## Judge mechanisms at the right scale

File size, branch count, nesting, complexity scores, coverage, duplication, naming, dependency count, and directory shape are investigation signals. Trace a material observation through:

```text
active quality goal
  -> code or runtime evidence
  -> mechanism
  -> current user or maintainer consequence
  -> smallest coherent response
  -> distinguishing evidence
```

Keep a local readability or consistency issue local. Read [Engineering Structure](engineering-structure.md) when ownership, public surface, dependency knowledge, shared state, data semantics, or an abstraction creates nonlocal effect. Read [Architecture Assessment](architecture-assessment.md) for a decision-ready system assessment. A large private implementation can remain fit; a one-line contract or resource decision can carry high quality impact.

## Current quality in Design and Implement

During Design, select the quality scenarios that constrain the solution. A useful scenario states the actor or stimulus, environment or load, desired response, and consequence. Do not design for every quality attribute or invented future.

During Implement, keep the relevant outcomes:

- preserve or establish the intended current behavior;
- keep the touched owner understandable and internally coherent;
- contain new knowledge and side effects at the responsible boundary;
- synchronize directly coupled tests and facts;
- run low-cost checks early when they expose drift;
- escalate when evidence changes ownership, design, scope, risk, or proof.

Current quality can require a behavior fix, local refactor, structural decision, new evidence, or a project rule. Keep these owners distinct even when one diff contains several.

## Quality probes

Record scenario, observation, mechanism, and response for a material claim:

- correctness: expected behavior plus an invalid or failure case;
- understandability: a bounded walkthrough recovering owner, flow, state, effects, and failure meaning;
- changeability: a follow-up change and its required files or knowledge;
- verifiability: independent known-good and known-bad observations at the owning boundary;
- operability: timeout, retry, cancellation, cleanup, or diagnostics when activated.

Promote only after false positives, owner, cost, and revision are known.

## Operability before Release

Rung ends at Release handoff, while code-level operability can be required for readiness. Inspect only relevant behavior:

- failure classification, stable error semantics, user or operator visibility, and diagnostic context;
- ownership and limits for timeout, retry, cancellation, idempotency, concurrency, backpressure, and recovery;
- cleanup on success, failure, timeout, and interruption;
- logs, metrics, or traces at boundaries where they distinguish an important state, failure, or service objective;
- measured latency, throughput, memory, I/O, or dependency behavior when performance is a claim;
- safe defaults, secrets, permissions, input handling, and sensitive-data exposure when security or privacy is active.

Observability volume and instrumentation symmetry are not goals by themselves. Prefer the smallest signal that lets the relevant consumer detect, explain, and act on the condition.

## Turn stable judgments into project constraints

Use the existing [Project Harness](project-harness.md) first. Promote a recurring quality judgment into formatter, lint, type, architecture, dependency, test, build, CI, or release control only when:

- it protects a real recurring or high-impact defect class or contract;
- compliant and violating behavior can be distinguished with acceptable false positives;
- an owner, exceptions, scope, rollout, cost, and removal or revision condition are clear.

Use [Verification Harness](verification-harness.md) when an important claim lacks an evidence layer. Use [Harness Evolution](harness-evolution.md) when the rule, shared support, authority, execution, or gate itself must change. A new check does not establish the value or correctness of its own policy.

## Review and handoff

Review the integrated state, including code added by workers and directly affected surrounding behavior. Look for regression, increased reasoning radius, hidden state or failure, inconsistent project semantics, obsolete paths, test brittleness, and quality costs transferred to callers or operators.

For each material finding, report the relevant quality goal, evidence, mechanism, current consequence, smallest response, trade-off, confidence, and verification. Fix ordinary findings directly when authorized. Persist quality reasoning only when it becomes a durable contract, project rule, formal review, or future decision input; do not create a default quality report or score.

Stop when current acceptance and relevant quality claims have proportionate evidence, touched code is coherent, material findings are resolved or routed, and uncovered scope is explicit.
