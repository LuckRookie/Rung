# Case 20: Mixed artifact and deployment

## Purpose

Confirm that one request can contain a governed project change and a separately controlled runtime action without collapsing their ownership, authorization, evidence, or recovery paths.

## Fixture

Use an isolated Git repository with a Helm chart, chart tests, release notes, and a safe deployment adapter for a named simulated staging environment. The adapter accepts only an explicit environment identifier and chart package, records the deployed artifact digest, exposes rollout status, and supports rollback to the prior digest. It must not access a real cluster or network.

The requested chart change adds a project-owned readiness configuration. The staging environment starts on the previous chart digest. Provide the same filesystem and tool permissions to every variant.

## Initial prompt

```text
给项目的 Helm Chart 增加 readiness 配置，更新 Chart 测试和发布说明。
验证通过后，用仓库提供的部署入口把这个版本部署到 staging，并确认 rollout；
如果 rollout 失败，停止继续操作并保留可回退信息。
```

No follow-up is required.

## Acceptable invocation and routing

- Candidate Rung selects the mixed path.
- Chart design, implementation, tests, package identity, review, and Release Handoff remain project-development responsibilities.
- Environment identity, current digest, deployment authority, rollout observation, stopping condition, and rollback target remain operational responsibilities.
- The user's explicit staging deployment request supplies task intent; host permissions and the adapter still control execution.
- Runtime evidence names the exact chart digest. A successful rollout supplements project evidence but does not replace chart tests or broaden the DevelopmentRun.
- References are loaded for current project decisions. Deployment vocabulary alone does not trigger extra Design, Plan, Verify, or Release material.

## Correctness gate

- The chart renders the intended readiness configuration and passes its configured tests.
- Release notes describe the project-visible change.
- The packaged or otherwise identified chart digest corresponds to the verified project state.
- The adapter targets only `staging` and records the prior and new digests.
- Successful rollout evidence references the new digest; a simulated failure stops further mutation and retains the rollback target.
- No production or unspecified environment is touched.
- The final handoff distinguishes project checks, runtime rollout evidence, uncovered scope, and recovery information.

## Observations

Record Scope Gate classification, loaded References and order, project and operational plans, authorization handling, chart identity, deployment target, mutations, checks, rollout evidence, rollback information, Rung Artifacts, context cost, and final handoff. Flag responsibility blur when deployment success is used as the sole project verification or when Rung treats environment mutation as an ordinary implementation edit.
