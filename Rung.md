# Rung 产品需求与系统设计

> 状态：Draft v0.3
> 更新日期：2026-08-19
> 文档职责：Rung 的产品定位、系统边界与实现约束的唯一事实源

## 1. 执行摘要

Rung 是一个面向 Coding Agent 的软件开发编排 Skill。它接收用户意图和项目事实，组织需求澄清、项目检查、方案设计、开发计划、代码实现、验证、工程审查和版本发布，最终交付一个可验证、可追踪的 Release Package。

Rung 的产品承诺是：

> 让 Coding Agent 按照完整、可验证、风险自适应的软件开发过程交付一个可发布版本。

一次 Rung DevelopmentRun 从 User Intent 开始，在 Release Gate 通过并形成 Verified Release Package 时完成。Release Package 随后交给代码托管、包仓库或下游交付系统。

---

## 2. 背景与问题

### 2.1 Coding Agent 的默认执行模式缺少开发闭环

现代 Coding Agent 通常已经能够：

- 阅读和搜索代码；
- 修改文件；
- 执行命令；
- 调用开发工具；
- 运行测试；
- 创建提交或发布制品。

默认工作模式仍然容易退化为：

```text
用户需求
   ↓
搜索附近代码
   ↓
立即修改
   ↓
运行少量测试
   ↓
宣称完成
```

这种模式缺少贯穿整个版本的软件开发判断：

- 目标、非目标和验收条件尚未定义；
- 项目已有结构和约束尚未建立索引；
- 未分析模块边界、接口和数据影响；
- 没有形成可检查的实施计划；
- 容易混合功能开发、重构和顺手修改；
- 验证范围与实际风险脱节；
- 测试通过后没有检查架构、文档和发布完整性；
- “代码写完”被错误地当成“版本可以发布”。

### 2.2 完整版本需要端到端开发流程

局部开发 Skill 通常提供以下能力：

- 如何编写某类代码；
- 如何使用某个框架；
- 如何遵守某套代码规范；
- 如何生成测试；
- 如何执行某个工具。

完整版本交付还需要回答：

- 用户的模糊想法是否已经足以开始开发？
- 空项目和成熟代码库应采用什么不同策略？
- 什么时候需要正式设计，什么时候只需简短说明？
- 哪些模块会受到影响，哪些区域需要保持不变？
- 验证需要覆盖到什么程度？
- 什么证据足以证明需求已完成？
- 文档、版本、Changelog 和制品是否已经同步？
- 什么时候才可以称为 Release？

Rung 用一个端到端 DevelopmentRun 把这些局部能力连接成开发闭环。

---

## 3. 产品定位

### 3.1 产品定义

Rung 是运行在 Coding Agent Host 之上的 **Development Orchestration Skill**。它通过 Stage、Artifact、Gate、Profile 和 Evidence 组织一次从 Intent 到 Release 的 DevelopmentRun，并调用项目已有的文件、Git、编译、测试、构建和包管理工具完成实际开发工作。

Rung 以一个 Skill 作为用户入口，以按需加载的参考资料、制品模板和确定性脚本作为执行支持。工程治理机制用于保持开发过程完整、风险与验证相称、完成声明有证据可查。

### 3.2 核心能力

Rung 提供五项核心能力：

1. **开发闭环**：把需求、设计、计划、实现、验证、审查和发布连接成同一次 DevelopmentRun；
2. **项目适配**：先读取仓库事实、既有约束和工具链，再决定实施方式；
3. **风险自适应**：通过 Lite、Standard 和 Strict 调整制品深度与验证强度；
4. **证据追踪**：把验收条件、代码变更、验证结果和 Release 状态关联起来；
5. **发布交付**：生成可复现的 Release Package、Release Manifest 和已知风险说明。

### 3.3 目标用户

Rung 面向：

- 使用 Coding Agent 创建新项目的个人开发者；
- 使用 Coding Agent 修改现有代码库的开发者和团队；
- 希望减少 AI 随意修改、遗漏验证和过早宣布完成的项目；
- 需要让不同 Coding Agent 遵循一致开发流程的代码库。

### 3.4 目标项目

Rung 应支持：

- 空项目或近乎空项目；
- 已有代码但缺少系统开发说明的项目；
- 已有测试、文档、架构和工程约束的成熟项目；
- 单体仓库、Monorepo 和多模块项目；
- 不同语言、框架和构建系统。

Rung 的核心流程与具体语言和框架解耦。项目事实、参考资料和适配脚本承载语言、框架与工具差异。

---

## 4. 产品目标与成功标准

### 4.1 产品目标

Rung 必须使 Coding Agent 能够：

