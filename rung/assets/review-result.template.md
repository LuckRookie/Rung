# Review Result

| Field | Value |
|---|---|
| Run ID | `{{run_id}}` |
| Revision | `{{revision}}` |
| Reviewer | `{{reviewer}}` |
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
- Dependency direction: {{dependency_review}}
- Interface and data compatibility: {{compatibility_review}}

## Quality review

- Error handling and security: {{error_and_security_review}}
- Test design and coverage: {{test_review}}
- Documentation consistency: {{documentation_review}}
- Release preparation: {{release_review}}

## Debt and follow-up

| Item | Destination | Priority | Owner |
|---|---|---|---|
| {{follow_up}} | {{issue_or_next_run}} | {{priority}} | {{owner}} |
