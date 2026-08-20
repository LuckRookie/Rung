# Case 10: Architecture assessment controls false positives

## Purpose

Test whether the Agent can recognize an unusual but evidence-backed design, resist pattern-driven cleanup, and report a sound architecture judgment without inventing a mandatory finding.

## Fixture

Use a high-throughput protocol decoder whose versioned schema generates one large flat dispatch table. The generated file contains repeated branches and exceeds normal hand-written file sizes. A small stable facade is the only caller-facing surface. Repository documentation records the generator and compatibility contract; benchmarks show that the flat representation materially improves the required hot path; tests compare generated behavior with the schema.

Include an ordinary hand-written parsing function with mediocre naming outside the architectural boundary. Preserve exact schema, generator, benchmarks, tests, history, and project rules across variants.

## Initial prompt

```text
Review this project's code architecture and modularity. Pay particular attention to the large decoder and tell me what should be changed before the next protocol version. Do not edit the project yet.
```

## Hidden follow-up

Reveal only after the assessment has reached handoff:

```text
The versioned schema now adds one event type. Update the decoder through the project's intended path, preserve compatibility and performance evidence, and prepare a verified handoff.
```

## Acceptable routing range

- Inspect, Architecture Assessment, Engineering Structure, and Review are relevant.
- Design is relevant only if evidence supports a structural change.
- Verification and Project Harness become relevant for the hidden generated-code, compatibility, and performance claims.

## Correctness gate

- The initial run leaves the working tree unchanged.
- The assessment recognizes the schema as authority, the generated table as an implementation choice, the facade as the stable boundary, and the benchmark as relevant counterevidence.
- File size, branch count, generated duplication, or missing class hierarchy do not independently justify modularization.
- A local naming observation may be reported at local priority but is not promoted into the dominant architecture finding.
- It is acceptable to report no material architecture defect within the inspected boundary.
- The hidden follow-up changes the authoritative schema and intended generated or verification artifacts without hand-editing generated policy or introducing parallel dispatch ownership.

## False-positive gate

- Findings distinguish fact, risk, and hypothesis.
- Recommendations state what evidence would justify revisiting the current design.
- The Agent does not introduce a strategy hierarchy, runtime plugin system, extra layers, or per-event files solely to satisfy a preferred pattern.
- Any proposed change accounts for compatibility and measured hot-path behavior.

## Observations

Record finding count, unsupported-finding count, whether counterevidence was inspected before judgment, generated-file treatment, suggested abstractions, hidden follow-up locality, performance and compatibility evidence, context cost, and any pressure toward architectural ceremony when no material problem is shown.
