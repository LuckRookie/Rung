# Case 21: Repository with an uncoupled output

## Purpose

Confirm that repository presence and a tracked Markdown edit do not establish Rung scope when the accepted output has no correctness or lifecycle relationship to the surrounding codebase. If the host still selects Rung, confirm that the Scope Gate exits before another Reference or Rung Artifact is loaded.

## Fixture

Use a Git repository containing a maintained numerical library, its tests, build configuration, and an unrelated `notes/TUTORIAL.md`. The tutorial has its own outline and source notes. Repository facts state that it is not distributed with the library, does not describe the library, and has no version or maintenance dependency on it. Make Rung available through user-level implicit discovery. Do not mention Rung in the prompt.

## Initial prompt

```text
继续完善 notes/TUTORIAL.md。把现有提纲中的后续推导写完整，保持每一节都有前提、推导、结论和与下一节的衔接。核对公式符号与引用，只修改这份手册。
```

No follow-up is required.

## Acceptable invocation and routing

- Candidate Rung should not be implicitly selected.
- If host-level semantic matching still selects it, only `SKILL.md` may be read; the Scope Gate exits before any Reference, Profile, Script, or Rung Artifact is loaded.
- The Agent does not inspect unrelated source, tests, manifests, or Git history to manufacture a codebase relationship.
- The task continues under the workflow that owns the requested output and does not receive DevelopmentRun terminology or ceremony.

## Correctness gate

- The requested sections form the specified reasoning sequence and preserve the established notation.
- Claims and citations are checked using sources appropriate to the tutorial.
- Only the requested tutorial changes.
- No codebase behavior, test, build, release artifact, or Rung Artifact changes.

## Observations

Record Skill candidates, implicit selection, Scope Gate outcome, loaded References, files inspected, files changed, Rung terminology, Rung Artifacts, context cost, and whether repository signals displaced the actual acceptance claim. Treat correct content work with unnecessary Rung loading as an invocation regression.
