# Harness Evolution

Read after [Project Harness](project-harness.md) identifies that an existing instruction, fact source, test system, static rule, build path, CI workflow, or release control is itself a material change target.

## Contents

Outcome · invariants · diagnosis · baseline · change claims · independent anchors · component patterns · test classification · coverage delta · validation · rollout · handoff

## Outcome

Evolve the Harness while preserving trustworthy product behavior, visible evidence, project ownership, user work, and a recoverable delivery path. Adapt the depth to blast radius. A local fixture repair may remain small; a shared framework, architecture rule, CI gate, or release-policy migration usually needs explicit comparison and handoff.

## Core invariants

- The changed Harness component cannot be the sole evidence of its own correctness.
- Every removal, relaxation, retry, quarantine, or replacement identifies the protected claim and resulting coverage delta.
- Existing reliable entry points, user changes, baseline failures, and original diagnostics remain visible until replacement evidence is established.
- Broad changes have an activation condition, rollback condition, and cleanup condition.
- Stable ownership, commands, and policy live in project documentation, configuration, or code.

## Diagnose the target

Classify the observed failure before choosing files to edit:

| Classification | Meaning | Typical direction |
|---|---|---|
| Product defect | The Harness reliably exposes incorrect product behavior | Repair product code and add or retain regression evidence |
| Harness defect | Product behavior matches an independent authority while the Harness misjudges or misexecutes it | Repair the affected Harness component |
| Coupled defect | Product and Harness share an invalid assumption or unstable boundary | Define both product and Harness claims, then repair each owner |
| Unresolved authority | Requirements, tests, implementation, or consumers disagree without a trusted anchor | Return to Clarify or Inspect before changing expectations |

Do not derive a new expected result, snapshot, mock response, or schema solely from current implementation output. Locate the source that owns the behavior or obtain a user decision when product meaning changes.

## Establish the baseline

Capture only the baseline needed to compare the proposed evolution:

- relevant branch, revision, working-tree state, and user-owned edits;
- commands, environments, platforms, and consumers using the component;
- current pass, fail, blocked, flaky, skipped, retried, or quarantined outcomes;
- the claims each rule or check is intended to protect;
- representative runtime and resource cost when cost motivates the change;
- current authority and ownership for instructions, data, contracts, and gates.

Preserve raw failures and distinguish a repeatable defect from an environmental limitation. Historical logs, prior releases, and change history can explain intent, but current project and user facts decide the target.

## Define the change claims

Separate claims that require different evidence:

1. **Product claim:** user-visible behavior, compatibility, data, errors, or quality remains correct.
2. **Harness claim:** the changed mechanism accepts known-good behavior and visibly rejects relevant known-bad behavior.
3. **Operational claim:** setup, isolation, cleanup, concurrency, diagnostics, runtime, and resource use are reliable enough for its role.
4. **Migration claim:** consumers, platforms, branches, and delivery gates can move to the new mechanism without an unrecorded protection gap.

Small changes may need only the first two. Keep untested claims explicit instead of allowing one green command to stand for all four.

## Use independent anchors

Choose at least one anchor outside the component being changed. Depending on the project, useful anchors include:

- user acceptance or a reviewed requirement;
- public API, schema, protocol, or domain invariant;
- a released compatibility fixture or real consumer;
- known-good and known-bad examples created before the change;
- an alternate implementation or independent tool;
- a real service or isolated environment instead of the changed mock;
- manual reproduction with observable output;
- fault injection, mutation, or an evaluation copy with the protected behavior broken.

An independent anchor should discriminate between correct and incorrect behavior. A second implementation that copies the same disputed assumption adds little evidence.

## Choose the evolution shape

Prefer the smallest reversible change that restores trustworthy judgment. Possible shapes include repairing an owner in place, consolidating duplicate authority, introducing a compatibility adapter, running old and new paths in parallel, promoting a diagnostic check after observation, or retiring a replaced component after coverage comparison.

Consider the affected Harness area:

### Instructions and documentation

- Identify the canonical fact source and its consumers, including Agents and generated docs.
- Reconcile conflicts by authority and revision; avoid duplicating the final rule.
- Validate commands, examples, links, schemas, and generated output where practical.
- Record any change to which document or configuration owns a lasting fact.

