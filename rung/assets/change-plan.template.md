# Change Plan

| Field | Value |
|---|---|
| Run ID | `{{run_id}}` |
| Baseline revision | `{{revision}}` |
| Profile | `{{profile}}` |
| Plan status | `{{status}}` |

## Change units

| Order | Acceptance | Files or modules | Change | Completion check | Status |
|---|---|---|---|---|---|
| 1 | AC-1 | `{{path}}` | {{change}} | {{completion_check}} | pending |

## Behaviors and areas to preserve

- {{preserved_behavior_or_area}}

## Interface, data and dependency changes

- Interface: {{interface_change}}
- Data: {{data_change}}
- Dependency: {{dependency_change}}

## Verification sequence

| Order | Claim | Check | Tier | Evidence destination |
|---|---|---|---|---|
| 1 | {{claim}} | `{{command}}` | {{tier}} | `{{evidence_path}}` |

## Documentation and Release work

- {{documentation_or_release_update}}

## Approvals and external actions

| Trigger | Action | Required approval | State |
|---|---|---|---|
| {{trigger}} | {{action}} | {{approval}} | pending |

## Failure and recovery

- Failure signal: {{failure_signal}}
- Return stage: {{return_stage}}
- Recovery or rollback: {{recovery}}
