# Case 02: Cross-entry-point ownership

## Purpose

Test whether the Agent locates a business rule in a coherent owner and whether a later entry point can reuse that rule without duplicating policy or exposing adapter details.

## Fixture

Use an existing application with an Order model, an HTTP adapter, a separate batch entry point, and tests for current behavior. Cancellation does not yet exist. HTTP and batch modules may translate inputs and outputs; neither currently owns order lifecycle rules.

## Initial prompt

```text
Add order cancellation to the HTTP API. A pending order can become cancelled. A shipped order must remain unchanged and return a conflict result. Follow the repository's existing API and test conventions.
```

## Hidden follow-up

Reveal only after the initial task has reached handoff:

```text
Add batch cancellation for a list of orders. It must use the same cancellation rules and return one result per order. Preserve the HTTP behavior.
```

## Acceptable routing range

- Inspect is relevant for model ownership, adapters, callers, tests, and commands.
- Design is relevant because rule ownership and the caller-visible boundary affect both implementation and future reuse.
- A short in-conversation decision is sufficient when the repository is small; an Artifact is optional only when coordination or recovery supports it.
- Review is relevant when the diff introduces new public surface or policy in an adapter.

## Correctness gate

- Pending and shipped behavior matches both prompts.
- HTTP and batch results follow their local conventions.
- Existing behavior and tests remain valid.
- Both entry points share one authoritative cancellation policy.

## Observations

Compare where the initial policy lives, which files the follow-up changes, whether adapters learn domain internals, public symbols added, dependency edges, duplicate conditions, tests coupled to internals, and any abstraction with no current use. Several domain-module or service-module solutions may be acceptable when ownership and dependencies remain clear.
