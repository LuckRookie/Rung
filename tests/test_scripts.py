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
    def test_skill_entrypoint_has_metadata_and_resolvable_links(self) -> None:
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(skill.startswith("---\n"))
        frontmatter_end = skill.find("\n---\n", 4)
        self.assertGreater(frontmatter_end, 0)
        frontmatter = skill[4:frontmatter_end]
        self.assertRegex(frontmatter, r"(?m)^name:\s*rung$")
        self.assertRegex(frontmatter, r"(?m)^description:\s*\S.+$")
        self.assertNotIn("TODO", frontmatter)

        links = re.findall(r"\]\(([^)#]+)(?:#[^)]+)?\)", skill)
        self.assertGreater(len(links), 0)
        missing = [link for link in links if not (SKILL_ROOT / link).exists()]
        self.assertEqual(missing, [])

    def test_json_assets_and_verification_plan_are_valid(self) -> None:
        paths = [
            SKILL_ROOT / "assets" / "verification-plan.template.json",
            REPOSITORY_ROOT / "tests" / "verification-plan.json",
        ]
        for path in paths:
            with self.subTest(path=path):
                parsed = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(parsed["schema_version"], 1)


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


class ArtifactValidationTests(unittest.TestCase):
    def test_standard_artifact_set_passes_then_reports_missing_file(self) -> None:
        required = {
            "brief.md": "complete\n",
            "context.md": "complete\n",
            "design.md": "complete\n",
            "plan.md": "complete\n",
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

            result = run_script(
                "validate_artifacts.py",
                "--run-dir",
                str(run_directory),
                "--profile",
                "standard",
            )
            self.assertEqual(result.returncode, 0, result.stdout)
            self.assertEqual(json.loads(result.stdout)["status"], "pass")

            (run_directory / "design.md").unlink()
            missing = run_script(
                "validate_artifacts.py",
                "--run-dir",
                str(run_directory),
                "--profile",
                "standard",
            )
            self.assertEqual(missing.returncode, 1)
            report = json.loads(missing.stdout)
            design = next(item for item in report["files"] if item["path"] == "design.md")
            self.assertEqual(design["status"], "missing")


class ReleaseContractTests(unittest.TestCase):
    def test_ready_release_with_local_evidence_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            project = Path(temporary_directory)
            (project / "dist").mkdir()
            (project / "dist" / "package.txt").write_text("artifact\n", encoding="utf-8")
            (project / "verification.md").write_text("pass\n", encoding="utf-8")
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
                    verification: "verification.md"
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
            (project / "verification.md").write_text("pass\n", encoding="utf-8")
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
                    verification: "verification.md"
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


if __name__ == "__main__":
    unittest.main()
