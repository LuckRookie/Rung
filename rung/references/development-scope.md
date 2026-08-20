# Development Scope

Read when the boundary between project development and runtime operation is unclear, or when one request contains both. Ordinary clear cases should use the short gate in `SKILL.md` without loading this guide.

## Classify the outcome

Use the requested observable result, its durable owner, and the claim needed for acceptance. File extensions, repository location, tools, and verbs are supporting evidence.

Choose **project development** when the outcome designs, creates, changes, assesses, verifies, or prepares the release of intended or existing project behavior or artifacts. This includes greenfield structure, code, tests, contracts, schemas, migration sources, project-owned configuration and documentation, dependencies, architecture, build inputs, delivery definitions, and release evidence.

Choose **runtime only** when the outcome solely observes or changes the present state of a machine, service, deployed environment, external resource, or incident. Typical work includes starting or restarting a service, applying an existing deployment, inspecting logs or metrics, changing host administration, switching traffic, scaling, or executing a prepared change against live data.

Choose **mixed** when acceptance requires both a project-development result and a runtime-state result. Split the responsibilities even when one agent or command sequence performs both.

Ask only if a consequential ambiguity remains. Useful probes are:

1. What must be different when the request is accepted: a reusable project result, the current environment, or both?
2. Which project or operational system owns the durable result?
3. Is a design, compatibility, evidence, or release claim required for a project artifact?
4. Would the requested runtime action still be the complete outcome if no project artifact changed?

## Boundary examples

| Request | Classification | Rung behavior |
|---|---|---|
| Change a repository Compose default and its documentation for future installs | Project | Govern the artifact and its evidence |
| Rebind the current Nextcloud instance and restart it | Runtime only | Load no Rung reference or artifact |
| Change a Helm chart, verify it, then deploy to staging | Mixed | Govern the chart to handoff; separate deployment execution |
| Author a Terraform module or reviewed infrastructure change | Project | Treat infrastructure as a project-owned artifact |
| Apply an already prepared Terraform plan | Runtime only | Follow operational authority and evidence |
| Author a migration with compatibility and rollback evidence | Project | Govern schema and migration artifacts |
| Execute a prepared migration against a live database | Runtime only | Follow data-operation controls |
| Assess project architecture without editing code | Project | Use the assessment route |
| Inspect live logs to restore service | Runtime only | Stay on the operational path |
| Trace an incident and repair the project defect it exposes | Mixed or project after discovery | Enter Rung when the project outcome becomes active |

## Mixed work and transitions

For mixed work, keep a visible boundary:

- Rung owns project facts, decisions, artifacts, integrated verification, review, and release handoff.
- The operational path owns environment identity, credentials, current state, mutation authority, rollout, traffic, live-data effects, and runtime recovery.
- A release handoff may carry an artifact identity, approved configuration, sequence, risks, rollback information, and unresolved limits to the operational system.
- Runtime observations can support a project claim when their environment and artifact identity are known. They do not silently broaden the DevelopmentRun or authorize another mutation.

Reclassify when evidence changes the outcome. A restart request can reveal a faulty generator that needs a project fix; a planned code change can reduce to an environment correction. Load Rung references only after the project concern becomes current.

## Guard against false boundaries

- Version control is evidence of ownership, not the sole test. A tracked file can be edited only to operate one environment; an untracked greenfield artifact can still be project work.
- Docker, Compose, Helm, Terraform, CI, build, test, and migration vocabulary can occur on either path. Identify what is being authored, assessed, proved, published, or applied.
- Running a service, test environment, build, or deployment can be part of project verification when it proves an active project claim. Command execution alone does not establish a DevelopmentRun.
- Preparing deployment definitions, release notes, packages, tags, or publications can belong to release handoff. Applying them to an environment remains operational execution.
- Explicit `$rung` invocation on runtime-only work merits a brief boundary explanation. Continue helping under host instructions and load no further Rung material unless the user adds a project-development outcome.

The scope gate controls Rung context and responsibility. It does not block the user's operational task or replace host permissions, safety rules, or a dedicated operations workflow.
