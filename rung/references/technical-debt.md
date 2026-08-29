# Technical Debt

Read when an active development decision must qualify, incur, carry, prioritize, reduce, repay, or retire a project-owned future engineering obligation. A code smell, TODO, age, tool score, repository size, or vague cleanup wish does not activate this guide without a current debt-bearing construct and a credible future cost mechanism.

Use [Software Quality](software-quality.md) for the software's current fitness. Technical debt adds the time dimension: how a present design, implementation, or coupled artifact changes the cost, risk, coordination, or feasibility of credible future evolution.

## Governing outcome

Keep the project's evolution capacity visible and controllable. A technical debt item is a present design, implementation, or coupled-artifact condition created by a past trade-off, partial understanding, accumulated drift, or context change that can make a credible future change avoidably costlier, riskier, more coordinated, or impossible.

Well-written, correct, tested code can carry debt when it embodies a superseded model, expiring dependency, temporary compatibility path, deferred migration, or future obligation. Poor internal quality becomes effective debt only when credible continued work activates avoidable future burden.

Debt can be a rational investment. The decision quality depends on borrowed value, boundary, exposure, interest, principal, propagation, owner, and revisit or exit condition—not blame for how it arose.

## Qualify before labeling

Use three confidence states:

- **Debt signal:** a smell, TODO, obsolete technology, drift, workaround, repeated pain, or temporary path worth investigating.
- **Debt hypothesis:** a plausible future burden with one or more causal links still unverified.
- **Qualified debt item:** repository evidence supports a present construct, credible trigger or exposure, avoidable consequence, and a management decision.

Build the minimum chain:

```text
current debt-bearing construct
  -> credible change, maintenance event, or time trigger
  -> interest, propagation, risk, coordination, or option loss
  -> carry, contain, reduce, repay, replace, or retire decision
```

If the trigger is speculative, keep the item latent or as a hypothesis. If no future burden exists until a direct implementation can simply be replaced, the current choice may be a sound option. Do not infer debt from a preferred pattern or ideal target state.

## Keep related concerns distinct

- A current behavior violation remains a **defect**. Track it with its present acceptance and regression evidence; deferral or a debt-bearing root can be recorded separately.
- A current exploitable weakness remains a **vulnerability** with its security priority. Debt may explain why remediation is costly but does not lower urgency.
- A **risk** is an uncertain event and impact. Debt is the present engineering condition that can create or amplify risk.
- A missing user capability is a **feature gap**. It becomes relevant to debt when implementing it activates a present burden.
- Necessary domain, performance, security, transaction, compatibility, generated, or organizational complexity is a project cost. Qualify debt only for avoidable burden relative to credible alternatives and constraints.
- Team, funding, skill, or process conditions can cause debt. Rung governs the resulting codebase or coupled-artifact condition; external owners retain their decisions.

Use the primary concern's severity and workflow when categories overlap. A debt label must not turn a current correctness, security, privacy, or data problem into discretionary cleanup.

## Understand the debt economics

Record only terms that change the decision:

- **Borrowed value:** delivery, learning, compatibility, risk reduction, or option preserved when the condition arose or is retained.
- **Principal:** the present work to reach a coherent target, including characterization, refactoring, migration, compatibility, activation, and cleanup.
- **Interest:** extra engineering effort, product risk, delay, or coordination paid while carrying the condition.
- **Exposure:** how likely and soon credible work or time will activate the interest.
- **Propagation:** new consumers, copies, data, exceptions, or contracts that increase future principal or interest.
- **Option loss:** a platform, product, security, data, or delivery path that becomes harder or impossible with delay.

Interest can be:

1. **change-driven:** every related feature, fix, or review touches extra owners or knowledge;
2. **time-driven:** end-of-life, security, data growth, compatibility, policy, or platform deadlines approach;
3. **spread-driven:** new work copies or depends on the debt-bearing path.

Avoid false precision. Estimate ranges or qualitative pressure when the evidence cannot support money, duration, or probability. Principal can grow, and repayment can introduce its own risk.

## Locate the debt-bearing surface

Use the surface to route investigation and repayment, not as an exhaustive taxonomy:

- **Code:** mixed responsibilities, repeated policy, hidden state, obsolete paths, or local knowledge that makes active work harder.
- **Architecture:** misplaced ownership, leaked dependency knowledge, shared state, unstable public contracts, or a structure that blocks quality scenarios.
- **Data and compatibility:** legacy schemas, dual writes, old formats, adapters, migration gaps, and permanent temporary contracts.
- **Dependency and platform:** end-of-life versions, vendor lock, blocked upgrades, unsupported environments, or delayed technology refresh.
- **Verification and Harness:** brittle tests, missing evidence layers, duplicated authority, slow or unreliable gates, temporary ignores, or checks tied to a superseded design.
- **Build and Release:** manual or irreproducible paths, obsolete generation, long-lived release exceptions, or delivery controls that block supported evolution.
- **Documentation and facts:** authoritative project claims that drift, conflict, or encode a superseded model and cause repeated incorrect decisions.

