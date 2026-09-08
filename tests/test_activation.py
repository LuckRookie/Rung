from __future__ import annotations

import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "rung" / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


scope = load_script("evaluate_scope")
validator = load_script("validate_contract")


class ActivationTests(unittest.TestCase):
    def test_labeled_scenarios(self):
        cases = json.loads((ROOT / "evals" / "activation-cases.json").read_text())
        for case in cases:
            with self.subTest(case=case["id"]):
                result = scope.evaluate_scope(case["judgments"])
                self.assertEqual(result["status"], "pass")
                self.assertEqual(result["scope"], case["expected"]["scope"])
                self.assertEqual(result["activation"], case["expected"]["activation"])
                self.assertEqual(
                    result["exited_before_references"], result["activation"] != "enter"
                )

    def test_explicit_invocation_never_supplies_membership(self):
        for relation, claim in [("absent", "present"), ("present", "absent"), ("mixed", "absent")]:
            for materiality in ["present", "absent", "uncertain"]:
                with self.subTest(relation=relation, claim=claim, materiality=materiality):
                    result = scope.evaluate_scope(
                        {
                            "codebase_relationship": relation,
                            "development_claim": claim,
                            "invocation_mode": "explicit",
                            "materiality": materiality,
                        }
                    )
                    self.assertEqual(result["activation"], "bypass")

    def test_old_input_does_not_assume_materiality(self):
        result = scope.evaluate_scope(
            {
                "codebase_relationship": "present",
                "development_claim": "present",
            }
        )
        self.assertEqual(result["scope"], "development")
        self.assertEqual(result["activation"], "defer")
        self.assertEqual(result["schema_version"], 2)

    def test_invalid_values_produce_structured_errors(self):
        for field in [
            "codebase_relationship",
            "development_claim",
            "materiality",
            "invocation_mode",
        ]:
            for bad in [None, [], {}, True, 5, "invalid"]:
                with self.subTest(field=field, bad=bad):
                    data = {
                        "codebase_relationship": "present",
                        "development_claim": "present",
                        "materiality": "present",
                        "invocation_mode": "implicit",
                    }
                    data[field] = bad
                    result = scope.evaluate_scope(data)
                    self.assertEqual(result["status"], "error")
                    self.assertTrue(result["problems"])

    def test_reclassification_has_no_sticky_activation(self):
        data = {"codebase_relationship": "present", "development_claim": "present"}
        observed = []
        for materiality in ["absent", "uncertain", "present", "absent"]:
            observed.append(
                scope.evaluate_scope({**data, "materiality": materiality})["activation"]
            )
        self.assertEqual(observed, ["bypass", "defer", "enter", "bypass"])


class PrunedContractTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.skill = Path(temporary.name) / "rung"
        shutil.copytree(ROOT / "rung", self.skill, ignore=shutil.ignore_patterns("__pycache__"))
        self.contract = json.loads((self.skill / "contracts" / "rung-contract.json").read_text())

    def test_missing_stage_file_is_reported_without_crashing(self):
        (self.skill / "references" / "design.md").unlink()
        errors = validator.validate_contract(self.skill, self.contract)
        self.assertTrue(any("not found" in error for error in errors))

    def test_indirect_guides_remain_reachable(self):
        self.assertEqual(validator.validate_contract(self.skill, self.contract), [])
        path = self.skill / "references" / "orphan.md"
        path.write_text("# Unreachable\n")
        self.contract["concerns"].append(
            {
                "id": "orphan",
                "entry": "references/orphan.md",
                "kind": "guide",
                "max_bytes": 100,
                "signals": ["material choice"],
            }
        )
        errors = validator.validate_contract(self.skill, self.contract)
        self.assertIn("unreachable concern: references/orphan.md", errors)

    def test_lifecycle_is_a_catalog_not_a_mandatory_sequence(self):
        self.contract["lifecycle"].reverse()
        self.assertEqual(validator.validate_contract(self.skill, self.contract), [])
        self.contract["lifecycle"].pop()
        self.assertTrue(validator.validate_contract(self.skill, self.contract))

    def test_activation_contract_cannot_enable_routine_implicit_work(self):
        self.contract["activation"]["routine_activation"] = "enter"
        self.assertTrue(validator.validate_contract(self.skill, self.contract))

    def test_entrypoint_growth_is_rejected(self):
        with (self.skill / "SKILL.md").open("a") as output:
            output.write("x" * 2400)
        errors = validator.validate_contract(self.skill, self.contract)
        self.assertIn("entrypoint exceeds 2400 bytes", errors)
