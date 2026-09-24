# Rung repository instructions

## Product facts

- `Rung.md` is the source of truth for product shape, system boundary, workflow, profiles, concepts, and release contract.
- `INSTALL.md` is the source of truth for package coordinates, installation scope, conflict handling, and installation verification.
- `rung/SKILL.md` is the user-facing Skill entrypoint. Keep it concise and route conditional detail to references.
- `rung/references/execution-model.md` is the source of truth for Primary Agent ownership, inspection radius, design persistence, plan and implementation ownership, Worker and Reviewer roles, cross-session recovery, and integrated responsibility.
- `rung/references/development-scope.md` defines the two-part membership test for codebase relationship and active development claim, early exit, mixed ownership, and the separate materiality/explicit-invocation activation policy.
- `rung/references/` contains concern cards and governance reminders loaded only when their signals are present.
- `rung/references/project-harness.md` defines the Project Harness scope, Test System relationship, problem signals, and routing.
- `rung/references/harness-evolution.md` is the detailed guide for independently evidenced repair, coverage change, migration, rollback, and cleanup of an existing Harness.
- `rung/references/verification-harness.md` is a specialized Verify reference for evidence gaps and growing test, documentation, build, CI, package, or end-to-end infrastructure.
- `rung/references/engineering-structure.md` is the shared guide for contextual ownership, change locality, information hiding, dependency knowledge, state, data, errors, abstractions, and structural testability.
- `rung/references/architecture-assessment.md` is the scenario- and evidence-driven guide for decision-ready assessment of an existing architecture, modularity, structural debt, dependency shape, or framework fit.
- `rung/references/architecture-design.md` guides new boundaries using current scenarios, credible evolution when relevant, and persistence only for a future consumer.
- `rung/references/project-model.md` defines how Clarify and Inspect recover an evidence-backed project identity, semantic center, feature-fit boundary, and credible evolution for Design and Review.
- `rung/references/design-exploration.md` defines scenario-driven exploration when materially different paths leave a consequential development decision under-supported.
- `rung/references/software-quality.md` defines current software fitness, touched-owner coherence, quality evidence, code-level operability, and promotion of stable judgments into the Project Harness.
- `rung/references/technical-debt.md` defines qualified future engineering obligations, debt economics and systems, management strategies, safe repayment, and consumer-driven persistence.
- `rung/profiles/` contains optional depth hints for Lite, Standard, and Strict governance.
- `rung/assets/` contains optional templates selected when persistence improves coordination, recovery, recurring decisions, review, or handoff; `project-model.template.md` is the fallback for shared identity facts and `technical-debt-item.template.md` for qualified debt without a project-owned issue shape.
- `rung/contracts/rung-contract.json` is the machine-readable owner for the Scope Gate, activation policy, claim-appropriate completion, Evidence applicability, reachable Concern routes, context budgets, and package channel facts.
- `rung/scripts/` contains deterministic, dependency-free helpers, including the structured Scope Gate evaluator and shared project-state identity support.
- `rung/scripts/README.md` owns helper state coverage, exclusions, unsupported configurations, and state-schema migration rules.
- `evals/` contains host-neutral behavioral scenarios for development-intent routing, Design Exploration, Project Model decisions, software quality, technical debt, engineering structure, architecture assessment, evidence, and context-cost evaluation.

## Documentation style

