# Case 36: Autonomous quality loop

## Purpose

Test whether the minimal entry guidance improves failure semantics and follow-up ownership without a default quality guide or required worksheet.

## Fixture

Use a small Python project with one public function that parses a user supplied value and writes a result. It has a focused test and one documented command. The parser currently accepts valid values but leaks a raw library exception for invalid input. Keep the fixture behavior and file format stable.

## Initial prompt

```text
修复这个项目的输入解析问题：无效输入应返回稳定、可理解的用户错误，同时保持有效输入和现有输出格式不变。请完成实现、测试和交接。
```

## Hidden follow-up

```text
再增加一个 JSON 输入来源，复用同一套校验和错误语义；命令行来源的行为保持兼容。
```

## Correctness gate

- The Agent preserves valid behavior and output format.
- Invalid input produces the stable project-level error and keeps diagnostic cause available to the operator.
- Tests cover one known-good and one known-bad public behavior.
- The follow-up change has one clear owner for validation and does not duplicate policy across input adapters.
- The final report links claims to checks and names uncovered scope.

## Observations

Record observable owner and boundary decisions, preserved behavior, failure checks, follow-up propagation, loaded references and bytes, evidence, and context cost. Do not require an internal reasoning trace, a Change Contract document, a fixed sequence, or a simulated future feature in the initial diff. Judge implicit activation from whether the error contract needs a material decision; evaluate explicit invocation separately.
