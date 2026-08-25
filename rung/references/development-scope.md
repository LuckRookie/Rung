# Development Scope

Read only when the accepted outcome's codebase relationship, development claim, or ownership is materially unclear, or when one request combines qualifying and non-qualifying work. Clear cases use the short gate in `SKILL.md`.

## Establish positive membership

Continue Rung only when both predicates hold:

1. **Codebase relationship:** the accepted outcome concerns a software codebase or an artifact coupled to it in correctness and maintenance.
2. **Active development claim:** the accepted outcome creates a durable project change, decides or directs a concrete change, or establishes evidence for a current change or release.

An artifact is coupled when codebase behavior, contracts, or release state determine its correctness, and the code project owns keeping it synchronized for its consumers. Coupling follows responsibility and lifecycle. Physical co-location does not establish it. Greenfield codebase work can qualify before a repository exists.

A design, review, diagnosis, or assessment qualifies when its accepted result is a decision or evidence claim that guides, accepts, rejects, prioritizes, or de-risks current codebase development. A result that ends with understanding current codebase facts has no active development claim. Possible future development does not qualify the present task.

## Exit before deeper governance

When either predicate is absent, exit Rung before loading another Reference, Profile, Script, or Artifact. Continue the user's task under host instructions or the workflow that owns its outcome. Rung does not need a taxonomy of work outside its scope.

Codebase relationship alone is insufficient. The following signals are also insufficient on their own:

- a repository, worktree, manifest, tracked file, or project-shaped directory;
- a path, file type, command, tool, technical vocabulary, or amount of work;
- incidental code used to obtain another accepted outcome;
- general needs for sources, planning, review, correctness, or evidence.

## Resolve material ambiguity

Determine the smallest qualifying portion before asking the user:

1. What exact result will be accepted?
2. Does that result change a maintained project surface, decide a current codebase change, or prove a current change or release?
3. Which owner must maintain or act on it?
4. Must an artifact remain synchronized with codebase behavior, contracts, or release state?

Ask one plain-language question only when the unresolved answer changes the work materially. Useful forms are “Will this result guide a code change you are making now?” and “Will this result be maintained and delivered as part of this code project?”

## Mixed ownership

When one request contains both active development and other outcomes, keep their claims and owners separate even if one Agent performs both:

- Rung governs codebase facts needed for the active claim, decisions, changes, integrated verification, review, and Release Handoff.
- Each remaining outcome keeps its owning workflow, evidence method, authorization, and recovery path.
- Shared observations support a codebase claim only when their relevant state and artifact identity are known. They do not broaden the DevelopmentRun by association.
- External execution remains subject to its own authority and does not inherit authorization from codebase change.

## Reclassify from evidence

Re-evaluate when the accepted outcome changes. Understanding can expose a development claim; enter Rung only when a concrete change, decision, or delivery claim becomes active. Development work can also reduce to understanding or another outcome; exit when either predicate disappears. Load References only after membership is current.

Explicit `$rung` invocation still passes through this gate. Briefly explain an out-of-scope result, load no further Rung material, and continue helping under host instructions.

The gate controls Rung context and responsibility. It does not block the user's task or replace host permissions, safety rules, or another workflow.