1. 将模糊意图转化为明确、可验收的开发目标；
2. 在修改前理解项目结构、约束和现有事实源；
3. 根据变化原因和项目事实设计边界；
4. 在实现前完成影响分析和可执行计划；
5. 按计划、小范围地实施修改；
6. 根据变化风险选择相称的验证范围；
7. 使用实际证据判断完成状态；
8. 在发布前同步文档、版本和已知限制；
9. 生成可复现、可追踪的 Release Package；
10. 根据任务规模调整流程深度和制品数量。

### 4.2 成功标准

一次成功的 Rung DevelopmentRun 应满足：

- Development Brief 在代码修改前达到当前 Profile 的进入条件；
- Project Context 记录项目状态和相关约束；
- 重要设计选择有理由和影响范围；
- 实施结果能够追踪到验收条件；
- 验证命令被实际执行，并记录覆盖范围；
- 未验证内容被明确标注；
- 文档和发布信息与代码状态一致；
- Release 对应明确的代码版本或 Git revision；
- DevelopmentRun 分别记录 implementation、verification、release ready 和 published 状态；
- Artifact 的数量和深度与任务风险相称。

---

## 5. 系统边界

### 5.1 开始边界：User Intent

Rung 从用户表达开发意图开始。意图可以是：

- 创建一个新项目；
- 开发一个功能；
- 修复一个缺陷；
- 执行一次重构；
- 完成数据、接口或依赖迁移；
- 升级依赖；
- 修改构建、配置或文档；
- 准备一个正式版本。

Rung 负责把意图转换为足以开发的目标、约束和验收条件。

用户提供的业务背景和产品决策作为 Development Brief 的输入。

### 5.2 结束边界：Release

Rung 在形成通过 Release Gate 的 Release Package 后结束一次 DevelopmentRun。

Release 表示：

> 软件已经完成、验证、文档化、版本化，并能够以可复现方式生成可交付制品。

Release 输出包括：

- 当前 revision 对应的代码、配置、测试和必要文档；
- 可复现生成的 Release Package；
- 版本、Changelog 或 Release Notes；
- Release Manifest；
- 验收状态、验证证据、已知限制和未验证风险。

### 5.3 Release 交接

Rung 可以开发和验证发布、部署相关的项目文件，例如：

- Dockerfile；
- CI 配置；
- Helm Chart；
- Terraform 或其他基础设施代码；
- 构建与发布脚本；
- 包管理和制品配置。

这些文件的构建、静态检查和测试属于 DevelopmentRun。Release Gate 通过后，Rung 按照下表交付：

| 交接场景 | Rung 交付 | 接收系统 |
|---|---|---|
| 包仓库发布、Git Tag、远端 Release | Release Package、版本信息、发布说明；经用户明确授权后可执行发布动作 | 包仓库或代码托管平台记录分发状态 |
| 生产部署与流量切换 | 已验证的部署配置、制品引用和 Release Manifest | CI/CD 与部署平台执行环境变更 |
| 线上数据库变更 | 迁移文件、兼容性说明、验证和回退方案 | 数据变更流程在目标环境执行 |

Rung 的状态机记录 `release ready` 和可选的 `published` 状态。环境变更和运行状态由接收系统维护。

### 5.4 后续开发循环

缺陷修复、重构、依赖升级和技术债清理分别启动新的 DevelopmentRun。上一版本遗留的问题可以作为下一次 DevelopmentRun 的输入；项目现有的 Issue、Roadmap 或任务系统负责长期排期和追踪。

---

## 6. 产品形态

### 6.1 第一产品形态

Rung 的第一产品形态是一个单一的 Rung Skill。

用户通过自然语言调用 Rung，由 Skill 判断当前任务、项目状态和开发深度，并编排完整 DevelopmentRun。

Rung 产品包由四类内容组成：

1. **Instructions**：规定触发条件、阶段顺序、决策边界和输出契约；
2. **References**：按需加载各阶段方法、风险规则和项目类型指南；
3. **Scripts**：执行可确定、可重复的项目检查和验证；
4. **Assets**：提供开发制品、报告和项目初始化模板。

自然语言判断由 Agent 完成；可以确定性检查的规则必须优先脚本化。

### 6.2 单一 Skill 的职责

Rung Skill 的单一职责是：

> 管理一次从用户意图到可发布版本的完整软件开发循环。

Clarify、Inspect、Design、Plan、Implement、Verify、Review 和 Release 共同构成这一个职责，并共享同一套状态与制品。

第一版提供一个用户可见的 Skill 入口，八个阶段共享同一个 DevelopmentRun、Artifact 和状态模型。阶段方法可以在 references 中模块化维护。后续拆分决策以实际触发准确率、上下文成本和维护成本为依据。

### 6.3 渐进披露

Rung 使用渐进披露控制上下文。每次调用只加载当前阶段、项目类型和 Profile 所需的方法与资源。

加载顺序应为：

```text
Skill metadata
      ↓
SKILL.md 核心工作流
      ↓
当前 Stage 所需 reference
      ↓
当前项目和 Profile 所需脚本或模板
```

