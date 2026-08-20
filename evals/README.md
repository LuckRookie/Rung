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
3. 保存 Agent 可见上下文、读取的 Rung References、工具调用、最终回复、工作区 diff、提交状态和实际检查结果。
4. 初始任务完成后，再发送 `Hidden follow-up`。使用同一个工作区和对话，除非场景明确测试跨会话恢复。
5. 先执行场景的正确性检查。未满足用户行为时记录失败，结构评分不能抵消正确性失败。
6. 对通过正确性检查的结果进行盲化成对评审。评审者不查看实验组名称和 Agent 的架构自述。
7. 跨 Session 或 Worker 场景记录 Primary Agent、Session 边界、Task Packet、集成点和最终验证 revision；Host 不支持对应能力时明确记录降级执行形态。

## 观察维度

| 维度 | 观察内容 |
|---|---|
| Routing relevance | 相关信号是否加载了有用提醒；普通任务是否保持安静 |
| Execution ownership | 是否始终有一个 Primary Agent 持有全局 Plan、集成结果、Finding 处理与 Handoff |
| Inspection proportionality | 检查是否从安全所需的最小半径开始，并只按影响证据扩展 |
| Persistence economy | Design、Plan 与恢复状态是否进入确实有未来消费者的承载位置 |
| Delegation quality | Worker 是否具有有界上下文、明确所有权、稳定契约和可检查 Handoff |
| Recovery fidelity | 接续 Session 是否校准指令、revision、用户工作、已完成单元、Evidence 与下一动作 |
| Integrated verification | 完成声明是否针对组合后的实际状态，Worker 局部结果是否只作为候选 Evidence |
| Ownership | 变化是否进入具有清楚概念职责的位置 |
| Change locality | 后续变化是否集中在对应概念范围，是否传播到无关模块 |
| Knowledge containment | 公共表面、外部 SDK、存储格式、共享状态和隐式行为的传播 |
| Dependency direction | 新依赖能否由当前业务或边界关系解释，是否形成反向或循环知识 |
| Abstraction economy | 新模块、接口、层、选项和扩展点是否有当前证据 |
| Test design | 测试是否保护行为、契约、不变量和失败路径 |
| Harness economy | 验证入口是否复用项目能力，Fixture 与环境是否有归属，隔离、清理、诊断、成本和淘汰条件是否清楚 |
| Harness evolution | 是否识别权威事实、产品与 Harness 问题，使用独立锚点，记录 Coverage Delta、生效、回退和旧路径清理 |
| Context cost | 加载字节或 tokens、工具调用、耗时、额外文档和沟通成本 |
| Solution diversity | 多次运行能否保留多个正确且可维护的方案 |

文件数、类数、行数和修改模块数作为证据记录，不设置通用阈值。评审说明具体知识传播、依赖或后续变化成本。

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
review: {}
```

原始产物与评审记录放在实验输出目录，不进入可安装的 `rung/` 包。场景内容进入被测 Agent 上下文时，只传递明确标注的用户提示和起始仓库。
