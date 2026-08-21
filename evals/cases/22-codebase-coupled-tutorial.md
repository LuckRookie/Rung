# Case 22: Codebase-coupled tutorial

## Purpose

Confirm that narrowing scope does not exclude a documentation-only change whose correctness and maintenance lifecycle are coupled to the codebase.

## Fixture

Use a small command-line codebase with a current public interface, executable examples, a configured documentation check, and a tutorial shipped with each release. The implementation and interface tests are correct. The tutorial still describes the previous invocation and output contract. Include an unrelated user change that must be preserved. Make Candidate Rung available through implicit discovery. Do not mention Rung in the prompt.

## Initial prompt

```text
按照项目当前实际接口更新随版本发布的使用教程和可执行示例。让教程中的命令、输出说明和错误处理与代码保持一致，运行项目已有的文档检查；不要修改接口行为，并保留我现有的其他改动。
```

No follow-up is required.

## Acceptable invocation and routing

- Candidate Rung is eligible for implicit selection because the accepted artifact is owned by the code project and must remain synchronized with its behavior and release.
- The Scope Gate establishes codebase membership without requiring a source-code edit.
- Inspect may load while the current interface, documentation owner, executable examples, or project check is unknown.
- Implement and Verify load only when their concerns become current. Development Scope is unnecessary once coupling is established.

## Correctness gate

- The tutorial and executable examples match the current public interface and observed output contract.
- The configured documentation check detects the stale form and passes after the update.
- Interface behavior and tests remain unchanged.
- The unrelated user change is preserved.
- The handoff identifies the codebase facts used, actual checks, and release-documentation state.

## Observations

Record implicit selection, Scope Gate outcome, loaded References and order, inspected codebase facts, files changed, checks, source behavior changes, user-work preservation, Rung Artifacts, context cost, and handoff. Compare false exclusion with unnecessary loading of the detailed Scope Guide.