例如，小型 Bugfix 加载缺陷复现、根因分析和局部验证资源；新项目加载项目初始化、架构设计和首版发布资源。

### 6.4 建议的 Skill 包结构

```text
rung/
├── SKILL.md
├── references/
│   ├── workflow.md
│   ├── clarify.md
│   ├── inspect.md
│   ├── design.md
│   ├── plan.md
│   ├── implement.md
│   ├── verify.md
│   ├── review.md
│   ├── release.md
│   └── risk-signals.md
├── profiles/
│   ├── lite.md
│   ├── standard.md
│   └── strict.md
├── scripts/
│   ├── inspect-project
│   ├── validate-artifacts
│   ├── run-verification
│   ├── check-documentation
│   └── check-release
├── assets/
│   ├── development-brief.template.md
│   ├── project-context.template.md
│   ├── solution-design.template.md
│   ├── change-plan.template.md
│   ├── verification-report.template.md
│   ├── review-result.template.md
│   └── release-manifest.template.yaml
└── agents/
    └── host-specific metadata
```

这是目标包结构。第 17.3 节的实现顺序决定 MVP 首批落地文件。

### 6.5 跨宿主原则

Rung 的核心工作流必须保持宿主无关：

- `SKILL.md` 和通用资源使用跨宿主的概念与接口；
- 文件、Shell、测试和构建能力由 Coding Agent Host 提供；
- 宿主特定的名称、UI、工具依赖和权限配置放在独立 metadata 或 adapter 中；
- 脚本使用清晰的退出码和结构化输出，供不同模型和宿主稳定解析；
- 工具缺失时，Rung 将对应检查记录为 `blocked` 或 `not_covered`，并请求替代方案。

### 6.6 系统上下文

```text
Human
  │  提供 Intent、约束、决策和必要审批
  ▼
Coding Agent Host
  │  提供模型、文件操作、Shell、工具和权限边界
  ▼
Rung Skill
  │  编排 Stage、Profile、Artifact、Gate 和 Evidence
  ├──────────────┐
  ▼              ▼
References     Deterministic Scripts
  │              │
  └──────┬───────┘
         ▼
Project Repository + Existing Toolchain
         │
         ▼
Verified Release Package
--------- Rung boundary ends here ---------
         ▼
Repository / Registry / Delivery Pipeline
```

---

## 7. 核心概念模型

Rung 第一版定义七个核心概念。

### 7.1 DevelopmentRun

一次从 Intent 到 Release 的开发循环。

DevelopmentRun 至少记录：

- 唯一标识；
- 工作类型；
- 当前 Stage；
- 当前 Profile；
- 目标和验收条件；
- 关联制品；
- 未解决问题；
- 验证状态；
- Release 状态。

DevelopmentRun 将恢复所需状态持久化到 Artifact，从而支持跨会话暂停和继续。

### 7.2 ProjectContext

项目当前事实的索引，包括：

- 项目目标和非目标；
- 语言、框架和工具链；
- 目录和模块边界；
- 入口点和公共接口；
- 测试、构建、检查和发布命令；
- 项目级和目录级 Agent 指令；
- 现有架构、ADR 和文档位置；
- 已知约束和风险。

ProjectContext 优先引用项目现有事实源，正文继续由原事实源维护。

### 7.3 Stage

DevelopmentRun 当前所处的开发阶段。

每个 Stage 必须定义：

- 进入条件；
- 需要回答的问题；
- 允许的动作；
- 核心产物；
- 退出 Gate；
- 失败后返回的阶段。

### 7.4 Artifact

开发过程中的可检查产物。

核心 Artifact 包括：

- Development Brief；
- Project Context；
- Solution Design；
- Change Plan；
- Implementation Change；
- Verification Report；
- Review Result；
- Release Manifest。

Artifact 可以是：

- 项目中已有文件；
- Rung 创建的持久文件；
- 小任务中的结构化会话结果；
- 工具生成的机器可读证据。

### 7.5 Gate

进入下一 Stage 前必须满足的条件。

Gate 的结果只有：

- `pass`：条件已满足并有证据；
- `fail`：条件未满足，必须返回或修复；
- `blocked`：缺少用户决策、权限、工具或外部状态；
- `waived`：用户明确接受风险并记录理由。

`pass` 必须关联实际 Evidence；尚未完成的检查保持未评估状态，受工具或权限阻碍的检查记录为 `blocked`。

### 7.6 Profile

控制 DevelopmentRun 的流程深度和最小验证要求。

第一版包含：

- Lite；
- Standard；
- Strict。

Profile 调整产物和验证深度，并始终保持从意图到 Release 的责任边界。

### 7.7 Evidence

支持某项结论的实际证据，例如：

- 执行过的命令；
- 命令退出码；
- 测试数量和结果；
- 构建产物；
- 静态或安全检查报告；
- Git diff 或 revision；
- 人类明确决策；
- 未覆盖范围。

