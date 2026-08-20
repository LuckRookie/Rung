# Change Plan

| Field | Value |
|---|---|
| Run ID | `{{run_id}}` |
| Primary Agent | `{{primary_agent}}` |
| Baseline revision | `{{revision}}` |
| Governance depth | `{{governance_depth_or_none}}` |
| Execution mode | `{{single_session_cross_session_or_worker_assisted}}` |
| Plan status | `{{status}}` |

## Change units

| Order | Acceptance | Owner | Files or modules | Prerequisite | Change | Completion check | Status |
|---|---|---|---|---|---|---|---|
| 1 | AC-1 | {{primary_or_worker}} | `{{path}}` | {{prerequisite}} | {{change}} | {{completion_check}} | pending |

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

## Worker task packets and integration

| Worker | Owned scope | Shared contract | Protected user work | Handoff | Integration check |
|---|---|---|---|---|---|
| {{worker}} | `{{owned_scope}}` | {{shared_contract}} | {{protected_work}} | {{handoff}} | {{integration_check}} |

## Failure and recovery

- Failure signal: {{failure_signal}}
- Return concern or recovery point: {{return_concern_or_recovery_point}}
- Recovery or rollback: {{recovery}}
- Resume state and next action: {{resume_state_and_next_action}}
