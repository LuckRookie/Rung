from __future__ import annotations

import io
import json
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class DistributionTests(unittest.TestCase):
    def assert_installable(self, exported: Path, *, core_contract: bool) -> None:
        skill = exported / "rung"
        self.assertRegex((skill / "SKILL.md").read_text(), r"(?m)^name: rung$")
        self.assertTrue((exported / "INSTALL.md").is_file())
        for directory in ("agents", "references", "profiles", "assets", "scripts"):
            self.assertTrue((skill / directory).is_dir(), directory)
        for document in skill.rglob("*.md"):
            for link in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", document.read_text()):
                if re.match(r"^[a-z][a-z0-9+.-]*:", link, re.IGNORECASE):
                    continue
                target = (document.parent / link).resolve()
                self.assertTrue(target.is_relative_to(skill.resolve()), (document, link))
                self.assertTrue(target.exists(), (document, link))

        contract = skill / "contracts/rung-contract.json"
        validator = skill / "scripts/validate_contract.py"
        self.assertEqual(contract.is_file(), core_contract)
        self.assertEqual(validator.is_file(), core_contract)
        if core_contract:
            result = subprocess.run(
                [sys.executable, "-B", str(validator), "--skill-root", str(skill)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_candidate_package_validates_after_installation_copy(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            destination = Path(temporary)
            shutil.copytree(
                ROOT / "rung", destination / "rung", ignore=shutil.ignore_patterns("__pycache__")
            )
            shutil.copy2(ROOT / "INSTALL.md", destination / "INSTALL.md")
            self.assert_installable(destination, core_contract=True)

    def test_stable_tag_uses_its_own_package_and_install_contract(self) -> None:
        contract = json.loads((ROOT / "rung/contracts/rung-contract.json").read_text())
        reference = contract["package"]["stable_ref"]
        archived = subprocess.run(
            ["git", "-C", str(ROOT), "archive", "--format=tar", reference, "rung", "INSTALL.md"],
            capture_output=True,
            check=False,
        )
        self.assertEqual(
            archived.returncode,
            0,
            f"Fetch stable tag {reference} before testing distribution: "
            + archived.stderr.decode(errors="replace"),
        )
        with tempfile.TemporaryDirectory() as temporary:
            destination = Path(temporary)
            with tarfile.open(fileobj=io.BytesIO(archived.stdout)) as archive:
                for member in archive.getmembers():
                    relative = Path(member.name)
                    self.assertFalse(relative.is_absolute() or ".." in relative.parts)
                    if member.isdir():
                        continue
                    self.assertTrue(member.isfile(), member.name)
                    source = archive.extractfile(member)
                    assert source is not None
                    target = destination / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(source.read())
            # Use the selected tag's capabilities. Future stable packages may
            # carry their own validator; v0.1.0 predates that capability.
            self.assert_installable(
                destination,
                core_contract=(destination / "rung/contracts/rung-contract.json").is_file(),
            )


if __name__ == "__main__":
    unittest.main()