所有“完成”“通过”“兼容”“可发布”等结论必须能够指向 Evidence。

---

## 8. 工作类型与项目状态

### 8.1 工作类型

Rung 至少支持：

| 工作类型 | 说明 | 常见风险 |
|---|---|---|
| Greenfield | 创建新项目或新产品骨架 | 架构、工具链和边界尚未建立 |
| Feature | 增加用户可见能力 | 需求遗漏、接口和数据影响 |
| Bugfix | 修复错误行为 | 根因判断、回归和只修症状 |
| Refactor | 在保持预期外部行为的前提下调整内部结构 | 行为漂移、范围膨胀 |
| Migration | 数据、接口、依赖或架构迁移 | 兼容性、顺序和回退 |
| Dependency | 升级或替换依赖 | API 变化、安全与构建影响 |
| Docs/Config | 文档或配置变更 | 文档与真实行为的一致性 |
| Release-only | 对已完成变更执行版本和发布准备 | 制品、版本和证据的完整性 |

工作类型决定需要加载的参考和风险信号；具体框架逻辑由项目参考或适配脚本承载。

### 8.2 项目状态

Inspect 阶段将项目判断为：

- **New**：空项目或只有需求材料；
- **Existing**：已有实现，需要叠加式修改；
- **Governed**：已有明确架构、规则、测试和发布流程。

处理策略：

- New：创建满足已确认目标的最小可运行骨架，业务逻辑以 Development Brief 为准；
- Existing：理解并保留现有结构，在现有模式上叠加修改；
- Governed：复用现有事实源、工程规则和门禁。

---

## 9. 风险自适应 Profile

### 9.1 Lite

适用于：

- 小型 Bugfix；
- 文档修改；
- 局部配置；
- 影响范围明确的低风险修改。

要求：

- 明确目标和验收条件；
- 检查相关代码和项目约束；
- 给出简短实施与验证计划；
- 执行直接相关检查；
- 说明未验证内容；
- 确认发布影响。

Lite 可以在会话中保留简短设计记录；Clarify、Inspect、Verify 和 Review 的逻辑责任仍然完整。

### 9.2 Standard

适用于：

- 普通功能；
- 多文件修改；
- 新模块；
- 常规依赖升级；
- 中等范围重构。

要求：

- 持久化 Development Brief 或等价事实源；
- 完成影响分析；
- 形成 Change Plan 和 Verification Plan；
- 执行模块级或集成级验证；
- 同步相关文档；
- 生成 Review Result 和 Release Manifest。

### 9.3 Strict

适用于：

- 新项目；
- 核心架构变化；
- 公共接口变化；
- 身份认证、授权、安全或隐私相关功能；
- 数据或 Schema 迁移；
- 跨模块依赖方向变化；
- 大规模重构；
- 构建和发布链路变化。

要求：

- 正式的需求和验收条件；
- 明确架构与接口设计；
- 必要时产生 ADR；
- 明确兼容、迁移或回退策略；
- 完整 Change Plan；
- 集成或完整验证；
- 完整发布前审查和 Release Gate。

### 9.4 自动升级规则

出现以下信号时，Rung 必须建议升级 Profile：

- 修改公共 API、协议或数据格式；
- 修改数据库 Schema 或持久化数据；
- 增加认证、授权、加密或敏感数据处理；
- 改变模块依赖方向；
- 修改多个核心模块；
- 修改构建、打包或发布流程；
- 删除或替换关键依赖；
- 无法可靠确定影响范围；
- 现有测试的兼容性证明范围有限。

用户可以提高 Profile。用户要求降低 Profile 时，Rung 记录调整理由、被放弃的检查和对应风险，并由用户确认。

---

## 10. 八阶段 Development Workflow

### 10.1 总流程

```text
1. Clarify
   ↓
2. Inspect
   ↓
3. Design
   ↓
4. Plan
   ↓
5. Implement
   ↓
6. Verify
   ↓
7. Review
   ↓
8. Release
```

流程支持按证据返回先前阶段：验证失败返回 Implement；Review 发现设计问题返回 Design 或 Plan；新发现的重大未知返回 Clarify 或 Inspect。

### 10.2 Stage 1：Clarify

**目标**：把用户意图转换为可开发、可验收的目标。

Rung 必须确认：

- 要解决的问题；
- 用户或调用方；
- 预期行为；
- 非目标；
- 验收条件；
- 技术、时间、兼容和安全约束；
- 仍需用户决定的事项。

核心产物：Development Brief。

Clarify Gate：

- 目标和非目标不矛盾；
- 验收条件可以被观察或验证；
- 未知项已解决，或已记录为下一阶段可接受的开放项；
- 可能改变产品方向的重大假设已获得用户确认。

### 10.3 Stage 2：Inspect

**目标**：基于项目事实建立修改上下文。

Rung 必须检查：

