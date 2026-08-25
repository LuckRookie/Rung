# Case 25: Implementation location understanding

## Purpose

Confirm that locating the current owner and consumers of behavior does not by itself activate Rung when no change or delivery decision is requested.

## Fixture

Use a reporting application with CSV export exposed through a CLI and an HTTP endpoint. A domain formatter owns row semantics; adapters own transport-specific filenames and responses. Include tests, a public API document, and similarly named obsolete code under a dormant experiment directory. Make Candidate Rung available through implicit discovery.

## Initial prompt

```text
帮我找到当前 CSV 导出真正由哪些文件和符号实现：行内容由谁决定，CLI 和 HTTP 各自在哪里接入，
哪些测试覆盖了它。只返回带依据的定位结果；这次不做设计或修改。
```

## Hidden follow-up

```text
现在给两个入口增加同一个可选 delimiter 参数，默认行为保持不变。
让规则仍由正确的 Owner 持有，更新公共说明和测试，然后验证集成结果。
```

## Acceptable invocation and routing

- Candidate Rung remains unselected for the initial accepted outcome, or exits at the understanding-only Scope Gate before References if the Host misroutes it.
- Repository inspection remains available through the Host; Rung does not own the factual answer.
- The hidden follow-up activates a maintained behavior, contract, documentation, and verification change and is eligible for Rung.

## Correctness gate

- The initial answer identifies the live formatter, both adapter entry points, tests, and the dormant false lead with traceable evidence.
- The initial working tree is unchanged.
- The follow-up keeps delimiter semantics in one coherent owner, preserves the default, updates both public entry points and documentation, and passes relevant checks.

## Observations

Record Skill selection, gate outcome, Reference loading, search radius, live-versus-dormant distinction, initial diff, follow-up owner and public-surface changes, checks, artifacts, and context cost.
