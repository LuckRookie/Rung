# Verification Harness

| Field | Value |
|---|---|
| Run ID | `{{run_id}}` |
| Revision | `{{revision}}` |
| Harness owner | `{{harness_owner}}` |
| Change reason | {{claim_or_risk_needing_evidence}} |

## Current inventory

| Tier | Existing entry point | Evidence provided | Gate, extended, or diagnostic | Typical cost |
|---:|---|---|---|---|
| {{tier}} | `{{command_or_path}}` | {{existing_evidence}} | {{role}} | {{cost}} |

## Claim and layer map

| Claim or risk | Current gap | Selected layer | Reused check | New or changed check |
|---|---|---:|---|---|
| {{claim_or_risk}} | {{evidence_gap}} | {{tier}} | `{{reused_entrypoint}}` | `{{new_check_path}}` |

## Harness changes

| Action | Component or path | Owner | Purpose | Removal or review condition |
|---|---|---|---|---|
| {{reuse_add_change_or_remove}} | `{{path}}` | {{owner}} | {{purpose}} | {{maintenance_condition}} |

## Environment and lifecycle

- Prerequisites: {{environment_and_permissions}}
- Fixture and test-data ownership: {{fixture_ownership}}
- Setup: {{setup}}
- Isolation: {{isolation}}
- Cleanup: {{cleanup}}
- External services and failure substitutes: {{services_or_fakes}}

## Execution and diagnostics

| Order | Tier | Command | Expected evidence | Failure location |
|---:|---:|---|---|---|
| 1 | {{tier}} | `{{command}}` | {{expected_evidence}} | {{diagnostic_location}} |

- Incorrect-behavior failure observed: {{negative_signal_evidence}}
- Timeout, retry, or flake policy: {{policy_and_original_failure_visibility}}
- Required gates: {{required_gates}}
- Extended checks: {{extended_checks}}
- Diagnostics: {{diagnostic_checks}}
- Known coverage gap: {{remaining_gap}}