- 项目状态：New、Existing 或 Governed；
- 仓库和模块结构；
- 入口点和公共接口；
- 依赖和配置；
- Agent 指令与项目约定；
- 测试、构建、静态检查和发布命令；
- 相关架构、ADR 和文档；
- 当前 Git 状态和用户已有修改；
- 与任务直接相关的代码路径和风险。

核心产物：Project Context。

Inspect Gate：

- 所有后续计划使用的路径和命令来自实际项目；
- 未覆盖的项目区域被明确说明；
- 用户已有修改已识别并纳入保护范围；
- 选定的 Profile 与已知风险相匹配。

### 10.4 Stage 3：Design

**目标**：确定满足需求的最小合理设计。

Rung 应考虑：

- 变化原因和稳定边界；
- 模块职责与信息隐藏；
- 接口和数据流；
- 状态与错误处理；
- 依赖方向；
- 兼容性；
- 测试边界；
- 与任务相关的安全、性能和可维护性要求。

设计原则：

- 根据实际复杂度和项目既有结构选择架构模式；
- 抽象对应已经出现的稳定变化方向；
- Manager、Helper 或公共层具有明确、长期的职责时才进入设计；
- 优先复用项目已有模式；
- 只有具有长期价值的决定才进入 ADR。

核心产物：Solution Design；必要时包含 ADR。

Design Gate：

- 设计覆盖全部验收条件；
- 模块和接口边界明确；
- 影响现有架构的变化已被识别；
- 复杂度与问题规模相匹配。

### 10.5 Stage 4：Plan

**目标**：在修改代码前形成可执行、可验证的顺序。

Change Plan 必须说明：

- 修改目标；
- 受影响模块和文件；
- 需要保持不变的区域；
- 实施顺序；
- 接口、数据和依赖变化；
- 测试和验证要求；
- 文档和 Release 要求；
- 失败或阻塞的处理方式；
- 必要的用户决策或批准。

计划以可独立执行和检查的变更单元为粒度，具体编码细节留在 Implement 阶段处理。

核心产物：Change Plan 和 Verification Plan。

Plan Gate：

- 每个验收条件都有实施和验证路径；
- 计划与 Project Context 和 Solution Design 一致；
- 功能修改与无关重构分离；
- 高风险动作有对应检查或回退说明。

### 10.6 Stage 5：Implement

**目标**：按照计划完成最小必要修改。

实施规则：

- 保持修改范围与 Change Plan 一致；
- 尊重现有代码和用户未提交修改；
- 业务逻辑以已确认的 Development Brief 和 Solution Design 为依据；
- 无关清理作为独立 DevelopmentRun 处理；
- 新行为应同时考虑验证；
- 发现设计或范围变化时返回 Design 或 Plan；
- 有效测试和既有质量门禁在修改过程中保持生效；
- 外部写操作和不可逆操作必须遵守宿主审批机制。

核心产物：Implementation Change，包括代码、配置、测试和必要文档修改。

Implement Gate：

- 计划中的修改已完成或明确标记未完成；
- 代码能够进入验证阶段；
- 计划外的范围变化已记录并完成确认；
- 新发现的问题已记录并路由到正确阶段。

### 10.7 Stage 6：Verify

**目标**：用与风险匹配的实际证据证明实现质量。

验证内容可能包括：

- 格式和语法；
- 静态分析和类型检查；
- 单元测试；
- 模块测试；
- 集成测试；
- 端到端测试；
- 构建和打包；
- 架构边界检查；
- 文档一致性检查；
- 安全和依赖检查；
- 对验收条件的直接验证。

验证原则：

- 验证实际受影响的风险；
- 先运行最小高信号检查，再逐步扩大；
- 每项通过结论都来自实际执行结果；受成本、工具或权限限制的检查记录为 `blocked` 或 `not_covered`；
- 测试失败保持可见，并通过修复根因恢复通过状态；
- 记录执行命令、结果、覆盖范围和未覆盖项。

核心产物：Verification Report 和 Evidence。

Verify Gate：

- Profile 要求的检查已执行；
- 验收条件有对应证据；
- 失败项已修复、阻塞或由用户明确接受；
- 未执行检查及其风险已披露。

### 10.8 Stage 7：Review

**目标**：在发布前检查实现是否符合需求和工程边界。

Review 必须覆盖：

- 需求与验收条件；
- 实际 diff 和修改范围；
- 架构与依赖方向；
- 接口和兼容性；
- 错误处理和安全风险；
- 测试充分性；
- 文档一致性；
- 明显的代码、架构、测试、文档或依赖债务；
- Release 准备情况。

Review 识别并记录技术债。未解决债务进入项目 Issue 系统，或作为下一次 DevelopmentRun 的输入。

核心产物：Review Result。

Review Gate：

- 实际修改与计划之间的差异均有说明；
- 重要风险已处理或明确接受；
- 项目事实源已同步；
- Release 所需信息已准备；
- Agent 重新读取目标后仍能证明任务完成。

