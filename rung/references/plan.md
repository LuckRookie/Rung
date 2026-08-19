# Stage 4：Plan

在开始实施前读取本文件。

## 目标

把 Solution Design 转换为可独立执行、检查和恢复的 Change Plan 与 Verification Plan。

## Change Plan

每个变更单元记录：

- 目标与对应验收条件；
- 受影响模块和文件；
- 需要保持的接口、行为或用户修改；
- 实施顺序与依赖；
- 数据、配置和文档变化；
- 完成判据；
- 失败、阻塞或回退处理。

功能变化、重构和清理分别列出。计划外工作在执行前完成范围确认。

## Verification Plan

每项检查记录：

- 支持的验收条件或风险结论；
- 命令数组和工作目录；
- 预期结果；
- Tier；
- 超时；
- 受环境或权限影响的前置条件。

需要脚本执行时，从 `assets/verification-plan.template.json` 创建计划。

## Artifact

使用 `assets/change-plan.template.md` 和 `assets/verification-plan.template.json`。

## Plan Gate

- 每项验收条件都有实施路径和验证路径；
- 顺序与项目依赖、迁移要求和回退策略一致；
- 高风险动作具有执行前检查和恢复条件；
- 计划粒度足以由另一个会话继续执行；
- 用户批准事项已经标注具体触发点。

计划暴露设计缺口时返回 Design；Gate 通过后进入 Implement。
