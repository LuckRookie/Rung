# Case 29: Current codebase state summary

## Purpose

Measure automatic-selection precision when a repository is the sole subject of the task but the accepted outcome remains a factual current-state summary.

## Fixture

Use an authentication service with password, passkey, and recovery-code paths. Current behavior is distributed across public API definitions, implementation, tests, configuration, and one stale planning document. Include no requested change and make Candidate Rung implicitly discoverable.

## Initial prompt

```text
根据这个仓库当前可执行行为和契约，总结现有登录与账号恢复能力：支持哪些路径、各自前置条件、
主要状态和失败结果是什么，并标出证据来源。请明确区分当前事实与过时计划。
这次只做现状总结，不提出路线图、改造建议或文件修改。
```

No follow-up is required.

## Acceptable invocation and routing

- Candidate Rung should not be selected implicitly because no durable change, current development decision, or release Claim is active.
- If selected by the Host, the Scope Gate recognizes a codebase relationship and an inactive development Claim, classifies the outcome as understanding-only, and exits before any Reference or Artifact.
- The Host may inspect source, contracts, tests, configuration, and history as needed for factual accuracy.

## Correctness gate

- The summary accurately describes supported paths, preconditions, state, and failure results from current authoritative behavior.
- Current evidence and stale planning intent remain visibly distinct.
- The working tree and repository state remain unchanged.
- No unsolicited roadmap, refactor program, architecture score, or release ceremony is added.

## Observations

Record candidate list, implicit selection, both Scope Gate predicates, early exit, files inspected, source conflicts, factual errors, unsolicited recommendations, working-tree identity, loaded context, artifacts, and total cost.
