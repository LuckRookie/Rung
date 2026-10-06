# 安装 Rung

本文件维护安装坐标和执行规则，供开发者和 Coding Agent 共同读取。确定 ref 后，使用该 ref 自带的 `INSTALL.md` 和完整包内容作为安装与验收依据；开发分支新增的文件要求只适用于包含这些文件的版本。

## 包坐标

```yaml
contract_version: 1
package:
  name: rung
  repository: https://github.com/LuckRookie/Rung.git
  ref: v0.1.0
  skill_path: rung
  entrypoint: rung/SKILL.md
```

安装单元是所选 ref 中的整个 `rung/` 目录，文件集合和相对路径保持不变。稳定版 `v0.1.0` 不包含 `contracts/` 与 `validate_contract.py`；候选开发线包含它们，分别按对应版本验收。

## 标准安装

[skills](https://github.com/vercel-labs/skills) CLI 能够扫描仓库中的 `SKILL.md`、读取 Skill 名称、选择目标 Agent 与作用域，并安装完整目录。

安装稳定版本 v0.1.0：

```bash
npx skills add https://github.com/LuckRookie/Rung/tree/v0.1.0/rung
```

Codex 用户级安装：

```bash
npx skills add https://github.com/LuckRookie/Rung/tree/v0.1.0/rung --skill rung --agent codex --global --yes
```

Codex 项目级安装；在目标项目根目录执行：

```bash
npx skills add https://github.com/LuckRookie/Rung/tree/v0.1.0/rung --skill rung --agent codex --yes
```

项目级安装目录为 `<project>/.agents/skills/rung`。用户级目录由安装器和宿主版本决定，安装完成时以安装器报告的路径为准。

`skills` CLI 会在安装记录中保存来源、Skill 路径和内容哈希。项目级安装还会在项目根目录生成或更新 `skills-lock.json`，供后续检查与更新使用。

### 发现范围与调用

用户级安装使 Rung 对该用户的不同项目和普通工作目录可见，适合希望在各项目中自动获得开发治理的用户。项目级安装只在对应项目的 Skill 扫描范围内可见，适合希望按仓库选择治理能力的团队。

候选开发线保留隐式调用，通过 `SKILL.md` 的 name 与 description 描述软件开发 Harness 能力；`agents/openai.yaml` 的 short_description 用于 UI 展示。完整入口加载后核对开发范围和启用条件；简单隐式修改或只读理解由 Host 继续处理，影响未知时先执行最小范围的项目检查。显式要求 `$rung` 或开发治理可用于范围内的小任务，适用项目指令中的明确要求同样有效；显式调用不豁免开发范围。详细边界以 [Rung.md §4.1](Rung.md#41-开始边界user-intent) 为准。

安装范围只影响可发现性，不强制每次任务加载。没有启动脚本。稳定 tag 与本地候选包的触发规则可能不同；修改仓库不会自动更新已安装副本，安装后记录实际来源与内容标识。

### 项目采用（候选开发线）

项目可在宿主实际读取的既有指令文件中声明采用 Rung，例如 `AGENTS.md` 或 `CLAUDE.md`。先核对现有规则和入口，合并所需引用；无需统一新建 `HARNESS.md`，也不复制已有命令、契约和计划状态。例如：

```text
本项目的软件修改、实施计划与变更评审使用 Rung。
项目事实源、检查命令和交付约束沿用本文列出的维护位置。
Rung 与现有规则出现差异时，先识别有效范围和依据；在授权范围内逐步修订，并保持同一事项的规则一致。
```

该示例是其范围内持续有效的明确使用要求；在每个适用任务中按显式调用解释，简单任务仍可采用简短执行方式。仅介绍 Rung、引用示例或列出安装位置属于信息性引用，不改变启用条件。项目也可以明确将使用范围限定为架构决定、迁移或复杂计划。持续要求不因换会话失效，也不自动扩大到未声明的任务或授权。

用户也可以明确指定 Rung 为 Harness 改造的目标规范，例如：

```text
以 Rung 的计划拆分与执行建议为目标，改造本项目的计划规范和相关 Agent 指令。
范围内与目标冲突的旧要求应予替换，同步更新引用与检查，完成验证并清理旧规则。
```

这种要求授权 Agent 在指定范围内落实选定建议，即使旧机制仍可运行；无需再次确认是否替换冲突约定。单纯采用 Rung 与按其建议改造 Harness 的授权范围不同，具体处理见下述融合原则。

接入后通过一个实际任务核对宿主是否读取项目入口、是否按声明范围加载 Rung，以及是否继续使用正确的项目检查。现有使用要求已经明确时，不重复请求批准。升级沿用安装记录和项目规则，避免覆盖本地维护内容；既有 Harness 的融合原则见 [Project Harness](rung/references/project-harness.md)。

## Codex 原生安装器

Codex 提供 `skill-installer` 时，可以把下面这句话直接发送给 Codex：

```text
使用 $skill-installer 安装这个 Skill：
https://github.com/LuckRookie/Rung/tree/v0.1.0/rung
```

原生安装器负责选择其支持的用户级 Skills 目录。安装完成后保留安装器返回的目录，不迁移到另一个约定目录。

## Coding Agent 执行协议

用户要求 Coding Agent 读取本文件并安装 Rung 时，Agent 按以下契约执行。

### 1. 确定作用域

- 用户明确指定用户级或项目级作用域时，采用指定作用域。
- 用户未指定作用域时，采用用户级作用域，使 Rung 可供该用户的所有项目调用；同时说明它也会在普通工作目录中进入宿主的 Skill 候选列表。
- 项目级安装写入当前项目；执行前确认项目根目录。
- 写入前向用户说明安装方式、作用域和目标路径。

### 2. 选择安装方式

按当前宿主实际具备的能力选择：

1. 宿主原生 Skill 安装器；
2. `npx skills add`；
3. 手动安装。

手动安装时，将仓库的 `v0.1.0` tag 下载至临时目录，验证 `rung/SKILL.md` 后，将完整 `rung/` 目录复制至宿主可发现的 Skills 目录。当前 Codex 的手动安装位置为：

| 作用域 | 目标目录 |
|---|---|
| 项目级 | `<project>/.agents/skills/rung` |
| 用户级 | `${HOME}/.agents/skills/rung` |

宿主提供的安装器使用其自身目标目录；手动路径只用于没有可用安装器的 Codex 环境。手动安装在临时目录完成来源检查，再执行最终复制。下载与复制阶段不执行 `rung/scripts/` 中的程序；安装后的验证阶段运行所选版本声明的只读检查。安装不修改 Codex 配置。

### 3. 处理已有安装

- 目标目录不存在时执行安装。
- 目标目录已经包含同一来源、同一内容的有效 Rung 时，报告 `already-installed`，不重复写入。
- 目标目录内容不同、来源无法确认或链接失效时停止安装，报告冲突并请求用户决定更新、备份或选择其他作用域。
- 普通安装请求不授权覆盖已有目录。更新和覆盖需要用户明确提出。

### 4. 验证安装

先完整读取所选 ref 的 `INSTALL.md`。安装完成需要满足该版本的要求，并确认：

1. 目标目录中的 `SKILL.md` 存在；
2. `SKILL.md` frontmatter 包含精确值 `name: rung`；
3. `SKILL.md` 引用的相对路径均可在安装目录中解析；
4. 目标包的文件集合与所选 ref 中的 `rung/` 一致，引用路径保持可解析；
5. 当所选 ref 包含 `contracts/rung-contract.json` 和 `scripts/validate_contract.py` 时，确认两者已安装并运行该版本的核心契约检查；`v0.1.0` 按其自带契约验证，不要求候选版新增的文件；
6. 使用 `skills` CLI 安装时，`npx skills list --global --json` 或项目级 `npx skills list --json` 能列出 `rung`；
7. 宿主能够发现并调用 `$rung`。宿主缓存 Skill 清单时，在新会话中完成这项检查。

### 5. 回报结果

Agent 最终向用户报告以下字段：

```yaml
status: installed | already-installed | blocked
skill: rung
scope: user | project
destination: <absolute-path>
source: https://github.com/LuckRookie/Rung.git
ref: v0.1.0
revision: <resolved-commit-if-available>
method: <native-installer | skills-cli | manual>
verification: <checks-and-results>
```

## 通过 Coding Agent 执行安装

将下面的指令发送给能够访问 GitHub 和本地文件系统的 Coding Agent：

```text
从 https://github.com/LuckRookie/Rung.git 获取 v0.1.0 tag，完整读取根目录 INSTALL.md，
按照其中的安装契约把 Rung 安装到用户级作用域。
写入前说明安装方式和目标路径；已有安装不得覆盖；完成后验证并报告来源 revision。
```

私有仓库使用 Agent 环境中已经配置的 Git 或 GitHub 凭据。安装过程不要求用户把访问令牌写入提示词、项目文件或安装报告。

仓库公开后，也可向 Agent 提供原始安装文档地址：

```text
https://raw.githubusercontent.com/LuckRookie/Rung/v0.1.0/INSTALL.md
```

Skill 会以 Coding Agent 的权限读取文件、执行命令和修改项目。安装前应审阅仓库中的 `rung/SKILL.md` 及其引用资源。
