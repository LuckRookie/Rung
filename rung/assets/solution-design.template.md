# Solution Design

| Field | Value |
|---|---|
| Run ID | `{{run_id}}` |
| Primary Agent | `{{primary_agent}}` |
| Governance depth | `{{governance_depth_or_none}}` |
| Related acceptance criteria | {{acceptance_ids}} |
| ADR | `{{adr_path_or_none}}` |
| Durable owner | `{{project_fact_owner_or_session_only}}` |

## Design summary

{{design_summary}}

## Decision authority

- User decisions: {{user_decisions}}
- Delegated design scope: {{delegated_design_scope}}
- Open decisions and owners: {{open_decisions_and_owners}}

## Change ownership and boundaries

| Concept / component | Current owner | Change reason | Stable caller-visible boundary |
|---|---|---|---|
| {{concept_or_component}} | {{current_owner}} | {{change_reason}} | {{stable_boundary}} |

- Code expected to change for the same reason: {{co_change_scope}}
- Information kept behind the boundary: {{hidden_details}}
- New public surface or abstraction and its current evidence: {{abstraction_evidence}}

## Interface and data flow

{{interface_and_data_flow}}

## State and error handling

{{state_and_error_handling}}

## Dependencies

- Existing dependencies used: {{existing_dependencies}}
- Dependency changes: {{dependency_changes}}
- Direction and ownership: {{dependency_direction}}
- External implementation details contained at: {{external_detail_boundary}}

## Compatibility, migration and rollback

- Compatibility contract: {{compatibility_contract}}
- Migration sequence: {{migration_sequence}}
- Rollback condition and path: {{rollback}}

## Security, privacy and performance

{{quality_risks_and_controls}}

## Human-facing design

- People and primary tasks: {{people_and_tasks}}
- Flow, hierarchy and defaults: {{flow_hierarchy_and_defaults}}
- Feedback, errors and recovery: {{feedback_errors_and_recovery}}
- Consistency, accessibility and trust: {{consistency_accessibility_and_trust}}
- Credible development signals and revisit conditions: {{development_and_revisit_signals}}

## Verification boundaries

| Risk or behavior | Verification level | Evidence source |
|---|---|---|
| {{risk_or_behavior}} | {{unit_module_integration_e2e}} | {{planned_evidence}} |

## Alternatives and decisions

| Option | Trade-off | Decision |
|---|---|---|
| {{option}} | {{tradeoff}} | {{decision}} |