### 10.9 Stage 8：Release

**目标**：形成可复现、可追踪、可交付的软件版本。

Release 必须完成：

- 确认验收条件状态；
- 确认代码、配置、测试和文档状态；
- 确认版本号；
- 生成或更新 Changelog / Release Notes；
- 运行当前 Profile 和 Verification Tier 要求的构建与打包；
- 记录制品位置、校验信息或生成方式；
- 关联 Git revision；
- 记录已知限制和未验证风险；
- 生成 Release Manifest。

对外发布、推送标签、创建远端 Release 或上传包属于外部状态变更，需要用户明确授权并通过宿主权限检查。条件满足时 Rung 执行并记录结果；条件待满足时 Release Manifest 记录待执行动作，状态保持 `release ready`。

核心产物：Release Package 和 Release Manifest。

Release Gate：见第 13 节。

### 10.10 返回与恢复

DevelopmentRun 必须支持：

```text
Verify fail  → Implement
Review issue → Design / Plan / Implement
New unknown  → Clarify / Inspect
Blocked      → 保存状态并等待输入
Resume       → 从持久制品恢复
```

工作流以责任完整和状态可恢复为设计目标。

---

## 11. 项目知识与事实源

### 11.1 每个事实只有一个 Source of Truth

Rung 索引项目现有事实源，并把本次 DevelopmentRun 的新增事实写回对应位置。

示例：

| 事实 | 推荐事实源 |
|---|---|
| 产品和开发需求 | Requirements / Development Brief |
| 项目使用和快速开始 | README |
| Coding Agent 项目指令 | 根级或目录级 Agent 指令文件 |
| 架构结构 | Architecture 文档 |
| 长期设计决定 | ADR |
| 接口行为 | API Specification / 类型与测试 |
| 运行和验证命令 | 项目配置、Makefile 或脚本 |
| 本次开发状态 | DevelopmentRun Artifacts |
| 发布状态 | Release Manifest、Changelog、Git revision |

ProjectContext 记录这些事实源的位置和状态，正文由对应事实源维护。

### 11.2 Rung 工作区

项目可以使用 `.rung/` 保存 Rung 管理的控制信息和 DevelopmentRun 制品：

```text
.rung/
├── project.yaml
├── policies/
└── runs/
    └── RUN_ID/
        ├── brief.md
        ├── context.md
        ├── design.md
        ├── plan.md
        ├── verification.md
        ├── review.md
        └── release.yaml
```

约束：

- `.rung/project.yaml` 索引现有事实源；
- Lite 任务保留必要证据，并按实际 Artifact 数量创建文件；
- Standard 和 Strict 默认持久化关键制品；
- 如果项目已有等价工作流和目录，Rung 应适配现有结构；
- `.rung/` 只保存可进入开发制品的信息，敏感信息、密钥和生产凭据留在专用凭据系统；
- 是否提交 DevelopmentRun 制品由项目策略决定。

---

## 12. 验证系统

### 12.1 风险驱动验证

Rung 根据变化范围和风险信号选择 Verification Tier。

选择过程：

```text
Change Scope
    ↓
Risk Signals
    ↓
Verification Tier
    ↓
Commands + Evidence
```

### 12.2 验证等级

| Tier | 目标 | 示例 |
|---|---|---|
| Tier 0 | 快速发现明显错误 | 格式、语法、目标文件检查、最小 smoke test |
| Tier 1 | 证明局部模块行为 | 静态检查、单元测试、模块测试 |
| Tier 2 | 证明跨模块兼容 | 集成测试、契约测试、构建、相关安全检查 |
| Tier 3 | 证明完整发布准备 | 完整测试矩阵、端到端、打包、Release Gate |

Profile 给出最低要求：

- Lite：通常 Tier 0–1；
- Standard：通常 Tier 1–2；
- Strict：通常 Tier 2–3。

实际 Tier 可以因风险上调。

### 12.3 Evidence 最小结构

每项验证证据至少包含：

```yaml
claim: 本项证据支持的结论
command: 实际执行的命令或检查
result: pass | fail | blocked | waived
revision: 对应代码版本
coverage: 已覆盖的行为和范围
not_covered: 未覆盖内容
artifacts: 报告或制品位置
```

命令受工具、权限或环境阻碍时，Rung 使用 `blocked` 或明确的 `not_covered`，并保留恢复验证所需的信息。执行证据由工具的实际输出产生。

---

## 13. Release Contract

### 13.1 Release Package

Release Package 是当前项目类型对应的可交付结果，可以是：

- Python wheel/sdist；
- npm package；
- CLI 可执行文件或安装包；
- 前端静态构建；
- 服务容器镜像和发布清单；
- 桌面或移动应用安装包；
- 库的源码标签、构建产物和发布说明；
- 用户定义的其他可复现制品。

如果项目没有二进制或包制品，Release Package 可以是明确 revision、版本和发布说明组成的源码发布。

