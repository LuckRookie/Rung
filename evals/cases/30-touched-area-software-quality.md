# Case 30: Touched-area software quality

## Purpose

Test whether an ordinary feature leaves the touched ownership boundary correct, understandable, changeable, verifiable, operable, and consistent without expanding into repository-wide cleanup or a speculative architecture.

## Fixture

Use an established report-export CLI with CSV and JSON formats. One export owner selects the format, validates options, opens the destination, translates stable caller errors, and invokes format-specific serialization. Its current tests protect successful output and unknown-format errors, while a serialization-failure test exposes that the destination handle can remain open. The same touched file contains one parameter and branch made obsolete by the current accepted behavior. Project naming, error, test, and documentation conventions are clear.

Place a large, untidy but unrelated legacy XML formatter in a neighboring directory. Give it weak names, deep control flow, old comments, duplicated helpers, and no relationship to the export path. Preserve one unrelated user-owned working-tree edit.

## Initial prompt

```text
给 report export 增加 TSV 格式，保持现有公共调用方式和 CSV、JSON 行为。未知格式不能创建或截断目标文件；序列化失败时资源必须被正确关闭，并保留可诊断的错误原因。同步帮助、项目文档和相关测试，运行现有检查并准备交付说明。不要动我当前的修改。
```

## Hidden follow-up

Reveal only after the initial task reaches handoff:

```text
现在让 CSV 和 TSV 支持项目已经定义的 line-ending 选项；JSON 行为保持不变。实现并验证这项变化。
```

## Acceptable routing range

- Candidate Rung is eligible because both prompts require durable verified codebase changes.
- Implement, Verify, and Review are relevant. Design is relevant only for a real format-owner, error, or lifecycle choice.
- Software Quality is relevant because current resource behavior and touched-owner coherence affect delivery.
- Engineering Structure is relevant only if repository evidence shows a nonlocal ownership or public-surface decision.
- Technical Debt and a repository-wide quality audit should remain unloaded unless inspection discovers a qualified future obligation.

## Correctness gate

- TSV output uses tab-delimited semantics and preserves the existing public entry point.
- CSV and JSON behavior remain compatible.
- Unknown formats fail before destination creation or truncation.
- Success and serialization failure close owned resources exactly once and preserve useful error context.
- Help, durable documentation, and behavior-focused tests agree with the implementation.
- The hidden line-ending option changes only the delimited formats and passes integrated checks.
- The user-owned edit remains intact.

## Quality gate

- Format selection, validation, destination lifecycle, error translation, and serialization ownership can be recovered from a bounded context.
- Directly obsolete state in the touched owner is removed when its consumers and removal safety are established.
- Tests protect caller behavior, failure meaning, and resource cleanup without asserting incidental call sequences.
- A shared delimited-format mechanism is accepted when the initial TSV need and hidden follow-up support it; a general plugin framework without further evidence counts as speculative abstraction.
- The unrelated XML formatter receives no broad restyle, rename, split, or cleanup. A material observation may be reported separately with its owner and consequence.

## Observations

Record loaded References, touched and affected boundaries, active quality goals, quality evidence, files changed, obsolete paths removed, unrelated cleanup, public-surface changes, resource and error behavior, test coupling, hidden-follow-up propagation, artifacts, final checks, and context cost.
