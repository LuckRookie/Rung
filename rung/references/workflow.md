# DevelopmentRun 工作流

在开始 DevelopmentRun、恢复中断任务或需要判断阶段回退时读取本文件。

## 状态模型

一次 DevelopmentRun 记录：

- `run_id`：稳定标识；
- `work_type`：Greenfield、Feature、Bugfix、Refactor、Migration、Dependency、Docs/Config 或 Release-only；
- `profile`：Lite、Standard 或 Strict；
- `stage`：当前开发阶段；
- `acceptance`：验收条件及状态；
- `artifacts`：事实源或持久化制品位置；
- `open_questions`：待决策事项；
- `evidence`：命令、结果、revision 和覆盖范围；
- `release_status`：implementation complete、verification complete、release ready、published 或 blocked。

## 八阶段

| Stage | 进入条件 | 核心结果 | Gate 关注点 |
|---|---|---|---|
| Clarify | 收到开发意图 | 可开发、可验收的目标 | 目标、范围、验收、开放问题 |
| Inspect | Clarify 足以指导项目检查 | 基于仓库事实的 ProjectContext | 路径、命令、约束、Git 状态、风险 |
| Design | ProjectContext 足以判断影响 | 满足需求的最小合理设计 | 边界、接口、数据、兼容性 |
| Plan | 设计方向稳定 | 可执行的变更与验证顺序 | 验收条件均有实现和验证路径 |
| Implement | Change Plan 可执行 | 代码、配置、测试和必要文档变更 | 计划范围完成、变化已路由 |
| Verify | 实现可运行 | 与风险匹配的 Evidence | 验收、回归、构建、未覆盖项 |
| Review | 主要验证已有结果 | 需求与工程审查结论 | 范围、架构、兼容、安全、文档 |
| Release | Review 达到发布条件 | Release Package 与 Manifest | 版本、revision、制品、证据、风险 |

## Gate 结果

- `pass`：条件满足并关联 Evidence；
- `fail`：条件未满足，返回对应阶段修复；
- `blocked`：等待用户决策、权限、工具或外部状态；
- `waived`：用户明确接受残余风险，记录范围和理由。

Stage 在 Gate 完成评估前保持当前状态。`waived` 只覆盖被明确接受的条件。

## 返回路径

```text
Verify fail  → Implement
Review issue → Design / Plan / Implement
New unknown  → Clarify / Inspect
Blocked      → 保存 Artifact 和下一步恢复条件
Resume       → 重读目标、当前 Stage、未解决问题和最新 Git 状态
```

恢复任务时，先验证持久化 Artifact 与当前仓库 revision 的关系。仓库已经变化时更新 ProjectContext，并重新评估 Profile、Plan 和 Evidence。
