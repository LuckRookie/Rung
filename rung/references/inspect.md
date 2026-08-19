# Stage 2：Inspect

在修改任何项目文件前读取本文件。

## 目标

建立由仓库事实支持的 ProjectContext，并识别实施范围、工具链和风险。

## 执行

1. 读取根级与目录级 Agent 指令。
2. 检查 Git 分支、revision、工作区状态和用户已有修改。
3. 识别项目状态：New、Existing 或 Governed。
4. 定位入口、模块边界、公共接口、配置、依赖和相关代码路径。
5. 定位 Requirements、README、架构文档、ADR 和接口规范。
6. 从实际配置识别格式、静态检查、测试、构建、打包和发布命令。
7. 根据任务建立影响范围和保持不变区域。
8. 结合风险信号确认 Profile 与 Verification Tier。

可使用只读项目检查脚本建立候选索引：

```bash
python scripts/inspect_project.py --project <project-path> --output <context.json>
```

## Artifact

使用 `assets/project-context.template.md`，记录实际路径、命令来源、相关事实源、Git 状态、用户修改和初始风险。

## Inspect Gate

- 后续使用的路径、命令和约束均能指向项目事实；
- 相关模块、接口、数据和依赖已经建立影响索引；
- 用户已有修改已经识别并进入保护范围；
- 未覆盖区域和未知风险已经披露；
- Profile 与已知风险相称。

重大需求缺口返回 Clarify；上下文足够时进入 Design。
