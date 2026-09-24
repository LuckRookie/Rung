# Architecture Design

Read when a new subsystem, top-level boundary, public contract, durable state model, external integration, or cross-module capability needs an architectural direction before implementation. Use [Engineering Structure](engineering-structure.md) for local structural choices and [Architecture Assessment](architecture-assessment.md) when an existing system must be judged for a change decision.

## Governing outcome

Choose the smallest boundary that gives a current capability a clear owner, stable contract, explicit state and failure semantics, and a credible path for the next relevant change. Architecture is a decision about knowledge, responsibility, and change propagation; a diagram or framework choice is only supporting evidence.

## Start from change scenarios

State the capability, actor or stimulus, affected boundary, expected response, and quality consequence. Walk the success and important failure behavior needed to choose the boundary. Include a follow-up change when credible evolution can distinguish the choices; keep its assumptions visible. Expand to migration, recovery, concurrency, performance, security, or compatibility only when material.

## Assign responsibility and contracts

For each proposed boundary, name its owned concept, invariants, inputs, outputs, side effects, persistent data, and meaningful failures. Keep callers from knowing internal formats, vendor types, lifecycle order, retries, or storage details unless those are current contracts. Identify the authority for schemas, generated output, configuration, and external protocol semantics.

## Make state and dependencies explicit

Model important states and transitions rather than correlated flags or caller-known sequencing. Draw dependency direction by knowledge: types, errors, ordering, retries, and configuration count as coupling even without an import. Put unstable external details behind a seam only when current variation, replacement, isolation, or policy independence justifies it.

## Check the future change and the evidence

When a credible next change informs the decision, trace it through the proposed boundary: does it enter a coherent owner, preserve stable caller behavior, and contain unstable knowledge? Without one, keep the boundary grounded in current behavior. Define the lowest-cost test or contract check that distinguishes intended behavior and important failure. Record performance, security, compatibility, deployment, and recovery evidence when they constrain the choice.

## Choose and record proportionally

Compare the direct implementation with alternatives only when their ownership, contract, state, migration, or risk consequences differ. Prefer a reversible slice, compatibility seam, or parallel path over a flag-day rewrite. Keep local reversible decisions in the session, code and tests. When future decisions, consumers or recovery need a lasting record, put the accepted direction, alternatives, assumptions, trade-offs and revisit signal in its project owner.

Stop when the boundary, owner, contract, state, dependencies, failure meaning, verification seam, and migration or rollback condition are clear enough for Plan and Implement. Read [Architecture Assessment](architecture-assessment.md) when the decision depends on evidence from an existing system.
