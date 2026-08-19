# 渐进式治理工作流

任务同时出现多个治理信号、需要跨会话恢复或当前路径难以判断时读取本文件。

## 关注面

Clarify、Inspect、Design、Plan、Implement、Verify、Review 和 Release 是可组合的开发关注面。Agent 根据当前决策自由选择和组织这些提示。

| 关注面 | 主要价值 |
|---|---|
| Clarify | 减少目标、范围和验收方式的关键歧义 |
| Inspect | 用仓库事实、项目规则和用户修改校准判断 |
| Design | 处理边界、接口、数据、依赖和错误语义选择 |
| Plan | 协调多步骤、跨模块、迁移、协作和恢复 |
| Implement | 保持变更范围、事实源和已有工作一致 |
| Verify | 为行为、兼容、构建和制品结论取得证据 |
| Review | 从需求、工程和交付角度寻找遗漏 |
| Release | 整理 revision、制品、说明、风险和交接状态 |

## 选择循环

1. 观察当前最可能影响结果的未知、风险或交付信号。
2. 读取对应的一个 Concern Card。
3. 使用其中有助于当前判断的提醒，继续正常开发。
4. 新证据改变方向时，读取新的相关卡片或回访先前关注面。

普通任务可以合并多个关注面。已有可靠事实源时直接复用。内部路由无需向用户逐项报告。

## 常见组合

- 局部 Bugfix：Inspect → Implement → Verify → 简短 Handoff；
- 普通 Feature：Clarify + Inspect → Design/Plan 按需 → Implement → Verify；
- 跨模块重构：Inspect → Design → Plan → Implement + Verify → Review；
- 数据迁移：Clarify → Inspect → Design + Plan → Implement → Verify + Release；
- Release-only：Inspect 现有 revision 与证据 → Verify 缺口 → Release。

这些组合提供导航示例。任务事实决定实际顺序和深度。

## 轻量检查点

切换关注面前只需判断一个问题：当前信息是否足以继续下一项有价值的行动？

关键产品决策、权限或外部状态缺失时向用户说明阻塞。普通工程细节由 Agent 结合项目事实处理。风险或范围扩大时增加相关治理深度。

## 恢复

跨会话任务可以保存目标、关键决策、当前代码基线、已完成工作、下一步、证据和未解决风险。恢复时先比较持久信息与最新 Git 状态，再选择当前最相关的 Concern Card。
