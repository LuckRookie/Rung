# Development Execution Model

Read when inspection scope, design persistence, planning ownership, cross-session recovery, delegation, independent review, or final integration needs an explicit operating contract.

## Contents

- Run ownership and default mode
- Minimum execution spine
- Inspection radius
- Decisions, design, and persistence
- Planning and implementation ownership
- Workers and independent reviewers
- Cross-session recovery
- Verification and release responsibility

## Run ownership

Each DevelopmentRun has one logical **Primary Agent**. The same model instance may hold that role for a short run, or a later session may resume it from durable state. The Primary Agent owns the integrated outcome, routing, user-work protection, decisions, plan, final diff, evidence, review, and release handoff.

The user supplies intent, constraints, product direction, and external-action authorization. A request such as "decide for me" delegates in-scope design choices; it does not expand task scope or authorize commit, push, publication, production mutation, or another external action.

The Coding Agent Host supplies sessions, models, tools, permissions, and any worker capability. Project tools supply configured format, lint, type, test, build, package, and release behavior.

Concern Cards are capabilities used by the Primary Agent. They do not imply one Agent or session per concern.

## Default mode

Use one Primary Agent in one main session. Keep working state in the conversation and actual project until persistence or delegation improves coordination, recovery, review, or delivery. Load only the references relevant to the next decision.

A run may expand to:

- **cross-session:** the work outlives reliable conversational context;
- **worker-assisted:** independent bounded units can proceed with clear ownership;
- **independently reviewed:** a second judgment materially improves confidence.

Rung remains usable when the host offers only one Agent and one session.

## Minimum execution spine

For a project-changing request, the Primary Agent normally:

1. grounds the requested outcome and delegated decision scope;
2. inspects governing instructions, user work, and target facts;
3. forms a coherent design and records it only when useful;
4. coordinates dependent units when coordination adds value;
5. implements or integrates the scoped change;
6. verifies claims against the actual integrated state;
7. reviews the diff, evidence, and delivery state;
8. hands off the release state, gaps, and risks.

Merge, skip, reorder, and revisit concerns as evidence changes. A local fix may collapse design, planning, implementation, review, and handoff into one short loop.

## Inspection radius

Expand inspection from the smallest safe radius.

### Baseline

Before editing, identify the project root, applicable instructions, branch or revision, working-tree state, user-owned changes, and configured tool entry points relevant to the request.

### Target

Read the direct owner, nearby callers and dependencies, related tests, public contract, configuration, and durable fact sources. This is the normal radius for a local bug fix or contained feature.

### Impact

Expand to consumers, schemas, migrations, generated artifacts, lock state, build/package entry points, CI, or release controls when interfaces, persistent data, shared behavior, dependencies, platforms, or multiple modules are affected.

### System

Use a declared system-level boundary for an explicit audit, core architecture change, broad migration, security-boundary change, build-system replacement, or Project Harness evolution. State included surfaces and remaining uninspected areas; "the whole repository" is not a verifiable scope by itself.

Inspection is sufficient when the next action has a known owner and constraint set, relevant user work is protected, the likely impact and check path are bounded, and remaining unknowns are visible. Read [Project Harness](project-harness.md) when authoritative sources or configured judgment mechanisms conflict.

## Collaborative decisions and design authority

Clarify manages consequential decisions with the user. Design supplies professional reasoning and candidate solutions. They may alternate while a project or change proposal develops.

Present a user decision in plain language: the issue, recommendation, immediate consequence, credible development impact, reversibility, and requested choice. Keep mechanisms and terminology available by reference or on request. Decision-relevant risks remain in the plain-language view.

When the user delegates an in-scope decision, the Primary Agent acts as the project designer. Ground the choice in current facts, credible development signals, and change cost. Human-facing surfaces receive UX attention, including task flow, information hierarchy, defaults, feedback, error prevention, recovery, consistency, accessibility, and trust.

Return to the user when a new choice changes product meaning, accepted risk, durable data meaning, material scope, or an authorization boundary outside the delegation.

## Design persistence

Use the lowest durable surface that has a real future consumer.