Read [Engineering Structure](engineering-structure.md) or [Architecture Assessment](architecture-assessment.md) for structural mechanisms, [Project Harness](project-harness.md) and [Harness Evolution](harness-evolution.md) for protection systems, and [Project Model](project-model.md) when new learning or product evolution may have made a formerly sound implementation obsolete.

## Inspect effective debt and debt systems

Retrieve evidence for the current hypothesis. Useful sources include accepted roadmap or Project Model changes, callers and consumers, issue and incident history, recent changes and co-change, dependency and support dates, compatibility commitments, test and build behavior, temporary controls, data growth, and measured rework or delay.

Static scans and counts expose potential debt. Effective debt depends on credible evolution. File count, TODO count, complexity, coverage, dependency age, cycle count, and backlog size have no universal debt threshold.

For an explicit system debt review, declare the inspected boundary and look for interaction:

- temporary paths become dependencies for new work;
- one debt forces another in data, tests, build, or release;
- exceptions and duplicate facts spread across owners;
- repeated local fixes preserve a deeper causal constraint;
- interest consumes delivery capacity or makes work unsafe;
- ownerless items and expired assumptions prevent cleanup.

Prioritize the few mechanisms driving the greatest current or approaching debt pressure. An inventory of isolated smells does not explain project chaos.

## Decide what to do

Compare each strategy with carrying the current condition:

- **Repay:** remove the causal construct and obsolete path when expected interest, option loss, or risk justifies the principal.
- **Reduce interest:** improve a seam, owner, test boundary, or internal representation while a full migration remains uneconomic.
- **Contain or mitigate:** stop propagation, isolate consumers, add diagnostics or evidence, or cap exposure.
- **Carry deliberately:** retain low-exposure debt with an owner and revisit condition when principal exceeds expected burden.
- **Replace or retire:** move consumers or end the component when incremental repayment has lower value than a bounded replacement or planned exit.

Use judgment rather than a universal score. Consider current or near-term relevance, observed interest, exposure, propagation, irreversibility, evidence strength, principal, repayment risk, intervention leverage, borrowed value, and opportunity cost. High-churn areas and roots shared by several debt items often deserve attention before visually worse but dormant code.

## Incur debt deliberately

When an accepted direction creates a known future obligation, keep a lightweight debt contract proportional to its consequences:

- decision and borrowed value;
- debt-bearing boundary and consumers;
- behavior and quality that must remain protected;
- expected trigger, interest, and propagation limit;
- owner and authority;
- repayment, mitigation, or retirement option;
- revisit, expiry, activation, rollback, and cleanup conditions where relevant.

Do not demand a persistent artifact for a local short-lived choice whose cleanup occurs in the same change. Record a durable item when another session, owner, release, or future trigger must act.

Intent and prudence describe history; they do not set current priority. Emergent debt discovered through learning deserves the same evidence and management decision as deliberate debt.

## Repay safely

Tie repayment to a qualified mechanism and observable future benefit. In an established project:

1. identify behavior, data, compatibility, user work, and project facts to preserve;
2. establish proportionate characterization or independent evidence when the current Harness is weak;
3. separate structural movement from behavior change where that improves diagnosis or rollback;
4. use small checkable slices, adapters, parallel paths, or migration windows only when they add evidence or safety;
5. prevent new consumers from deepening the old path;
6. remove old code, flags, data paths, tests, configuration, documentation, and exceptions under a visible condition;
7. verify the integrated revision and remaining debt.

Read [Plan](plan.md) for dependent repayment units, migration, or recovery. Read [Verify](verify.md) and [Verification Harness](verification-harness.md) for evidence. A check modified with the debt-bearing system cannot be its sole proof.

Verify repayment against the activating scenario:

- Does the next similar change touch fewer unrelated owners and require less unstable knowledge?
- Did the time, compatibility, platform, or security blocker disappear or move under a controlled boundary?
- Did propagation stop and can the old path be removed?
- Are current behavior, data, performance, security, and recovery evidence preserved?
- Did the intervention merely move interest into callers, tests, operations, or another owner?

## Persist for a real consumer

Prefer the project's issue tracker, roadmap, architecture owner, dependency system, migration plan, or Harness record. Avoid a parallel debt register that no owner reviews. Use `assets/technical-debt-item.template.md` only when a qualified item needs durable coordination and the project has no better shape; `.rung/` remains optional.

A durable item records the current construct and location, evidence and confidence, borrowed value or origin when known, trigger and exposure, interest and propagation, principal and options, affected claims, owner, chosen strategy, priority reasoning, revisit condition, links to separate defects or vulnerabilities, and retirement evidence.

Useful states are candidate, qualified, carried, scheduled, in repayment, mitigated, and retired. Adapt them to the project's existing workflow instead of creating a second state machine.

At Review and Release, report only debt that affects delivery, residual risk, a committed follow-up, or an owner handoff. Stop when the active debt decision is qualified enough to act or carry, its evidence and uncertainty are visible, and the next owner or revisit condition is explicit.