- Define products through capabilities, behavior, inputs, outputs, and responsibility handoffs.
- Use direct statements. Category-exclusion inventories and comparison slogans do not belong in product descriptions.
- Keep each fact in one maintained location and link to it from other documents.
- Preserve the User Intent → Development Scope Gate → Active Codebase Development Claim → Claim-appropriate Handoff boundary established in `Rung.md`.
- Before References, check codebase relationship and active development claim, then activation. Implicit use requires material engineering decisions; explicit governance requests waive materiality only. Routine local reversible work with direct checks bypasses Rung. Unknown activation uses minimal host inspection, not speculative governance or a classification question.
- Treat a codebase relationship, repository presence, path, file type, tool use, and incidental code as insufficient scope evidence on their own. An outcome that ends with understanding current codebase facts exits before another Rung resource loads. Runtime guidance defines the positive set without inventorying the open-ended space outside it.
- Keep work outside the positive set on the Host or its owning workflow. For mixed work, govern only the qualifying codebase portion through its claim-appropriate Handoff and preserve independent ownership and authorization for the rest.
- Preserve progressive governance: thin by default, signal-driven, composable, and proportional to risk.
- New prompt content must justify its context cost by changing a meaningful Agent decision.
- Concern cards provide questions and evidence hints; they do not impose a mandatory stage sequence or default Artifact set.
- Keep one logical Primary Agent responsible for each DevelopmentRun. Concern Cards are capabilities of that role and do not map to separate Agents or Sessions.
- Default to one Primary Agent in one main Session. Workers, independent Reviewers, and durable recovery state remain optional, signal-driven, and subject to Host capability and policy.
- Give Workers bounded context and explicit, non-overlapping ownership. The Primary Agent owns global planning, integration, finding resolution, and final Handoff; Release applies to active delivery claims.
- Verify completion against an identified integrated Commit or working-tree state. Evidence records target and final state plus Plan identity; drift removes applicability. Worker checks are candidate evidence until integration preserves their relevance.
- Keep the entrypoint and Concern Cards short. Put complex domain reasoning in precisely routed Domain Guides; measure context cost by what a task actually loads.
- Default to zero or one Reference for the current decision; reuse loaded guidance. Future phases do not justify preloading; combine References only when concerns interact in the current judgment.
- Treat Software Quality as current fitness and Technical Debt as avoidable future burden under credible evolution. Either axis can be high while the other remains low.
- Keep ordinary implementation and review focused on the touched ownership boundary. A repository-wide quality audit or debt-system review requires a material current signal or an explicit request.
- Qualify debt through a present construct, credible trigger or exposure, and an interest, propagation, risk, coordination, or option-loss mechanism. Smells, TODOs, age, size, and tool scores remain investigation signals.
- Preserve current defects, vulnerabilities, privacy violations, data failures, risks, feature gaps, and necessary complexity under their primary classification and severity when debt also contributes.
- Prefer the project's issue tracker, roadmap, architecture, dependency, migration, or Harness owner for durable debt state. Create a Rung debt Artifact only for a real future consumer and when no better project shape exists.
- Load Project Model only when project meaning, semantic center, feature fit, intentional evolution, or multiple product centers can change a consequential decision. Keep clear local work on its ordinary path.
- Load Design Exploration only when an active consequential decision remains under-supported because several materially different interpretations or behavior paths can change ownership, contracts, state, UX, risk, or implementation direction. Do not impose a fixed scenario or alternative count.
- Distinguish accepted, evidenced, inferred, contested, and unknown Project Model statements. Existing code and documentation are contextual evidence; neither receives universal authority.
- Keep a reversible Project Model in the session. Persist it only for coordination, recovery, formal review, or recurring decisions; prefer an existing project fact owner and avoid duplicate identity documents.
- Lite, Standard, and Strict govern decision and coordination depth. Verification Tier 0-3 governs evidence breadth. Keep these axes independent.
- Treat the Test System as a subset of the Verification Harness and the Verification Harness as a subset of the Project Harness. Set membership alone does not escalate governance.
- An edited Harness component cannot be the sole evidence of its correctness. Relaxed or replaced protection records the claim-level coverage delta.
- Write the installable Skill's runtime guidance in English: `rung/SKILL.md`, `rung/references/`, `rung/profiles/`, `rung/assets/`, and `rung/agents/`.
- Route project-meaning and semantic-drift signals through Clarify, Inspect, Design, and Review to `project-model.md`; unresolved consequential design paths through Clarify, Project Model, and Design to `design-exploration.md`; material current-fitness signals through Design, Implement, and Review to `software-quality.md`; qualified future obligations through the concern that discovers them to `technical-debt.md`; material engineering-structure signals through Design, Implement, and Review to `engineering-structure.md`; and decision-ready existing-system architecture assessment to `architecture-assessment.md`. Keep each route contextual and evidence-driven.

## Implementation conventions

- Python scripts target Python 3.11+ and use the standard library.
- Script stdout is machine-readable JSON; diagnostics belong in structured fields.
- Verification commands use argument arrays and `shell=False`.
- Verification-plan tiers are integers from 0 through 3. Tier filtering records both selected and skipped checks without adding hidden retries or orchestration.
- Ready or published Release Manifests use internally consistent local Evidence v2 that matches the target state and covers every check declared `required_for_release`, or an external Evidence URI reported as delegated-unverified.
- Local Evidence uses State schema v2. Git identity covers the repository; unmodeled gitlinks, nested repositories, and unreadable state block helper evidence. Apply coverage rules to historical commits as well as current worktrees.
- Candidate commands from project inspection distinguish project-declared entry points from convention-based inference; a tests directory alone supplies no language evidence.
- Runtime helper examples resolve scripts from the installed Skill root and pass the target project explicitly.
- External writes remain subject to user authorization and host permissions.
- User changes and dirty worktrees enter the protection scope before edits.

## Verification

Run after changing scripts, templates, or Skill routing:

```bash
python -B -m unittest discover -s tests -v
ruff check --no-cache .
python rung/scripts/validate_contract.py --skill-root rung
python rung/scripts/evaluate_scope.py --input <scope-classification.json>
```

Run the host `skill-creator` quick validator after changing `SKILL.md` or `agents/openai.yaml`.
