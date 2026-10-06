# Project Harness

Read when adopting Rung in a project, reconciling project rules, or changing unreliable instructions, checks, build tooling, CI or release policies.

## Scope and relationship

The Project Harness is the project-owned system that shapes how software is understood, changed, checked, built, and handed off. Its logical components include:

```text
Project Harness
|-- intent and fact sources: instructions, requirements, README, ADR, API, schema
|-- engineering constraints: formatter, lint, types, architecture, dependencies
|-- Verification Harness
|   |-- Test System: cases, assertions, fixtures, data, fakes, mocks, runners
|   `-- contract, integration, E2E, docs, build, package, and evidence checks
|-- development and build tooling: environment, dependencies, codegen, migration
`-- delivery controls: CI workflows, required gates, release and artifact policy
```

The Test System is a subset of the Verification Harness, which is a subset of the Project Harness. One file or service may serve several roles: CI can execute tests and enforce release policy; a schema can be both an authoritative fact and contract-check input.

Rung contributes reusable methods and development requirements to this system. Project facts, commands and effective local constraints retain their owning documents or tools. Adoption aims at one consistent set of effective rules, not two independently maintained Harnesses or a mandatory new instruction file.

## Adoption and reconciliation

Use the host's instruction hierarchy to establish applicable authority. Neither the Rung label, an older project rule, nor the stricter wording establishes universal precedence. Identify each difference's scope, protected behavior, owner and evidence before treating it as a conflict.

| Relationship | Response |
|---|---|
| Equivalent rules | Reuse the project owner and link to it; avoid duplicate instructions. |
| Project-specific implementation of a general principle | Reuse local mechanisms unless an explicit adoption target calls for their replacement. |
| Missing capability | Add the smallest useful guidance or check at its existing owner. |
| Incompatible requirements or unreliable checks | Establish the currently effective rule and its authority, then use [Harness Evolution](harness-evolution.md) for an evidenced revision. |

Default to the rules touched by the current task. If the user explicitly selects Rung's recommendations as the target for a defined adoption scope, implement that target and replace conflicting local rules; no prior defect or repeated approval is required. Record the selected guidance and scope in the existing plan or instruction owner. A general request to use Rung alone does not authorize wholesale replacement. Preserve unaffected behavior, user work and migration evidence under host authority. Report concrete incompatibilities instead of silently substituting the old convention or treating generic guidance as infallible.

Reconcile ordinary in-scope inconsistencies under existing authorization. A genuinely unresolved owner decision or an action outside that authority needs resolution before dependent work; continue unaffected work where useful. Adoption does not silently remove a required check, override a supported contract, or authorize external operations.

During a transition, state which rule governs each claim. A replacement may first run diagnostically; make it required only under the established activation conditions and authority. Until then, retain effective protection or explicitly record an authorized exception with replacement evidence and remaining risk. Retire superseded instructions and checks once replacement coverage is established. Use an existing plan, issue or rule document for this record, not a separate conflict-management system.

## Ordinary use

Absent an explicit replacement target, use a reliable existing Harness directly. Follow its local instructions, reuse its commands and fixtures, update lasting facts in their owning documents or configuration, and keep the change within the established delivery path.

## Problem signals

Treat the Harness itself as a candidate change target when:

- instructions, requirements, tests, implementation, or CI disagree;
- correct behavior is rejected or incorrect behavior passes;
- fixtures, mocks, snapshots, schemas, or generated artifacts have drifted;
- checks depend on order, time, network, shared state, or hidden environment facts;
- retries, quarantine, ignores, or manual reruns hide the original failure;
- duplicate sources define the same rule with different results;
- failure output cannot identify the broken claim or owning boundary;
- build or verification cost grows without distinct evidence;
- a framework, platform, dependency, schema, or delivery contract has moved;
- a check, rule, matrix entry, or required gate may be removed or relaxed.

## Classify the change

Set membership and governance escalation are separate decisions.

| Change class | Example | Routing |
|---|---|---|
| Content maintenance | Add a regression case or synchronize an approved example | Normal Implement and Verify |
| Harness extension | Add a fixture, contract check, or missing evidence layer | [Verification Harness](verification-harness.md) |
| Harness evolution | Change shared execution, authority, isolation, framework, or ownership | [Harness Evolution](harness-evolution.md) |
| Governance evolution | Relax, replace, or promote a gate or release rule | Harness Evolution with stronger Review and Release attention |

A regression case using reliable existing helpers stays content maintenance. Load the evolution guide for changes to shared judgment, execution, isolation or diagnostic mechanisms; coverage policy or gates; or the removal or relaxation of existing protection. Added case coverage alone does not escalate governance.

Read [Technical Debt](technical-debt.md) when a Harness condition or temporary control is being qualified or carried as a future obligation. Continue to Verification Harness or Harness Evolution for the actual evidence or governance change.

## Authority and ownership

Before changing a disputed rule, identify its owner, consumers, revision, and authority basis. Useful anchors include current user intent, accepted requirements, public API or schema, released compatibility behavior, real callers, project governance documents, and independently observed behavior. Current implementation output alone does not establish an expected result.

Write durable Harness facts to the project location that owns them. Use `.rung/` only when temporary comparison, migration, coordination, or recovery state has no project home. For a material cross-session change, adapt `assets/harness-change.template.md`.
