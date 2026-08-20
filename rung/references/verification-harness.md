# Verification Harness

Read when existing checks cannot support a material claim, or when work starts adding or expanding tests, fixtures, mocks, test services, test databases, documentation checks, static checks, CI execution, build checks, packaging checks, or end-to-end infrastructure.

The Verification Harness is the evidence-producing subset of the [Project Harness](project-harness.md). The Test System—cases, assertions, fixtures, data, fakes, mocks, helpers, runners, and environments—is a subset of the Verification Harness.

## Contents

Claims · evidence layers · inventory · construction · signal quality · lifecycle · gates and cost · maintenance versus evolution · durable output

## Start from the claim

Map each material completion, compatibility, build, artifact, or release claim to a direct observation. Use the lowest-cost boundary that can distinguish correct from relevant incorrect behavior. Reuse configured project commands and existing reliable components before adding infrastructure.

Useful questions include:

- Which claim or risk lacks reliable evidence?
- What incorrect behavior must remain visible?
- Which native entry point or component already provides part of the evidence?
- Which boundary owns the behavior and its test support?
- Does the proposed check add distinct evidence or repeat another layer?
- What environment, permission, platform, timing, or data remains uncovered?

## Evidence layers

Verification Tier describes evidence breadth. Governance depth describes decision, coordination, persistence, and review effort. Select the two axes independently.

| Tier | Evidence boundary | Typical observations |
|---:|---|---|
| 0 | Target and basic execution | format, syntax, focused smoke, generated-file consistency |
| 1 | Component behavior | static analysis, unit or module behavior, local invariants and failures |
| 2 | Boundaries and compatibility | contract, integration, build, security, dependency, schema, docs checks |
| 3 | Release system | supported matrices, end-to-end, package, artifact, install and delivery checks |

Lower tiers do not have to precede every higher-tier project check. The current claim, existing project topology, cost, and risk determine which observations are useful. `--max-tier` is a plan filter, not a universal promotion gate.

## Inventory before construction

Inspect only the relevant current Harness:

- entry commands and configuration;
- tests and the behavior or contract each group protects;
- shared fixtures, data builders, snapshots, fakes, mocks, and services;
- environment provisioning, setup, isolation, cleanup, and concurrency;
- static, schema, documentation, build, package, and artifact checks;
- CI triggers, matrices, caches, retries, quarantine, and required gates;
- runtime, external dependencies, credentials, permissions, and failure reports.

Identify the owner and consumers of shared components. A fixture that encodes domain policy belongs near that policy or a clearly owned test-support boundary. A mock should expose only the contract needed by its consumers and remain comparable with the real boundary.

## Construct the missing evidence

Add the smallest component that closes the identified gap. Keep product behavior and Harness support separately owned when they change for different reasons. Prefer public behavior, stable contracts, invariants, and failure semantics over incidental call sequences or private representation.

For a new component, make these facts discoverable where relevant:

- supported claim and layer;
- entry command and working directory;
- prerequisites and environment assumptions;
- fixture, data, fake, mock, service, or database owner;
- setup, isolation, cleanup, timeout, and concurrency behavior;
- expected evidence and failure location;
- required, extended, or diagnostic role;
- runtime or resource cost;
- review, repair, or removal condition.

Small local checks can express these facts directly in code and naming. Use a persistent artifact only when coordination, recovery, or formal review needs it.

## Signal quality

A green result is useful when the check can also expose a relevant failure. When practical and proportionate, observe a known-bad example, fault injection, mutation, or evaluation copy fail for the intended reason. Avoid deriving both the expected result and the implementation from the same disputed source.

Preserve exit code, command, revision, scope, raw failure, and artifact location. Retries may measure or contain an understood transient condition; retain the original attempt and do not let a later pass erase the reliability signal.

## Isolation and lifecycle

Control the state that can couple runs:

- allocate unique paths, ports, databases, tenants, queues, identities, or namespaces;
- make time, randomness, locale, platform, network, and concurrency assumptions explicit;
- keep setup idempotent where repeated execution is expected;
- clean up resources on pass, fail, timeout, and interruption when the environment allows;
- preserve enough failed-state diagnostics to reproduce the issue safely;
- avoid production credentials and restricted data in fixtures or evidence.

Use real dependencies when their behavior is the claim. Use fakes or mocks when isolation is the claim or the real boundary is unavailable, and validate their contract at a suitable boundary.

## Gates, diagnostics, and cost

- **Required gates** protect claims that must hold for merge, build, or release.
- **Extended checks** broaden platforms, environments, or quality evidence without blocking every local iteration.
- **Diagnostics** investigate failures, drift, performance, or reliability and can mature into gates after their signal is understood.

Track cost in relation to distinct evidence. Duplication, broad matrices, serial environments, long setup, flaky dependencies, and opaque failures are signals to consolidate or redesign. A fast check with weak discrimination and a slow check with duplicate coverage both deserve review.

## Maintenance versus evolution

Adding a regression case with existing helpers is Test System maintenance. Adding a missing fixture or contract layer is Verification Harness extension. Changing shared execution, authority, framework, isolation, coverage policy, retries, quarantine, or required gates is Harness evolution.

When the existing Harness may itself be wrong or a change removes or relaxes protection, read [Harness Evolution](harness-evolution.md). Establish an independent anchor and record the coverage delta before relying on the changed component for release evidence.

## Durable output and execution

For durable coordination, adapt `assets/verification-harness.template.md`. Keep stable test, CI, build, and release facts in the project documentation, configuration, or code that owns them.

For an explicit command plan, use `assets/verification-plan.template.json` and run:

```text
python <rung-skill-root>/scripts/run_verification.py \
  --project <path> --plan <plan.json> --max-tier <0-3> --output <evidence.json>
```

The runner executes selected checks sequentially with argument arrays, project-root working-directory protection, timeouts, captured output, and selected/skipped evidence. Environment orchestration, retries, dependency graphs, and matrices remain project-owned decisions.
