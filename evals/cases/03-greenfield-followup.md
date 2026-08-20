# Case 03: Greenfield structure under a hidden change

## Purpose

Test whether a new project starts with a runnable slice and evidence-backed boundaries, while remaining easy to extend after a plausible requirement change.

## Fixture

Start from an empty Git repository. Provide the same available Python version, filesystem permissions, and network policy to every variant. No framework or directory pattern is prescribed.

## Initial prompt

```text
Build a Python 3.11 command-line tool named dispatch-note. It accepts a recipient and message, appends one JSON record to a local outbox file, reports success, and includes automated tests and a short usage guide. Use only the standard library and prepare a verified first release.
```

## Hidden follow-up

Reveal only after the initial release handoff:

```text
Add a dry-run delivery mode that validates and renders the same note but does not write to the outbox. Keep the existing command behavior and file format compatible.
```

## Acceptable routing range

- Clarify is useful only for an ambiguity that changes observable behavior.
- Design is relevant for the minimum runnable slice, data contract, command boundary, and outbox ownership.
- Plan and persistent Artifacts remain optional unless the implementation or host creates a real coordination need.
- Verify and Release are relevant to the requested first release.

## Correctness gate

- The initial command writes the specified JSON record and reports success.
- Tests exercise public behavior and relevant failures.
- The usage guide matches the actual command.
- Dry-run preserves validation and rendering, produces no outbox write, and keeps original behavior compatible.

## Observations

Compare the initial amount of scaffolding, placeholder abstractions, public surface, location of validation and rendering, follow-up files changed, duplicate logic, test churn, and release evidence. A compact module and a small package can both pass; the review should explain change locality and knowledge containment rather than reward a preferred directory tree.
