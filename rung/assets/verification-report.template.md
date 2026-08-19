# Verification Report

| Field | Value |
|---|---|
| Run ID | `{{run_id}}` |
| Revision | `{{revision}}` |
| Profile / Tier | `{{profile}} / {{tier}}` |
| Evidence file | `{{evidence_path}}` |
| Overall result | `{{pass_fail_blocked_or_waived}}` |

## Acceptance evidence

| Acceptance | Claim | Evidence | Result |
|---|---|---|---|
| AC-1 | {{claim}} | {{command_or_artifact}} | {{result}} |

## Executed checks

| Check | Command | Exit code | Duration | Result |
|---|---|---:|---:|---|
| {{check_name}} | `{{command}}` | {{exit_code}} | {{duration}} | {{result}} |

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