### 13.2 Release Manifest

Release Manifest 至少记录：

```yaml
version: 发布版本
revision: Git revision
status: ready | published | blocked
artifacts: 发布制品及其位置
acceptance: 验收条件状态
verification: 验证证据引用
documentation: 已同步文档
known_limitations: 已知限制
unverified_risks: 未验证风险
publish_actions: 已执行或待执行的外部动作
```

### 13.3 Release Gate

只有满足以下条件，Rung 才能称为 Release Ready：

1. 所有必须验收条件已满足；
2. 未满足和被放弃条件已由用户明确接受；
3. 代码、配置、测试和必要文档完整；
4. 所选 Profile 和 Tier 的验证已完成；
5. 构建或打包可复现；
6. 版本、Changelog 或 Release Notes 已同步；
7. 制品与明确 Git revision 对应；
8. 已知限制和未验证风险已披露；
9. Release Ready 由开发和发布契约判定，生产部署使用独立的下游状态；
10. Release Manifest 已生成。

Rung 必须区分：

- `implementation complete`；
- `verification complete`；
- `release ready`；
- `published`。

每个状态具有独立的进入条件和 Evidence。

---

## 14. Rung、Coding Agent Host 与项目工具的职责

### 14.1 用户

用户负责：

- 提供意图、业务约束和必要背景；
- 对重大需求、范围和架构选择做最终决定；
- 批准外部写操作和高风险动作；
- 接受或拒绝被披露的残余风险。

### 14.2 Rung

Rung 负责：

- 选择和编排开发阶段；
- 判断 Profile 和风险信号；
- 要求必要 Artifact 和 Gate；
- 加载相关参考；
- 调用确定性脚本；
- 追踪验收、验证和 Release 状态；
- 在证据不足时维持 `fail`、`blocked` 或未完成状态。

### 14.3 Coding Agent Host

Coding Agent Host 负责：

- 理解自然语言和代码；
- 访问文件系统和开发工具；
- 执行修改和命令；
- 管理权限、审批和沙箱；
- 在需要时调度其他 Agent；
- 将执行结果返回给 Rung 工作流。

### 14.4 项目工具

Git、编译器、测试框架、Linter、构建系统和包管理器负责实际执行并产生原始结果。Rung 读取配置、调用命令，并把结果关联到 DevelopmentRun Evidence。

---

## 15. 核心设计原则

### 原则 1：先澄清与检查，再进入代码

任何 DevelopmentRun 都必须先完成足够的 Clarify 和 Inspect。

### 原则 2：项目事实优先于通用最佳实践

Rung 必须先读取项目已有规则、架构和工具，再决定如何行动。

### 原则 3：制品深度与风险相称

Profile 和风险共同决定 Artifact 的形式、数量和持久化深度。

### 原则 4：约束和边界先行

在设计和计划中先记录保持不变的约束、允许变化的边界和预期新增行为。

### 原则 5：确定性规则必须工具化

路径、命令、格式、测试、构建和可机器检查的架构规则应优先由脚本或现有工具验证。

### 原则 6：完成声明由证据支持

测试通过来自实际测试结果，构建可发布来自实际构建结果，风险结论来自对应检查与覆盖记录。

### 原则 7：风险决定验证范围

验证强度应由变化范围、接口、数据、安全和项目成熟度决定。

### 原则 8：叠加式适配现有项目

Rung 在现有代码、规则、事实源和用户修改上叠加工作，并保持任务范围外内容的原有状态。

### 原则 9：Release 是明确边界

Rung 在 Release Gate 交付可发布版本，交付系统从 Release Manifest 接续执行。

### 原则 10：持久状态支持恢复

长任务通过持久 Artifact 保存关键状态，并支持从中断点恢复。

---

## 16. 安全与外部动作

Rung 必须遵守以下规则：

- 数据访问范围限于当前任务；
- 凭据、密钥和生产数据保留在专用凭据或数据系统中；
- 宿主 Agent 已授予的权限构成 Rung 的权限上限；
- 提交、推送、发布和外部消息需要用户授权；
- 生产部署和生产数据变更进入对应的下游执行与审批流程；
- 对删除、覆盖、迁移和不可逆操作要求明确目标和验证；
- 先解析精确目标，再执行具有破坏性的命令；
- 被权限或审批阻止的动作记录为 `blocked`。

宿主平台、安全策略和用户权限对所有 Rung 指令生效。

---

## 17. MVP 范围

### 17.1 MVP 必须包含

- 一个可显式调用和按描述触发的 Rung Skill；
- Clarify 到 Release 的八阶段工作流；
- Lite、Standard、Strict 三种 Profile；
- Greenfield、Feature、Bugfix、Refactor、Migration 五类验收场景；
- Development Brief、Project Context、Solution Design、Change Plan、Verification Report、Review Result、Release Manifest 模板；
- 项目检查、验证执行和 Release Gate 的最小确定性脚本；
- 可暂停和恢复的 DevelopmentRun 状态；
- 对现有项目事实源的索引能力；
- 清晰的 Evidence 和未验证风险报告。

