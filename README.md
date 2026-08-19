# Rung

Rung 是一个面向 Coding Agent 的软件开发编排 Skill。它从用户意图出发，组织需求澄清、项目检查、方案设计、开发计划、实现、验证、工程审查和版本发布，最终交付具有实际证据的 Release Package。

项目当前处于 MVP 构建阶段。产品定义、系统边界和实现约束以 [Rung.md](Rung.md) 为准。

## 核心能力

| 能力 | 结果 |
|---|---|
| 开发闭环 | 同一次 DevelopmentRun 连接需求、设计、实施、验证与发布 |
| 项目适配 | 从仓库事实、现有规则和工具链建立 ProjectContext |
| 风险自适应 | Lite、Standard、Strict 控制制品深度与验证强度 |
| 证据追踪 | 验收条件、代码变更、命令结果和 Release 状态保持关联 |
| 发布交付 | 生成可复现的 Release Package、Release Manifest 和风险说明 |

## Development Workflow

```text
Clarify → Inspect → Design → Plan → Implement → Verify → Review → Release
```

流程支持按证据返回先前阶段，并通过持久 Artifact 恢复中断任务。

## Skill 包

```text
rung/
├── SKILL.md                 # Skill 入口与阶段路由
├── agents/openai.yaml       # Codex UI 元数据
├── references/              # 八阶段、风险和 Artifact 契约
├── profiles/                # Lite、Standard、Strict
├── assets/                  # DevelopmentRun 制品模板
└── scripts/                 # 项目检查、验证执行和 Release Gate
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

完整的作用域、冲突处理、手动安装和验证规则见 [INSTALL.md](INSTALL.md)。该文件也可以直接交给 Coding Agent：

```text
读取 https://raw.githubusercontent.com/LuckRookie/Rung/main/INSTALL.md，
按照其中的安装契约把 Rung 安装到用户级作用域，并在完成后验证安装结果。
```

### 调用

```text
$rung 为现有项目实现导出功能，并准备一个经过验证的可发布版本。
```

Rung 会根据任务和项目风险选择 Profile，按阶段推进，并在最终结果中报告实现、验证证据、残余风险和 Release 状态。

## 确定性工具

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
  --run-dir .rung/runs/RUN_ID \
  --profile standard

python rung/scripts/check_release.py \
  --manifest .rung/runs/RUN_ID/release.yaml \
  --project .
```

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

第一条纵向切片已经包含：

- 单一 Rung Skill 入口；
- 八阶段 Stage Contract；
- Lite、Standard、Strict 三档 Profile；
- DevelopmentRun Artifact 模板；
- 项目检查、验证执行、Artifact 检查和 Release Gate 脚本；
- 脚本行为测试。

下一轮通过真实 Bugfix 和 Feature 场景校准工作流，再扩展 Greenfield、Refactor 与 Migration 验收。
