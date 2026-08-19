# 安装 Rung

本文件是 Rung 的安装契约，供开发者和 Coding Agent 共同读取。安装过程以这里记录的包坐标、作用域规则、冲突处理和验证条件为准。

## 包坐标

```yaml
contract_version: 1
package:
  name: rung
  repository: https://github.com/LuckRookie/Rung.git
  ref: main
  skill_path: rung
  entrypoint: rung/SKILL.md
```

安装单元是仓库中的整个 `rung/` 目录。`SKILL.md`、`agents/`、`references/`、`profiles/`、`assets/` 和 `scripts/` 需要保持相对路径不变。

## 标准安装

[skills](https://github.com/vercel-labs/skills) CLI 能够扫描仓库中的 `SKILL.md`、读取 Skill 名称、选择目标 Agent 与作用域，并安装完整目录。

交互式安装：

```bash
npx skills add LuckRookie/Rung
```

Codex 用户级安装：

```bash
npx skills add LuckRookie/Rung --skill rung --agent codex --global --yes
```

Codex 项目级安装；在目标项目根目录执行：

```bash
npx skills add LuckRookie/Rung --skill rung --agent codex --yes
```

项目级安装目录为 `<project>/.agents/skills/rung`。用户级目录由安装器和宿主版本决定，安装完成时以安装器报告的路径为准。

`skills` CLI 会在安装记录中保存来源、Skill 路径和内容哈希。项目级安装还会在项目根目录生成或更新 `skills-lock.json`，供后续检查与更新使用。

## Codex 原生安装器

Codex 提供 `skill-installer` 时，可以把下面这句话直接发送给 Codex：

```text
使用 $skill-installer 安装这个 Skill：
https://github.com/LuckRookie/Rung/tree/main/rung
```

原生安装器负责选择其支持的用户级 Skills 目录。安装完成后保留安装器返回的目录，不迁移到另一个约定目录。

## Coding Agent 执行协议

用户要求 Coding Agent 读取本文件并安装 Rung 时，Agent 按以下契约执行。

### 1. 确定作用域

- 用户明确指定用户级或项目级作用域时，采用指定作用域。
- 用户未指定作用域时，采用用户级作用域，使 Rung 可供该用户的所有项目调用。
- 项目级安装写入当前项目；执行前确认项目根目录。
- 写入前向用户说明安装方式、作用域和目标路径。

### 2. 选择安装方式

按当前宿主实际具备的能力选择：

1. 宿主原生 Skill 安装器；
2. `npx skills add`；
3. 手动安装。

手动安装时，将仓库的 `main` 分支下载到临时目录，验证 `rung/SKILL.md` 后，再把整个 `rung/` 目录复制到宿主可发现的 Skills 目录。当前 Codex 的手动安装位置为：

| 作用域 | 目标目录 |
|---|---|
| 项目级 | `<project>/.agents/skills/rung` |
| 用户级 | `${HOME}/.agents/skills/rung` |

宿主提供的安装器使用其自身目标目录；手动路径只用于没有可用安装器的 Codex 环境。手动安装在临时目录完成来源检查，再执行最终复制。安装过程不执行 `rung/scripts/` 中的程序，也不修改 Codex 配置。

### 3. 处理已有安装

- 目标目录不存在时执行安装。
- 目标目录已经包含同一来源、同一内容的有效 Rung 时，报告 `already-installed`，不重复写入。
- 目标目录内容不同、来源无法确认或链接失效时停止安装，报告冲突并请求用户决定更新、备份或选择其他作用域。
- 普通安装请求不授权覆盖已有目录。更新和覆盖需要用户明确提出。

### 4. 验证安装

安装完成需要同时满足：

1. 目标目录中的 `SKILL.md` 存在；
2. `SKILL.md` frontmatter 包含精确值 `name: rung`；
3. `SKILL.md` 引用的相对路径均可在安装目录中解析；
4. `agents/`、`references/`、`profiles/`、`assets/` 和 `scripts/` 已完整安装；
5. 使用 `skills` CLI 安装时，`npx skills list --global --json` 或项目级 `npx skills list --json` 能列出 `rung`；
6. 宿主能够发现并调用 `$rung`。宿主缓存 Skill 清单时，在新会话中完成这项检查。

### 5. 回报结果

Agent 最终向用户报告以下字段：

```yaml
status: installed | already-installed | blocked
skill: rung
scope: user | project
destination: <absolute-path>
source: https://github.com/LuckRookie/Rung.git
ref: main
revision: <resolved-commit-if-available>
method: <native-installer | skills-cli | manual>
verification: <checks-and-results>
```

## 让 AI 直接安装

将下面的指令发送给能够访问 GitHub 和本地文件系统的 Coding Agent：

```text
从 https://github.com/LuckRookie/Rung.git 获取 main 分支，完整读取根目录 INSTALL.md，
按照其中的安装契约把 Rung 安装到用户级作用域。
写入前说明安装方式和目标路径；已有安装不得覆盖；完成后验证并报告来源 revision。
```

私有仓库使用 Agent 环境中已经配置的 Git 或 GitHub 凭据。安装过程不要求用户把访问令牌写入提示词、项目文件或安装报告。

仓库公开后，也可以把原始文档地址直接交给 Agent：

```text
https://raw.githubusercontent.com/LuckRookie/Rung/main/INSTALL.md
```

Skill 会以 Coding Agent 的权限读取文件、执行命令和修改项目。安装前应审阅仓库中的 `rung/SKILL.md` 及其引用资源。
