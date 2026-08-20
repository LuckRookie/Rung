# Project Harness Change

| Field | Value |
|---|---|
| Run ID | `{{run_id}}` |
| Baseline revision | `{{baseline_revision}}` |
| Harness area | {{instructions_tests_static_build_ci_or_release}} |
| Change owner | {{owner}} |
| Governance depth | `{{governance_depth}}` |
| Current state | {{proposed_active_rolled_back_or_complete}} |

## Observed problem and authority

- Observable failure or limitation: {{observed_problem}}
- Product, Harness, coupled, or unresolved classification: {{classification}}
- Canonical fact source: `{{authority_path_or_reference}}`
- Authority basis and revision: {{authority_basis}}
- Affected consumers, platforms, and delivery paths: {{consumers_and_scope}}
- User-owned work to preserve: {{existing_changes}}

## Baseline

| Entry point | Protected claim | Current result | Reliability or cost | Raw evidence |
|---|---|---|---|---|
| `{{command_or_path}}` | {{claim}} | {{pass_fail_blocked_flaky_or_skipped}} | {{runtime_flake_or_resource_observation}} | `{{evidence_path}}` |

## Target claims and independent anchors

| Claim type | Target claim | Evidence independent of changed component | Result |
|---|---|---|---|
| Product | {{product_claim}} | {{product_anchor}} | {{result}} |
| Harness | {{known_good_and_known_bad_claim}} | {{independent_harness_anchor}} | {{result}} |
| Operational | {{isolation_cleanup_diagnostics_or_cost_claim}} | {{operational_evidence}} | {{result}} |
| Migration | {{consumer_activation_or_rollback_claim}} | {{transition_evidence}} | {{result}} |

## Component changes

| Component or path | Owner | Repair, extend, replace, relax, or remove | Reason | Reversible action |
|---|---|---|---|---|
| `{{path}}` | {{owner}} | {{action}} | {{reason}} | {{rollback_or_restore_action}} |

## Coverage delta

| Previous protection | Retained or replacement evidence | Coverage gained | Coverage reduced | Residual risk |
|---|---|---|---|---|
| {{previous_claim_and_failure_class}} | {{replacement_or_retained_check}} | {{gain}} | {{reduction}} | {{risk}} |

## Rollout and cleanup

- Comparison or compatibility window: {{old_new_comparison}}
- Diagnostic-to-required activation condition: {{activation_condition}}
- Rollback trigger and action: {{rollback_condition_and_action}}
- Old-path removal condition: {{removal_condition}}
- Temporary exceptions, retries, quarantine, or ignores: {{temporary_controls_and_expiry}}
- Permanent project fact sources to update: {{documentation_configuration_or_code}}

## Evidence and handoff

- Product evidence: {{product_evidence}}
- Harness signal evidence: {{known_good_pass_and_known_bad_fail}}
- Transition evidence: {{parallel_consumer_or_platform_evidence}}
- Unverified areas: {{unverified_scope}}
- Required approval or owner decision: {{approval}}
- Next review or cleanup owner: {{next_owner_and_condition}}
