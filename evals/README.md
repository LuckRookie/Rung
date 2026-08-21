# Rung 行为评测

本目录评估 Rung 是否改变 Coding Agent 的实际开发行为。评测关注正确性、治理触发、代码结构、后续修改成本和上下文开销，不检查回答是否复述了 Rung 的术语。

## 对照组

每个场景使用相同的模型、宿主、工具权限、起始仓库和用户提示运行：

1. **Host baseline**：不加载 Rung；
2. **Control Rung**：使用本次实验声明的稳定 revision；
3. **Candidate Rung**：使用待评估 revision。

每组运行多次，记录随机性相关设置。Control 和 Candidate 必须记录精确 Git revision，避免用可移动分支名称代表版本。

## 执行协议

1. 将场景起始仓库复制到独立临时目录。
2. 只把场景中的 `Initial prompt` 交给被测 Agent；隐藏后续任务和评审预期。
3. 保存 Agent 可见的 Skill 候选、Rung 是否被隐式或显式调用、读取的 References、工具调用、最终回复、工作区 diff、提交状态和实际检查结果。
4. 初始任务完成后，再发送 `Hidden follow-up`。使用同一个工作区和对话，除非场景明确测试跨会话恢复。
5. 先执行场景的正确性检查。未满足用户行为时记录失败，结构评分不能抵消正确性失败。
6. 对通过正确性检查的结果进行盲化成对评审。评审者不查看实验组名称和 Agent 的架构自述。
7. 跨 Session 或 Worker 场景记录 Primary Agent、Session 边界、Task Packet、集成点和最终验证 revision；Host 不支持对应能力时明确记录降级执行形态。

## 观察维度

| 维度 | 观察内容 |
|---|---|
| Invocation precision | 主要验收对象与代码项目存在正向关系时是否进入 Rung，关系缺失时是否保持在 Host 或对应工作流 |
| Scope recovery | 宿主偶发误触时，Scope Gate 是否在读取 Reference 或创建 Artifact 前结束 Rung 路由 |
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
| Test design | 测试是否保护行为、契约、不变量和失败路径 |
| Harness economy | 验证入口是否复用项目能力，Fixture 与环境是否有归属，隔离、清理、诊断、成本和淘汰条件是否清楚 |
| Harness evolution | 是否识别权威事实、产品与 Harness 问题，使用独立锚点，记录 Coverage Delta、生效、回退和旧路径清理 |
| Context cost | 加载字节或 tokens、工具调用、耗时、额外文档和沟通成本 |
| Solution diversity | 多次运行能否保留多个正确且可维护的方案 |

文件数、类数、行数和修改模块数作为证据记录，不设置通用阈值。评审说明具体知识传播、依赖或后续变化成本。

显式架构评估不按 Finding 数量得分。评测使用带有已知主因、干扰性代码异味和有意设计约束的 Fixture，分别观察主因命中、症状误判、反证处理和过度改造。Finding 至少关联驱动或变化场景、仓库证据、结构机制、实际成本或风险、修改方向和验证方式；缺少其中一项时记录相应不确定性。

具有 Hidden follow-up 的架构场景同时检查建议的反事实价值：后续合理变化是否进入更清楚的 Owner、减少无关传播并保留原有行为。无问题或非常规但有依据的 Fixture 用于测量 False architecture finding 和 Harmful redesign，防止候选提示通过增加评论数量虚增覆盖。

Project Model 场景检查 Agent 能否把稀疏用户表达和项目现实合成为可修正的语义模型。评分关注模型是否帮助判断一个能力自然属于当前中心、构成相邻扩展，或需要用户确认产品身份变化；篇幅、术语数量和图表数量不产生分数。

画像中的陈述分别记录为用户确认、仓库证据、推断、冲突或未知。现有代码和文档只提供证据，不自动成为产品意图。Hidden follow-up 检查画像能否预测实际 Owner、边界、UX 与变化传播；用户明确扩展产品方向时，能够修正画像也是成功行为。

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
  mode: implicit | explicit | none
  scope: codebase | outside | mixed | uncertain
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
context_cost: {}
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
review:
  assessment_boundary: []
  primary_tensions: []
  unsupported_findings: []
  counterevidence: []
  intervention_validation: []
```

原始产物与评审记录放在实验输出目录，不进入可安装的 `rung/` 包。场景内容进入被测 Agent 上下文时，只传递明确标注的用户提示和起始仓库。
