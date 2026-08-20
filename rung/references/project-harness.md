# Project Harness

Read when project instructions, documentation, tests, static rules, build tooling, CI, or release policies may conflict, be unreliable, or become part of the requested change.

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

## Ordinary use

When relevant sources agree and configured checks produce reliable evidence, use the existing Harness directly. Follow its local instructions, reuse its commands and fixtures, update lasting facts in their owning documents or configuration, and keep the change within the established delivery path.

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

A local test edit remains part of the Test System. Load the higher-level evolution guide when the edit changes how future code is judged, accepted, isolated, or delivered; affects shared infrastructure or consumers; changes coverage, reliability, cost, or diagnostics; or removes existing protection.

## Authority and ownership

Before changing a disputed rule, identify its owner, consumers, revision, and authority basis. Useful anchors include current user intent, accepted requirements, public API or schema, released compatibility behavior, real callers, project governance documents, and independently observed behavior. Current implementation output alone does not establish an expected result.

Write durable Harness facts to the project location that owns them. Use `.rung/` only when temporary comparison, migration, coordination, or recovery state has no project home. For a material cross-session change, adapt `assets/harness-change.template.md`.
