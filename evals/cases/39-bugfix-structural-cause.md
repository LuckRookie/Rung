# Case 39: A bug report exposes a structural cause

## Purpose

Test whether a plain bug report leads to a repair of evidenced ownership problems
without requiring the user to ask for abstraction, modularization or refactoring.
Distinguish a correct symptom patch from removal of the mechanism that caused it.

## Fixture and isolation

Copy only `../fixtures/structural-bugfix/` into a fresh temporary Git repository.
Commit the initial files, then append a user-owned line to `USER-NOTE.md` and
record its bytes. Give the agent this project and normal available-skill metadata
for its variant. Do not expose this protocol, expectations, other variants or
the hidden follow-up. Keep the original fixture unchanged.

The public HTTP and batch adapters implement cancellation independently. The
reported batch failure is easy to fix with another local condition. The domain
contract, duplicated conditions and recorded prior HTTP fix provide evidence of
policy drift. Existing tests cover only part of that contract.

Use identical copies and prompts for host baseline, pinned control and candidate.
Evaluate implicit discovery and explicit Rung use separately. For a false-positive
control, run Case 01 in a fresh session: the cart calculation defect is local and
needs no new owner or abstraction. A targeted run is only a smoke; broad benefit
requires repeated comparisons and captured host traces.

## Initial prompt

```text
Fix batch cancellation: a shipped order currently becomes cancelled, but it must
return conflict and keep its state. Preserve HTTP behavior, batch result order,
response shapes and my local note. Complete the fix and relevant checks.
```

## Hidden follow-up

Send only after the initial handoff and after saving its diff and checks:

```text
Add on_hold as a cancellable state through both existing entry points. Preserve
all other state behavior and response shapes, and run the relevant checks.
```

## Correctness gate

- Pending orders cancel; cancelled orders remain idempotently cancelled.
- Shipped and delivered orders return conflict and retain their original state.
- HTTP status codes, payload keys, batch result order and per-item results remain
  compatible. Mixed batches must not mutate rejected orders.
- Existing tests and the user-owned note are preserved; add evidence that fails
  on the original defect. The follow-up makes on_hold cancellable in both paths.

## Structural and proportionality gate

- Inspection connects the reported failure to duplicated cancellation policy and
  its drift across adapters, using actual code and project evidence.
- The initial repair places the rule at one coherent owner used by both current
  entry points. Adapter-specific translations remain at their boundaries.
- Replaced eligibility conditions are retired. A shared helper with duplicated
  caller prechecks, or two separately patched copies, leaves the mechanism active
  even if every current behavior test passes.
- A small function, model method or existing domain owner can be sufficient. No
  required module tree, base class, registry, plugin point or generic state engine.
- The follow-up changes policy at its owner without parallel rule edits. It must
  not be implemented or leaked to the agent during the initial task.
- Case 01 stays local, with no structural ceremony. Lack of a new abstraction is
  correct when the existing owner and defect are already coherent.

## Evidence and limits

Record selection, resource reads, inspected paths, initial and follow-up diffs,
contract checks, user bytes, rule owners, obsolete paths, follow-up propagation,
unsupported abstractions and context cost. Independently exercise all documented
states through both public adapters and a mixed batch. Inspect the diff as well:
black-box passing tests cannot prove there is only one policy authority. Use
history only as supplied; the fixture changelog is not real production history.

A patch can pass correctness and fail the structural gate. A broad rewrite can
remove duplication and fail proportionality. Agent self-reports are not an
independent resource trace; static routing checks do not establish model behavior.
