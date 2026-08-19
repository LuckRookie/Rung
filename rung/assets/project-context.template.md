# Project Context

| Field | Value |
|---|---|
| Run ID | `{{run_id}}` |
| Project state | `{{new_existing_or_governed}}` |
| Repository root | `{{repository_root}}` |
| Branch | `{{branch}}` |
| Baseline revision | `{{revision}}` |
| Working tree | `{{clean_or_dirty}}` |

## Project facts

- Purpose: {{project_purpose}}
- Languages and frameworks: {{languages_and_frameworks}}
- Package and build systems: {{package_and_build_systems}}
- Primary entry points: {{entry_points}}

## Instructions and fact sources

| Fact | Source | Relevance to this run |
|---|---|---|
| Agent instructions | `{{instruction_path}}` | {{instruction_relevance}} |
| Requirements | `{{requirements_path}}` | {{requirements_relevance}} |
| Architecture | `{{architecture_path}}` | {{architecture_relevance}} |
| API or schema | `{{interface_path}}` | {{interface_relevance}} |

## Relevant structure

| Path | Responsibility | Planned relationship |
|---|---|---|
| `{{path}}` | {{responsibility}} | {{relationship}} |

## Commands

| Purpose | Command | Source | Last observed result |
|---|---|---|---|
| Format or lint | `{{lint_command}}` | `{{lint_source}}` | {{result}} |
| Test | `{{test_command}}` | `{{test_source}}` | {{result}} |
| Build | `{{build_command}}` | `{{build_source}}` | {{result}} |
| Package | `{{package_command}}` | `{{package_source}}` | {{result}} |

## User work in progress

| Path | State | Protection required |
|---|---|---|
| `{{user_modified_path}}` | {{state}} | {{protection}} |

## Initial impact and risk

- Affected modules: {{affected_modules}}
- Interfaces or data: {{interface_and_data_impact}}
- Dependencies: {{dependency_impact}}
- Known risks: {{known_risks}}
- Areas not inspected: {{uninspected_areas}}
- Selected Profile and Tier: {{profile_and_tier}}
