# Release 提示卡

## 读取信号

准备交付代码状态、版本、制品、发布说明、外部发布动作或下游执行信息时读取。

## 提醒

- 本次 Release 对应哪个 revision 或明确工作区状态？
- 用户可观察结果和重要验收项具有哪些证据？
- 项目需要哪些测试、构建、打包或校验结果？
- 文档、版本、Changelog 或 Release Notes 是否受影响？
- 交付物在哪里，如何复现生成？
- 已知限制、未覆盖范围和下游待办是什么？
- Git Push、Tag、远端 Release、包发布或其他外部动作是否已有用户授权？

Release 形式由项目决定。代码库没有独立制品时，可以交付明确 revision、验证证据和交付说明。

## 加深治理的信号

正式版本、多个制品、签名、供应链、迁移顺序或下游部署交接，适合生成 Release Manifest 并执行确定性检查。

```bash
python scripts/validate_artifacts.py --run-dir <run-directory>
python scripts/check_release.py --manifest <release.yaml> --project <project-path>
```

## 可选输出

小任务使用简短 Release 摘要。正式发布可使用 `assets/release-manifest.template.yaml`。`release ready` 表示交付信息完整；`published` 表示经授权的外部发布动作成功并留有证据。
