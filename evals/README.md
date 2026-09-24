# Rung 行为评测

本目录评估 Rung 是否改变 Coding Agent 的实际开发行为。评测关注正确性、治理触发、代码结构、后续修改成本和上下文开销，不检查回答是否复述了 Rung 的术语。

## 对照组

每个场景使用相同的模型、宿主、工具权限、起始仓库和用户提示运行：

1. **Host baseline**：不加载 Rung；
2. **Control Rung**：使用本次实验声明的稳定 revision；
3. **Candidate Rung**：使用待评估 revision。

每组运行多次，记录随机性相关设置。Control 和 Candidate 必须记录精确 Git revision，避免用可移动分支名称代表版本。

## 范围与启用

开发 Scope 和治理 Activation 分别评测。候选的隐式调用只因实质工程决定进入；显式调用可用于小任务，但仍须具备开发范围。`activation-cases.json` 提供提示、人工标注的宿主判断和预期结果。确定性测试只证明给定判断的分类逻辑，不能证明模型能从提示正确判断。

对真实 Agent，先只展示提示和可发现 metadata，隐藏判断与预期。分别记录是否选中 Skill、是否读取入口、实际 Reference Trace 与 `enter | bypass | defer`；明确区分未选中、误触后退出和主动治理。未知情形继续最小 Host 检查，事实改变后重新判断。隐式简单任务的目标是零 Reference、零治理 Artifact；显式小任务可使用 Lite。项目大小、公共调用者、普通测试和交接要求都不单独触发。

历史场景的开发范围判断不等于自动启用；以当前 Scope + Activation 定义更新预期，不改变 fixture 的正确性要求。

Case 15 将理解型首轮、后续实施请求和独立的当前决策变体分别评分。隐藏后续需求不进入首轮判断。普通测试新增与共享 Harness 变化也使用独立对照，覆盖增加本身不算治理升级信号。

## 可重建的内容边界 fixture

[`fixtures/content-review/`](fixtures/content-review/README.md) 提供项目现状与后续决定、既有测试维护、部分发布失败三个小型 fixture 及隔离执行协议。被测 Agent 只接收其中的用户提示、项目副本和对应版本的 Skill，不读取评测预期。Fixture 代码和原始数据可复用；它们尚未覆盖全部场景。

静态契约和给定标注的分类检查分别证明结构与映射。单次候选前向检查提供有限行为证据；只有在相同输入下进行多次 baseline/control/candidate 比较、保留真实读取与结果记录后，才能形成更广的质量或上下文收益结论。

## 执行协议

1. 将场景起始仓库复制到独立临时目录。
2. 只把场景中的 `Initial prompt` 交给被测 Agent；隐藏后续任务和评审预期。
3. 保存 Agent 可见的 Skill 候选、Rung 是否被隐式或显式调用、代码库关系与活跃开发 Claim 的 Scope Gate 结果、读取的 References、工具调用、最终回复、工作区 diff、提交状态和实际检查结果。
4. 初始任务完成后，再发送 `Hidden follow-up`。使用同一个工作区和对话，除非场景明确测试跨会话恢复。
5. 先执行场景的正确性检查。未满足用户行为时记录失败，结构评分不能抵消正确性失败。
6. 对通过正确性检查的结果进行盲化成对评审。评审者不查看实验组名称和 Agent 的架构自述。
7. 跨 Session 或 Worker 场景记录 Primary Agent、Session 边界、Task Packet、集成点和最终验证 revision；Host 不支持对应能力时明确记录降级执行形态。

## 观察维度

