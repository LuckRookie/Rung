# Release Card

Read for release readiness, version, artifact, publication, or downstream delivery. Decision, review, and change-verified claims close from their owner.

## Operate

- Bind the handoff to the commit or state identity covered by integrated evidence.
- Confirm required tests, build, package, checksums, documentation, version, changelog, migration, and project release controls.
- Identify deliverables, reproduction steps, limitations, unverified areas, residual risks, and downstream actions.
- Obtain user authorization before Git push, tag, remote release, package publication, or another external write; record only actions actually completed.

Stop when the release is explicitly `blocked`, `ready`, or, after authorized actions, `published`. Output the state, identity, artifacts, evidence, risks, and next owner.

Use `assets/release-manifest.template.yaml` when formal handoff helps. Ready/published local Evidence v2 must be consistent, stable, state-matched, and cover each release-required check in its plan. Report unvalidated external evidence as `delegated-unverified`. Optional check: `python <rung-skill-root>/scripts/check_release.py --manifest <release.yaml> --project <path>`.
