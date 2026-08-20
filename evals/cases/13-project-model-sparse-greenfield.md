# Case 13: Sparse greenfield intent becomes a useful project model

## Purpose

Test whether the Agent turns a sparse human description into a small, correctable Project Model before consequential product and architecture choices, while keeping user interaction easy to judge.

## Fixture

Start from an empty Git repository. The user wants a food-recording application but has not selected whether its center is personal meal history, household inventory, or recipe planning. Provide the same available runtime, filesystem permissions, and network policy to every variant. No framework or interface is prescribed.

## Initial prompt

```text
我想做一个记录食物的小应用。你先帮我把这个项目想清楚，我不懂那些专业术语；不影响产品含义的设计你可以自己决定。
```

## Hidden follow-up

After the Agent has established or calibrated a model, provide the selected direction that the primary user wants to record meals quickly and review personal eating history, then ask:

```text
按照我们确定的方向，做出最小可运行版本。接着增加“家里还有多少食材”的库存管理，你判断应该怎么处理，并说明这个决定怎样影响项目结构。
```

## Acceptable routing range

- Clarify and Project Model are relevant to product meaning, delegated design scope, plain-language calibration, and fit judgment.
- Inspect is limited to the empty repository, available tools, and user work. Broad technical discovery has no value before the product direction is known.
- Design becomes relevant after the model supports a runnable slice.
- Persistent Project Model, Plan, Worker, and independent Reviewer remain optional unless coordination or future reuse creates a consumer.

## Correctness gate

- The Agent identifies the materially different meal-history, inventory, and recipe-planning interpretations without pretending the initial sentence selects one.
- The user receives a concise, concrete decision view and is not required to understand product or architecture terminology.
- Delegated choices account for the human task flow and record assumptions that affect the result.
- The first implementation follows the accepted meal-history direction and is runnable and verified.
- Household inventory is treated as an adjacent capability or identity-expanding direction whose cost and ownership are made visible; it is not silently mixed into the meal-history model.

## Model quality gate

- The model states people, core situation, observable outcome, central capability, semantic concepts, and important unknowns proportionally.
- User-confirmed facts remain distinguishable from Agent inference.
- The implementation's main flow, names, data, and module ownership correspond to the accepted model.
- No generic platform, plugin architecture, exhaustive ontology, or default Project Model document appears without a current consumer.

## Observations

Record questions asked, decision readability, delegated scope, candidate models, evidence labels, Project Model size and home, time before implementation, architecture choices, inventory fit judgment, files and concepts added, verification evidence, extra artifacts, and context cost.
