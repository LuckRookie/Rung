# Rung repository instructions

## Product facts

- `Rung.md` is the source of truth for product shape, system boundary, workflow, profiles, concepts, and release contract.
- `INSTALL.md` is the source of truth for package coordinates, installation scope, conflict handling, and installation verification.
- `rung/SKILL.md` is the user-facing Skill entrypoint. Keep it concise and route conditional detail to references.
- `rung/references/execution-model.md` is the source of truth for Primary Agent ownership, inspection radius, design persistence, plan and implementation ownership, Worker and Reviewer roles, cross-session recovery, and integrated responsibility.
- `rung/references/development-scope.md` defines the outcome-based boundary among project development, runtime-only operation, and mixed work.
- `rung/references/` contains concern cards and governance reminders loaded only when their signals are present.
- `rung/references/project-harness.md` defines the Project Harness scope, Test System relationship, problem signals, and routing.
- `rung/references/harness-evolution.md` is the detailed guide for independently evidenced repair, coverage change, migration, rollback, and cleanup of an existing Harness.
- `rung/references/verification-harness.md` is a specialized Verify reference for evidence gaps and growing test, documentation, build, CI, package, or end-to-end infrastructure.
- `rung/references/engineering-structure.md` is the shared guide for contextual ownership, change locality, information hiding, dependency knowledge, state, data, errors, abstractions, and structural testability.
- `rung/references/architecture-assessment.md` is the scenario- and evidence-driven guide for explicit assessment of an existing architecture, modularity, structural debt, dependency shape, or framework fit.
- `rung/references/project-model.md` defines how Clarify and Inspect recover an evidence-backed project identity, semantic center, feature-fit boundary, and credible evolution for Design and Review.
- `rung/profiles/` contains optional depth hints for Lite, Standard, and Strict governance.
- `rung/assets/` contains optional templates selected when persistence improves coordination, recovery, recurring decisions, review, or handoff; `project-model.template.md` is the fallback when no project-owned identity fact exists.
- `rung/scripts/` contains deterministic, dependency-free helpers.
- `evals/` contains host-neutral behavioral scenarios for routing, Project Model decisions, engineering structure, architecture assessment, evidence, and context-cost evaluation.

## Documentation style

- Define products through capabilities, behavior, inputs, outputs, and responsibility handoffs.
- Use direct statements. Category-exclusion inventories and comparison slogans do not belong in product descriptions.
- Keep each fact in one maintained location and link to it from other documents.
- Preserve the User Intent → Scope Gate → Project Development Intent-to-Release boundary established in `Rung.md`.
- Run the development Scope Gate before loading any Reference. Project outcome and durable ownership determine scope; file types, configuration syntax, and command names are supporting signals.
- Keep runtime-only service, machine, environment, monitoring, and incident work on the Host or operations path. For mixed work, govern the project portion through Release Handoff and keep runtime execution independently authorized.
- Preserve progressive governance: thin by default, signal-driven, composable, and proportional to risk.
- New prompt content must justify its context cost by changing a meaningful Agent decision.
- Concern cards provide questions and evidence hints; they do not impose a mandatory stage sequence or default Artifact set.
- Keep one logical Primary Agent responsible for each DevelopmentRun. Concern Cards are capabilities of that role and do not map to separate Agents or Sessions.
- Default to one Primary Agent in one main Session. Workers, independent Reviewers, and durable recovery state remain optional, signal-driven, and subject to Host capability and policy.
- Give Workers bounded context and explicit, non-overlapping ownership. The Primary Agent owns global planning, integration, finding resolution, and Release Handoff.
- Verify completion against the integrated revision or explicitly identified working-tree state. Worker checks are candidate evidence until integration preserves their relevance.
- Keep the entrypoint and Concern Cards short. Put complex domain reasoning in precisely routed Domain Guides; measure context cost by what a task actually loads.
- Default to one Reference for the current decision. Future phases do not justify preloading; combine References only when concerns interact in the current judgment.
- Load Project Model only when project meaning, semantic center, feature fit, intentional evolution, or multiple product centers can change a consequential decision. Keep clear local work on its ordinary path.
- Distinguish accepted, evidenced, inferred, contested, and unknown Project Model statements. Existing code and documentation are contextual evidence; neither receives universal authority.
- Keep a reversible Project Model in the session. Persist it only for coordination, recovery, formal review, or recurring decisions; prefer an existing project fact owner and avoid duplicate identity documents.
- Lite, Standard, and Strict govern decision and coordination depth. Verification Tier 0-3 governs evidence breadth. Keep these axes independent.
- Treat the Test System as a subset of the Verification Harness and the Verification Harness as a subset of the Project Harness. Set membership alone does not escalate governance.
- An edited Harness component cannot be the sole evidence of its correctness. Relaxed or replaced protection records the claim-level coverage delta.
- Write the installable Skill's runtime guidance in English: `rung/SKILL.md`, `rung/references/`, `rung/profiles/`, `rung/assets/`, and `rung/agents/`.
- Route project-meaning and semantic-drift signals through Clarify, Inspect, Design, and Review to `project-model.md`; route material engineering-structure signals through Design, Implement, and Review to `engineering-structure.md`; route explicit existing-system architecture, modularity, structural-debt, dependency-shape, or framework-fit assessment to `architecture-assessment.md`. Keep these contextual and evidence-driven; do not create universal structure rules.

## Implementation conventions

- Python scripts target Python 3.11+ and use the standard library.
- Script stdout is machine-readable JSON; diagnostics belong in structured fields.
- Verification commands use argument arrays and `shell=False`.
- Verification-plan tiers are integers from 0 through 3. Tier filtering records both selected and skipped checks without adding hidden retries or orchestration.
- Ready or published Release Manifests use passing local JSON evidence or an external evidence URI.
- Runtime helper examples resolve scripts from the installed Skill root and pass the target project explicitly.
- External writes remain subject to user authorization and host permissions.
- User changes and dirty worktrees enter the protection scope before edits.

## Verification

Run after changing scripts, templates, or Skill routing:

```bash
python -B -m unittest discover -s tests -v
ruff check --no-cache .
```

Run the host `skill-creator` quick validator after changing `SKILL.md` or `agents/openai.yaml`.
