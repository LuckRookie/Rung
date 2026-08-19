# Rung repository instructions

## Product facts

- `Rung.md` is the source of truth for product shape, system boundary, workflow, profiles, concepts, and release contract.
- `INSTALL.md` is the source of truth for package coordinates, installation scope, conflict handling, and installation verification.
- `rung/SKILL.md` is the user-facing Skill entrypoint. Keep it concise and route conditional detail to references.
- `rung/references/` contains instructions loaded for a specific Stage or decision.
- `rung/profiles/` defines the minimum responsibilities for Lite, Standard, and Strict.
- `rung/assets/` contains templates copied into DevelopmentRun output.
- `rung/scripts/` contains deterministic, dependency-free helpers.

## Documentation style

- Define products through capabilities, behavior, inputs, outputs, and responsibility handoffs.
- Use direct statements. Category-exclusion inventories and comparison slogans do not belong in product descriptions.
- Keep each fact in one maintained location and link to it from other documents.
- Preserve the Intent-to-Release boundary established in `Rung.md`.

## Implementation conventions

- Python scripts target Python 3.11+ and use the standard library.
- Script stdout is machine-readable JSON; diagnostics belong in structured fields.
- Verification commands use argument arrays and `shell=False`.
- External writes remain subject to user authorization and host permissions.
- User changes and dirty worktrees enter the protection scope before edits.

## Verification

Run after changing scripts, templates, or Skill routing:

```bash
python -B -m unittest discover -s tests -v
ruff check --no-cache .
```

Run the host `skill-creator` quick validator after changing `SKILL.md` or `agents/openai.yaml`.
