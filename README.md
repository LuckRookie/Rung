# Rung

Rung 是一个面向 Coding Agent 的软件开发渐进式治理 Skill。它从用户意图覆盖到可验证 Release，并在任务出现不确定性、风险、协作、验证声明或发布准备信号时，按需加载相关提醒、模板和确定性工具。

当前稳定版本为 [v0.1.0](https://github.com/LuckRookie/Rung/releases/tag/v0.1.0)。产品定义、系统边界和实现约束以 [Rung.md](Rung.md) 为准。

`main` 分支当前形成 v0.1.2 候选开发内容；稳定安装坐标继续锁定 `v0.1.0` tag。

## 核心能力

| 能力 | 结果 |
|---|---|
| 代码项目范围路由 | 根据主要验收对象与长期维护关系判断代码项目工作、范围外工作和混合任务 |
| 薄层导航 | 默认只提醒 Outcome、Context、Approach、Evidence 和 Handoff |
| 执行责任 | 每次 DevelopmentRun 由一个 Primary Agent 持有全局 Plan、集成结果与 Release Handoff |
| 按需治理 | 当前信号决定加载哪个开发关注面和治理深度 |
| 项目适配 | 仓库事实、现有规则、工具链和用户修改进入当前判断 |
| 项目画像 | 项目含义、语义中心、能力归属或演进方向存在实质不确定性时，将用户意图与项目现实合成为可修正的 Project Model |
| 工程结构治理 | Design、Implement 和 Review 出现实质结构信号时，按需检查归属、局部性、信息隐藏、依赖知识、状态语义和抽象依据 |
| 架构评估 | 显式审查已有架构、模块化、结构债务或框架适配时，以变化场景、仓库证据、因果机制和反证识别主要结构矛盾 |
| Project Harness 演进 | 复用可靠的已有约束，并在事实源、测试、规则、构建、CI 或 Gate 自身出现问题时进行独立诊断和渐进迁移 |
| 分层验证系统 | 在证据缺口或 Harness 增长时治理测试、Fixture、文档检查、CI、构建、打包和端到端入口 |
| 相称证据 | 完成、兼容和可发布结论关联与风险相称的实际结果 |
| 发布交接 | 整理 revision、制品、说明、限制和下游待办 |

## Progressive Governance

```text
User Intent
   ↓
Codebase Scope Gate
   ├─ 未建立代码项目关系 → Host / 对应工作流
   └─ 代码项目或与其耦合的内容 → 按当前信号加载一张提示卡 → Verified Release Handoff
```

Rung 只在主要验收对象属于软件代码库，或者某项内容的正确性与维护周期持续耦合于该代码库时进入 DevelopmentRun。仓库存在、文件位置、文件类型、工具使用和偶然产生的代码都不能单独建立这种关系。范围外工作由 Host 或其对应工作流继续处理；混合任务只把满足条件的代码项目部分推进到 Release Handoff。

Rung 覆盖八个可组合关注面：

```text
Clarify · Inspect · Design · Plan · Implement · Verify · Review · Release
```

Agent 可以合并、跳过和回访这些关注面。普通任务不创建 Rung 工作区；复杂、跨会话或高风险任务可以按需使用 Profile、Artifact 和脚本。

每次 DevelopmentRun 由一个逻辑 Primary Agent 负责。默认在一个主 Session 中完成相称检查、方案、修改、集成验证、Review 和 Handoff；跨 Session 状态、Worker 与独立 Reviewer 只在能够改善恢复、并行或置信度时加入。完整的执行契约见 [Execution Model](rung/references/execution-model.md)。

项目检查从 Baseline 和 Target 开始，公共接口、持久数据、共享行为、依赖、平台或多模块影响会把半径扩展到 Impact；明确审查、核心架构、广泛迁移、安全边界或 Harness Evolution 使用声明过的 System 边界。局部可逆 Design 可以留在对话、代码与测试中，长期契约和架构事实进入项目自己的事实源，临时恢复状态可以按需进入 `.rung/`。

当稀疏用户表达支持多个产品解释、已有项目事实描绘出冲突身份、新能力接近语义边界、用户准备主动扩展产品方向，或一个仓库包含多个产品中心时，Clarify 与 Inspect 可以按需建立 Project Model。它区分用户确认、仓库证据、Agent 推断、来源冲突和未知信息，并把人、核心情境、结果、语义中心、决策优先级、边界样例和可信演进提供给 Design 与 Review。普通明确任务不生成画像文件。

Primary Agent 编写全局 Plan，也默认执行修改。Worker 接收互不重叠的有界 Task Packet，返回的局部结果由 Primary Agent 复查和集成；最终 Verification 针对组合后的实际代码状态。Multi-Agent 能力取决于 Host，单 Agent Host 可以完整运行 Rung。

Lite / Standard / Strict 控制治理、协调和持久化深度；Verification Tier 0–3 控制证据覆盖范围。两条轴独立选择。完整的责任与覆盖流程见 [Rung.md 的责任流程图](Rung.md#131-责任流程图)。

Rung 按实际加载量控制上下文：Scope Gate 在任何 Reference 前运行，`SKILL.md` 和 Concern Cards 保持短小，复杂领域使用按信号加载的详细 Domain Guides。默认一次只加载当前判断需要的一张 Reference，未来阶段不触发预加载。当前 Harness 关系为 `Test System ⊂ Verification Harness ⊂ Project Harness`；局部测试维护沿用正常开发路径，共享判断机制、覆盖、可靠性、成本或 Gate 变化进入 Harness Evolution。

工程结构同样按两层加载：日常方案、实现与 diff 复查在出现实质结构影响时读取 Engineering Structure；用户明确请求已有系统架构、模块化、结构债务、依赖形态或框架适配审查时，再读取 Architecture Assessment。重要 Finding 需要连接 Driver、仓库证据、结构机制、实际成本或风险、最小干预和独立验证；文件大小、目录形态和模式名称只作为调查线索。

Project Model 可以留在 Session 中；跨 Session、多人协作、正式审查或多个后续决策会复用时，可以进入项目已有 Product Definition、README、Requirement、Domain Glossary、Architecture Overview，或临时 `.rung/runs/<run-id>/project-model.md`。可选模板只在持久化具有消费者时使用。

## Skill 包

```text
rung/
├── SKILL.md                 # 代码项目范围门、薄提示与信号路由
├── agents/openai.yaml       # Codex UI 元数据
├── references/              # Execution Model、Development Scope、关注面、Project Model、Engineering Structure、Architecture Assessment 与其他按需 Domain Guides
├── profiles/                # 可选治理深度提示
├── assets/                  # 可选开发制品模板
└── scripts/                 # 确定性检查助手
```

## 安装

Rung 采用 Agent Skills 仓库分发方式。`skills` CLI 会在仓库中发现 `rung/SKILL.md`，安装完整 Skill 包，并记录来源和内容哈希。

安装稳定版本 v0.1.0：

```bash
npx skills add https://github.com/LuckRookie/Rung/tree/v0.1.0/rung
```

Codex 用户级安装：

```bash
npx skills add https://github.com/LuckRookie/Rung/tree/v0.1.0/rung --skill rung --agent codex --global --yes
```

安装到当前项目时移除 `--global`，目标目录为 `.agents/skills/rung`。用户级安装会让 Rung 对该用户的不同项目与工作目录可见；项目级安装把发现范围限制在当前项目。Rung 默认保留隐式调用，并通过精确 description 与 Scope Gate 控制任务相关性。

Codex 提供 `$skill-installer` 时，也可以直接发送：

```text
使用 $skill-installer 安装这个 Skill：
https://github.com/LuckRookie/Rung/tree/v0.1.0/rung
```

完整的作用域、冲突处理、手动安装和验证规则见 [INSTALL.md](INSTALL.md)。该文件也可以直接交给 Coding Agent；私有仓库沿用 Agent 环境中已经配置的 GitHub 访问权限：

```text
从 https://github.com/LuckRookie/Rung.git 获取 v0.1.0 tag，完整读取根目录 INSTALL.md，
按照其中的安装契约把 Rung 安装到用户级作用域，并在完成后验证安装结果。
```

### 调用

```text
$rung 为现有项目实现导出功能，并准备一个经过验证的可发布版本。
```

Rung 默认保持轻量，先确认当前验收对象与代码项目的关系，再根据任务信号加载相关提示。未建立关系时立即退出；进入 DevelopmentRun 后以与任务规模相称的方式说明实现结果、实际验证、残余风险和 Release 交接状态。

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
  --max-tier 2 \
  --output .rung/runs/RUN_ID/evidence.json
```

`--max-tier` 选择本次执行的最高验证层，并把跳过项写入 Evidence。需要设计或扩展 Fixture、Mock、测试服务、文档检查、CI Gate、构建、打包或端到端环境时，可以按需形成 `.rung/runs/RUN_ID/verification-harness.md`；长期 Harness 代码和配置进入目标项目自己的正式结构。

已有 Project Harness 自身进入修改范围时，可以按需形成 `.rung/runs/RUN_ID/harness-change.md`，记录权威事实、基线、独立证据、Coverage Delta、生效、回退和旧路径清理条件。

检查持久化 Artifact 和 Release Manifest：

```bash
python rung/scripts/validate_artifacts.py \
  --run-dir .rung/runs/RUN_ID

python rung/scripts/check_release.py \
  --manifest .rung/runs/RUN_ID/release.yaml \
  --project .
```

Artifact 检查默认验证运行目录中实际存在的 Rung 制品；需要特定集合时可以重复使用 `--require` 精确声明。

Release Manifest 标记为 `ready` 或 `published` 时，本地 `verification` 引用使用顶层 `status` 为 `pass` 的 JSON Evidence；外部 CI 或制品系统可以提供 URI。

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
evals/                     # 代码项目范围、项目画像、工程结构、架构评估、Harness 与上下文成本的行为评测场景
tests/                     # 确定性脚本测试
.github/workflows/ci.yml   # 持续集成
AGENTS.md                  # 本仓库的 Agent 开发约定
```

## v0.1.0

首个稳定版本包含：

- 单一、轻量的 Rung Skill 入口；
- 五个默认治理提示与信号驱动路由；
- 一个明确 Primary Agent、检查半径、Design 持久化、Plan/Implement 责任、Worker/Reviewer 和跨 Session 恢复的 Execution Model Guide；
- 八张可组合的开发关注面提示卡；
- 按代码结构信号加载的工程设计与 diff 复查提醒；
- 按冲突、误报、漏报、漂移和 Gate 变化加载的 Project Harness 与 Harness Evolution 详细指南；
- 按证据缺口加载的 Verification Harness 详细指南、可选 Harness Artifact 与 Tier 筛选执行；
- Lite、Standard、Strict 可选深度提示；
- 可选 DevelopmentRun Artifact 模板；
- 项目检查、验证执行、Artifact 与 Release 检查脚本；
- 无信号、小型 Bugfix、跨模块归属、连续变化、Harness 增长、已有 Harness 演进、单 Session 执行、跨 Session 恢复和 Worker 集成的行为评测协议；
- 脚本行为测试。

下一轮通过无额外治理信号的 Bugfix、跨模块 Feature、连续 Greenfield 变化、跨 Session 恢复和 Worker-assisted integration 场景，对比基线、当前 Rung 与候选提示，校准触发准确性、执行责任、工程收益、实现多样性和上下文成本。