| 维度 | 观察内容 |
|---|---|
| Invocation precision | 持久项目修改、指导具体修改的决定或当前 Release Claim 是否进入 Rung；只有代码库关系且结果止于当前事实理解时是否保持在 Host |
| Scope recovery | 宿主偶发误触时，理解型或范围外结果是否在读取 Reference 或创建 Artifact 前结束 Rung 路由 |
| Operational separation | 混合任务是否分别维护项目制品与环境执行的责任、授权、证据和恢复信息 |
| Routing relevance | 相关信号是否加载了有用提醒；普通任务是否保持安静 |
| Execution ownership | 是否始终有一个 Primary Agent 持有全局 Plan、集成结果、Finding 处理与 Handoff |
| Inspection proportionality | 检查是否从安全所需的最小半径开始，并只按影响证据扩展 |
| Persistence economy | Design、Plan 与恢复状态是否进入确实有未来消费者的承载位置 |
| Semantic fidelity | Project Model 是否准确表达当前用户、核心情境、结果、概念、不变量和产品形态 |
| Epistemic calibration | 用户确认、仓库证据、推断、冲突和未知项是否保持可区分、可修正 |
| Fit judgment | 新能力是否被有依据地判断为核心归属、相邻扩展或产品身份变化 |
| Model utility | 画像是否真实改善 Owner、边界、命名、依赖、UX、验证或后续变化局部性 |
| Model economy | 画像是否只在语义信号出现时建立，并进入确有消费者的承载位置 |
| Exploration precision | Design Exploration 是否只在活跃重要决定仍存在多条实质不同路径时加载；清楚局部变化是否沿普通路径继续 |
| Scenario discrimination | 代表性场景是否以最少数量揭示会改变方向的行为、状态、失败、恢复或生命周期差异 |
| Responsibility discovery | 探索是否在模块设计前发现真实 Owner、契约、状态、失败语义、恢复责任和证据需要 |
| Convergence quality | 候选方向是否具有不同工程后果，是否在足够证据出现后停止，并控制过早收敛与无界发散 |
| Delegation quality | Worker 是否具有有界上下文、明确所有权、稳定契约和可检查 Handoff |
| Recovery fidelity | 接续 Session 是否校准指令、revision、用户工作、已完成单元、Evidence 与下一动作 |
| Integrated verification | 完成声明是否针对组合后的实际状态，Worker 局部结果是否只作为候选 Evidence |
| Ownership | 变化是否进入具有清楚概念职责的位置 |
| Change locality | 后续变化是否集中在对应概念范围，是否传播到无关模块 |
| Knowledge containment | 公共表面、外部 SDK、存储格式、共享状态和隐式行为的传播 |
| Dependency direction | 新依赖能否由当前业务或边界关系解释，是否形成反向或循环知识 |
| Abstraction economy | 新模块、接口、层、选项和扩展点是否有当前证据 |
| Driver alignment | 结构判断是否对应当前业务目标、质量属性或可信变化场景 |
| Causal diagnosis | Finding 是否从代码症状追到造成成本或风险的结构机制 |
| Finding precision | 结论是否由仓库事实支持，是否控制无依据架构问题和模式驱动误判 |
| Intervention value | 建议是否以相称风险降低原机制，并提供可验证的未来变化收益 |
| Touched-area quality | 修改是否让 touched ownership boundary 在当前正确性、职责、命名、流、错误、资源、测试与事实源上保持连贯，同时控制无关 Cleanup |
| Understandability | 维护者能否在有界上下文中恢复目的、Owner、控制与数据流、状态、副作用和失败含义 |
| Current changeability | 可信后续变化是否进入清楚 Owner，并减少无关知识、文件和模块传播 |
| Operability | Release 前相关失败、Timeout、Retry、Cancellation、Concurrency、Recovery、Cleanup、诊断和资源行为是否清楚且可验证 |
| Consistency and predictability | 同类行为、代码、测试、配置、错误与事实是否遵循项目有依据的共同方式 |
| Debt qualification | 当前承载状态、可信 Trigger 或 Exposure、未来负担机制与管理决定是否形成完整因果链 |
| Debt pressure | Interest、Exposure、Propagation、Option Loss 与 Principal 是否以证据支持的粒度进入判断 |
| Debt strategy | Repay、Reduce、Contain、Carry、Replace 或 Retire 是否匹配当前压力、偿还风险、Borrowed Value 与机会成本 |
| Debt-system prioritization | 系统审查是否识别驱动项目 Chaos 的主要交互机制，并控制容易计数但低影响的清理项 |
| False debt finding | 年龄、异味、TODO、复杂度和工具分数是否在缺少可信未来负担时保持为 Signal 或 Hypothesis |
| Retirement evidence | 偿还后当前 Claim、激活 Scenario、传播停止、旧路径清理和负担转移是否得到验证 |
| Test design | 测试是否保护行为、契约、不变量和失败路径 |
| Harness economy | 验证入口是否复用项目能力，Fixture 与环境是否有归属，隔离、清理、诊断、成本和淘汰条件是否清楚 |
| Harness evolution | 是否识别权威事实、产品与 Harness 问题，使用独立锚点，记录 Coverage Delta、生效、回退和旧路径清理 |
| Context cost | 加载字节或 tokens、工具调用、耗时、额外文档和沟通成本 |
| Solution diversity | 多次运行能否保留多个正确且可维护的方案 |

文件数、类数、行数和修改模块数作为证据记录，不设置通用阈值。评审说明具体知识传播、依赖或后续变化成本。

显式架构评估不按 Finding 数量得分。评测使用带有已知主因、干扰性代码异味和有意设计约束的 Fixture，分别观察主因命中、症状误判、反证处理和过度改造。Finding 至少关联驱动或变化场景、仓库证据、结构机制、实际成本或风险、修改方向和验证方式；缺少其中一项时记录相应不确定性。

具有 Hidden follow-up 的架构场景同时检查建议的反事实价值：后续合理变化是否进入更清楚的 Owner、减少无关传播并保留原有行为。无问题或非常规但有依据的 Fixture 用于测量 False architecture finding 和 Harmful redesign，防止候选提示通过增加评论数量虚增覆盖。

Software Quality 场景根据当前用户、维护者、环境、Project Model 和接受方向判断适用性。评测先检查 Correctness，再观察 touched owner 的 Understandability、Changeability、Verifiability、Operability、Consistency 与 Predictability；条件质量属性只在场景证据使其相关时进入。全仓库扫描、统一分数、额外文件与广泛 Cleanup 不产生收益分数。

