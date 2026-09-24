# Content boundary forward smoke — 2026-09-25

This is a targeted candidate-only forward smoke of the content corrections. It
does not establish improvement over host baseline or the stable skill. The
candidate is based on commit `aa2312e`; the exact installable file set is identified
by the SHA256 manifest and aggregate identity in the result files below.

Three independent Codex task agents received isolated Git project copies, user
requests and the candidate skill path. They were not given the review, proposed
fixes, evaluator protocol or expected outcomes. Rung metadata was supplied as an
available skill for the first roster request; the other requests explicitly used
Rung. The roster and delivery follow-ups reused their respective task sessions.

The model was inherited from the host; exact model/sampling settings and an
independent host read trace were not captured. Resource reads in this table are
the agents' reports. Project bytes, configured checks and the regression mutant
were independently checked by the Primary Agent.

| Request | Observed handoff | Reported Rung reads | Project outcome |
|---|---|---|---|
| Explain current roster project | Grounded explanation, source conflicts and unknowns | None | No edit; user note preserved |
| Decide substitution ownership | Rota owner, preserved interval/coverage contracts, bounded proposal and open decisions | SKILL, Design | No edit or release claim |
| Add existing-helper regression | Verified test change | SKILL, Verify | One 3-line test added; production unchanged |
| Hand off failed package publication | Blocked, completed push distinguished from failed target, recovery owner and condition | SKILL, Release | No external action or edit |
| Hand off successful Git-only target | Published for that authorized target, based on the local receipt | Reused SKILL and Release | No external action or edit |

The roster decision proposed a pure slot transformation and explicitly declined
to claim it had implemented or tested that algorithm. It used the existing lookup
to check a manually constructed example. These observations support a bounded
decision handoff, not implementation correctness for the proposed feature.

The Primary Agent independently ran the roster suite (3 tests) and the completed
timeout suite (3 tests). In a separate evaluation copy, replacing the parser with
`return int(value)` made the new empty-value regression fail with the relevant
`ValueError`; the other two checks passed. File hashes showed only the intended
test changed. Roster files, its pre-existing user note and the delivery receipt
remained unchanged. No fixture gained a governance artifact.

Reproduction sources and prompts are in
[the fixture protocol](../fixtures/content-review/README.md). Use fresh copies,
preserve the user-note change, and hide the protocol's evaluator sections from the
tested agent. The Git-target receipt is a separate data variant; its follow-up
prompt replaces “publishing the package” with “pushing the verified source
revision to the named Git remote branch.”

Evidence:

- [Forward observations and limits](2026-09-25-content-boundaries/forward-results.json)
- [Exact candidate file hashes](2026-09-25-content-boundaries/candidate-skill-manifest.json)
- [Fixture starting hashes](2026-09-25-content-boundaries/fixture-baseline.json)
- [Independent checks and failure output](2026-09-25-content-boundaries/independent-forward-checks.json)
- [Generated test diff](2026-09-25-content-boundaries/local-check.patch)
- [Git-target receipt](2026-09-25-content-boundaries/delivery-push-only.json)

These results support the tested routing and handoff boundaries on the small
fixtures. They do not measure fresh-session production discovery, actual registry
publication, architectural benefit, multi-model reliability or context savings.
The full baseline/control/candidate evaluation protocol remains separate work.
