# {{block_id}}: {{verifiable_result}}

- Parent plan: {{overview_link}}
- Status / Owner: {{status_and_owner}}

## Outcome and boundaries

{{observable_result_and_acceptance_ids}}

- Entry conditions: {{required_contracts_inputs_task_ids_evidence_and_authority}}
- Owned and affected scope: {{modules_producers_consumers_and_preserved_behavior}}
- Source references: {{verified_paths_contracts_and_design_decisions}}

## Tasks

Repeat this unit for each executable task. Use stable IDs such as `2.3`; split again when distinct outputs or dependency chains require separate tracking. Reference shared checks precisely instead of duplicating them.

- [ ] **{{task_id}} — {{concrete_action_and_output}}**
  - Prerequisites: {{task_ids_required_outputs_and_readiness_evidence}}
  - Change: {{where_what_and_behavior_to_preserve}}
  - Completion check: {{command_or_procedure_expected_assertions_and_relevant_failure_cases}}
  - Evidence after execution: {{revision_or_patch_actual_result_evidence_location_and_residual_gaps}}

## Integration and verification

- Consumer handoff: {{output_contract_and_downstream_task_ids}}
- Block checks: {{checks_expected_results_and_required_environment}}
- Unproven scope: {{fixtures_only_paths_unrun_checks_or_planning_gaps}}

Stable contracts may support preparation; integrated acceptance requires the actual prerequisite implementation and evidence. Attribute shared evidence to the task IDs it proves.

## Exit conditions and recovery

- Exit conditions: {{facts_following_blocks_can_rely_on}}
- Remaining exit conditions: {{unfinished_conditions_blockers_and_owning_task_ids}}
- Failure response: {{stop_condition_preserved_work_and_recovery_action_if_needed}}
- Resume: {{current_task_next_ready_action_and_state_to_revalidate}}