Technical Debt 场景将当前质量与未来负担分别记录。Qualified Debt Item 需要 Current Construct、可信 Trigger 或 Exposure、Interest、Propagation、Risk、Coordination 或 Option Loss 机制，以及 Carry、Contain、Reduce、Repay、Replace 或 Retire 决定。Defect、Vulnerability、Risk、Feature Gap 和 Necessary Complexity 保留各自分类；债务标签不能提高清理项分数或降低当前问题严重度。

`35-lifecycle-guidance-smoke.md` 检查当前变化所需的生命周期决定是否有责任与证据；关注面允许组合、跳过和回访，无八步执行或文案匹配要求。

`36-autonomous-quality-loop.md` 检查简短默认指导是否改善错误语义、验证与隐藏后续变化，不要求 Change Contract、质量 Guide 或内部思考自述。`37-activation-and-context-economy.md` 专门测量隐式/显式触发、误触退出与上下文成本。`38-claim-handoff-and-evidence-identity.md` 检查决策型任务能否在相称 Handoff 结束，以及后续实施与 Release 是否识别 Evidence 之后的 working-tree 漂移。

显式 Debt System 场景记录债务间传播、共同根因、交付能力消耗、Owner 缺失和过期清理条件。评审比较主要机制命中、False debt finding、干预杠杆、当前行为保护与 Hidden follow-up 的 Interest 变化，不设置统一债务分数、数量目标或零债务标准。

Project Model 场景检查 Agent 能否把稀疏用户表达和项目现实合成为可修正的语义模型。评分关注模型是否帮助判断一个能力自然属于当前中心、构成相邻扩展，或需要用户确认产品身份变化；篇幅、术语数量和图表数量不产生分数。

画像中的陈述分别记录为用户确认、仓库证据、推断、冲突或未知。现有代码和文档只提供证据，不自动成为产品意图。Hidden follow-up 检查画像能否预测实际 Owner、边界、UX 与变化传播；用户明确扩展产品方向时，能够修正画像也是成功行为。

Design Exploration 场景使用一个高不确定性设计和一个方向清楚的局部变化进行对照。评测记录 Premature convergence、遗漏职责与状态、失败与恢复语义、无依据抽象、用户问题负担、候选方向的实质差异、停止时点、Hidden follow-up 修改局部性和上下文成本。方案数、场景数、文档篇幅与图表数量不产生分数。

开发意图场景分别观察 metadata 选择和 Skill 已加载后的 Scope Gate。运行时只保留抽象的双条件成员定义；代码库事实理解的具体表面变化放在独立 Case 中，防止候选提示通过记忆排除词取得虚假精度。

## 结果记录

每次运行至少保存：

```yaml
case: <case-id>
variant: host-baseline | control-rung | candidate-rung
model: <model-and-settings>
host: <host-version>
permissions: <tool-and-network-scope>
fixture_revision: <revision-or-content-hash>
rung_revision: <revision-or-none>
invocation:
  selected: <true-or-false>
  entrypoint_read: <true-or-false>
  mode: implicit | explicit | none
  scope: development | understanding-only | outside | mixed | uncertain
  activation: enter | bypass | defer
  materiality: present | absent | uncertain
  codebase_relationship: present | absent | mixed | uncertain
  development_claim: present | absent | mixed | uncertain
  exited_before_references: <true-or-false-or-not-applicable>
loaded_references: []
execution:
  primary_agent: <logical-owner-id-or-description>
  sessions: []
  inspection_radius: []
  persistence: []
  workers: []
  reviewer: <none-or-description>
  integrated_state: <revision-or-working-tree-identity>
correctness: pass | fail | blocked
checks: []
context_cost: {} # separate metadata, entrypoint, unique and repeated reference bytes
diff_summary: {}
project_model:
  boundary: []
  accepted: []
  evidenced: []
  inferred: []
  conflicts: []
  unknowns: []
  fit_decisions: []
  persistence: <none-or-location>
design_exploration:
  decision: <none-or-current-decision>
  scenarios: []
  discovered_responsibilities: []
  discovered_states: []
  failure_semantics: []
  candidate_directions: []
  owned_unknowns: []
  revisit_signals: []
  persistence: <none-or-location>
software_quality:
  active_goals: []
  touched_boundary: []
  current_findings: []
  tradeoffs: []
  operability: []
  evidence: []
technical_debt:
  signals: []
  hypotheses: []
  qualified_items: []
  dominant_mechanisms: []
  strategies: []
  persistence: []
  retirement_evidence: []
  false_findings: []
review:
  assessment_boundary: []
  primary_tensions: []
  unsupported_findings: []
  counterevidence: []
  intervention_validation: []
```

原始产物与评审记录放在实验输出目录，不进入可安装的 `rung/` 包。场景内容进入被测 Agent 上下文时，只传递明确标注的用户提示和起始仓库。
