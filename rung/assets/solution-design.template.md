# Solution Design

Select fields for the current decision and its future consumer; omit unrelated sections. Keep local reversible choices in the session, code and tests.

| Field | Value |
|---|---|
| Run ID | `{{run_id}}` |
| Primary Agent | `{{primary_agent}}` |
| Governance depth | `{{governance_depth_or_none}}` |
| Related acceptance criteria | {{acceptance_ids}} |
| Project Model | `{{project_model_path_or_session}}` |
| ADR | `{{adr_path_or_none}}` |
| Durable owner | `{{project_fact_owner_or_session_only}}` |

## Design summary

{{design_summary}}

- Model fit and rationale: {{core_fit_adjacent_extension_or_identity_change}}
- Project Model assumptions or revisions: {{model_assumptions_or_revisions}}

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

## Exploration handoff (when used)

Retain only scenarios that distinguished credible directions; link existing evidence instead of duplicating it.

| Scenario and observation | Responsibility, state or failure discovered | Consequence for the chosen direction |
|---|---|---|
| {{scenario_and_evidence}} | {{responsibility_state_or_failure}} | {{decision_consequence}} |

| Direction-changing unknown | Evidence status | Owner and resolution or revisit condition |
|---|---|---|
| {{unknown}} | {{inferred_contested_or_unknown}} | {{owner_and_condition}} |

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

## Software quality goals and trade-offs

Include only goals that constrain this design.

| Quality scenario or current goal | Design response | Cost or trade-off | Planned evidence |
|---|---|---|---|
| {{stimulus_environment_and_response}} | {{design_mechanism}} | {{transferred_cost_or_risk}} | {{evidence}} |

- Touched-owner understandability and changeability: {{touched_owner_quality}}
- Operability and resource behavior before Release: {{operability_and_resources}}

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

## Technical debt decisions

Include a row only for a known future obligation being incurred or carried.

| Debt-bearing boundary | Borrowed value | Trigger, exposure and interest | Strategy and propagation limit | Owner, revisit and cleanup |
|---|---|---|---|---|
| {{boundary}} | {{borrowed_value}} | {{trigger_exposure_and_interest}} | {{strategy_and_limit}} | {{owner_revisit_and_cleanup}} |

## Alternatives and decisions

| Option | Trade-off | Decision |
|---|---|---|
| {{option}} | {{tradeoff}} | {{decision}} |
