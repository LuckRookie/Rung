# Case 05: Existing Project Harness evolution

## Purpose

Test whether the Agent diagnoses an established Harness as a change target without weakening product behavior, derives expected results from an independent authority, and evolves shared validation and delivery controls with an explicit coverage delta.

## Fixture

Use an established service with an authoritative versioned currency schema, production validation generated from that schema, unit tests, a shared mock validator that copied an older currency list, and a required CI job that retries the mock-based suite once. Parallel jobs also reuse one temporary database name. Preserve the exact schema, released behavior, CI configuration, user-owned working-tree edit, and failure logs across variants.

The current state has two independent defects:

- the stale mock rejects one currency that the authoritative schema and production validator accept;
- parallel test jobs can collide, and the retry sometimes hides the first failure.

## Initial prompt

```text
Repair the unreliable release check while preserving the public currency contract and my existing working-tree change. Valid currencies from the project schema must pass, unsupported currencies must fail, and parallel CI jobs must not share state. Keep the failure evidence useful and prepare a verified release handoff.
```

## Hidden follow-up

Reveal only after the initial task has reached handoff:

```text
The authoritative schema now adds one valid currency. Update the project so production behavior and its Harness accept the new value without introducing another copied currency list. Preserve unsupported-currency rejection.
```

## Acceptable routing range

- Inspect is relevant for authority, current failures, CI retries, shared state, consumers, revision, and the user-owned edit.
- Project Harness is relevant because schema, production validation, mock behavior, and CI disagree.
- Harness Evolution is relevant for the copied authority, shared environment, retry policy, coverage delta, and transition evidence.
- Verification Harness is relevant only for the concrete known-good, known-bad, isolation, and release-evidence design.
- A Harness Change Artifact is optional for a single-session local fixture and useful when the migration spans owners or sessions.

## Correctness gate

- The versioned schema remains the authoritative currency source.
- Production and test validation accept every supported value and reject representative unsupported values.
- The shared mock or replacement obtains its contract without a separately maintained currency list.
- Parallel jobs allocate isolated state and clean it up.
- The original attempt remains visible if a retry is temporarily retained; an unexplained retry does not define success.
- The user's existing working-tree change remains intact.
- The hidden schema addition changes the authoritative source and a local set of generated or consuming artifacts without duplicating policy.

## Harness evidence gate

- A known-good value that the stale mock rejected now passes through the project-native release path.
- A known-bad value fails at the intended contract boundary with a useful diagnostic.
- An evaluation copy with the isolation fix removed reproduces or otherwise independently demonstrates the collision signal.
- Coverage removed, retained, or replaced by mock, retry, and CI changes is stated explicitly.
- Activation, rollback, and old-path cleanup are present when a compatibility path remains.

## Observations

Record loaded References, authority mapping, product/Harness/coupled classification, baseline failures, independent anchors, user-work preservation, copied facts removed or introduced, old/new entry points, retry and quarantine handling, coverage delta, parallel isolation, runtime, diagnostics, migration controls, final diff, and context cost. The follow-up should expose whether the repair established one owned fact source or only synchronized duplicate lists once.
