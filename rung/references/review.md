# Stage 7：Review

在 Release 前进行独立工程审查时读取本文件。

## 目标

从需求、实际 diff 和发布契约三个视角确认 DevelopmentRun 的完整性。

## 审查范围

1. 重读 Development Brief 和验收条件。
2. 检查实际 diff、修改范围和计划差异。
3. 检查模块职责、依赖方向、接口与数据兼容性。
4. 检查错误处理、安全、隐私、性能和资源风险。
5. 检查测试设计、失败路径和 Verification Report 的覆盖范围。
6. 检查 README、接口文档、配置说明和架构事实源的一致性。
7. 检查版本、Changelog、Release Notes、构建与制品准备情况。
8. 将技术债与后续工作写入项目 Issue 系统或下一次 DevelopmentRun 输入。

审查发现项使用严重度：

- `critical`：发布前必须修复；
- `major`：影响需求、兼容、安全或主要维护性；
- `minor`：局部质量或清晰度问题；
- `note`：已知限制或后续机会。

## Artifact

使用 `assets/review-result.template.md`，每个发现项包含位置、影响、证据和处理状态。

## Review Gate

- 实际修改与计划差异均有说明；
- critical 和 major 风险已经处理或获得明确 `waived`；
- 项目事实源与实现同步；
- Release 所需版本、制品和风险信息已经准备；
- Agent 可以从验收条件追踪到实现与 Evidence。

发现问题时返回 Design、Plan 或 Implement；Gate 通过后进入 Release。
