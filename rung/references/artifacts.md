# Artifact 与可选持久化

任务需要跨会话恢复、多人协作、正式审查或发布交接时读取本文件。

## 使用信号

以下情况常常适合持久化：

- 任务会跨会话继续；
- 多个执行者共享目标、决策或进度；
- 接口、数据、迁移或发布具有长期影响；
- 项目已有正式 Requirements、ADR、测试计划或发布流程；
- 用户希望审阅结构化制品。

普通单会话任务可以依靠对话、实际 diff 和验证结果完成治理。

## 项目事实源

先索引项目已有 README、Requirements、架构文档、ADR、接口规范、构建配置和测试配置。具有长期价值的新事实写回对应项目事实源。

`.rung/` 适合保存运行控制状态，以及项目暂时没有承载位置的开发制品。创建前结合项目约定决定是否跟踪这些文件。

## 可选结构

```text
.rung/runs/<run-id>/
├── brief.md
├── context.md
├── design.md
├── plan.md
├── verification-plan.json
├── verification.md
├── review.md
├── evidence.json
└── release.yaml
```

只创建当前任务有实际用途的文件。已有等价制品时记录或引用其路径与 revision。

## 模板

| 需要 | 模板 |
|---|---|
| 目标、范围和验收 | `assets/development-brief.template.md` |
| 仓库事实与影响 | `assets/project-context.template.md` |
| 边界、接口和数据设计 | `assets/solution-design.template.md` |
| 多步骤协调 | `assets/change-plan.template.md` |
| 可重复验证执行 | `assets/verification-plan.template.json` |
| 验证证据摘要 | `assets/verification-report.template.md` |
| 正式工程审查 | `assets/review-result.template.md` |
| 发布交接 | `assets/release-manifest.template.yaml` |

模板字段可以按需选用。复制完整模板时替换实际使用部分的占位符。

## 恢复所需的最小信息

跨会话恢复通常只需要：目标、关键决策、代码基线、用户已有修改、已完成工作、下一步、证据和未解决风险。

## 敏感信息

Artifact 记录凭据名称、权限要求或安全引用。密钥、令牌、生产凭据和受限数据保留在专用系统中。
