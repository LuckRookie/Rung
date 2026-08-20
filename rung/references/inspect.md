# Inspect Card

Read when relevant project facts, rules, code, contracts, commands, dependencies, or user work have not entered the current judgment.

## Operate

- Establish the project root, applicable instructions, revision, working-tree state, user-owned edits, and relevant tool entry points.
- Inspect the direct owner, callers, dependencies, tests, configuration, requirements, API, schema, and prior design facts needed for the next action.
- Expand to consumers, migrations, generated artifacts, build, CI, and release controls when public, data, shared, dependency, platform, or multi-module impact appears.
- Declare the boundary for a system-level audit.

Stop when the next action has a known owner and constraints, user work is protected, likely impact and checks are bounded, and uninspected areas are visible. Output facts with sources, protected changes, candidate commands, impact, and remaining unknowns.

Optional index: `python <rung-skill-root>/scripts/inspect_project.py --project <path> --output <context.json>`. Persist Project Context only for coordination or recovery. Read [Execution Model](execution-model.md) for inspection radius and [Project Harness](project-harness.md) when sources or controls conflict.
