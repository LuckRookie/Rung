# Artifact 与持久化规则

在创建 `.rung/` 工作区、恢复任务或选择模板时读取本文件。

## 事实源原则

ProjectContext 先索引项目已有的 Requirements、README、架构文档、ADR、接口规范、构建配置和测试配置。本次 DevelopmentRun 产生的新事实写回相应事实源。

`.rung/` 保存运行控制状态、证据引用以及项目中尚无对应事实源的开发制品。

## 建议结构

```text
.rung/
└── runs/
    └── <run-id>/
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

## 模板映射

| Artifact | 模板 |
|---|---|
| Development Brief | `assets/development-brief.template.md` |
| Project Context | `assets/project-context.template.md` |
| Solution Design | `assets/solution-design.template.md` |
| Change Plan | `assets/change-plan.template.md` |
| Verification Plan | `assets/verification-plan.template.json` |
| Verification Report | `assets/verification-report.template.md` |
| Review Result | `assets/review-result.template.md` |
| Release Manifest | `assets/release-manifest.template.yaml` |

复制模板后替换所有 `{{placeholder}}`。项目已有等价制品时，在运行状态中记录其路径和 revision。

## 持久化深度

- Lite：单会话低风险任务可以使用结构化会话 Artifact；需要恢复时持久化 brief、context、verification、review 和 release。
- Standard：持久化全部关键 Artifact；无设计变化时 design 记录沿用的现有设计与理由。
- Strict：持久化全部 Artifact，并增加兼容、迁移、回退、安全或 ADR 记录。

## 敏感信息

Artifact 只记录凭据名称、权限要求或安全引用。密钥、令牌、生产凭据和受限数据保留在专用系统中。
