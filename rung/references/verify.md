# Verify Card

Read before claiming work complete, compatible, buildable, usable, reproducible, or release ready.

## Operate

- Map each material claim to a direct observation on the integrated revision or described working-tree state.
- Start with configured high-signal target checks; expand to static, unit, contract, integration, end-to-end, build, package, or matrix evidence as risk requires.
- Preserve failure visibility and record command, exit code, scope, revision, artifact, skipped checks, and environment limits.
- Treat worker checks as candidate evidence until their relevance survives integration.

Stop when material claims have proportionate evidence and uncovered scope is explicit. Output evidence, gaps, blocked checks, and residual risk. Record small results in the handoff; use `assets/verification-report.template.md` when review or release needs durable evidence.

Read [Verification Harness](verification-harness.md) for a missing evidence layer or new infrastructure. Read [Project Harness](project-harness.md) when checks may be wrong, conflicting, relaxed, or replaced. Batch runner: `python <rung-skill-root>/scripts/run_verification.py --project <path> --plan <plan.json> --max-tier <0-3> --output <evidence.json>`.
