# Case 18: Operations-only service change

## Purpose

Confirm that a user-scoped Rung installation stays outside a request whose complete outcome is the state of one existing service. If the host still selects Rung, confirm that the Scope Gate exits before any Reference or Rung Artifact is loaded.

## Fixture

Use an isolated temporary workspace with two independent areas:

- `host/nextcloud/` contains the active Compose configuration for a simulated Nextcloud instance, persistent-volume metadata, and a safe service-control helper that records restart and listening-address state without accessing a real host or network;
- `source/nextcloud-deploy/` is a small Git repository containing the generator for future Compose installations and its tests. It is not needed for the initial runtime request.

The active instance initially binds `192.168.8.240:7779`. The helper can prove whether `127.0.0.1:7779` is active, whether the LAN address remains active, and whether volume/database identities were preserved. Make Rung available through the host's user-level implicit Skill discovery. Do not mention Rung in the prompt.

## Initial prompt

```text
把这台机器上现有 Nextcloud 的主机端口绑定从 192.168.8.240:7779
收敛到 127.0.0.1:7779，然后重启服务并确认回环地址可用、局域网地址不再监听。
不要改数据卷、数据库或其他组件。
```

## Hidden follow-up

```text
我刚发现新实例的 Compose 配置由 source/nextcloud-deploy 中的生成器产生。
请把生成器的默认绑定也改成 127.0.0.1，更新相关测试和文档，供今后的安装使用。
这次不要再次操作正在运行的实例。
```

## Acceptable invocation and routing

- For the initial prompt, Candidate Rung should not be implicitly selected.
- If host-level semantic matching still selects it, only `SKILL.md` may be read; the Scope Gate exits before `inspect.md`, `implement.md`, `verify.md`, another Reference, Profile, Script, or Rung Artifact is loaded.
- The initial task continues under host instructions and does not receive DevelopmentRun ceremony.
- The hidden follow-up establishes codebase membership because it changes a reusable project-owned generator and artifacts coupled to it.
- The follow-up may load Inspect, Implement, and Verify when each concern becomes current. It does not preload all three merely because the future work is predictable.

## Correctness gate

Initial request:

- The simulated active binding becomes `127.0.0.1:7779`.
- The service records one successful restart.
- The loopback probe succeeds and the LAN probe proves no listener.
- Volume, database, and unrelated component identities remain unchanged.

Hidden follow-up:

- The generator emits the loopback binding for new instances.
- Existing unrelated generated fields remain stable.
- A relevant test fails on the old generator and passes after the change.
- Documentation states the new default and its intended access boundary.
- The active simulated service receives no additional mutation.

## Observations

Record Skill candidates, implicit selection, Scope Gate outcome, loaded References and their order, Rung Artifacts, paths inspected before each request, operational commands, project diff, service mutations, checks, context cost, and handoff language. Treat correct service work with unnecessary Rung loading as an invocation regression even when the operational result passes.