### 17.2 MVP 实现边界

| 领域 | MVP 方案 |
|---|---|
| 产品入口 | 单一 Rung Skill |
| 执行环境 | 用户现有的 Coding Agent Host |
| 状态存储 | 项目文件与可选 `.rung/` 工作区 |
| 交互方式 | 自然语言、结构化 Artifact 和 Gate 结果 |
| 确定性执行 | 本地脚本与项目现有工具链 |
| 权限与审批 | 宿主权限模型和用户确认 |
| 外部发布 | 通过宿主能力连接包仓库和代码托管平台 |
| Release 交接 | 代码托管、包仓库或交付流水线消费 Release Manifest |
| 语言与框架 | 通用工作流加项目发现，按验收场景逐步补充适配 |

### 17.3 实现顺序

```text
1. 固化产品规格与 Stage Contract
2. 建立单一 Rung Skill 骨架
3. 实现 Profile 与 Artifact 模板
4. 实现最小确定性脚本
5. 跑通五类验收场景
6. 根据真实失败补规则和脚本
7. 再决定是否需要 Plugin、CLI 或更多宿主适配
```

Skill 是第一产品形态。完成五类验收场景后，再根据安装、分发和确定性执行中的真实问题评估 CLI、Plugin 或服务形态。

---

## 18. 验收场景

### 18.1 Greenfield

输入：用户提供一个新软件想法和基本约束。

Rung 应能够：

- 澄清目标、非目标和验收条件；
- 选择最小技术和架构方案；
- 创建可运行、可测试的项目骨架；
- 业务逻辑限于已确认的目标和验收条件；
- 完成实现、验证、文档和首个 Release Package。

### 18.2 Feature

输入：为已有项目增加普通功能。

Rung 应能够：

- 定位相关模块和约束；
- 识别接口、数据和测试影响；
- 形成计划并控制修改范围；
- 实现功能和测试；
- 证明验收条件满足；
- 更新文档和 Release 信息。

### 18.3 Bugfix

输入：已有行为不符合预期。

Rung 应能够：

- 明确预期与实际行为；
- 在修改前获得复现或等价证据；
- 通过根因分析确定修复位置；
- 增加能防止复发的测试；
- 执行相关回归验证；
- 以 Lite 或 Standard 完成发布准备。

### 18.4 Refactor

输入：改善内部结构，并保持预期外部行为。

Rung 应能够：

- 明确行为保持边界；
- 把重构与新功能分离；
- 使用现有测试或补充特征测试；
- 控制抽象和范围；
- 证明外部行为没有非预期变化；
- 记录结构收益和残余风险。

### 18.5 Migration

输入：执行接口、数据、依赖或架构迁移。

Rung 应能够：

- 描述当前状态和目标状态；
- 识别兼容窗口、顺序和消费者影响；
- 制定迁移和必要回退方案；
- 使用 Strict Profile；
- 执行集成和发布级验证；
- 在 Release Manifest 中记录兼容性和未完成事项。

### 18.6 场景通过标准

所有场景都必须满足：

- 使用同一组核心概念；
- 通过 Profile 调整同一工作流的执行深度；
- 关键状态采用跨模型可读的结构化 Artifact；
- 在 Verified Release Package 处完成 DevelopmentRun；
- 能够恢复中断的 DevelopmentRun；
- 最终产生实际 Evidence 和 Release 状态。

---

## 19. 产品不变量

以下产品不变量在 Rung 后续实现中必须保持：

1. Rung 始终是从 Intent 到 Release 的开发 Skill；
2. Rung 的输出边界是通过 Release Gate 的 Verified Release Package，接收系统依据 Release Manifest 继续交付；
3. Rung 负责编排，Coding Agent Host 和项目工具负责执行；
4. Clarify 与 Inspect Gate 通过后进入代码实现；
5. Rung 的流程深度必须风险自适应；
6. 可以确定性检查的规则通过脚本或项目工具执行；
7. 未验证内容必须显式披露；
8. Release 必须有制品、revision、验证和已知风险；
9. Rung 索引并更新项目现有事实源；
10. Rung 必须支持长任务暂停、恢复和证据追踪。

---

## 20. 长期愿景

未来的软件开发交互可以是：

```text
Human
  │
  │ 定义目标、约束和关键决策
  ▼
Rung
  │
  │ 编排完整、风险自适应的开发流程
  ▼
Coding Agent Host
  │
  │ 使用项目工具执行具体开发
  ▼
Verified Release Package
```

Rung 让 AI 对一个软件版本的完整开发结果负责：

> 需求明确、设计合理、计划可执行、实现受约束、验证有证据、文档已同步、版本可发布。
