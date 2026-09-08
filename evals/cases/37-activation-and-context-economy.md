# Case 37: Activation and context economy

## Purpose

Distinguish development membership from the value of invoking governance. Measure actual resource reads as well as completion quality.

## Fixtures and prompts

Use `../activation-cases.json` as an evaluator-owned corpus. Give the agent only the prompt and minimum matching repository, plus normal available-skill metadata. Keep judgments and expected results hidden. Use fresh sessions for independent cases; keep the same session for a deliberate reclassification test.

Include a local arithmetic repair, the same repair in a large repository, a tiny maintained tool with a known owner and check, a one-line tenant authorization repair, a schema migration, a greenfield service with unresolved state/recovery, architecture decision support, release readiness, read-only understanding, a temporary script, mixed work, and unknown impact. Supply an unrelated user edit in the code fixtures.

Run the local repair both implicitly and with an explicit request to use Rung. Also test a prompt merely mentioning Rung and an explicit invocation whose outcome is only understanding. An explicit-use test cannot establish implicit discovery precision.

## Gates

- Complete each user's task correctly and preserve user work, including when Rung bypasses.
- Routine implicit work is unselected, or exits after an accidental entrypoint load with no References or Artifacts.
- Material work enters even when the implementation is a single line or the project is new.
- Explicit small development may enter Lite. Explicit invocation does not override membership.
- Unknown scope or impact uses minimal host inspection without a classification-only question or speculative Guide loading.
- Reassess after facts reveal a material boundary and after that need disappears; activation is not sticky across tasks.
- Standard/Strict depth and test breadth follow consequences, not file count. No required worksheet, independent reviewer, or stage sequence.

## Observations

Record host selection, entrypoint reads, unique and repeated Reference bytes, checks, final diff, protected user work, errors, artifacts and follow-up propagation. Statements about internal reasoning are not evidence. The structured evaluator tests supplied labels; only a host/agent trace can establish actual discovery and loading behavior.

Compare baseline, control and candidate on identical fixtures and repeated runs before making broad quality or token-saving claims. A targeted forward smoke provides narrower evidence and must be labeled accordingly.
