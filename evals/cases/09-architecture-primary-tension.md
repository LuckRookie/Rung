# Case 09: Architecture assessment finds the primary tension

## Purpose

Test whether an explicit architecture assessment identifies the structural mechanism that drives repeated change cost, grounds it in repository evidence, and keeps visible code smells in proportion.

## Fixture

Use an established subscription-billing application with HTTP checkout, scheduled invoicing, and batch quoting entry points. Each entry point independently implements the same regional pricing and discount policy. Recent issue and commit history shows that two pricing changes touched all three paths, and the product brief names a reseller channel as the next likely extension.

Include plausible distractions: one long private formatting function, imperfect local names, a small `helpers` module with cohesive formatting utilities, and a few harmless duplicated assertions. Preserve the same project instructions, tests, history, and clean working tree across variants.

## Initial prompt

```text
请审查这个项目当前的代码架构是否适合继续增加销售渠道和地区定价规则。找出最重要的结构问题，给出有证据、可渐进实施的修改建议；先不要修改代码。
```

## Hidden follow-up

Reveal only after the assessment has reached handoff:

```text
Implement the highest-priority recommendation and add reseller quotes using the same regional pricing and discount behavior. Preserve the existing HTTP, invoice, and batch behavior and run the relevant checks.
```

## Acceptable routing range

- Inspect is relevant for intent, change history, entry points, rule owners, tests, dependencies, and assessment boundary.
- Architecture Assessment and Engineering Structure are relevant to the explicit request.
- Review is relevant to findings and delivery judgment. Design becomes relevant when a concrete boundary change is proposed or implemented.
- Project Harness is relevant only if the assessment finds conflicting or unreliable project controls.
- The initial assessment does not authorize code edits.

## Correctness gate

- The initial run leaves the working tree unchanged.
- The assessment identifies duplicated pricing authority and cross-entry-point change propagation as the dominant structural tension.
- Evidence connects current product direction or observed history to concrete code paths; directory shape and names alone do not establish the finding.
- The long formatter and local naming issues do not outrank the pricing ownership problem.
- The recommendation preserves adapter-specific input and output behavior while giving pricing policy one coherent owner.
- The follow-up produces one authoritative pricing policy used by all four entry points and preserves existing behavior.

## Causal evidence gate

- Each material finding states the driver or change scenario, repository evidence, structural mechanism, resulting cost or risk, and confidence or uncertainty.
- The proposed intervention explains how a similar future pricing change becomes more local and how that claim will be checked.
- Alternatives and transition risk are proportional to the existing project; a wholesale rewrite or speculative plugin framework fails this gate.

## Observations

Record loaded References, declared assessment boundary, facts and history inspected, candidate findings, primary-cause rank, unsupported claims, counterevidence considered, files touched by the hidden follow-up, public-surface changes, duplicated policy remaining, tests changed, context cost, and whether the recommendation actually reduces change propagation.
