# Case 11: Architecture assessment traces framework leakage

## Purpose

Test whether the Agent can look past a tidy directory tree and identify an unstable vendor contract that has become a project-wide source of knowledge and migration cost.

## Fixture

Use an established notification service organized into many small packages and interfaces. Vendor SDK request types, status enums, exception classes, retry hints, and webhook payloads appear in domain policy, API handlers, queue messages, persistence, and tests. A product decision names a second provider for one region while the current provider remains supported.

Keep naming, formatting, lint, and unit tests clean so superficial code-quality review offers few distractions. Include one project document that incorrectly claims the vendor is isolated behind an adapter. Preserve exact code, history, project rules, and provider contract across variants.

## Initial prompt

```text
Assess whether the current notification architecture can safely support a second provider. Identify the main code and architecture risks, show the evidence, and recommend a migration shape. Do not implement it yet.
```

## Hidden follow-up

Reveal only after the assessment has reached handoff:

```text
Implement the first migration slice and add the regional provider for one notification type. Keep the existing provider and public behavior compatible, and verify the integrated result.
```

## Acceptable routing range

- Inspect is relevant for product intent, provider flows, public contracts, data, tests, documentation, and dependency knowledge.
- Architecture Assessment, Engineering Structure, and Review are relevant.
- Design and Plan become relevant for the migration slice, compatibility, data transition, and dependent units.
- Project Harness is relevant if tests or architecture rules encode the vendor contract as project policy.

## Correctness gate

- The initial assessment leaves the working tree unchanged.
- The dominant finding is the spread of vendor-specific knowledge across core policy and durable boundaries, supported by concrete paths and types.
- The clean directory tree and numerous interfaces do not establish effective isolation.
- The recommendation defines the smallest useful internal contract, translation boundary, compatibility path, and migration order from current facts.
- The hidden follow-up keeps existing behavior working and contains new provider knowledge at an owned boundary.

## Causal evidence gate

- The assessment distinguishes external-detail leakage from the mere existence of an SDK dependency.
- It explains how the planned provider variation activates current migration cost.
- It checks for counterevidence such as required vendor semantics, performance constraints, or public contracts before recommending translation.
- New interfaces and abstractions correspond to current provider variation or a stable contract; speculative framework design fails this gate.

## Observations

Record loaded References, documentation drift, SDK symbols and semantics traced, affected owners, public and persistent compatibility, migration steps, abstraction count, hidden follow-up change propagation, tests coupled to vendor details, residual provider knowledge, context cost, and any unsupported architecture claims.
