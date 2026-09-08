# Case 01: No-signal local bug fix

## Purpose

Confirm that Rung stays thin when ownership, boundary, dependency, data, coordination, and release risk are already clear.

## Fixture

Use a small existing repository with one pure calculation function, a nearby unit test, an explicit test command, and no unrelated working-tree changes. The defect and expected behavior must be local to that function. Preserve the exact fixture across variants.

## Initial prompt

```text
Fix the failing cart-total behavior so applying store credit can never produce a negative total. Preserve the existing API and run the relevant checks.
```

No follow-up is required.

## Acceptable routing range

- Implicit Candidate Rung remains unselected: this is development with no material governance decision.
- If the host loads the entrypoint, bypass before any Reference or Artifact and complete the fix normally.
- A separate explicit `$rung` variant may use Lite and zero or one current card. Do not conflate this with implicit discovery.
- Reassess only if inspection exposes a consequential boundary absent from the supplied fixture.

## Correctness gate

- The reported total floors at zero.
- Existing non-negative cases remain unchanged.
- The relevant configured test passes.
- Unrelated files and user work remain untouched.

## Observations

Record prompt bytes or tokens, References read, files changed, abstractions introduced, extra documents created, commands run, and handoff length. A candidate that adds design ceremony without improving the result regresses progressive governance.
