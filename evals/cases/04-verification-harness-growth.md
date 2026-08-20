# Case 04: Verification harness growth

## Purpose

Test whether the Agent fills a real evidence gap at the lowest reliable layer, reuses project-native verification, and keeps new harness infrastructure owned, isolated, diagnosable, and proportionate.

## Fixture

Use an existing application with configured unit tests, a temporary-data helper, one command-line entry point, and a documented build command. The fixture has no cross-boundary test for atomic import behavior. Preserve the same test framework, CI constraints, supported platforms, and fixture revision across variants.

## Initial prompt

```text
Add a JSON import command. Valid records must be persisted in input order. If any record is invalid, the command must report the failing record and persist nothing. Preserve existing commands and prepare a verified release.
```

## Hidden follow-up

Reveal only after the initial task has reached handoff:

```text
The import checks now need to run in parallel CI jobs on Linux and Windows. Remove any shared temporary state, keep failures diagnosable, and avoid duplicating the existing unit coverage.
```

## Acceptable routing range

- Verify is relevant for mapping the atomicity and diagnostic claims to evidence.
- The Verification Harness reference is relevant when existing unit checks cannot prove the cross-boundary behavior or when shared temporary state appears.
- Design may be relevant for transaction ownership in production code. Plan and a persistent Harness Artifact remain optional unless coordination or recovery creates a concrete need.
- A new custom runner, service, retry layer, or broad matrix requires evidence that project-native entry points cannot cover the claim.

## Correctness gate

- Valid records persist in order through the public command boundary.
- An invalid record produces a useful location and leaves persistent state unchanged.
- Existing commands and configured checks remain valid.
- Parallel runs use isolated state and clean up their resources on both supported platforms.
- The verification can be observed failing when atomicity, ordering, or isolation is intentionally broken in an evaluation copy.

## Observations

Record the claims mapped to each check, reused entry points, new fixture or helper ownership, setup and cleanup behavior, failure output, Tier selection, required versus extended checks, runtime, retries, flake handling, duplicated assertions, coupling to incidental internals, and files changed by the follow-up. Compare whether additional harness infrastructure produces distinct evidence and whether its maintenance condition is visible.
