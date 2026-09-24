# Release Card

Read for readiness, version, artifact, publication or downstream delivery claims.

## Operate

- Bind the handoff to the commit or state identity covered by integrated evidence.
- Confirm required checks, artifacts, checksums, docs, version, migration and project release controls.
- Identify the delivery target, reproduction steps, limits, risks and next owner.
- Act within user authorization and host permissions; record only completed actions.

Manifest `ready` maps to `release ready`; `blocked` maps to `blocked handoff`. `published` requires success at the authorized delivery target. A prerequisite push or tag cannot complete a package publication. On partial failure, report completed actions, remaining blockers and recovery.

Use `assets/release-manifest.template.yaml` when needed. Ready/published local Evidence v2 must be consistent, stable, state-matched and cover all release-required plan checks. Unvalidated external evidence is `delegated-unverified`. Optional check: `python <rung-skill-root>/scripts/check_release.py --manifest <release.yaml> --project <path>`.
