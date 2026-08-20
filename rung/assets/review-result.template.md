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

## Quality review

- Human-facing UX: {{ux_review}}
- Error handling and security: {{error_and_security_review}}
- Test design and coverage: {{test_review}}
- Documentation consistency: {{documentation_review}}
- Release preparation: {{release_review}}

## Integration responsibility

- Worker outputs reviewed: {{worker_outputs_reviewed}}
- Integrated-state checks: {{integrated_state_checks}}
- Findings returned to Primary Agent: {{primary_agent_resolution}}

## Debt and follow-up

| Item | Destination | Priority | Owner |
|---|---|---|---|
| {{follow_up}} | {{issue_or_next_run}} | {{priority}} | {{owner}} |
