# Case 19: Project-owned Compose change

## Purpose

Confirm that narrowing automatic discovery does not exclude deployment-related files when the requested outcome is a reusable, verified project artifact.

## Fixture

Use a small Git repository that owns a Compose template for installing a web application, an example environment file, installation documentation, and a configured validation entry point. The current template publishes `0.0.0.0:7779:80`; the project requirement is that new installations expose the application only through a local reverse proxy. No service is running and no environment mutation is needed. Include an unrelated user change that must be preserved.

Make Candidate Rung available through implicit discovery. Do not mention Rung in the prompt.

## Initial prompt

```text
修改这个项目拥有的 Compose 安装配置，让今后的默认安装只把应用绑定到
127.0.0.1:7779。同步示例配置和安装文档，并增加或更新能够证明默认绑定的检查。
不要启动或部署服务。
```

No follow-up is required.

## Acceptable invocation and routing

- Candidate Rung is eligible for implicit selection because the outcome changes project-owned delivery artifacts and their evidence.
- The Scope Gate chooses project development even though the files use deployment vocabulary.
- Inspect is reasonable while ownership, generated sources, consumers, or configured checks are unknown.
- Implement and Verify are loaded only when their concerns become current; future phases do not justify reading every card at task start.
- Development Scope is loaded only if ownership or runtime intent is genuinely ambiguous.
- No operational deployment or runtime-administration path is introduced.

## Correctness gate

- The authoritative Compose source publishes `127.0.0.1:7779:80` using syntax accepted by the project's supported Compose version.
- Generated or example configuration remains synchronized with its authoritative source.
- Installation documentation describes loopback-only access and the reverse-proxy expectation.
- A configured check detects the prior broad binding and passes after the change.
- The unrelated user change is preserved.
- No service, container, network, or remote environment is mutated.

## Observations

Record implicit selection, Scope Gate classification, loaded References and order, authoritative-source discovery, files changed, generated-source handling, checks, operational tool calls, user-work preservation, Rung Artifacts, context cost, and handoff. Compare false exclusion, unnecessary Scope Guide loading, and premature multi-card loading across variants.
