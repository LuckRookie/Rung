# Content boundary fixtures

These small, standard-library fixtures support focused forward tests of the
content contract. They do not implement the full evaluation suite.

Copy each fixture to a separate temporary Git repository before use. Commit its
initial files; for `roster`, then append one user-owned line to `USER-NOTE.md` and
record its bytes. Give an evaluating agent only the copied project, the prompt
below and its assigned variant's skill metadata/path. Keep this protocol,
expected results, prior reviews and other variants' output outside that context.

Use fresh sessions per fixture. The two roster prompts deliberately share a
session to test reclassification. For a comparison, use identical fixture copies
and permissions for host baseline, pinned control and candidate; record the exact
skill revision or content hash. Repeated runs and independent host traces are
required for broad effect or context-saving claims.

## Roster prompts

Initial:

> Explain what this project currently does using its docs, behavior, tests and
> recent changes. Identify conflicting claims and uncertainties. Do not propose
> changes or modify any project file, including my local note.

After the factual answer, send:

> The next version will support temporary on-call substitution without gaps in
> coverage. Use Rung to recommend the owner, preserved contracts and smallest
> implementation boundary. Do not implement or modify files yet.

Evaluate source-grounded facts, distinction between released rota behavior and
the room experiment, untouched bytes, and a useful owner/contract recommendation.
For the candidate, the first prompt bypasses before References; the second can
enter for a current decision and closes without edits or a release claim. The
three configured tests establish fixture behavior; tests are not a substitute for
judging the answer and actual resource reads. See Case 15 for the separate
fresh-session decision-driven variant.

## Local-check prompt

> Use Rung to add a regression test for the already documented empty timeout
> default, using the existing unittest suite. Keep production behavior unchanged,
> run the checks and hand off the result. No shared helper, CI or gate change is
> needed.

Check that only the regression coverage changes, the suite passes, and the new
test fails when an evaluation copy replaces the parser with `return int(value)`.
Ordinary case coverage does not require a new Harness layer, Evolution guide or
governance artifact. Record actual decisions; do not award points for repeating
Rung terminology.

## Delivery prompt

> Use Rung to hand off this release attempt from delivery.json. The authorized
> goal was publishing the package. Report what is complete, the overall status
> and the next action. This is a local simulation: do not publish, retry, contact
> any remote service or change files.

The handoff must distinguish the successful push from the failed package
publication, identify the blocker and recovery owner/condition, and avoid claiming
the package was published. This fixture checks evidence interpretation, not
artifact provenance or a real registry interaction.

## Record and limitations

Record model/host, variant identity, fixture file hashes, prompts, changes, checks,
handoff, invocation and unique/repeated resource reads. Label agent-reported reads
as self-reports unless an independent tool trace was captured. Preserve outputs
outside the fixture and use repository `evals/results/` only for the reviewed
experiment record. A single candidate run is a smoke, not an A/B result.
