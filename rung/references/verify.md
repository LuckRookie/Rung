# Stage 6：Verify

在判断实现质量、验收状态或发布准备度时读取本文件。

## 目标

使用与风险匹配的实际执行结果，证明验收条件和关键工程结论。

## 执行

1. 将每项验收条件和风险映射到 Verification Plan 中的检查。
2. 先运行目标文件、语法、格式、静态检查和相关单元测试等高信号检查。
3. 根据 Profile 和风险扩大到模块、集成、契约、端到端、构建、打包、安全或依赖检查。
4. 失败结果保持可见，修复根因后重新执行受影响检查。
5. 环境、工具或权限限制使用 `blocked` 或 `not_covered`。
6. 为命令、退出码、revision、覆盖范围和制品位置生成 Evidence。

可使用：

```bash
python scripts/run_verification.py \
  --project <project-path> \
  --plan <verification-plan.json> \
  --output <evidence.json>
```

## Artifact

使用 `assets/verification-report.template.md`，并引用脚本产生的 Evidence JSON 或项目工具报告。

## Verify Gate

- 当前 Profile 和 Tier 要求的检查已执行；
- 每项必须验收条件具有对应 Evidence；
- 失败项已经修复、明确阻塞或经用户 `waived`；
- 未执行检查、覆盖缺口和残余风险已经披露；
- 构建与打包结论来自实际执行结果。

实现问题返回 Implement；验证充分后进入 Review。
