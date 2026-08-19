# Stage 8：Release

在生成 Release Package、Release Manifest 或执行经授权的发布动作时读取本文件。

## 目标

形成可复现、可追踪、可交付的软件版本。

## 执行

1. 确认必须验收条件及 `waived` 项状态。
2. 确认代码、配置、测试、文档和 Review Result 对应同一 revision。
3. 确认版本号，并更新 Changelog 或 Release Notes。
4. 执行当前 Profile 与 Tier 要求的构建和打包。
5. 记录制品路径、生成命令和可用校验信息。
6. 从 `assets/release-manifest.template.yaml` 生成 Release Manifest。
7. 运行 Artifact 与 Release Gate 检查。
8. 在获得用户授权和宿主权限后执行包发布、Git Tag、远端 Release 或推送。
9. 将外部动作结果写入 Manifest；待授权动作保持清晰的 pending 记录。

```bash
python scripts/validate_artifacts.py --run-dir <run-directory> --profile <profile>
python scripts/check_release.py --manifest <release.yaml> --project <project-path>
```

## Release Gate

- 必须验收条件为 `pass`，例外条件具有用户确认的 `waived`；
- 代码、配置、测试和必要文档完整；
- Verification Report 与 Review Result 达到当前 Profile 要求；
- 构建或打包可以复现；
- 版本与发布说明同步；
- Release Package 对应明确 revision；
- 已知限制和未验证风险已经披露；
- Release Manifest 通过确定性检查。

## 状态

- `implementation complete`：计划实现完成；
- `verification complete`：要求的验证已经执行并记录；
- `release ready`：Release Gate 通过；
- `published`：经授权的外部发布动作成功并留有证据；
- `blocked`：等待完成 Gate 所需的决策、权限、工具或外部状态。

DevelopmentRun 在 `release ready` 或 `published` 状态完成。
