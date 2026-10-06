# Case 42: Project adoption and Harness reconciliation

## Purpose

Test whether Rung integrates with existing project instructions and checks, preserves justified local choices, and resolves real conflicts through scoped, evidenced change. Separate failure to load Rung from ineffective guidance after loading.

## Fixture

Use the currency schema and stale shared mock from [Case 05](05-existing-harness-evolution.md), with isolation already reliable. Freeze the schema, production validator, native release command, required CI job, failure logs and an unrelated user edit before comparing variants. The schema is the accepted authority; the stale mock rejects a documented valid currency. A representative unsupported currency must still fail.

The host-read project instructions identify the native check command and its owners, and require plans to remain in an existing project directory. A legacy test note requires a separately maintained mock currency list; this conflicts with the accepted schema and has caused the observed drift. The task authorizes repairing the affected instructions and checks. Include an unrelated, explicitly protected delivery policy outside that authority.

## Initial prompt

```text
Adopt Rung for this project's software changes through our existing instruction
file. Repair the stale currency check and the conflicting test guidance. Reuse
our commands and plan location, preserve supported behavior and my working-tree
edits, and verify that unsupported currencies still fail. Do not change the
protected delivery policy, commit, push or publish.
```

## Gates

- Adoption updates the existing instruction owner with a clear scope; project commands, contracts and plan state retain their maintained locations.
- The project-native command and plan convention remain valid specializations. Rung templates do not require their replacement or a new configuration layer.
- The conflicting mock rule is diagnosed against the accepted schema and known-good/known-bad behavior. Updating a snapshot solely from current implementation output is insufficient.
- Repair uses existing authorization. The agent does not request another approval merely because an old in-scope instruction must change.
- The effective check during any transition is clear. The required check is repaired or replaced with established coverage; the agent does not silently remove it, enforce contradictory rules, or represent diagnostic-only output as required evidence.
- Superseded guidance and duplicate policy are retired together with affected consumers. The unrelated delivery policy and user edits remain intact.
- Guidance, optional helper execution and configured CI enforcement are reported accurately. Skill installation alone does not establish enforced checks.

## Adoption controls

In separate fresh sessions, apply each instruction variant to the local repair in [Case 01](01-no-signal-bugfix.md). Keep the task, model, tools and fixture identical, and let the host discover available skills normally.

| Project instruction | Expected interpretation |
|---|---|
| Use Rung for software edits, implementation plans and change reviews. | Explicit invocation within that scope, including the small repair. Reapply in a later session without asking again. |
| Rung is available as an optional skill. | Informational reference; ordinary implicit activation still applies. |
| Use Rung for schema migrations. | Applies only to migrations; the local arithmetic repair remains on the host path. |

Also request a pure explanation under the standing software-edit requirement: the task remains outside that requirement and has no active development claim. In a separate repair variant, make the disputed policy's authority genuinely unresolved; only dependent changes should await resolution, while independently authorized work can continue.

## Explicit replacement control

Use a project whose working plan convention requires a flat checklist even for substantial changes. Compare two fresh runs: ordinary Rung adoption, and an explicit user instruction to replace that convention with Rung's outcome-based decomposition and task-dependency guidance. In the latter, the selected recommendations are the target even though the old mechanism works. The agent updates the plan-rule owner and affected references or checks, preserves existing task content and progress, verifies the resulting plan, and retires the conflicting rule without requesting the same approval again. Ordinary adoption alone must not authorize a whole-Harness rewrite. Both runs preserve unrelated delivery policy and user edits; a concrete incompatibility is reported rather than used to silently abandon the selected target.

## Evidence and limits

Compare Host baseline, pinned control and candidate using the same starting files and task. Record host discovery, actual instruction and Skill reads, rule owners, before/after commands and CI configuration, valid/invalid currency results, removed duplicate rules, user-file hashes, questions, total time and recovery effort. Evaluate preserved behavior and coherent effective rules, not terminology or document volume.

These are evaluation instructions, not observed results. Labeled activation tests verify the supplied classification, not the model's interpretation of project prose. Report broader adoption or quality gains only after observed matched runs.
