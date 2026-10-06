# Engineering-first entrypoint trial — 2026-09-29

The candidate puts engineering decisions ahead of detailed routing and handoff
classification. Its installable package differs from control commit `2745157`
only in `SKILL.md`. The final entrypoint is 2,323 bytes, versus 2,393 for control;
this is a redistribution of guidance, not a material context-saving claim.

## Setup

Claude Code 2.1.281 reported model `claude-opus-5-5` for all runs. Each run used a
fresh nonpersistent session in safe mode, with only Read, Write, Edit, Glob, Grep
and Bash enabled. No model override was used. Tasks prohibited network, installs,
other agents, commits and publication. All projects were isolated Git copies with
the same user-owned note appended after the initial commit.

The structural task reuses [Case 39](../cases/39-bugfix-structural-cause.md), with
the synthetic history hint removed from the fixture README in every arm. Public
contracts and code remain unchanged. Each arm ran three times:

- baseline: no Rung metadata or skill available;
- control: metadata and package from `2745157`;
- candidate: metadata and exact final package snapshot.

Three additional candidate runs used a local cart-total floor defect. These are
proportionality checks, not a three-arm comparison of local-task discovery.
The exact prompts and host tool traces are preserved in the raw archive recorded
in [observations](2026-09-29-entrypoint-trial.json). Skill metadata and paths were
supplied in the task; native skill discovery was disabled. This measures behavior
under controlled availability, not automatic selection from a production catalog.

An earlier candidate snapshot was explored before independent review. Review
identified that authorization and decision-only work needed clearer wording;
the final entrypoint also retains migration/release discovery and blocker recovery.
All candidate and local runs below were rerun on that final snapshot. Earlier
candidate runs are excluded. Baseline and control used the same fixtures and host
configuration, but ran earlier; there is no randomized timing or cost experiment.

## Results

| Condition | Public behavior | Policy ownership, inspected in code | Skill reads |
|---|---|---|---|
| No Rung, 3 runs | 3/3 pass | All retain separate HTTP and batch eligibility predicates | None |
| Previous Rung, 3 runs | 3/3 pass | All share eligibility and mutation in `orders.py`; adapters translate results | Entrypoint only |
| Final candidate, 3 runs | 3/3 pass | All share eligibility and mutation in `orders.py`; adapters translate results | Entrypoint only |
| Candidate local control, 3 runs | 3/3 pass | Each changes one calculation line; no new abstraction or document | Entrypoint only |

The parent independently checked all four released order states through both
public adapters and a mixed batch: nine observations per structural run. All
configured suites passed. Each local run passed 36 subtotal/credit combinations
and its two existing tests. All user notes remained byte-identical. Production
sources and diffs are retained in the observations so structural judgments can be
inspected independently of the agent's explanation.

Both Rung versions changed the structural outcome relative to baseline in this
small fixture. The candidate did not outperform control on correctness or rule
ownership. Local runs still read the entrypoint, so this does not demonstrate zero
Rung overhead on local tasks. No deeper references or governance artifacts were
needed in these runs. No hidden follow-up was executed in this trial.

## Test maintenance controls

Pure-prose assertions were removed while package, link, schema and executable
behavior checks remain. Isolated copies exercised the coverage change:

- Rephrasing `independent reviewer` as `independent review` fails the old structure
  suite and passes the revised suite.
- A broken reference still fails the revised suite.
- Removing required machine handoff states still fails the revised suite.

These controls show what the deterministic checks accept and reject; they do not
prove that arbitrary prose changes preserve instructional meaning. That remains
a review and behavioral-evaluation responsibility. The final repository passed all
81 tests, Ruff, contract/scope checks, skill-creator validation and diff checks.

## Decision and limits

Keep the candidate for further use: it makes the default engineering guidance
explicit, removes prose-maintenance friction and preserves the observed outcomes
without expanding the runtime package or size limits. Retain the previous version
as the control for subsequent tasks.

These are three repeats per condition on one small synthetic structural fixture,
plus local controls. They do not establish a general success rate, improvement
over the previous version, production discovery, cross-model benefit, or lower
token/time cost. A real historical failure with less obvious ownership remains
the next useful test. Full host JSON and isolated copies are in the local raw
archive; compact results, source diffs, oracle code, runtime hashes and controls
are retained alongside this report.
