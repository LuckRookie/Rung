# Release Card

Read when preparing a code state, version, artifact, note, publication, or downstream execution handoff.

## Operate

The Primary Agent assembles the release state.

- Bind the handoff to a revision or explicit working-tree state and the integrated evidence that covers user-visible acceptance.
- Confirm required tests, build, package, checksums, documentation, version, changelog, migration, and project release controls.
- Identify deliverables, reproduction steps, limitations, unverified areas, residual risks, and downstream actions.
- Obtain user authorization before Git push, tag, remote release, package publication, or another external write; record only actions actually completed.

Stop when the release is explicitly `blocked`, `ready`, or, after authorized actions, `published`. Output the state, identity, artifacts, evidence, risks, and next owner.

Use `assets/release-manifest.template.yaml` for a formal handoff. Ready or published manifests reference passing local JSON evidence or an external evidence URI. Optional checks: `python <rung-skill-root>/scripts/validate_artifacts.py --run-dir <run-dir>` and `python <rung-skill-root>/scripts/check_release.py --manifest <release.yaml> --project <path>`.
