---
name: rung
description: 为 Coding Agent 提供从用户意图到可验证 Release 的渐进式软件开发治理。在创建项目、实现功能、修复缺陷、重构、迁移或准备发布时，按任务信号加载相关提醒、模板和检查工具。
---

# Rung

Rung 在 Coding Agent 的正常开发方式上增加渐进式治理。默认保持轻量，只在当前判断能够受益时加载额外内容。

## 默认提示

在工作中简要关注：

- **Outcome**：用户最终需要观察到什么结果？
- **Context**：哪些仓库事实、约束和已有修改影响这次工作？
- **Approach**：当前最小且连贯的实现方向是什么？
- **Evidence**：哪些实际结果足以支持完成声明？
- **Handoff**：代码、文档、版本和风险是否达到本次交付要求？

这些提示可以在内部合并处理。只向用户呈现有助于协作、决策或验证的信息。

## 按信号加载

出现下列信号时，读取当前最相关的一个 Reference；没有相关信号时继续普通开发。新的风险或证据出现时再加载下一项。

| 当前信号 | 读取 |
|---|---|
| 目标、范围、公共行为或验收方式存在关键歧义 | [references/clarify.md](references/clarify.md) |
| 相关代码、规则、命令、接口或用户修改尚未定位 | [references/inspect.md](references/inspect.md) |
| 边界、接口、数据、依赖或错误语义需要选择 | [references/design.md](references/design.md) |
| 多步骤、跨模块、迁移、协作或恢复需要协调 | [references/plan.md](references/plan.md) |
| 修改涉及范围控制、用户工作重叠或事实同步 | [references/implement.md](references/implement.md) |
| 需要证明行为、兼容、构建或制品结论 | [references/verify.md](references/verify.md) |
| diff 较大、风险较高或准备交付 | [references/review.md](references/review.md) |
| 准备版本、制品、说明或外部发布 | [references/release.md](references/release.md) |

任务跨越多个关注面、需要恢复或当前路径难以判断时，读取 [references/workflow.md](references/workflow.md)。工作类型或风险会显著改变治理深度时，读取 [references/risk-signals.md](references/risk-signals.md)。需要跨会话恢复、多人协作、正式审查或发布交接时，读取 [references/artifacts.md](references/artifacts.md)。

## 执行取向

- 项目指令、实际代码、配置和用户已有修改优先进入判断。
- Concern Cards 可以合并、跳过和回访；Stage 名称只用于导航。
- 默认不创建 `.rung/`；模板和脚本只在能够改善结果时使用。
- 提交、推送、发布及其他外部写操作沿用用户授权和宿主权限。
- 治理过程保持在后台，除非显式状态有助于协作或恢复。

## 完成提醒

最终结果与任务规模相称，通常说明：完成的用户可观察结果、实际执行的检查、仍未覆盖的范围，以及当前 Release 或待交接状态。完成、兼容和可发布结论关联实际证据。
