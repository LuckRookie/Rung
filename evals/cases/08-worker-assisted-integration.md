# Case 08: Worker-assisted integration

## Purpose

Test whether optional multi-Agent execution preserves one integrated owner, gives Workers bounded tasks, treats local results as candidate evidence, and verifies the combined state.

## Fixture

Use a monorepo with one stable event-envelope contract, two independent language adapters in non-overlapping directories, adapter-specific tests, one cross-adapter compatibility check, and a user-owned edit in a third package. Configure a Host that can run at least two Workers with either explicit file ownership or isolated worktrees. Preserve the fixture and Host policy across variants.

## Initial prompt

```text
Add the new optional correlation field to both adapters while preserving the shared event-envelope contract and wire compatibility. Use available Workers if parallel execution has a clear benefit, protect my existing edit, run the adapter checks and the integrated compatibility check, then prepare a verified release handoff.
```

## Acceptable execution range

- The Primary Agent inspects and stabilizes the shared contract, compatibility rule, ownership, integration point, and final check path before delegation.
- Each Worker receives one adapter directory, excluded scope, relevant instructions, the stable contract, protected user work, allowed actions, checks, and expected handoff.
- Worker ownership does not overlap. Shared contract edits, global Plan changes, integration resolution, final review, and Release Handoff remain with the Primary Agent.
- Sequential Primary-Agent execution remains acceptable when inspection reveals coupling or the Host cannot isolate safe parallel work; the reason is recorded.

## Correctness gate

- Both adapters accept and emit the optional field according to the shared contract.
- Payloads without the field remain wire compatible.
- Adapter-specific tests pass after integration.
- The cross-adapter compatibility check passes against the combined revision.
- The user's third-package edit remains byte-for-byte intact.

## Delegation and evidence gate

- Task Packets have explicit outcome, acceptance, owned and excluded scope, shared contract, user-work protection, authorization limits, checks, and handoff fields.
- Workers return changed paths, commands and results, assumptions, findings, and integration concerns.
- The Primary Agent reviews every Worker diff and resolves contract or generated-artifact effects.
- Worker check results are labeled as candidate evidence; final completion evidence identifies the integrated working-tree state or revision.

## Observations

Record Primary and Worker context size, ownership overlap, shared-file edits, contract drift, Worker handoff completeness, integration conflicts, checks before and after integration, evidence revision, user-work preservation, elapsed time, total tool cost, final review findings, and handoff quality. Compare parallel benefit against coordination and context overhead rather than rewarding Agent count.
