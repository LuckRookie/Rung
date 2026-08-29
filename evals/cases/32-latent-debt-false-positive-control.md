# Case 32: Latent debt false-positive control

## Purpose

Test whether age, size, TODOs, and complexity remain investigation signals when a current construct has no credible future burden, and whether new evidence can later qualify debt.

## Fixture

Use an old protocol parser isolated behind one stable boundary. It is large, branch-heavy, sparsely commented, and contains historical TODOs. A static report gives it the repository's worst complexity score. Golden contract tests cover every released message, incidents show no parser-related failure for three years, no other module knows its internal representation, and the accepted product plan retires the protocol in six weeks. Removal work is already owned and bounded. The parser has no current defect in the fixture.

## Initial prompt

```text
请判断这个旧协议解析器是否构成现在应该处理的技术债，并形成明确的改造、携带或退役决定。根据仓库事实说明依据，先不要修改代码。
```

## Hidden follow-up

Reveal only after the initial decision reaches handoff:

```text
产品计划刚刚确认继续支持该协议十二个月，并将在这期间加入六种有差异的消息方言。请根据这个已接受变化重新判断，并给出下一步开发决定。
```

## Acceptable routing range

- The request directs a concrete development decision and may load Inspect and Technical Debt.
- Software Quality may describe current maintainability evidence, while Architecture Assessment requires a decision-ready system or structural assessment signal.
- Initial static signals justify bounded inspection, not automatic repayment, a debt score, or code edits.
- The hidden accepted roadmap change is new evidence and should trigger recalibration rather than preservation of the first label.

## Initial decision gate

- The working tree remains unchanged.
- The Agent distinguishes visible internal quality concerns from effective debt exposure.
- Isolation, complete released-contract evidence, stable history, near-term retirement, and bounded removal count as counterevidence.
- The result may retain a Debt Signal or latent Hypothesis, but it does not schedule a broad rewrite solely from age, TODOs, size, style, or complexity.
- Carrying to owned retirement, with the current contract protected, is an acceptable management decision.

## Requalification gate

- The twelve-month commitment and six planned dialects become credible change exposure.
- The Agent inspects how dialect additions would interact with the current state and branch model before qualifying debt.
- A Qualified Debt Item identifies a concrete mechanism, expected change-driven or spread-driven interest, principal options, current contract protection, and an owner or revisit condition.
- Proposed intervention stays proportional; a full parser rewrite requires evidence that a smaller seam, state model, containment, or staged replacement cannot manage the burden.

## Observations

Record initial and follow-up debt states, counterevidence, static signals, current quality findings, trigger change, exposure, interest mechanism, strategy change, false findings, user questions, files inspected, code edits, persistence, and context cost.
