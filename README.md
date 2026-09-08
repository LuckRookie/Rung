# Rung

Rung 是一个面向 Coding Agent 的软件开发渐进式治理 Skill。它为持续软件开发中的实质工程决定提供从设计到交付的按需指导；简单、局部、可逆且已有直接检查的修改沿用 Host 普通编码路径。

当前稳定版本为 [v0.1.0](https://github.com/LuckRookie/Rung/releases/tag/v0.1.0)；`main` 上的候选开发线版本为 `0.1.2`。稳定引用和候选版本由 [`rung/contracts/rung-contract.json`](rung/contracts/rung-contract.json) 维护。产品定义、系统边界和实现约束以 [Rung.md](Rung.md) 为准。

`main` 分支当前形成 v0.1.2 候选开发内容；稳定安装坐标继续锁定 `v0.1.0` tag。

## 核心能力

| 能力 | 结果 |
|---|---|
| 开发意图路由 | 分别判断开发范围与治理启用；隐式调用需要实质工程决定，显式调用可用于范围内的小任务 |
| 薄层导航 | 默认只提醒 Outcome、Context、Approach、Evidence 和 Handoff |
| 执行责任 | 每次 DevelopmentRun 由一个 Primary Agent 持有全局 Plan、集成结果与 Release Handoff |
| 按需治理 | 当前信号决定加载哪个开发关注面和治理深度 |
| 项目适配 | 仓库事实、现有规则、工具链和用户修改进入当前判断 |
| 项目画像 | 项目含义、语义中心、能力归属或演进方向存在实质不确定性时，将用户意图与项目现实合成为可修正的 Project Model |
| 设计探索 | 重要设计仍存在多条后果明显不同的合理路径时，以最少代表性场景发现隐藏职责、状态、失败语义和真实权衡，再交给 Design 收敛 |
| 工程结构治理 | Design、Implement 和 Review 出现实质结构信号时，按需检查归属、局部性、信息隐藏、依赖知识、状态语义和抽象依据 |
| 架构评估 | 已有系统审查需要形成改造、兼容或 Release 决策时，以变化场景、仓库证据、因果机制和反证识别主要结构矛盾 |
| 架构设计 | 新子系统、公共契约或跨模块边界需要方向时，以变化场景、职责契约、状态、依赖和验证接缝收敛最小边界 |
| 默认编码指导 | 在会话内联系目标、不变量、Owner、失败与证据；后续变化只在影响边界时检查 |
| 软件质量 | 当前修改与 Review 按需判断正确性、可理解性、可修改性、可验证性、可运行性、一致性和可预测性，并让触及 Owner 保持连贯 |
| 技术债治理 | 以当前承载状态、可信 Trigger 与未来负担机制限定有效债务，管理 Interest、Exposure、Propagation、Principal、策略与 Revisit |
| Project Harness 演进 | 复用可靠的已有约束，并在事实源、测试、规则、构建、CI 或 Gate 自身出现问题时进行独立诊断和渐进迁移 |
| 分层验证系统 | 在证据缺口或 Harness 增长时治理测试、Fixture、文档检查、CI、构建、打包和端到端入口 |
| 相称证据 | 完成、兼容和可发布结论关联与风险相称的实际结果 |
| 发布交接 | 整理 revision、制品、说明、限制和下游待办 |

## Progressive Governance

```text
User Intent
   ↓
Development Scope Gate
   ├─ 理解型结果或未建立代码库关系 → Host / 对应工作流
   └─ 满足开发范围及启用条件的部分 → 按当前信号加载零到一张提示卡 → Verified Release Handoff
```

Rung 先确认代码库关系与活跃开发 Claim，再决定是否启用。自动调用需要实质的职责、契约、状态、失败、兼容、迁移、验证或交付决定。行为、Owner、影响与检查已知的局部可逆修改直接由 Host 完成；文件数、项目规模和常规测试不单独触发。显式 `$rung` 或开发治理请求可用于小任务，仍须满足开发范围。边界的权威定义见 [Rung.md §4.1](Rung.md#41-开始边界user-intent)。

未知情况先进行最小 Host 检查，发现实质影响后再进入。已安装或提到 Skill 不表示启用。每个新任务重新判断，实际需要哪个关注面才读取哪张卡。

Rung 覆盖八个可组合关注面：

```text
Clarify · Inspect · Design · Plan · Implement · Verify · Review · Release
```

Agent 可以合并、跳过和回访这些关注面。普通任务不创建 Rung 工作区；复杂、跨会话或高风险任务可以按需使用 Profile、Artifact 和脚本。

每次 DevelopmentRun 由一个逻辑 Primary Agent 负责。默认在一个主 Session 中完成相称检查、方案、修改、集成验证、Review 和 Handoff；跨 Session 状态、Worker 与独立 Reviewer 只在能够改善恢复、并行或置信度时加入。完整的执行契约见 [Execution Model](rung/references/execution-model.md)。

项目检查从 Baseline 和 Target 开始，公共接口、持久数据、共享行为、依赖、平台或多模块影响会把半径扩展到 Impact；明确审查、核心架构、广泛迁移、安全边界或 Harness Evolution 使用声明过的 System 边界。局部可逆 Design 可以留在对话、代码与测试中，长期契约和架构事实进入项目自己的事实源，临时恢复状态可以按需进入 `.rung/`。

当稀疏用户表达支持多个产品解释、已有项目事实描绘出冲突身份、新能力接近语义边界、用户准备主动扩展产品方向，或一个仓库包含多个产品中心时，Clarify 与 Inspect 可以按需建立 Project Model。它区分用户确认、仓库证据、Agent 推断、来源冲突和未知信息，并把人、核心情境、结果、语义中心、决策优先级、边界样例和可信演进提供给 Design 与 Review。普通明确任务不生成画像文件。

Project Model 已经给出方向后，重要设计仍可能存在多条会改变 Owner、契约、状态、UX、风险或实现方向的合理路径。此时 Clarify、Project Model 或 Design 可以按需加载 Design Exploration：选择能够区分方向的最小代表性场景，沿成功、失败、恢复和生命周期发现隐藏职责与状态，只保留后果真实不同的候选方向，再把接受方向、权衡和 Revisit signal 交给 Design。清楚的局部修改不加载这份 Guide，探索结果默认留在 Session。

Primary Agent 编写全局 Plan，也默认执行修改。Worker 接收互不重叠的有界 Task Packet，返回的局部结果由 Primary Agent 复查和集成；最终 Verification 针对组合后的实际代码状态。Multi-Agent 能力取决于 Host，单 Agent Host 可以完整运行 Rung。

Lite / Standard / Strict 控制治理、协调和持久化深度；Verification Tier 0–3 控制证据覆盖范围。两条轴独立选择。完整的责任与覆盖流程见 [Rung.md 的责任流程图](Rung.md#131-责任流程图)。

Rung 按实际加载量控制上下文：Development Scope Gate 在任何 Reference 前运行，`SKILL.md` 和 Concern Cards 保持短小，复杂领域使用按信号加载的详细 Domain Guides。默认一次只加载当前判断需要的一张 Reference，未来阶段不触发预加载。当前 Harness 关系为 `Test System ⊂ Verification Harness ⊂ Project Harness`；局部测试维护沿用正常开发路径，共享判断机制、覆盖、可靠性、成本或 Gate 变化进入 Harness Evolution。

工程结构同样按两层加载：日常方案、实现与 diff 复查在出现实质结构影响时读取 Engineering Structure；已有系统审查需要形成改造、兼容或 Release 决策时，再读取 Architecture Assessment。重要 Finding 需要连接 Driver、仓库证据、结构机制、实际成本或风险、最小干预和独立验证；文件大小、目录形态和模式名称只作为调查线索。

默认编码指导直接写在入口中，完整架构、质量、债务和 Harness 指南由相应阶段卡按信号进入。没有默认质量 Guide、固定四步、必填 Change Contract 或自动 Python 启动命令。是否真正降低上下文占用，要观察宿主实际选中、读取与重复读取的内容。

[Software Quality](rung/references/software-quality.md) 与 [Technical Debt](rung/references/technical-debt.md) 是两个独立判断维度。前者关注软件当前对使用者、维护者、环境和已接受方向的适用性；后者关注当前工程状态在可信变化、维护事件或时间节点下产生的可避免未来负担。普通任务只整理 touched ownership boundary，详细质量 Guide 由实质权衡或 Finding 触发；代码异味、TODO、年龄和工具分数只产生 Debt Signal，当前 Construct、可信 Trigger 或 Exposure、Interest 或 Propagation 机制和管理决定共同限定 Qualified Debt Item。

技术债覆盖 Code、Architecture、Data and Compatibility、Dependency and Platform、Verification and Harness、Build and Release、Documentation and Fact Sources。显式系统审查寻找驱动项目 Chaos 的少数 Debt Mechanism；日常开发只处理当前变化实际激活、引入、携带或偿还的义务。持久债务优先进入项目已有 Issue、Roadmap、Architecture、Dependency、Migration 或 Harness Owner；缺少合适形态且存在未来消费者时，才使用可选 Technical Debt Item 模板。

Project Model 可以留在 Session 中；跨 Session、多人协作、正式审查或多个后续决策会复用时，可以进入项目已有 Product Definition、README、Requirement、Domain Glossary、Architecture Overview，或临时 `.rung/runs/<run-id>/project-model.md`。可选模板只在持久化具有消费者时使用。

## Skill 包

```text
rung/
├── SKILL.md                 # 活跃开发范围门、薄提示与信号路由
├── agents/openai.yaml       # Codex UI 元数据
├── references/              # 阶段卡与按需领域指南
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

安装到当前项目时移除 `--global`，目标目录为 `.agents/skills/rung`。用户级安装会让 Rung 对该用户的不同项目与工作目录可见；项目级安装把发现范围限制在当前项目。Rung 默认保留隐式调用，description 聚焦实质软件开发决定，Development Scope Gate 负责误触后的二次核对。

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

Rung 默认保持轻量，先确认当前验收对象同时具备代码库关系和活跃开发 Claim，再检查启用条件。简单隐式修改、理解型与范围外结果沿用 Host；进入 DevelopmentRun 后以与任务规模相称的方式说明实现结果、实际验证、残余风险和 Release 交接状态。

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

Qualified Debt Item 通常写入项目已有管理系统。项目缺少可用形态且后续 Owner 需要持久状态时，可以从 [Technical Debt Item 模板](rung/assets/technical-debt-item.template.md)选择必要字段，并在可选运行目录中保存为 `debt.md`。

Release Manifest 标记为 `ready` 或 `published` 时，本地 `verification` 引用使用顶层 `status` 为 `pass` 的 JSON Evidence；外部 CI 或制品系统可以提供 URI。

所有脚本只使用 Python 标准库，并输出机器可读 JSON。

核心契约检查：

```bash
python rung/scripts/validate_contract.py --skill-root rung
```

该检查验证范围与启用契约、间接路由可达性、可组合关注面覆盖、上下文预算和包版本事实。它把运行时入口中的关键承诺固定为可验证的契约，但不替代真实 Agent 行为评测。

Scope Gate 的结构化评估：

```bash
python rung/scripts/evaluate_scope.py --input scope-classification.json
```

输入由 Host 提供判断：`codebase_relationship`、`development_claim` 取 `present | absent | mixed | uncertain`；`materiality` 取 `present | absent | uncertain`；`invocation_mode` 取 `implicit | explicit`。Mixed 表示存在可识别的活跃开发部分；未知不应填写 Mixed。

输出协议为 v2，分别报告 `scope` 和 `activation: enter | bypass | defer`。旧的两个字段输入仍能读取，缺失的实质性默认 `uncertain`，缺失调用方式默认 `implicit`，不会静默启用。`exited_before_references` 是退出建议，实际读取必须由 Host Trace 验证；`status: pass` 仅表示输入有效。工具不替 Agent 判断自然语言，不在每次启动时运行。

## 开发验证

```bash
python -B -m unittest discover -s tests -v
ruff check --no-cache .
python rung/scripts/validate_contract.py --skill-root rung
python rung/scripts/evaluate_scope.py --input <scope-classification.json>
```

Codex 环境中还应使用 `skill-creator` 提供的 `quick_validate.py` 检查 Skill 元数据和结构。

## 仓库结构

```text
Rung.md                    # 产品与架构事实源
INSTALL.md                 # 人与 Coding Agent 共用的安装契约
rung/                      # 可安装 Skill 包
rung/contracts/            # Scope Gate、路由、预算和版本的机器可读契约
evals/                     # 开发意图、设计探索、项目画像、软件质量、技术债、工程结构、架构评估、Harness 与上下文成本评测
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
- 无信号、小型 Bugfix、跨模块归属、连续变化、Harness 增长、已有 Harness 演进、单 Session 执行、跨 Session 恢复、Worker 集成和全生命周期指导的行为评测协议；
- 脚本行为测试。

下一轮通过无额外治理信号的 Bugfix、跨模块 Feature、连续 Greenfield 变化、跨 Session 恢复和 Worker-assisted integration 场景，对比基线、当前 Rung 与候选提示，校准触发准确性、执行责任、工程收益、实现多样性和上下文成本。
