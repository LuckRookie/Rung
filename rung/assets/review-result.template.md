# Review Result

| Field | Value |
|---|---|
| Run ID | `{{run_id}}` |
| Revision | `{{revision}}` |
| Primary Agent | `{{primary_agent}}` |
| Reviewer | `{{reviewer}}` |
| Review mode | `{{primary_self_review_or_independent}}` |
| Overall result | `{{pass_fail_blocked_or_waived}}` |

## Traceability

| Acceptance | Implementation | Evidence | Review result |
|---|---|---|---|
| AC-1 | `{{implementation_location}}` | `{{evidence_location}}` | {{result}} |

## Findings

| ID | Severity | Location | Finding and impact | Resolution | State |
|---|---|---|---|---|---|
| RV-1 | {{critical_major_minor_or_note}} | `{{path_and_line}}` | {{finding}} | {{resolution}} | {{state}} |

## Scope and architecture

- Plan differences: {{plan_differences}}
- Project Model fit and semantic drift: {{project_model_fit_and_drift}}
- Concept ownership and change locality: {{ownership_and_locality_review}}
- Public surface and information leakage: {{public_surface_review}}
- Dependency direction: {{dependency_review}}
- Shared state, implicit behavior and abstraction evidence: {{state_and_abstraction_review}}
- Interface and data compatibility: {{compatibility_review}}

## Software quality review

- Active quality goals and evidence: {{quality_goals_and_evidence}}
- Current correctness and failure semantics: {{correctness_and_errors}}
- Touched-owner understandability and changeability: {{understandability_and_changeability}}
- Verifiability and test design: {{verifiability_and_tests}}
- Operability and resource behavior: {{operability_and_resources}}
- Project consistency and predictability: {{consistency_and_predictability}}
- Relevant UX, security, privacy, performance, and compatibility: {{conditional_qualities}}
- Documentation and Release preparation: {{facts_and_release_review}}

## Integration responsibility

- Worker outputs reviewed: {{worker_outputs_reviewed}}
- Integrated-state checks: {{integrated_state_checks}}
- Findings returned to Primary Agent: {{primary_agent_resolution}}

## Debt and follow-up

| Debt item and status | Construct, trigger and exposure | Interest or propagation | Strategy | Owner and revisit |
|---|---|---|---|---|
| {{debt_item}} | {{construct_trigger_and_exposure}} | {{interest_or_propagation}} | {{strategy}} | {{owner_and_revisit}} |

- Non-debt follow-up and destination: {{other_follow_up}}
