# Verify Card

Read before claiming work complete, compatible, buildable, usable, reproducible, or release ready.

## Operate

- Map each material claim to an observation on the identified integrated state.
- Start with configured target checks; expand through static, unit, contract, integration, end-to-end, build, package, or matrix evidence as risk requires.
- Preserve failure visibility and record command, exit code, scope, target state, artifact, skipped checks, and environment limits.
- Identify state before and after checks. Source or plan drift removes applicability; rerun against the final state.
- Treat worker checks as candidate evidence until their relevance survives integration.

Stop when material claims have proportionate evidence and uncovered scope is explicit. Output evidence, gaps, blocked checks, and risk. Keep small results in the handoff; use `assets/verification-report.template.md` when persistence helps.

Read [Verification Harness](verification-harness.md) for a missing layer and [Project Harness](project-harness.md) when checks may be wrong. Optional Evidence v2 runner: `python <rung-skill-root>/scripts/run_verification.py --project <path> --plan <plan.json> --max-tier <0-3> --output <evidence.json>`.