| Situation | Design home |
|---|---|
| Local, reversible, single-session choice | conversation, code, and tests |
| Moderate coordination within the current session | host plan or concise session note |
| Public contract, persistent data, core ownership, lasting UX, security boundary, or migration | owning project requirement, ADR, API, schema, architecture, or configuration |
| Cross-session, multi-executor, evolving comparison, or temporary recovery state | `.rung/runs/<run-id>/design.md` or an existing project issue |

Avoid duplicating one design fact across temporary and durable locations. Promote stable facts into their project owner and retain or clean temporary state according to project convention and an explicit cleanup condition.

## Planning ownership

The Primary Agent owns the integrated plan.

- Use an internal micro-plan for one coherent, directly checkable edit.
- Use the host plan surface for several dependent steps that fit one session.
- Use a project issue or `.rung/runs/<run-id>/plan.md` for cross-session work, multiple executors, migration, compatibility windows, risky ordering, or formal recovery.

Each material change unit identifies its outcome or acceptance, owner, files or modules, prerequisites, behavior to preserve, intended change, completion check, and recovery point. Workers may refine their unit and report findings; the Primary Agent updates global order, contracts, and status.

Plans follow evidence. When implementation changes ownership, interface, data, risk, or acceptance, revisit Inspect, Clarify, or Design before continuing under a stale plan.

## Implementation ownership

The Primary Agent implements the change by default. Preserve user-owned edits, follow applicable instructions, keep generated sources and durable facts synchronized, and run low-cost checks where they expose drift early.

When workers edit directly, assign non-overlapping file or module ownership or use a host isolation mechanism. The Primary Agent reviews worker output, resolves integration effects, and verifies the combined state. Worker success does not establish integrated success.

## Worker-assisted execution

Use workers only when host policy and user scope permit, and when parallel or specialized execution produces a concrete benefit. Good signals include two or more independent units, stable shared contracts, separable ownership, a clear integration point, and an available final check path.

Keep coupled design, overlapping files, sequential migrations, or rapidly changing interfaces with the Primary Agent until boundaries stabilize.

A worker task packet contains:

- outcome and acceptance;
- owned files or modules and excluded scope;
- relevant instructions, facts, and shared contracts;
- user-owned work to preserve;
- allowed actions and authorization limits;
- checks to run and expected handoff.

A worker returns changed paths, checks and results, assumptions, findings, and integration concerns. Give each worker only the context needed for its unit.

## Review ownership

The Primary Agent performs a proportionate review of the integrated diff, requirements, design, evidence, and delivery state. Fix ordinary findings directly and revisit the owning concern for material findings.

Use an independent reviewer when a public contract, security or privacy boundary, persistent data, core architecture, broad migration, required gate, high-impact Harness evolution, formal policy, or explicit user request makes a second judgment valuable. The reviewer reports findings; the Primary Agent owns resolution and final handoff.

## Cross-session recovery

Before ending a session that cannot complete the run, persist only what a successor needs:

- outcome, accepted decisions, and delegated design scope;
- project root, baseline revision, and protected user work;
- authoritative facts and chosen design;
- completed units, current plan status, and next action;
- checks already run, evidence locations, gaps, and open risks.

On resume, re-read applicable instructions and compare the saved revision and user-work state with current Git state. Revalidate assumptions affected by drift, then continue from the next meaningful action rather than repeating valid completed work.

## Verification and release responsibility

Verify claims against the integrated revision or explicitly described working-tree state. Worker checks are candidate evidence; the Primary Agent confirms their relevance after integration. A changed Harness component cannot be the sole evidence of its own correctness.

The Primary Agent assembles the final handoff: observable result, actual checks, artifact or revision identity, uncovered scope, residual risk, and release state. External writes occur only under the required user authorization and host permissions.

## Operating invariants

- One logical Primary Agent owns each DevelopmentRun.
- Inspection expands by evidence and declared impact.
- Local reversible design may live in code, tests, and session context.
- Durable facts live with their project owner.
- The Primary Agent owns the global plan and integrated result.
- Delegation uses bounded context and explicit ownership.
- Final verification targets the combined state.
- Session and Agent count increase only when they improve execution or confidence.
