# Case 07: Cross-session recovery

## Purpose

Test whether a DevelopmentRun can cross a real Session boundary while preserving accepted decisions, user work, completed units, evidence, and the next meaningful action.

## Fixture

Use an existing service with repository instructions, a shared notification contract, two adapters, configured unit and integration commands, and an unrelated user-owned working-tree edit. The requested refactor has at least three dependent units and a stable target contract. Preserve the fixture, initial Git state, and Session-boundary timing across variants.

## Initial prompt

```text
Refactor notification rendering so both adapters use the shared contract while preserving their public payloads and error behavior. Keep my working-tree edit, update the relevant project design fact, run appropriate checks, and prepare a verified handoff. This task will continue in another session, so leave only the recovery state a successor actually needs.
```

## Forced Session boundary

After the Agent has inspected the target, accepted or made the material design decisions, and completed no more than one coherent change unit, send:

```text
This session must end now. Persist a minimal recovery handoff without committing, pushing, or discarding any working-tree changes.
```

Start a fresh Agent Session in the same workspace with only the repository, durable project facts, saved recovery state, and this prompt:

```text
Continue the current DevelopmentRun from its saved state. Reconcile it with the current repository before acting, finish the requested change, verify the integrated result, and prepare the handoff.
```

## Acceptable execution range

- One logical Primary Agent role spans both Sessions even when different model instances execute them.
- Durable project design facts live in the owning project document; temporary outcome, plan status, next action, evidence, and risk may live in an existing issue or `.rung/runs/<run-id>/`.
- The resumed Session re-reads applicable instructions and compares the saved baseline, current revision, working tree, and protected user edit before continuing.
- Valid completed work and checks remain usable when the underlying state still matches; drifted assumptions are revalidated.

## Correctness gate

- Both adapters use the shared notification contract and preserve public payloads and errors.
- The unrelated user edit remains intact across both Sessions.
- The durable design fact matches the final contract and is maintained in one authoritative location.
- The resumed Session continues from the next meaningful unit without redoing or silently replacing valid work.
- Final verification covers the integrated state after every unit is combined.

## Recovery evidence gate

- Saved state identifies outcome, accepted decisions and delegated scope, project root, baseline, protected user work, authoritative facts, chosen design, completed units, next action, evidence, gaps, and risks.
- Resume evidence identifies any drift found and the assumptions or checks revisited because of it.
- The final handoff distinguishes evidence reused from the first Session from evidence run against the final integrated state.

## Observations

Record Session boundaries, durable and temporary locations, duplicated facts, state size, baseline and working-tree comparisons, repeated inspection or implementation, stale assumptions, preserved user bytes, plan changes, checks by Session and revision, final diff, recovery time, and context cost.
