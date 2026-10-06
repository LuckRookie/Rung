# Change Plan: {{change_name}}

- Status: Draft
- Primary owner: {{owner}}
- Baseline and protected work: {{revision_and_user_owned_changes}}
- Next action: {{ready_task_id_or_planning_gap}}

Keep Draft until all required blocks are written and coverage, dependencies and checks have been reviewed. Then update readiness or execution status from actual evidence; identify partial, blocked or superseded work explicitly.

## Goal and accepted direction

{{target_behavior_and_accepted_decisions_with_fact_source_links}}

- Scope and preserved behavior: {{included_outcomes_excluded_work_and_invariants}}
- Authority: {{authorized_work_and_relevant_action_limits}}
- Assumptions and open decisions: {{evidence_needed_owner_and_affected_task_ids}}

## Result blocks and coverage

| ID / Link | Verifiable outcome | Acceptance covered | Prerequisite outputs / Task IDs | Integration handoff | Status |
|---|---|---|---|---|---|
| {{block_id_and_link}} | {{outcome}} | {{acceptance_ids}} | {{dependencies}} | {{consumer_and_output}} | {{status}} |

Expand each block using `plan-result-block.template.md`, in its own file or inline for a smaller plan. Keep task details in the block. Add blocks until the agreed scope is covered; numbering does not prescribe execution order.

## Integrated acceptance

| Acceptance | Observable condition | Check / Expected result | Required blocks or tasks |
|---|---|---|---|
| {{acceptance_id}} | {{condition}} | {{check_and_assertion}} | {{ids}} |

- Remaining planning or evidence gaps: {{gap_affected_outcome_and_resolution_condition}}
- Overall completion: {{all_required_outputs_and_integrated_checks}}

## Cross-block risks and recovery

| Risk / Trigger | Owning block | Response / Recovery point |
|---|---|---|
| {{risk}} | {{block_id}} | {{response}} |

## Progress and handoff

- Current focus: {{block_id_current_task_and_exit_conditions_to_close}}
- Remaining work: {{unfinished_exit_conditions_blockers_and_responsible_task_ids}}
- Latest integrated evidence: {{revision_or_patch_checks_results_and_evidence_links}}
- Decision changes: {{change_reason_and_affected_ids}}
- Final or partial handoff: {{verified_outputs_remaining_work_risks_and_next_owner}}
- Closure or replacement: {{completion_cancellation_or_superseding_plan_and_project_archive_convention}}

For cross-block work, record the following here or link the existing session note. Omit when unused; return to the current focus after the bounded work, or record an explicit priority change.

| Target task | Reason to advance now | Satisfied prerequisites / Evidence | Bounded output | Return condition / Main task |
|---|---|---|---|---|
| {{task_id}} | {{reason}} | {{required_outputs_and_evidence}} | {{preparation_or_integrated_result}} | {{condition_and_task_to_resume}} |
