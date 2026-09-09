# Verification Report

| Field | Value |
|---|---|
| Run ID | `{{run_id}}` |
| Primary Agent | `{{primary_agent}}` |
| Target state | `{{target_commit_or_state_identity}}` |
| State stable during checks | `{{true_or_false}}` |
| Plan digest | `{{plan_sha256}}` |
| Governance depth | `{{governance_depth}}` |
| Requested maximum Tier | `{{requested_max_tier}}` |
| Selected plan checks | `{{selected_check_count}} / {{planned_check_count}}` |
| Evidence file | `{{evidence_path}}` |
| Overall result | `{{pass_fail_blocked_or_waived}}` |
| Evidence applicability | `{{pass_blocked_and_reason}}` |

## Acceptance evidence

| Acceptance | Claim | Evidence | Result |
|---|---|---|---|
| AC-1 | {{claim}} | {{command_or_artifact}} | {{result}} |

## Executed checks

| Check | Tier | Command | Exit code | Duration | Result |
|---|---:|---|---:|---:|---|
| {{check_name}} | {{tier}} | `{{command}}` | {{exit_code}} | {{duration}} | {{result}} |

## Skipped checks

| Check | Tier | Reason | Resulting coverage gap |
|---|---:|---|---|
| {{skipped_check}} | {{tier}} | {{skip_reason}} | {{coverage_gap_or_none}} |

## Build and package evidence

- Build command and result: {{build_evidence}}
- Package command and result: {{package_evidence}}
- Artifact location: `{{artifact_path}}`

## Failures and blocked checks

| Check | State | Evidence | Recovery condition |
|---|---|---|---|
| {{check}} | {{fail_or_blocked}} | {{evidence}} | {{recovery_condition}} |

## Coverage and residual risk

- Covered behaviors: {{covered_behaviors}}
- Areas not covered: {{not_covered}}
- Waived items: {{waived_items}}
- Residual risks: {{residual_risks}}
