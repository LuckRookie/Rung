# Development Scope

Read for an unresolved scope decision after minimal host inspection. Clear cases use `SKILL.md`; uncertain activation stays on the host path until facts justify governance.

## Establish positive membership

Development membership requires both predicates; activation is a separate decision:

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

## Activate proportionally

For implicit invocation, require a consequential decision about ownership, contracts, persistent state, failure semantics, compatibility, migration, verification authority, or delivery readiness. New maintained software can qualify when these decisions are still open. A small security fix or schema change can qualify; repository size, file count, a public caller, and ordinary tests do not establish materiality alone.

When behavior, owner, impact, and checks are clear, and the change is local and reversible, bypass Rung and finish under host instructions. This is still development. Repairing an implementation to honor a known contract differs from choosing or changing the contract. A request to run tests or hand off a patch alone does not request governance.

An explicit instruction to use Rung or perform development governance (such as architecture assessment, design trade-offs, or release readiness) can activate small in-scope work. Mentioning the skill, quoting a command, or finding its installed files does not constitute that instruction. Explicit invocation waives materiality only; it never supplies a missing development claim or codebase relationship.

Materiality that remains unknown is a reason for minimal host inspection, not speculative Guide loading or a question about whether to use Rung. Reassess if evidence exposes a consequential boundary; return to the host path when the need disappears. Activation applies to the current change, not every future task in the same repository.

After entry, use Lite for a bounded decision or explicit small task, Standard for interacting owners or design choices, and Strict at high-impact contract, security, data, migration, or delivery boundaries. Depth does not prescribe a document, reviewer, test tier, or stage count.

## Resolve material ambiguity

Determine the smallest qualifying portion before asking the user:

1. What exact result will be accepted?
2. Does that result change a maintained project surface, decide a current codebase change, or prove a current change or release?
3. Which owner must maintain or act on it?
4. Must an artifact remain synchronized with codebase behavior, contracts, or release state?

Ask one plain-language question only when the unresolved answer changes the work materially. Useful forms are “Will this result guide a code change you are making now?” and “Will this result be maintained and delivered as part of this code project?”

## Mixed ownership

When one request contains both active development and other outcomes, keep their claims and owners separate even if one Agent performs both:

- Rung governs codebase facts needed for the active claim, decisions, changes, integrated verification, review, and claim-appropriate Handoff. Release joins when delivery is active.
- Each remaining outcome keeps its owning workflow, evidence method, authorization, and recovery path.
- Shared observations support a codebase claim only when their relevant state and artifact identity are known. They do not broaden the DevelopmentRun by association.
- External execution remains subject to its own authority and does not inherit authorization from codebase change.

## Reclassify from evidence

Re-evaluate when the accepted outcome changes. Understanding can expose a development claim; enter Rung only when a concrete change, decision, or delivery claim becomes active. Development work can also reduce to understanding or another outcome; exit when either predicate disappears. Load References only after membership is current.

Explicit `$rung` invocation still passes through membership. On bypass, continue helping without a governance report. Read deeper guidance only when its current signal holds.

The gate controls Rung context and responsibility. It does not block the user's task or replace host permissions, safety rules, or another workflow.
