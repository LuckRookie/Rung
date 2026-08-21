# Development Scope

Read only when the relationship between the accepted outcome and a software codebase is materially unclear, or when one request combines qualifying and non-qualifying work. Clear cases use the short gate in `SKILL.md`.

## Establish positive membership

Continue Rung only after establishing that the primary accepted outcome designs, creates, changes, assesses, verifies, or prepares the release of a software codebase, or changes an artifact coupled to that codebase.

An artifact is coupled when codebase behavior, contracts, or release state determine its correctness, and the code project owns keeping it synchronized for its consumers. Coupling follows responsibility and lifecycle. Physical co-location does not establish it. Greenfield codebase work can qualify before a repository exists.

Use the current acceptance claim and durable owner. The relationship must be active in the requested work; a possible future code change does not qualify the present task.

## Exit without classifying the outside world

When positive membership is not established, exit Rung before loading another Reference, Profile, Script, or Artifact. Continue the user's task under host instructions or the workflow that owns its outcome. Rung does not need a taxonomy of work outside its scope.

The following signals are insufficient on their own:

- a repository, worktree, manifest, tracked file, or project-shaped directory;
- a path, file type, command, tool, technical vocabulary, or amount of work;
- incidental code used to obtain another accepted outcome;
- general needs for sources, planning, review, correctness, or evidence.

## Resolve material ambiguity

Determine the smallest qualifying portion before asking the user. Useful questions are:

1. What exact result will be accepted, and does that acceptance concern the codebase itself?
2. Which owner must maintain the result after this task?
3. Must the result stay synchronized with codebase behavior, contracts, or release state?
4. Does any produced code become a maintained codebase surface or remain instrumental to another outcome?

Ask one plain-language question only when the unresolved relationship would materially change the work. A useful form is: “Will this result be maintained and delivered as part of this code project?”

## Mixed ownership

When one request contains both qualifying codebase work and other outcomes, keep their claims and owners separate even if one Agent performs both:

- Rung governs codebase facts, decisions, changes, integrated verification, review, and Release Handoff.
- Each remaining outcome stays with its owning workflow, evidence method, authorization, and recovery path.
- Shared observations support a codebase claim only when their relevant state and artifact identity are known. They do not broaden the DevelopmentRun by association.
- External execution remains subject to its own authority and does not inherit authorization from the codebase change.

## Reclassify from evidence

Re-evaluate when the accepted outcome changes. Work outside Rung can expose an active codebase defect; enter only when resolving or assessing that codebase becomes part of the request. Codebase work can also end with no qualifying change; exit when the positive relationship disappears. Load References only after membership is current.

Explicit `$rung` invocation still passes through this gate. Briefly explain an out-of-scope result, load no further Rung material, and continue helping under host instructions.

The gate controls Rung context and responsibility. It does not block the user's task or replace host permissions, safety rules, or another workflow.
