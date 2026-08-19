# Rung

Rung 是一个面向 Coding Agent 的软件开发渐进式治理 Skill。它从用户意图覆盖到可验证 Release，并在任务出现不确定性、风险、协作、验证声明或发布准备信号时，按需加载相关提醒、模板和确定性工具。

项目当前处于 MVP 构建阶段。产品定义、系统边界和实现约束以 [Rung.md](Rung.md) 为准。

## 核心能力

| 能力 | 结果 |
|---|---|
| 薄层导航 | 默认只提醒 Outcome、Context、Approach、Evidence 和 Handoff |
| 按需治理 | 当前信号决定加载哪个开发关注面和治理深度 |
| 项目适配 | 仓库事实、现有规则、工具链和用户修改进入当前判断 |
| 相称证据 | 完成、兼容和可发布结论关联与风险相称的实际结果 |
| 发布交接 | 整理 revision、制品、说明、限制和下游待办 |

## Progressive Governance

```text
正常开发
   │
   ├─ 出现治理信号 → 加载一个相关提示卡 → 继续开发
   │
   └─ 收集相称证据 → Release 交接
```

Rung 覆盖八个可组合关注面：

```text
Clarify · Inspect · Design · Plan · Implement · Verify · Review · Release
```

Agent 可以合并、跳过和回访这些关注面。普通任务不创建 Rung 工作区；复杂、跨会话或高风险任务可以按需使用 Profile、Artifact 和脚本。

## Skill 包

```text
rung/
├── SKILL.md                 # 薄提示与信号路由
├── agents/openai.yaml       # Codex UI 元数据
├── references/              # 按需加载的关注面与治理提醒
├── profiles/                # 可选治理深度提示
├── assets/                  # 可选开发制品模板
└── scripts/                 # 确定性检查助手
```

## 安装

Rung 采用 Agent Skills 仓库分发方式。`skills` CLI 会在仓库中发现 `rung/SKILL.md`，安装完整 Skill 包，并记录来源和内容哈希。

交互式安装：

```bash
npx skills add LuckRookie/Rung
```

Codex 用户级安装：

```bash
npx skills add LuckRookie/Rung --skill rung --agent codex --global --yes
```

安装到当前项目时移除 `--global`，目标目录为 `.agents/skills/rung`。

Codex 提供 `$skill-installer` 时，也可以直接发送：

```text
使用 $skill-installer 安装这个 Skill：
https://github.com/LuckRookie/Rung/tree/main/rung
```

完整的作用域、冲突处理、手动安装和验证规则见 [INSTALL.md](INSTALL.md)。该文件也可以直接交给 Coding Agent；私有仓库沿用 Agent 环境中已经配置的 GitHub 访问权限：

```text
从 https://github.com/LuckRookie/Rung.git 获取 main 分支，完整读取根目录 INSTALL.md，
按照其中的安装契约把 Rung 安装到用户级作用域，并在完成后验证安装结果。
```

### 调用

```text
$rung 为现有项目实现导出功能，并准备一个经过验证的可发布版本。
```

Rung 默认保持轻量，根据当前任务信号加载相关提示。最终结果与任务规模相称，说明实现结果、实际验证、残余风险和 Release 交接状态。

## 可选确定性工具

重复执行、结构化证据或可靠退出码能够改善任务时，可以使用以下脚本。

项目检查：

```bash
python rung/scripts/inspect_project.py --project .
```

执行显式 JSON 验证计划：

```bash
python rung/scripts/run_verification.py \
  --project . \
  --plan .rung/runs/RUN_ID/verification-plan.json \
  --output .rung/runs/RUN_ID/evidence.json
```

检查持久化 Artifact 和 Release Manifest：

```bash
python rung/scripts/validate_artifacts.py \
  --run-dir .rung/runs/RUN_ID

python rung/scripts/check_release.py \
  --manifest .rung/runs/RUN_ID/release.yaml \
  --project .
```

Artifact 检查默认验证运行目录中实际存在的 Rung 制品；需要特定集合时可以重复使用 `--require` 精确声明。

所有脚本只使用 Python 标准库，并输出机器可读 JSON。

## 开发验证

```bash
python -B -m unittest discover -s tests -v
ruff check --no-cache .
```

Codex 环境中还应使用 `skill-creator` 提供的 `quick_validate.py` 检查 Skill 元数据和结构。

## 仓库结构

```text
Rung.md                    # 产品与架构事实源
INSTALL.md                 # 人与 Coding Agent 共用的安装契约
rung/                      # 可安装 Skill 包
tests/                     # 确定性脚本测试
.github/workflows/ci.yml   # 持续集成
AGENTS.md                  # 本仓库的 Agent 开发约定
```

## 当前里程碑

渐进式治理基线已经包含：

- 单一、轻量的 Rung Skill 入口；
- 五个默认治理提示与信号驱动路由；
- 八张可组合的开发关注面提示卡；
- Lite、Standard、Strict 可选深度提示；
- 可选 DevelopmentRun Artifact 模板；
- 项目检查、验证执行、Artifact 与 Release 检查脚本；
- 脚本行为测试。

下一轮通过真实 Bugfix 和 Feature 场景校准触发准确性、治理收益和上下文成本，再扩展 Greenfield、Refactor 与 Migration 验收。
