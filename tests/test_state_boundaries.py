from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from test_scripts import create_passing_evidence, run_git, run_script


def commit(project: Path, *paths: str) -> str:
    run_git(project, "add", *(paths or (".",)))
    run_git(
        project,
        "-c",
        "user.name=Rung Tests",
        "-c",
        "user.email=rung@example.invalid",
        "commit",
        "--quiet",
        "-m",
        "fixture",
    )
    return run_git(project, "rev-parse", "HEAD")


def behavior_checks(path: str = "app.py", value: int = 2) -> list[dict[str, object]]:
    return [
        {
            "name": "behavior",
            "claim": "the public value is correct",
            "tier": 0,
            "required_for_release": True,
            "command": [
                sys.executable,
                "-B",
                "-c",
                f"import runpy; assert runpy.run_path({path!r})['VALUE'] == {value}",
            ],
        }
    ]


class StateBoundaryTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name)

    def project(self, name: str = "project", *, git: bool = True) -> Path:
        root = self.base / name
        root.mkdir(parents=True)
        (root / "app.py").write_text("VALUE = 2\n")
        if git:
            run_git(root, "init", "--quiet")
            commit(root)
        return root

    def evidence(self, project: Path, path: str = "app.py") -> tuple[Path, dict]:
        location, evidence = create_passing_evidence(project, checks=behavior_checks(path))
        self.assertEqual(evidence["status"], "pass", evidence)
        return location, evidence

    def release(self, project: Path, location: Path, evidence: dict) -> tuple[int, dict]:
        manifest = location.parent / "release.yaml"
        values = {
            "schema_version": 1,
            "run_id": "RUN-1",
            "version": "1.0.0",
            "revision": evidence["target_state"]["identity"],
            "status": "ready",
            "artifacts": [],
            "acceptance": "pass",
            "verification": str(location),
            "documentation": "complete",
            "known_limitations": [],
            "unverified_risks": [],
            "publish_actions": [],
        }
        manifest.write_text(
            "".join(f"{key}: {json.dumps(value)}\n" for key, value in values.items())
        )
        result = run_script(
            "check_release.py", "--project", str(project), "--manifest", str(manifest)
        )
        self.assertFalse(result.stderr, result.stderr)
        return result.returncode, json.loads(result.stdout)

    def assert_release(self, project: Path, location: Path, evidence: dict, expected: int) -> dict:
        code, report = self.release(project, location, evidence)
        self.assertEqual(code, expected, report)
        return report

    def nested_project(self, *, ignored_runs: bool) -> tuple[Path, Path]:
        root = self.project()
        project = root / "packages/app"
        project.mkdir(parents=True)
        (project / "app.py").write_text("VALUE = 1\n")
        if ignored_runs:
            (root / ".gitignore").write_text(".rung/\n")
        commit(root)
        (project / "app.py").write_text("VALUE = 2\n")
        return root, project

    def test_nested_project_accepts_stable_source_and_rejects_further_changes(self) -> None:
        root, project = self.nested_project(ignored_runs=True)
        location, evidence = self.evidence(project)
        self.assertEqual(evidence["target_state"]["repository_root"], str(root))
        self.assertEqual(evidence["target_state"]["project_subpath"], "packages/app")
        self.assert_release(project, location, evidence, 0)
        (project / "app.py").write_text("VALUE = 3\n")
        changed_behavior = subprocess.run(
            behavior_checks()[0]["command"], cwd=project, capture_output=True
        )
        self.assertNotEqual(changed_behavior.returncode, 0)
        self.assert_release(project, location, evidence, 1)

    def test_nested_run_files_do_not_invalidate_unchanged_source(self) -> None:
        root, project = self.nested_project(ignored_runs=False)
        location, evidence = self.evidence(project)
        root_run = root / ".rung/runs/other"
        root_run.mkdir(parents=True)
        (root_run / "note.md").write_text("independent run metadata")
        self.assert_release(project, location, evidence, 0)

    def test_stdout_and_relocated_run_evidence_remain_applicable(self) -> None:
        for git in (True, False):
            for mode in ("stdout", "moved"):
                with self.subTest(git=git, mode=mode):
                    project = self.project(f"{git}-{mode}", git=git)
                    (project / "uncommitted.py").write_text("VALUE = 2\n")
                    location, evidence = self.evidence(project)
                    if mode == "stdout":
                        result = run_script(
                            "run_verification.py",
                            "--project",
                            str(project),
                            "--plan",
                            str(location.parent / "plan.json"),
                        )
                        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                        evidence = json.loads(result.stdout)
                        location.write_text(result.stdout)
                    else:
                        moved = location.with_name("moved.json")
                        location.rename(moved)
                        location = moved
                    self.assert_release(project, location, evidence, 0)

    def test_run_directory_link_does_not_exclude_source_target(self) -> None:
        for git in (True, False):
            with self.subTest(git=git):
                project = self.project(f"linked-{git}", git=git)
                (project / "src").mkdir()
                (project / ".rung").mkdir()
                (project / ".rung/runs").symlink_to("../src", target_is_directory=True)
                source = project / "src/app.py"
                source.write_text("VALUE = 1\n")
                if git:
                    commit(project)
                source.write_text("VALUE = 2\n")
                location, evidence = self.evidence(project, "src/app.py")
                if git:
                    self.assertTrue(evidence["target_state"]["dirty"])
                self.assert_release(project, location, evidence, 0)
                source.write_text("VALUE = 1\n")
                self.assert_release(project, location, evidence, 1)

    def test_nested_scope_covers_sibling_sources_and_metadata(self) -> None:
        root, project = self.nested_project(ignored_runs=False)
        location, evidence = self.evidence(project)
        (root / "app.py").write_text("VALUE = 3\n")
        self.assert_release(project, location, evidence, 1)
        (root / "app.py").write_text("VALUE = 2\n")
        self.assert_release(project, location, evidence, 0)
        sibling_run = root / "packages/other/.rung/runs/run"
        sibling_run.mkdir(parents=True)
        (sibling_run / "source.py").write_text("VALUE = 7\n")
        self.assert_release(project, location, evidence, 1)

    def test_nested_mutation_during_verification_blocks_evidence(self) -> None:
        _, project = self.nested_project(ignored_runs=False)
        checks = behavior_checks()
        checks[0]["command"] = [
            sys.executable,
            "-B",
            "-c",
            "from pathlib import Path; Path('app.py').write_text('VALUE = 3\\n')",
        ]
        location, evidence = create_passing_evidence(project, checks=checks)
        self.assertEqual(evidence["status"], "blocked")
        self.assertFalse(evidence["state_stable"])
        self.assert_release(project, location, evidence, 1)

    @unittest.skipUnless(hasattr(os, "mkfifo"), "requires POSIX FIFO")
    def test_failed_final_capture_preserves_executed_checks(self) -> None:
        project = self.project(git=False)
        checks = behavior_checks()
        checks[0]["command"] = [sys.executable, "-B", "-c", "import os; os.mkfifo('pipe')"]
        location, evidence = create_passing_evidence(project, checks=checks)
        self.assertEqual(evidence["status"], "blocked")
        self.assertIsNone(evidence["final_state"])
        self.assertEqual(evidence["checks"][0]["return_code"], 0)
        self.assertIn("Unsupported state path", " ".join(evidence["applicability"]["reasons"]))
        self.assert_release(project, location, evidence, 1)

    def test_revision_error_replaces_old_passing_output(self) -> None:
        project = self.project()
        location, _ = self.evidence(project)
        plan_path = location.parent / "plan.json"
        plan = json.loads(plan_path.read_text())
        plan["revision"] = "does-not-exist"
        plan_path.write_text(json.dumps(plan))
        result = run_script(
            "run_verification.py",
            "--project",
            str(project),
            "--plan",
            str(plan_path),
            "--output",
            str(location),
        )
        self.assertEqual(result.returncode, 2)
        diagnostic = json.loads(location.read_text())
        self.assertEqual(diagnostic["status"], "error")
        self.assertIn("revision", diagnostic["message"])

    def test_output_cannot_overwrite_plan_or_its_hard_link(self) -> None:
        project = self.project()
        location, _ = self.evidence(project)
        plan_path = location.parent / "plan.json"
        original = plan_path.read_bytes()
        hard_link = location.parent / "plan-alias.json"
        os.link(plan_path, hard_link)
        for output in (plan_path, hard_link):
            with self.subTest(output=output.name):
                result = run_script(
                    "run_verification.py",
                    "--project",
                    str(project),
                    "--plan",
                    str(plan_path),
                    "--output",
                    str(output),
                )
                self.assertEqual(result.returncode, 2)
                self.assertIn("must differ", json.loads(result.stdout)["message"])
                self.assertEqual(plan_path.read_bytes(), original)

    def test_directory_symlink_switch_invalidates_filesystem_evidence(self) -> None:
        project = self.project(git=False)
        for name, value in (("one", 2), ("two", 3)):
            (project / name).mkdir()
            (project / name / "app.py").write_text(f"VALUE = {value}\n")
        link = project / "current"
        link.symlink_to("one", target_is_directory=True)
        location, evidence = self.evidence(project, "current/app.py")
        self.assert_release(project, location, evidence, 0)
        link.unlink()
        link.symlink_to("two", target_is_directory=True)
        changed_behavior = subprocess.run(
            behavior_checks("current/app.py")[0]["command"], cwd=project, capture_output=True
        )
        self.assertNotEqual(changed_behavior.returncode, 0)
        self.assert_release(project, location, evidence, 1)

    def add_submodule(self, project: Path, dependency: Path, name: str = "lib") -> Path:
        run_git(
            project,
            "-c",
            "protocol.file.allow=always",
            "submodule",
            "add",
            "--quiet",
            str(dependency),
            name,
        )
        commit(project, ".gitmodules", name)
        return project / name

    def assert_capture_blocked(self, project: Path, reason: str) -> None:
        run = project / ".rung/runs/RUN-1"
        run.mkdir(parents=True, exist_ok=True)
        plan, output = run / "plan.json", run / "evidence.json"
        checks = behavior_checks()
        checks[0]["command"] = [
            sys.executable,
            "-B",
            "-c",
            "from pathlib import Path; Path('should-not-run').touch()",
        ]
        plan.write_text(json.dumps({"schema_version": 2, "run_id": "RUN-1", "checks": checks}))
        output.write_text('{"status": "pass"}')
        result = run_script(
            "run_verification.py",
            "--project",
            str(project),
            "--plan",
            str(plan),
            "--output",
            str(output),
        )
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        report = json.loads(output.read_text())
        self.assertEqual(report["status"], "blocked", report)
        self.assertIn(reason, report["message"])
        self.assertFalse((project / "should-not-run").exists())

    def test_submodules_block_before_checks_including_clean_and_uninitialized(self) -> None:
        dependency = self.project("dependency")
        for mode in ("clean", "dirty", "ignore", "checkout", "uninitialized"):
            with self.subTest(mode=mode):
                project = self.project(mode)
                submodule = self.add_submodule(project, dependency)
                if mode in {"dirty", "ignore"}:
                    (submodule / "app.py").write_text("VALUE = 999\n")
                if mode == "ignore":
                    run_git(project, "config", "-f", ".gitmodules", "submodule.lib.ignore", "all")
                    commit(project, ".gitmodules")
                    self.assertEqual(run_git(project, "status", "--porcelain"), "")
                if mode == "checkout":
                    (submodule / "app.py").write_text("VALUE = 999\n")
                    commit(submodule)
                    self.assertEqual(run_git(submodule, "status", "--porcelain"), "")
                if mode == "uninitialized":
                    run_git(project, "submodule", "deinit", "--force", "lib")
                self.assert_capture_blocked(project, "submodules")

    def test_nested_submodule_ignore_cannot_create_false_clean_commit_evidence(self) -> None:
        leaf = self.project("leaf")
        middle = self.project("middle")
        self.add_submodule(middle, leaf, "leaf")
        run_git(middle, "config", "-f", ".gitmodules", "submodule.leaf.ignore", "all")
        commit(middle, ".gitmodules")
        outer = self.project("outer")
        submodule = self.add_submodule(outer, middle, "mid")
        run_git(submodule, "-c", "protocol.file.allow=always", "submodule", "update", "--init")
        (submodule / "leaf/app.py").write_text("VALUE = 999\n")
        self.assertEqual(run_git(outer, "status", "--porcelain", "--ignore-submodules=none"), "")
        self.assert_capture_blocked(outer, "submodules")

    def test_release_checks_historical_commit_for_gitlinks(self) -> None:
        project = self.project()
        location, evidence = self.evidence(project)
        dependency = self.project("dependency")
        self.add_submodule(project, dependency)
        revision = run_git(project, "rev-parse", "HEAD")
        # Simulate a previously issued record with a clean commit attribution.
        # A schema marker alone must not make unsupported commit coverage valid.
        for key in ("target_state", "final_state"):
            evidence[key]["head_revision"] = revision
            evidence[key]["identity"] = revision
        location.write_text(json.dumps(evidence))
        report = self.assert_release(project, location, evidence, 1)
        self.assertIn("submodules", " ".join(report["problems"]))

    def test_original_clean_commit_remains_valid_after_checkout_changes(self) -> None:
        project = self.project()
        location, evidence = self.evidence(project)
        (project / "app.py").write_text("VALUE = 3\n")
        dependency = self.project("dependency")
        self.add_submodule(project, dependency)
        self.assert_release(project, location, evidence, 0)

    def test_historical_subtree_uses_commit_coverage_not_current_ignore_policy(self) -> None:
        root, project = self.nested_project(ignored_runs=False)
        commit(root, "packages/app/app.py")
        location, evidence = self.evidence(project)
        self.assertFalse(evidence["target_state"]["dirty"])
        (root / ".gitignore").write_text("packages/\n")
        commit(root, ".gitignore")
        self.assert_release(project, location, evidence, 0)

    def test_clean_commit_must_actually_contain_the_recorded_project_subtree(self) -> None:
        root = self.project()
        location, evidence = self.evidence(root)
        project = root / "scratch"
        project.mkdir()
        (project / "app.py").write_text("VALUE = 2\n")
        evidence["plan"] = str(location.parent / "plan.json")
        for key in ("target_state", "final_state"):
            evidence[key]["project_subpath"] = "scratch"
            evidence[key]["excluded_paths"].append("scratch/.rung/runs")
        location.write_text(json.dumps(evidence))
        report = self.assert_release(project, location, evidence, 1)
        self.assertIn("does not contain", " ".join(report["problems"]))

    def test_unversioned_state_evidence_requires_rerun(self) -> None:
        project = self.project()
        location, evidence = self.evidence(project)
        for key in ("target_state", "final_state"):
            evidence[key].pop("schema_version")
        location.write_text(json.dumps(evidence))
        report = self.assert_release(project, location, evidence, 1)
        self.assertIn("rerun verification", " ".join(report["problems"]))

    def test_release_rejects_wrong_project_scope_and_arbitrary_exclusions(self) -> None:
        root, project = self.nested_project(ignored_runs=False)
        location, evidence = self.evidence(project)
        evidence["plan"] = str(location.parent / "plan.json")
        location.write_text(json.dumps(evidence))
        report = self.assert_release(root, location, evidence, 1)
        self.assertIn("project_subpath", " ".join(report["problems"]))
        for state in ("target_state", "final_state"):
            evidence[state]["excluded_paths"].append("packages/app/app.py")
        location.write_text(json.dumps(evidence))
        report = self.assert_release(project, location, evidence, 1)
        self.assertIn("exclusions", " ".join(report["problems"]))

    def test_filesystem_evidence_does_not_silently_become_git_evidence(self) -> None:
        project = self.project(git=False)
        location, evidence = self.evidence(project)
        run_git(project, "init", "--quiet")
        commit(project, "app.py")
        report = self.assert_release(project, location, evidence, 1)
        self.assertIn("filesystem evidence", " ".join(report["problems"]))

    def test_unborn_empty_git_repository_has_working_tree_evidence(self) -> None:
        project = self.base / "unborn"
        project.mkdir()
        run_git(project, "init", "--quiet")
        location, evidence = create_passing_evidence(project)
        self.assertEqual(evidence["status"], "pass")
        self.assertIsNone(evidence["target_state"]["head_revision"])
        self.assert_release(project, location, evidence, 0)

    def test_normal_rename_delete_and_staged_then_deleted_paths(self) -> None:
        for mode in ("rename", "delete", "staged-delete", "added-deleted"):
            with self.subTest(mode=mode):
                project = self.project(mode)
                (project / "other.py").write_text("VALUE = 2\n")
                commit(project)
                if mode == "rename":
                    run_git(project, "mv", "other.py", "renamed.py")
                    changed_path = project / "renamed.py"
                elif mode == "staged-delete":
                    run_git(project, "rm", "other.py")
                    changed_path = project / "other.py"
                else:
                    changed_path = project / "other.py"
                    if mode == "added-deleted":
                        changed_path = project / "added.py"
                        changed_path.write_text("VALUE = 2\n")
                        run_git(project, "add", "added.py")
                    changed_path.unlink()
                location, evidence = self.evidence(project)
                self.assert_release(project, location, evidence, 0)
                changed_path.write_text("VALUE = 3\n")
                self.assert_release(project, location, evidence, 1)

    def test_untracked_nested_repository_is_blocked(self) -> None:
        for git in (True, False):
            with self.subTest(git=git):
                project = self.project(f"root-{git}", git=git)
                self.project(f"root-{git}/nested")
                self.assert_capture_blocked(project, "repository" if git else "repositories")

    def test_ignored_selected_project_is_blocked(self) -> None:
        root = self.project()
        (root / ".gitignore").write_text("scratch/\n")
        commit(root, ".gitignore")
        for name in ("scratch", "scratch/nested"):
            with self.subTest(name=name):
                project = root / name
                project.mkdir(parents=True, exist_ok=True)
                (project / "app.py").write_text("VALUE = 2\n")
                self.assert_capture_blocked(project, "ignored by Git")

    @unittest.skipIf(hasattr(os, "geteuid") and os.geteuid() == 0, "root bypasses file permissions")
    def test_git_status_partial_scan_warning_blocks_capture(self) -> None:
        project = self.project()
        unreadable = project / "untracked"
        unreadable.mkdir()
        (unreadable / "app.py").write_text("VALUE = 3\n")
        unreadable.chmod(0)
        try:
            self.assert_capture_blocked(project, "Git status emitted diagnostics")
        finally:
            unreadable.chmod(0o700)

    @unittest.skipIf(hasattr(os, "geteuid") and os.geteuid() == 0, "root bypasses file permissions")
    def test_unreadable_source_is_blocked(self) -> None:
        project = self.project(git=False)
        source = project / "app.py"
        source.chmod(0)
        try:
            self.assert_capture_blocked(project, "Cannot read")
        finally:
            source.chmod(0o600)


if __name__ == "__main__":
    unittest.main()