### Tests and verification support

- Distinguish case-level maintenance from shared fixture, mock, runner, environment, or gate evolution.
- Keep assertions on behavior, contracts, invariants, and failure semantics at the nearest reliable boundary.
- Compare fixtures and mocks with the real contract they represent.
- Make setup, isolation, cleanup, concurrency, and failure locations explicit.
- Preserve a negative signal: a relevant broken behavior should still fail visibly.

### Static and architecture rules

- State the defect class or dependency rule the check protects.
- Evaluate ignores and exceptions as coverage decisions with owners and removal conditions.
- Test representative compliant and violating examples when the rule engine or configuration changes.
- Stage wide rule adoption when existing violations need intentional migration.

### Build, generation, and migration tooling

- Identify source inputs, generated outputs, reproducibility assumptions, and version compatibility.
- Avoid editing generated output as the lasting fix when its source owns the fact.
- Compare artifacts, schemas, checksums, or runtime behavior at the boundary consumers use.
- Preserve rollback or recovery information for persistent data and irreversible formats.

### CI and release controls

- Separate execution orchestration from the evidence and policy it enforces.
- Keep required, extended, diagnostic, and quarantined checks distinguishable.
- Treat retry, timeout, matrix, cache, permission, and trigger changes as observable policy changes.
- Promote a new required gate only after its signal, reliability, cost, and failure ownership are understood.

## Test-change classification

| Test change | Default interpretation | Evolution signal |
|---|---|---|
| Add a regression case using existing helpers | Content maintenance | Escalate only if it exposes a shared Harness defect |
| Update an expected result after an approved contract change | Content synchronization | Escalate when authority or compatibility remains disputed |
| Add a fixture, fake, mock, database, or service | Harness extension | Shared ownership, lifecycle, or contract representation matters |
| Change a shared helper, runner, framework, or environment | Test Harness evolution | Compare consumers, isolation, diagnostics, and old/new results |
| Delete, skip, loosen, snapshot-update, retry, or quarantine | Verification governance evolution | Identify lost claim, replacement evidence, and coverage delta |
| Change CI requirement, matrix, timeout, or merge/release gate | Delivery-governance evolution | Define activation, rollback, and downstream impact |

This classification controls governance depth; all rows remain structurally inside the Test System or its delivery controls.

## Record the coverage delta

For each removed, relaxed, or replaced mechanism, record:

- the claim and failure class it previously protected;
- evidence that the old mechanism is defective, redundant, or superseded;
- the new or retained mechanism that protects the claim;
- differences in boundary, platform, data, timing, or environment coverage;
- any accepted gap and its residual risk;
- the owner and condition for later review or removal.

File count, assertion count, coverage percentage, and runtime are supporting observations. They do not replace a claim-level explanation.

## Validate three surfaces

Use evidence proportionally across:

- **Product surface:** relevant behavior, compatibility, data, errors, build, and artifacts.
- **Harness surface:** known-good acceptance, known-bad rejection, isolation, cleanup, diagnostics, and cost.
- **Transition surface:** old/new comparison, consumer compatibility, activation, rollback, and cleanup readiness.

Run the project-native path that real consumers use. When the current Harness is unreliable, retain independent observations and clearly label results produced by the component under repair.

## Rollout and cleanup

Large or shared changes may use a compatibility window:

```text
baseline -> parallel or diagnostic use -> reliability observation
         -> required activation -> old-path removal -> fact-source cleanup
```

This is a selectable migration shape. Skip steps that add no evidence. Avoid indefinite dual systems by recording who can activate the new path, what triggers rollback, and what proves the old path can be removed.

## Review and handoff

Review the actual diff together with the authority map, product evidence, Harness evidence, and coverage delta. Highlight relaxed protection, unresolved disagreement, unverified platforms, flaky or quarantined checks, temporary compatibility paths, and downstream actions.

Use `assets/harness-change.template.md` when cross-session recovery, multiple owners, broad migration, or formal review benefits from persistence. Store lasting facts in their project-owned location and keep secrets or production data in their dedicated systems.
