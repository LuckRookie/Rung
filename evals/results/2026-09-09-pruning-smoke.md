# Candidate pruning smoke — 2026-09-09

This is a targeted forward-test, not a repeated host-baseline/control/candidate experiment. The uncommitted candidate is based on `aac3e057be579c7153178767f68c5ef087131e66`. No installed skill, tag, or remote package was changed.

## Scope

The evaluating subagent received the candidate metadata, two concrete user requests and isolated Python repositories. It was not given expected activation decisions or evaluator labels. Both tasks ran in one evaluation session as separate task scopes; this does not measure fresh-session production discovery or cross-model reliability. Resource reads below are the evaluator's recorded paths, not an independently instrumented host trace.

## Outcomes

| Fixture | Activation | Recorded resources | Implementation and evidence |
|---|---|---|---|
| Local cart total | Bypass | No Rung files | Clamp excessive credit at zero; 2 configured tests pass |
| Tenant authorization | Enter | SKILL.md, Design, Verify | Remove admin cross-tenant bypass; 4 configured tests pass |

The Primary Agent separately checked 6 cart cases and 8 authorization cases, reproduced the original cross-tenant admin failure, and checked both user-edited README files byte for byte. Neither fixture gained a `.rung/` artifact. These checks support correctness on the fixtures; they do not establish universal code quality or an appropriate policy for unspecified identity models.

## Pruning footprint

At the start of this revision, SKILL.md was 2770 UTF-8 bytes. The final entrypoint is 2387 bytes (including metadata); its budget is now 2,400. The 3752-byte default quality guide was removed, and its essential actions remain in the entrypoint and relevant cards. Domain guidance remains reachable through the stage cards.

Final entrypoint SHA-256: `aec89301f15c00fb55a35c0f9ecf5d0f3c7bf62541ad5e9bc7cbfa8e1c0a2180`. This identifies the finalized file after metadata quoting and minor wording corrections; it is not a hash of a captured model prompt. Byte reduction is a static package measurement, not measured token savings or a comparison against the stable skill.

## Evidence locations and limits

The recorded raw outputs are retained beside this report in `2026-09-09-pruning-smoke/forward-result.json` and `2026-09-09-pruning-smoke/independent-checks.json`. Their embedded `/tmp/rung-pruning-bc97ail7/` paths identify the original isolated run; temporary fixtures and complete process logs remain outside the repository and installable package.

The repository tests also cover the labeled activation corpus, malformed inputs, legacy input defaults, reclassification, explicit membership limits, indirect guide reachability, and entrypoint growth. They test supplied host judgments and structure, not natural-language intent classification. Full host traces, repeated variants, broad lifecycle tasks, and real integration/release environments remain outside this smoke.
