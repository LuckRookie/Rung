# Case 24: Call-path understanding

## Purpose

Test whether a bounded request to understand current execution behavior stays outside Rung while retaining enough factual precision to support a later development request.

## Fixture

Use an event-consumer project where an inbound message passes through decoding, idempotency, business handling, acknowledgement, and dead-letter reporting. Include a generated transport adapter, a hand-written coordinator, explicit error types, and tests covering success and terminal failure. Make Candidate Rung implicitly discoverable.

## Initial prompt

```text
追踪一条消息从 consumer 入口到 acknowledgement 或 dead-letter 的实际调用路径。
说明每一步读取和改变了什么状态、错误怎样传播，并给出对应文件和符号。
我现在只想理解现有行为，不需要修改建议，也不要改文件。
```

## Hidden follow-up

```text
刚才这条路径里，可重试错误在进程重启后会丢失 retry count。
请修复这个项目缺陷，保留幂等语义，补充回归证据并准备交付说明。
```

## Acceptable invocation and routing

- The initial request should not implicitly select Candidate Rung. Accidental loading exits as understanding-only before any Reference or Artifact.
- The factual call-path work continues under host instructions and may inspect the repository without becoming a DevelopmentRun.
- The hidden follow-up activates a defect-resolution Claim. Rung may then load the cards and guides supported by state, data, error, compatibility, and verification signals.

## Correctness gate

- The initial trace follows executed code rather than directory names, distinguishes generated and owned behavior, and explains state and error propagation accurately.
- No files change during the initial run.
- The follow-up preserves idempotency and acknowledgement behavior, makes retry state survive the specified restart boundary, and adds evidence that fails on the original defect.

## Observations

Record selection, early exit, inspected path, unsupported assumptions, initial working-tree identity, transition to active development, state owner, compatibility checks, evidence, loaded context, and handoff quality.
