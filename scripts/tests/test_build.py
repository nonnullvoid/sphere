"""Tests for scripts/new-sphere and the base build: a fresh sphere assembles, inits and checks clean."""

import os
import re
import shutil
import tempfile
import unittest

from sphere_testing import SCRIPTS, run

NEW_SPHERE = os.path.join(SCRIPTS, "new-sphere")
LINK = re.compile(r"\]\(([^)\s]+)\)")


class BaseBuildTest(unittest.TestCase):
    base: str = ""  # set in setUp, the unittest way
    root: str = ""  # set in setUp, the unittest way

    def setUp(self):
        self.base = tempfile.mkdtemp(prefix="sphere-build-test-")
        self.root = os.path.join(self.base, "my-sphere")
        result = run([NEW_SPHERE, "base", self.root], cwd=self.base)
        self.assertEqual(result.code, 0, result.text)

    def tearDown(self):
        shutil.rmtree(self.base, ignore_errors=True)

    def read(self, path: str) -> str:
        with open(os.path.join(self.root, path), encoding="utf-8") as handle:
            return handle.read()

    def test_assembles_the_build_over_the_common_set(self):
        for path in [
            "AGENTS.md",
            "CLAUDE.md",
            "sphere.md",
            "core/init.md",
            "core/engine.md",
            "core/build.json",
            "core/protocol/protocol.md",
            "core/protocol/lenses/principles.md",
            "core/protocol/frames/sphere-framework/reactions.md",
            "layers/projections/templates/dashboard/template.md",
            "surface/projections.html",
            "surface/projections/me/today/index.html",
            "scripts/sphere",
            "scripts/shapes",
        ]:
            self.assertTrue(os.path.isfile(os.path.join(self.root, path)), path)
        self.assertEqual(self.read("CLAUDE.md").strip(), "@AGENTS.md")
        self.assertIn('name: "today"', self.read("surface/projections/assets/registry.js"))
        self.assertFalse(os.path.exists(os.path.join(self.root, "README.md")))

    def test_ships_every_common_lens(self):
        lenses = os.listdir(os.path.join(self.root, "core/protocol/lenses"))
        self.assertEqual(len(lenses), 18)  # the 17 common lenses and the empty principles slot

    def test_refuses_a_folder_with_something_in_it(self):
        result = run([NEW_SPHERE, "base", self.root], cwd=self.base)
        self.assertEqual(result.code, 2)
        self.assertIn("already has something in it", result.err)

    def test_a_fresh_sphere_inits_and_checks_clean(self):
        run(["git", "init", "-q", "-b", "main"], cwd=self.root)
        run(["git", "config", "user.email", "test@example.com"], cwd=self.root)
        run(["git", "config", "user.name", "Test"], cwd=self.root)
        init = run([os.path.join(self.root, "scripts", "sphere"), "init", "--git"], cwd=self.root)
        self.assertEqual(init.code, 0, init.text)
        self.assertIn("Sphere ready", init.out)
        structure = run([os.path.join(self.root, "scripts", "structure-check")], cwd=self.root)
        self.assertEqual(structure.out.strip(), "structure-check: clean")
        manifest = run([os.path.join(self.root, "scripts", "manifest-check")], cwd=self.root)
        self.assertEqual(
            manifest.out.strip().splitlines(),
            ["core/manifest.md: no manifest yet: build it from the lenses and frames", "manifest-check: 1 to look at"],
        )

    def test_links_inside_the_sphere_resolve(self):
        broken: list[str] = []
        for folder, _, names in os.walk(self.root):
            for name in names:
                if not name.endswith(".md"):
                    continue
                path = os.path.join(folder, name)
                with open(path, encoding="utf-8") as handle:
                    text = re.sub(r"```.*?```", "", handle.read(), flags=re.S)
                for target in LINK.findall(text):
                    target = target.split("#")[0]
                    if not target or re.match(r"^[a-z]+:", target):
                        continue
                    resolved = os.path.normpath(os.path.join(folder, target))
                    if resolved == os.path.join(self.root, "core", "manifest.md"):
                        continue  # built in the first conversation
                    if not os.path.exists(resolved):
                        broken.append(f"{os.path.relpath(path, self.root)} → {target}")
        self.assertEqual(broken, [])

    def test_optional_frames_link_correctly_once_adopted(self):
        optional = os.path.join(SCRIPTS, "..", "common", "optional", "frames")
        for folder, _, names in os.walk(optional):
            for name in names:
                adopted = os.path.join(self.root, "core", "protocol", "frames", os.path.relpath(folder, optional), name)
                shutil.copy2(os.path.join(folder, name), adopted)
        out = run([os.path.join(self.root, "scripts", "manifest-check")], cwd=self.root).out
        self.assertNotIn("links to", out)


if __name__ == "__main__":
    unittest.main()
