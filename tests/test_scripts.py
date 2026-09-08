from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPOSITORY_ROOT / "rung" / "scripts"
SKILL_ROOT = REPOSITORY_ROOT / "rung"


def run_script(name: str, *arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPTS / name), *arguments],
        check=False,
        capture_output=True,
        text=True,
    )


class SkillStructureTests(unittest.TestCase):
    def test_skill_entrypoint_has_metadata(self) -> None:
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(skill.startswith("---\n"))
        frontmatter_end = skill.find("\n---\n", 4)
        self.assertGreater(frontmatter_end, 0)
        frontmatter = skill[4:frontmatter_end]
        self.assertRegex(frontmatter, r"(?m)^name:\s*rung$")
        self.assertRegex(frontmatter, r"(?m)^description:\s*\S.+$")
        self.assertNotIn("TODO", frontmatter)

    def test_metadata_keeps_implicit_invocation_available(self) -> None:
        metadata = (SKILL_ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertRegex(metadata, r"(?m)^\s{2}allow_implicit_invocation:\s*true$")
        description = re.search(r'(?m)^\s{2}short_description:\s*"([^"]+)"$', metadata)
        self.assertIsNotNone(description)
        assert description is not None
        self.assertTrue(25 <= len(description.group(1)) <= 64)

    def test_internal_markdown_links_resolve(self) -> None:
        missing: list[str] = []
        for document in SKILL_ROOT.rglob("*.md"):
            content = document.read_text(encoding="utf-8")
            links = re.findall(r"\]\(([^)#]+)(?:#[^)]+)?\)", content)
            for link in links:
                if re.match(r"^[a-z][a-z0-9+.-]*:", link, re.IGNORECASE):
                    continue
                target = (document.parent / link).resolve()
                if not target.exists():
                    missing.append(f"{document.relative_to(SKILL_ROOT)} -> {link}")

        self.assertEqual(missing, [])

    def test_progressive_governance_prompt_budget(self) -> None:
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertLessEqual(len(skill.encode("utf-8")), 2400)
        self.assertLessEqual(len(skill.splitlines()), 60)

        concern_cards = [
            "clarify.md",
            "inspect.md",
            "design.md",
            "plan.md",
            "implement.md",
            "verify.md",
            "review.md",
            "release.md",
        ]
        for name in concern_cards:
            with self.subTest(concern_card=name):
                content = (SKILL_ROOT / "references" / name).read_text(encoding="utf-8")
                self.assertLessEqual(len(content.encode("utf-8")), 1300)

        for name in [
            "workflow.md",
            "risk-signals.md",
            "artifacts.md",
        ]:
            with self.subTest(shared_reference=name):
                content = (SKILL_ROOT / "references" / name).read_text(encoding="utf-8")
                self.assertLessEqual(len(content.encode("utf-8")), 2200)

        detailed_guides = {
            "execution-model.md": 11_000,
            "development-scope.md": 6000,
            "project-harness.md": 4500,
            "verification-harness.md": 8000,
            "harness-evolution.md": 11_000,
            "engineering-structure.md": 9_000,
            "architecture-assessment.md": 11_000,
            "architecture-design.md": 8000,
            "project-model.md": 11_000,
            "design-exploration.md": 7_000,
            "software-quality.md": 9_000,
            "technical-debt.md": 12_500,
        }
        for name, budget in detailed_guides.items():
            with self.subTest(detailed_guide=name):
                content = (SKILL_ROOT / "references" / name).read_text(encoding="utf-8")
                self.assertLessEqual(len(content.encode("utf-8")), budget)

        for profile in (SKILL_ROOT / "profiles").glob("*.md"):
            with self.subTest(profile=profile.name):
                content = profile.read_text(encoding="utf-8")
                self.assertLessEqual(len(content.encode("utf-8")), 360)

    def test_agent_facing_skill_text_uses_english(self) -> None:
        locations = [
            SKILL_ROOT / "SKILL.md",
            *sorted((SKILL_ROOT / "agents").glob("*.yaml")),
            *sorted((SKILL_ROOT / "references").glob("*.md")),
            *sorted((SKILL_ROOT / "profiles").glob("*.md")),
            *sorted((SKILL_ROOT / "assets").glob("*")),
            *sorted((SKILL_ROOT / "contracts").glob("*.json")),
        ]
        cjk = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
        violations = [
            str(path.relative_to(SKILL_ROOT))
            for path in locations
            if path.is_file()
            and path.suffix in {".json", ".md", ".txt", ".yaml", ".yml"}
            and cjk.search(path.read_text(encoding="utf-8"))
        ]

        self.assertEqual(violations, [])

    def test_harness_guides_are_progressively_routed(self) -> None:
        project_harness = (
            SKILL_ROOT / "references" / "project-harness.md"
        ).read_text(encoding="utf-8")
        verify = (SKILL_ROOT / "references" / "verify.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("(harness-evolution.md)", project_harness)
        self.assertIn("(verification-harness.md)", project_harness)
        self.assertIn("(verification-harness.md)", verify)
        harness = (SKILL_ROOT / "references" / "verification-harness.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Design the harness boundary", harness)
        self.assertIn("known-good and known-bad", harness)

    def test_engineering_structure_guides_are_progressively_routed(self) -> None:
        references = SKILL_ROOT / "references"
        cards = {
            name: (references / f"{name}.md").read_text(encoding="utf-8")
            for name in ["design", "implement", "review"]
        }
        assessment = (references / "architecture-assessment.md").read_text(
            encoding="utf-8"
        )

        for card in cards.values():
            self.assertIn("(engineering-structure.md)", card)
        self.assertIn("(architecture-assessment.md)", cards["review"])
        self.assertIn("(engineering-structure.md)", assessment)
        architecture_design = (references / "architecture-design.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("(architecture-assessment.md)", architecture_design)
        self.assertIn("(architecture-design.md)", cards["design"])

    def test_project_model_is_progressively_routed(self) -> None:
        references = SKILL_ROOT / "references"
        cards = {
            name: (references / f"{name}.md").read_text(encoding="utf-8")
            for name in ["clarify", "inspect", "design", "review"]
        }
        engineering = (references / "engineering-structure.md").read_text(
            encoding="utf-8"
        )
        assessment = (references / "architecture-assessment.md").read_text(
            encoding="utf-8"
        )
        project_model = (references / "project-model.md").read_text(
            encoding="utf-8"
        )
        execution = (references / "execution-model.md").read_text(encoding="utf-8")
        artifacts = (references / "artifacts.md").read_text(encoding="utf-8")

        for card in cards.values():
            self.assertIn("(project-model.md)", card)
        self.assertIn("(project-model.md)", engineering)
        self.assertIn("(project-model.md)", assessment)
        self.assertIn("(project-model.md)", execution)
        for target in [
            "(design.md)",
            "(engineering-structure.md)",
            "(architecture-assessment.md)",
            "(project-harness.md)",
        ]:
            self.assertIn(target, project_model)
        self.assertIn("assets/project-model.template.md", artifacts)
        self.assertTrue((SKILL_ROOT / "assets" / "project-model.template.md").is_file())

    def test_design_exploration_is_progressively_routed(self) -> None:
        references = SKILL_ROOT / "references"
        clarify = (references / "clarify.md").read_text(encoding="utf-8")
        design = (references / "design.md").read_text(encoding="utf-8")
        project_model = (references / "project-model.md").read_text(encoding="utf-8")
        exploration = (references / "design-exploration.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("(design-exploration.md)", clarify)
        self.assertIn("(design-exploration.md)", design)
        self.assertIn("(design-exploration.md)", project_model)
        self.assertIn("several materially different", exploration)
        self.assertIn("representative scenarios", exploration)
        self.assertIn("There is no fixed number of alternatives", exploration)
        self.assertIn("Keep the exploration in the session by default", exploration)
        for target in [
            "(clarify.md)",
            "(design.md)",
            "(engineering-structure.md)",
            "(architecture-assessment.md)",
        ]:
            self.assertIn(target, exploration)

    def test_quality_and_debt_are_distinct_and_progressively_routed(self) -> None:
        references = SKILL_ROOT / "references"
        cards = {
            name: (references / f"{name}.md").read_text(encoding="utf-8")
            for name in ["design", "implement", "review"]
        }
        software_quality = (references / "software-quality.md").read_text(
            encoding="utf-8"
        )
        technical_debt = (references / "technical-debt.md").read_text(
            encoding="utf-8"
        )
        engineering = (references / "engineering-structure.md").read_text(
            encoding="utf-8"
        )
        architecture = (references / "architecture-assessment.md").read_text(
            encoding="utf-8"
        )
        project_model = (references / "project-model.md").read_text(
            encoding="utf-8"
        )
        project_harness = (references / "project-harness.md").read_text(
            encoding="utf-8"
        )
        artifacts = (references / "artifacts.md").read_text(encoding="utf-8")

        for card in cards.values():
            self.assertIn("(software-quality.md)", card)
            self.assertIn("(technical-debt.md)", card)
        for target in [engineering, architecture, project_model, project_harness]:
            self.assertIn("(technical-debt.md)", target)
        self.assertIn("(software-quality.md)", engineering)

        for quality in [
            "Correctness",
            "Understandability",
            "Changeability",
            "Verifiability",
            "Operability",
            "Consistency",
            "Predictability",
        ]:
            self.assertIn(quality, software_quality)
        self.assertIn("touched ownership boundary", software_quality)
        self.assertIn("repository-wide quality audit", software_quality)
        self.assertIn("Quality probes", software_quality)
        self.assertIn("known-good and known-bad", software_quality)

        for confidence in ["Debt signal", "Debt hypothesis", "Qualified debt item"]:
            self.assertIn(confidence, technical_debt)
        for mechanism in [
            "current debt-bearing construct",
            "credible change, maintenance event, or time trigger",
            "change-driven",
            "time-driven",
            "spread-driven",
            "Propagation",
            "Option loss",
        ]:
            self.assertIn(mechanism, technical_debt)
        self.assertIn("defect", technical_debt)
        self.assertIn("vulnerability", technical_debt)
        self.assertIn("issue tracker", technical_debt)
        self.assertIn("assets/technical-debt-item.template.md", artifacts)
        self.assertTrue(
            (SKILL_ROOT / "assets" / "technical-debt-item.template.md").is_file()
        )

    def test_execution_model_routes_integrated_run_ownership(self) -> None:
        workflow = (SKILL_ROOT / "references" / "workflow.md").read_text(
            encoding="utf-8"
        )
        execution = (
            SKILL_ROOT / "references" / "execution-model.md"
        ).read_text(encoding="utf-8")
        cards = {
            name: (SKILL_ROOT / "references" / f"{name}.md").read_text(
                encoding="utf-8"
            )
            for name in [
                "clarify",
                "inspect",
                "design",
                "plan",
                "implement",
                "verify",
                "review",
                "release",
            ]
        }

        self.assertIn("(execution-model.md)", workflow)
        self.assertIn("one logical **Primary Agent**", execution)
        self.assertIn("one main session", execution)
        for radius in ["Baseline", "Target", "Impact", "System"]:
            self.assertIn(radius, execution)
        self.assertIn("The Primary Agent owns the integrated plan", execution)
        self.assertIn("Worker success does not establish integrated success", execution)
        self.assertIn("On resume, re-read applicable instructions", execution)
        self.assertIn("Verify claims against the integrated revision", execution)

        self.assertIn("delegates an in-scope choice", cards["clarify"])
        self.assertIn("inspection radius", cards["inspect"])
        self.assertIn("human-facing surfaces", cards["design"])
        self.assertIn("owns the integrated plan", cards["plan"])
        self.assertIn("integrate all worker output", cards["implement"])
        self.assertIn("integrated revision", cards["verify"])
        self.assertIn("independent reviewer", cards["review"])
        self.assertIn("Primary Agent assembles", cards["release"])

    def test_runtime_helper_examples_resolve_from_skill_root(self) -> None:
        runtime_text = "\n".join(
            path.read_text(encoding="utf-8")
            for path in [
                SKILL_ROOT / "SKILL.md",
                *sorted((SKILL_ROOT / "references").glob("*.md")),
            ]
        )

        self.assertNotIn("python scripts/", runtime_text)

    def test_json_assets_and_verification_plan_are_valid(self) -> None:
        paths = [
            SKILL_ROOT / "assets" / "verification-plan.template.json",
            REPOSITORY_ROOT / "tests" / "verification-plan.json",
        ]
        for path in paths:
            with self.subTest(path=path):
                parsed = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(parsed["schema_version"], 1)

    def test_machine_readable_core_contract_is_valid(self) -> None:
        result = run_script("validate_contract.py", "--skill-root", str(SKILL_ROOT))

        self.assertEqual(result.returncode, 0, result.stdout)
        report = json.loads(result.stdout)
        self.assertEqual(report["status"], "pass")
        self.assertEqual(report["problems"], [])

    def test_core_contract_covers_the_full_development_lifecycle(self) -> None:
        contract = json.loads(
            (SKILL_ROOT / "contracts" / "rung-contract.json").read_text(encoding="utf-8")
        )
        self.assertEqual(
            sorted(stage["id"] for stage in contract["lifecycle"]),
            sorted([
                "clarify", "inspect", "design", "plan", "implement", "verify", "review", "release"
            ]),
        )

    def test_core_contract_rejects_missing_route_entry(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            skill_root = Path(temporary_directory)
            (skill_root / "contracts").mkdir()
            (skill_root / "references").mkdir()
            (skill_root / "SKILL.md").write_text("# Skill\n", encoding="utf-8")
            contract = {
                "schema_version": 1,
                "package": {
                    "name": "rung",
                    "stable_ref": "v0.1.0",
                    "candidate_version": "0.1.2",
                },
                "entrypoint": "SKILL.md",
                "scope_gate": {
                    "required_predicates": [
                        "codebase_relationship",
                        "active_development_claim",
                    ],
                    "development_outcomes": ["durable_codebase_change"],
                    "understanding_only_exits_before_references": True,
                },
                "concerns": [
                    {
                        "id": "clarify",
                        "entry": "references/missing.md",
                        "kind": "card",
                        "max_bytes": 1300,
                        "signals": ["direction"],
                    }
                ],
            }
            contract_path = skill_root / "contracts" / "rung-contract.json"
            contract_path.write_text(json.dumps(contract), encoding="utf-8")

            result = run_script(
                "validate_contract.py",
                "--skill-root",
                str(skill_root),
                "--contract",
                str(contract_path),
            )

            self.assertEqual(result.returncode, 1)
            report = json.loads(result.stdout)
            self.assertEqual(report["status"], "fail")
            self.assertTrue(any("not found" in item for item in report["problems"]))

    def test_scope_gate_evaluator_exits_for_understanding_only_work(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            scope_input = Path(temporary_directory) / "scope.json"
            scope_input.write_text(
                json.dumps(
                    {
                        "codebase_relationship": "present",
                        "development_claim": "absent",
                    }
                ),
                encoding="utf-8",
            )

            result = run_script("evaluate_scope.py", "--input", str(scope_input))

            self.assertEqual(result.returncode, 0, result.stdout)
            report = json.loads(result.stdout)
            self.assertEqual(report["scope"], "understanding-only")
            self.assertTrue(report["exited_before_references"])

    def test_scope_gate_evaluator_accepts_active_development(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            scope_input = Path(temporary_directory) / "scope.json"
            scope_input.write_text(
                json.dumps(
                    {
                        "codebase_relationship": "present",
                        "development_claim": "present",
                        "materiality": "present",
                    }
                ),
                encoding="utf-8",
            )

            result = run_script("evaluate_scope.py", "--input", str(scope_input))

            self.assertEqual(result.returncode, 0, result.stdout)
            report = json.loads(result.stdout)
            self.assertEqual(report["scope"], "development")
            self.assertFalse(report["exited_before_references"])

    def test_scope_gate_evaluator_preserves_non_development_classifications(self) -> None:
        cases = {
            ("absent", "present"): ("outside", True),
            ("present", "mixed"): ("mixed", False),
            ("uncertain", "present"): ("uncertain", True),
        }
        for (relationship, claim), expected in cases.items():
            with (
                self.subTest(relationship=relationship, claim=claim),
                tempfile.TemporaryDirectory() as temporary_directory,
            ):
                scope_input = Path(temporary_directory) / "scope.json"
                scope_input.write_text(
                    json.dumps(
                        {
                            "codebase_relationship": relationship,
                            "development_claim": claim,
                            "materiality": "present",
                        }
                    ),
                    encoding="utf-8",
                )

                result = run_script("evaluate_scope.py", "--input", str(scope_input))

                self.assertEqual(result.returncode, 0, result.stdout)
                report = json.loads(result.stdout)
                self.assertEqual(
                    (report["scope"], report["exited_before_references"]),
                    expected,
                )


class InspectProjectTests(unittest.TestCase):
    def test_detects_governed_python_project_and_candidate_commands(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            project = Path(temporary_directory)
            (project / "src").mkdir()
            (project / "tests").mkdir()
            (project / "AGENTS.md").write_text("# Instructions\n", encoding="utf-8")
            (project / "src" / "app.py").write_text("VALUE = 1\n", encoding="utf-8")
            (project / "tests" / "test_app.py").write_text(
                "def test_value():\n    assert 1 == 1\n", encoding="utf-8"
            )
            (project / "pyproject.toml").write_text(
                textwrap.dedent(
                    """
                    [build-system]
                    requires = ["setuptools"]
                    build-backend = "setuptools.build_meta"

                    [tool.ruff]
                    line-length = 100
                    """
                ).strip()
                + "\n",
                encoding="utf-8",
            )

            result = run_script("inspect_project.py", "--project", str(project))

            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads(result.stdout)
            self.assertEqual(report["project_state"], "Governed")
            self.assertEqual(report["languages"]["Python"], 2)
            self.assertEqual(report["instruction_files"], ["AGENTS.md"])
            purposes = {entry["purpose"] for entry in report["candidate_commands"]}
            self.assertTrue({"test", "lint", "build"}.issubset(purposes))
            test_command = next(
                entry["command"]
                for entry in report["candidate_commands"]
                if entry["purpose"] == "test"
            )
            self.assertEqual(test_command[:4], ["python", "-m", "unittest", "discover"])

    def test_uses_package_manager_declared_by_project(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            project = Path(temporary_directory)
            (project / "package.json").write_text(
                json.dumps(
                    {
                        "packageManager": "pnpm@10.0.0",
                        "scripts": {"test": "vitest run", "build": "vite build"},
                    }
                ),
                encoding="utf-8",
            )

            result = run_script("inspect_project.py", "--project", str(project))

            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads(result.stdout)
            commands = {
                entry["purpose"]: entry["command"]
                for entry in report["candidate_commands"]
            }
            self.assertEqual(commands["test"], ["pnpm", "run", "test"])
            self.assertEqual(commands["build"], ["pnpm", "run", "build"])


class VerificationRunnerTests(unittest.TestCase):
    def test_runs_argument_array_and_writes_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            project = Path(temporary_directory)
            plan = project / "plan.json"
            output = project / "evidence.json"
            plan.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "run_id": "RUN-1",
                        "revision": "working-tree",
                        "checks": [
                            {
                                "name": "smoke",
                                "claim": "Python can execute the project check",
                                "tier": 0,
                                "command": [sys.executable, "-c", "print('verified')"],
                                "cwd": ".",
                                "timeout_seconds": 10,
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )

            result = run_script(
                "run_verification.py",
                "--project",
                str(project),
                "--plan",
                str(plan),
                "--output",
                str(output),
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            evidence = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(evidence["status"], "pass")
            self.assertEqual(evidence["checks"][0]["return_code"], 0)
            self.assertIn("verified", evidence["checks"][0]["stdout"])

    def test_rejects_working_directory_outside_project(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            project = Path(temporary_directory)
            plan = project / "plan.json"
            plan.write_text(
                json.dumps(
                    {
                        "checks": [
                            {
                                "name": "escape",
                                "tier": 0,
                                "command": [sys.executable, "-c", "pass"],
                                "cwd": "..",
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )

            result = run_script(
                "run_verification.py", "--project", str(project), "--plan", str(plan)
            )

            self.assertEqual(result.returncode, 2)
            self.assertIn("escapes project root", result.stdout)

    def test_filters_checks_by_maximum_tier_and_records_skips(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            project = Path(temporary_directory)
            plan = project / "plan.json"
            output = project / "evidence.json"
            plan.write_text(
                json.dumps(
                    {
                        "checks": [
                            {
                                "name": f"tier-{tier}",
                                "claim": f"tier {tier} claim",
                                "tier": tier,
                                "command": [sys.executable, "-c", f"print({tier})"],
                            }
                            for tier in (0, 2, 3)
                        ]
                    }
                ),
                encoding="utf-8",
            )

            result = run_script(
                "run_verification.py",
                "--project",
                str(project),
                "--plan",
                str(plan),
                "--max-tier",
                "2",
                "--output",
                str(output),
            )

            self.assertEqual(result.returncode, 0, result.stdout)
            evidence = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(evidence["requested_max_tier"], 2)
            self.assertEqual(evidence["planned_check_count"], 3)
            self.assertEqual(evidence["selected_check_count"], 2)
            self.assertEqual(
                [check["name"] for check in evidence["checks"]],
                ["tier-0", "tier-2"],
            )
            self.assertEqual(evidence["skipped_checks"][0]["name"], "tier-3")

    def test_rejects_invalid_or_unselected_tiers(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            project = Path(temporary_directory)
            plan = project / "plan.json"

            for invalid_tier in (True, "1", 4):
                with self.subTest(invalid_tier=invalid_tier):
                    plan.write_text(
                        json.dumps(
                            {
                                "checks": [
                                    {
                                        "name": "invalid",
                                        "tier": invalid_tier,
                                        "command": [sys.executable, "-c", "pass"],
                                    }
                                ]
                            }
                        ),
                        encoding="utf-8",
                    )
                    result = run_script(
                        "run_verification.py",
                        "--project",
                        str(project),
                        "--plan",
                        str(plan),
                    )
                    self.assertEqual(result.returncode, 2)
                    self.assertIn("tier must be an integer between 0 and 3", result.stdout)

            plan.write_text(
                json.dumps(
                    {
                        "checks": [
                            {
                                "name": "release-only",
                                "tier": 3,
                                "command": [sys.executable, "-c", "pass"],
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            result = run_script(
                "run_verification.py",
                "--project",
                str(project),
                "--plan",
                str(plan),
                "--max-tier",
                "2",
            )
            self.assertEqual(result.returncode, 2)
            self.assertIn("no checks at or below tier 2", result.stdout)


class ArtifactValidationTests(unittest.TestCase):
    def test_discovers_and_validates_present_artifacts_without_profile(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            run_directory = Path(temporary_directory)
            (run_directory / "brief.md").write_text("complete\n", encoding="utf-8")
            (run_directory / "evidence.json").write_text(
                '{"status": "pass"}\n', encoding="utf-8"
            )

            result = run_script(
                "validate_artifacts.py", "--run-dir", str(run_directory)
            )

            self.assertEqual(result.returncode, 0, result.stdout)
            report = json.loads(result.stdout)
            self.assertEqual(report["selection"], "discovered")
            self.assertEqual(
                [item["path"] for item in report["files"]],
                ["brief.md", "evidence.json"],
            )

    def test_empty_artifact_directory_reports_no_selection(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            result = run_script(
                "validate_artifacts.py", "--run-dir", temporary_directory
            )

            self.assertEqual(result.returncode, 1, result.stdout)
            report = json.loads(result.stdout)
            self.assertEqual(report["files"], [])
            self.assertIn("no supported artifacts", report["problems"][0])

    def test_explicit_artifact_set_passes_then_reports_missing_file(self) -> None:
        required = {
            "brief.md": "complete\n",
            "context.md": "complete\n",
            "project-model.md": "complete\n",
            "design.md": "complete\n",
            "plan.md": "complete\n",
            "debt.md": "complete\n",
            "harness-change.md": "complete\n",
            "verification-harness.md": "complete\n",
            "verification-plan.json": '{"checks": []}\n',
            "verification.md": "complete\n",
            "review.md": "complete\n",
            "evidence.json": '{"status": "pass"}\n',
            "release.yaml": "status: ready\n",
        }
        with tempfile.TemporaryDirectory() as temporary_directory:
            run_directory = Path(temporary_directory)
            for name, content in required.items():
                (run_directory / name).write_text(content, encoding="utf-8")

            arguments = ["--run-dir", str(run_directory)]
            for name in required:
                arguments.extend(["--require", name])

            result = run_script("validate_artifacts.py", *arguments)
            self.assertEqual(result.returncode, 0, result.stdout)
            self.assertEqual(json.loads(result.stdout)["status"], "pass")

            (run_directory / "design.md").unlink()
            missing = run_script("validate_artifacts.py", *arguments)
            self.assertEqual(missing.returncode, 1)
            report = json.loads(missing.stdout)
            design = next(item for item in report["files"] if item["path"] == "design.md")
            self.assertEqual(design["status"], "missing")


class ReleaseContractTests(unittest.TestCase):
    def test_ready_release_can_use_revision_without_independent_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            project = Path(temporary_directory)
            (project / "evidence.json").write_text(
                '{"status": "pass"}\n', encoding="utf-8"
            )
            manifest = project / "release.yaml"
            manifest.write_text(
                textwrap.dedent(
                    """
                    schema_version: 1
                    run_id: "RUN-LIGHT"
                    version: "unversioned"
                    revision: "working-tree"
                    status: ready
                    artifacts: []
                    acceptance: pass
                    verification: "evidence.json"
                    documentation: not-applicable
                    known_limitations: []
                    unverified_risks: []
                    publish_actions: []
                    """
                ).strip()
                + "\n",
                encoding="utf-8",
            )

            result = run_script(
                "check_release.py",
                "--manifest",
                str(manifest),
                "--project",
                str(project),
            )

            self.assertEqual(result.returncode, 0, result.stdout)
            self.assertEqual(json.loads(result.stdout)["status"], "pass")

    def test_ready_release_with_local_evidence_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            project = Path(temporary_directory)
            (project / "dist").mkdir()
            (project / "dist" / "package.txt").write_text("artifact\n", encoding="utf-8")
            (project / "evidence.json").write_text(
                '{"status": "pass"}\n', encoding="utf-8"
            )
            manifest = project / "release.yaml"
            manifest.write_text(
                textwrap.dedent(
                    """
                    schema_version: 1
                    run_id: "RUN-1"
                    version: "1.0.0"
                    revision: "source-release-1"
                    status: ready
                    artifacts:
                      - "dist/package.txt"
                    acceptance: pass
                    verification: "evidence.json"
                    documentation: complete
                    known_limitations: []
                    unverified_risks: []
                    publish_actions: []
                    """
                ).strip()
                + "\n",
                encoding="utf-8",
            )

            result = run_script(
                "check_release.py",
                "--manifest",
                str(manifest),
                "--project",
                str(project),
            )

            self.assertEqual(result.returncode, 0, result.stdout)
            self.assertEqual(json.loads(result.stdout)["status"], "pass")

    def test_ready_release_reports_missing_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            project = Path(temporary_directory)
            (project / "evidence.json").write_text(
                '{"status": "pass"}\n', encoding="utf-8"
            )
            manifest = project / "release.yaml"
            manifest.write_text(
                textwrap.dedent(
                    """
                    schema_version: 1
                    run_id: "RUN-1"
                    version: "1.0.0"
                    revision: "source-release-1"
                    status: ready
                    artifacts:
                      - "dist/missing.txt"
                    acceptance: pass
                    verification: "evidence.json"
                    documentation: complete
                    known_limitations: []
                    unverified_risks: []
                    publish_actions: []
                    """
                ).strip()
                + "\n",
                encoding="utf-8",
            )

            result = run_script(
                "check_release.py",
                "--manifest",
                str(manifest),
                "--project",
                str(project),
            )

            self.assertEqual(result.returncode, 1)
            self.assertIn("artifact 1 not found", result.stdout)

    def test_ready_release_rejects_non_passing_local_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            project = Path(temporary_directory)
            (project / "evidence.json").write_text(
                '{"status": "fail"}\n', encoding="utf-8"
            )
            manifest = project / "release.yaml"
            manifest.write_text(
                textwrap.dedent(
                    """
                    schema_version: 1
                    run_id: "RUN-FAILED-EVIDENCE"
                    version: "1.0.0"
                    revision: "working-tree"
                    status: ready
                    artifacts: []
                    acceptance: pass
                    verification: "evidence.json"
                    documentation: complete
                    known_limitations: []
                    unverified_risks: []
                    publish_actions: []
                    """
                ).strip()
                + "\n",
                encoding="utf-8",
            )

            result = run_script(
                "check_release.py",
                "--manifest",
                str(manifest),
                "--project",
                str(project),
            )

            self.assertEqual(result.returncode, 1)
            self.assertIn("verification evidence status must be pass", result.stdout)


if __name__ == "__main__":
    unittest.main()
