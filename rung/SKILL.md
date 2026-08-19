---
name: rung
description: 编排一次从用户意图到可验证 Release Package 的完整软件开发流程。用于创建项目、实现功能、修复缺陷、重构、迁移、升级依赖或准备版本发布。
---

# Rung

Rung 管理一次从 Intent 到 Release 的 DevelopmentRun。目标是交付满足验收条件、具有实际验证证据、文档与版本同步、能够复现构建的 Release Package。

## 开始 DevelopmentRun

1. 读取用户意图、仓库级指令、相关事实源和当前 Git 状态。
2. 将工作归类为 Greenfield、Feature、Bugfix、Refactor、Migration、Dependency、Docs/Config 或 Release-only。
3. 依据 [references/risk-signals.md](references/risk-signals.md) 选择 Lite、Standard 或 Strict，并读取对应 Profile：
   - [profiles/lite.md](profiles/lite.md)
   - [profiles/standard.md](profiles/standard.md)
   - [profiles/strict.md](profiles/strict.md)
4. 读取 [references/workflow.md](references/workflow.md)，建立当前 Stage、Artifact、Gate 和 Evidence 状态。
5. Standard、Strict、跨会话任务以及需要恢复的任务使用 `.rung/runs/<run-id>/` 持久化状态。具体规则见 [references/artifacts.md](references/artifacts.md)。

项目检查可以使用：

```bash
python scripts/inspect_project.py --project <project-path>
```

脚本输出属于 ProjectContext 的候选证据。Agent 必须结合实际文件确认其含义。

## 阶段路由

每次只读取当前 Stage 所需的参考文件。Stage Gate 通过后进入下一阶段；新证据改变既有判断时返回相应阶段。

| Stage | 读取 | 核心 Artifact |
|---|---|---|
| Clarify | [references/clarify.md](references/clarify.md) | Development Brief |
| Inspect | [references/inspect.md](references/inspect.md) | Project Context |
| Design | [references/design.md](references/design.md) | Solution Design / ADR |
| Plan | [references/plan.md](references/plan.md) | Change Plan / Verification Plan |
| Implement | [references/implement.md](references/implement.md) | Implementation Change |
| Verify | [references/verify.md](references/verify.md) | Verification Report / Evidence |
| Review | [references/review.md](references/review.md) | Review Result |
| Release | [references/release.md](references/release.md) | Release Package / Release Manifest |

## 执行规则

- ProjectContext 中的结论来自实际仓库、项目工具或用户确认。
- Clarify 与 Inspect Gate 达到当前 Profile 要求后进入代码实现。
- Change Plan 控制修改范围；范围、接口或数据假设变化时更新 Design 与 Plan。
- 用户已有修改始终进入保护范围。先理解重叠内容，再实施叠加式修改。
- 每项 `pass`、`complete`、`compatible` 和 `release ready` 结论都关联实际 Evidence。
- 工具、权限或外部状态阻碍检查时记录 `blocked`；用户接受残余风险时记录 `waived` 和理由。
- 提交、推送、包发布、远端 Release 和其他外部写操作在执行前获取用户授权，并遵守宿主权限机制。
- DevelopmentRun 在 `release ready` 或经过授权后的 `published` 状态完成。Release Manifest 记录下游交付所需信息。

## 验证与完成报告

验证命令较多时，使用 JSON 计划驱动确定性执行：

```bash
python scripts/run_verification.py \
  --project <project-path> \
  --plan <verification-plan.json> \
  --output <verification-evidence.json>
```

持久化 Artifact 后运行：

```bash
python scripts/validate_artifacts.py --run-dir <run-directory> --profile <profile>
python scripts/check_release.py --manifest <release-manifest.yaml> --project <project-path>
```

最终回复至少说明：

- 已实现的行为和对应验收条件；
- 修改范围；
- 实际执行的验证及结果；
- 未覆盖范围、残余风险和 `waived` 项；
- Release 状态、revision、制品及待授权外部动作。
