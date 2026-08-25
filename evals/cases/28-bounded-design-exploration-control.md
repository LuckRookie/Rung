# Case 28: Bounded change avoids design exploration

## Purpose

Confirm that adding Design Exploration does not impose divergence, alternative generation, or a design artifact on a clear local codebase change.

## Fixture

Use a small CLI whose existing `render` command owns terminal color selection through one documented configuration object. The parser, owner, tests, help generation, and verification command are clear. The requested `--no-color` flag maps directly to an existing `color_enabled` field. Include one unrelated user change that must remain untouched.

## Initial prompt

```text
给现有 render 命令增加 --no-color。它只需要把已有 color_enabled 设置为 false；
默认行为、配置文件语义和其他命令保持不变。更新帮助与测试，运行项目现有检查并准备交付说明。
```

No follow-up is required.

## Acceptable invocation and routing

- Candidate Rung is eligible because the accepted result is a durable, verified codebase change.
- Inspect, Implement, Verify, or Review may load only when their concern is current.
- Design Exploration should not load: behavior, owner, state mapping, compatibility boundary, and verification path are already sufficient for the next decision.

## Correctness gate

- `render --no-color` disables color through the existing configuration owner.
- Default behavior, configuration-file semantics, and other commands remain unchanged.
- Help and relevant tests are updated, the configured checks pass, and the unrelated user change is preserved.

## Economy gate

- The Agent does not generate multiple architecture directions, broad product scenarios, a Discovery document, or `.rung/` state.
- Inspection and verification stay proportional to the known owner and affected public surface.
- The handoff reports the integrated result, actual evidence, and any uncovered scope concisely.

## Observations

Record invocation, loaded References, Design Exploration selection, questions, alternatives, files and lines changed, checks, artifacts, elapsed time, and context cost.
