# Artifacts and Persistence

Read when future work, recovery, review, or release needs durable information.

## Homes

| State | Preferred home |
|---|---|
| Local reversible choice | conversation, code, and tests |
| Session coordination | host plan or concise session note |
| Lasting requirement, contract, architecture, data, UX, build, test, or release fact | owning project document, config, or code |
| Cross-session, multi-executor, comparison, or recovery state | existing issue or `.rung/runs/<run-id>/` |

Create an Artifact when it improves resumption, coordination, review, migration, evidence, or handoff. Keep each fact with one owner. Promote stable decisions to their owner; retain or clean run state by project convention and an explicit condition.

## Run state

For recovery, retain outcome, decisions and delegated scope, root and baseline, protected user work, authoritative facts, design, completed units, next action, evidence, gaps, and risks. On resume, compare saved and current Git state.

`.rung/` is optional. Run files may include `brief.md`, `context.md`, `project-model.md`, `design.md`, `plan.md`, `debt.md`, Harness or verification state, `review.md`, `evidence.json`, and `release.yaml`. Reuse project artifacts by path and revision.

## Templates

- collaborative outcome and decisions: `assets/development-brief.template.md`
- inspected facts: `assets/project-context.template.md`
- shared project identity and fit: `assets/project-model.template.md`
- durable design: `assets/solution-design.template.md`
- qualified debt without a project issue shape: `assets/technical-debt-item.template.md`
- coordinated execution: `assets/change-plan.template.md`
- existing Harness evolution: `assets/harness-change.template.md`
- verification infrastructure: `assets/verification-harness.template.md`
- repeatable checks: `assets/verification-plan.template.json`
- evidence: `assets/verification-report.template.md`
- formal review: `assets/review-result.template.md`
- release: `assets/release-manifest.template.yaml`

Select fields proportionally. Record only credential names, permissions, or secure references; keep secrets and restricted data in dedicated systems.
