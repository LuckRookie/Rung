# Rung repository instructions

## Product facts

- `Rung.md` is the source of truth for product shape, system boundary, workflow, profiles, concepts, and release contract.
- `INSTALL.md` is the source of truth for package coordinates, installation scope, conflict handling, and installation verification.
- `rung/SKILL.md` is the user-facing Skill entrypoint. Keep it concise and route conditional detail to references.
- `rung/references/execution-model.md` is the source of truth for Primary Agent ownership, inspection radius, design persistence, plan and implementation ownership, Worker and Reviewer roles, cross-session recovery, and integrated responsibility.
- `rung/references/` contains concern cards and governance reminders loaded only when their signals are present.
- `rung/references/project-harness.md` defines the Project Harness scope, Test System relationship, problem signals, and routing.
- `rung/references/harness-evolution.md` is the detailed guide for independently evidenced repair, coverage change, migration, rollback, and cleanup of an existing Harness.
- `rung/references/verification-harness.md` is a specialized Verify reference for evidence gaps and growing test, documentation, build, CI, package, or end-to-end infrastructure.
- `rung/profiles/` contains optional depth hints for Lite, Standard, and Strict governance.
- `rung/assets/` contains optional templates selected when persistence improves coordination, recovery, review, or handoff.
- `rung/scripts/` contains deterministic, dependency-free helpers.
- `evals/` contains host-neutral behavioral scenarios for routing, engineering decisions, evidence, and context-cost evaluation.

## Documentation style

- Define products through capabilities, behavior, inputs, outputs, and responsibility handoffs.
- Use direct statements. Category-exclusion inventories and comparison slogans do not belong in product descriptions.
- Keep each fact in one maintained location and link to it from other documents.
- Preserve the Intent-to-Release boundary established in `Rung.md`.
- Preserve progressive governance: thin by default, signal-driven, composable, and proportional to risk.
- New prompt content must justify its context cost by changing a meaningful Agent decision.
- Concern cards provide questions and evidence hints; they do not impose a mandatory stage sequence or default Artifact set.
- Keep one logical Primary Agent responsible for each DevelopmentRun. Concern Cards are capabilities of that role and do not map to separate Agents or Sessions.
- Default to one Primary Agent in one main Session. Workers, independent Reviewers, and durable recovery state remain optional, signal-driven, and subject to Host capability and policy.
- Give Workers bounded context and explicit, non-overlapping ownership. The Primary Agent owns global planning, integration, finding resolution, and Release Handoff.
- Verify completion against the integrated revision or explicitly identified working-tree state. Worker checks are candidate evidence until integration preserves their relevance.
- Keep the entrypoint and Concern Cards short. Put complex domain reasoning in precisely routed Domain Guides; measure context cost by what a task actually loads.
- Lite, Standard, and Strict govern decision and coordination depth. Verification Tier 0-3 governs evidence breadth. Keep these axes independent.
- Treat the Test System as a subset of the Verification Harness and the Verification Harness as a subset of the Project Harness. Set membership alone does not escalate governance.
- An edited Harness component cannot be the sole evidence of its correctness. Relaxed or replaced protection records the claim-level coverage delta.
- Write the installable Skill's runtime guidance in English: `rung/SKILL.md`, `rung/references/`, `rung/profiles/`, `rung/assets/`, and `rung/agents/`.
- Treat code ownership, change locality, information hiding, dependency direction, and abstraction evidence as contextual design judgments. Route them through Design and Review signals instead of universal structure rules.

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
