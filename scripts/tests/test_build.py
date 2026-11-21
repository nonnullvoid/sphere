"""Tests for scripts/new-sphere and the base build: a fresh sphere assembles, inits and checks clean."""

import os
import re
import shutil
import tempfile
import unittest

from sphere_testing import SCRIPTS, run

NEW_SPHERE = os.path.join(SCRIPTS, "new-sphere")
LINK = re.compile(r"\]\(([^)\s]+)\)")


class BuildCase(unittest.TestCase):
    """A fresh sphere, assembled from the base build in a temporary folder."""

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


class BaseBuildTest(BuildCase):
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
        imports = ["@AGENTS.md", "@sphere.md", "@core/engine.md", "@core/manifest.md", "@core/init.md"]
        self.assertEqual(self.read("CLAUDE.md").split(), imports)
        for line in imports:
            self.assertTrue(os.path.isfile(os.path.join(self.root, line[1:])), line)
        self.assertIn("## First run", self.read("AGENTS.md"))
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
        who = {"GIT_AUTHOR_NAME": "Test", "GIT_AUTHOR_EMAIL": "test@example.com"}
        who.update(GIT_COMMITTER_NAME="Test", GIT_COMMITTER_EMAIL="test@example.com")
        init = run([os.path.join(self.root, "scripts", "sphere"), "init", "--git"], cwd=self.root, env=who)
        self.assertEqual(init.code, 0, init.text)
        self.assertIn("Sphere ready", init.out)
        status = run(["git", "status", "--porcelain"], cwd=self.root)
        self.assertEqual(status.out, "", "the whole assembled build is in the first commit")
        structure = run([os.path.join(self.root, "scripts", "structure-check")], cwd=self.root)
        self.assertEqual(structure.out.strip(), "structure-check: clean")
        manifest = run([os.path.join(self.root, "scripts", "manifest-check")], cwd=self.root)
        self.assertEqual(manifest.out.strip(), "manifest-check: clean")  # new-sphere built it
        opened = run(
            [os.path.join(self.root, "scripts", "sphere"), "open", "garden", "-i", "Plant a garden"], cwd=self.root
        )
        self.assertIn("sense: focus-opened\n  focus-holds (", opened.out)  # each sense comes with its reactions
        self.assertIn("focus-nodes (if it's the first focus", opened.out)

    def test_the_manifest_is_built_by_script_and_fits_its_budget(self):
        manifest = self.read("core/manifest.md")
        self.assertLess(len(manifest.encode()), 12 * 1024)
        for part in ["## Always on", "## Lenses", "## Frames", "- `outbound-guard`:", "- `focus-nodes`:"]:
            self.assertIn(part, manifest)
        sphere = os.path.join(self.root, "scripts", "sphere")
        self.assertEqual(run([sphere, "init"], cwd=self.root).code, 0)
        self.assertEqual(run([sphere, "manifest"], cwd=self.root).code, 0)
        undated = re.compile(r"^_Built [0-9-]+ ", re.M)  # the same files always build the same manifest
        self.assertEqual(undated.sub("", self.read("core/manifest.md")), undated.sub("", manifest))
        reactions = run([sphere, "reactions", "stale-found", "knowledge:money"], cwd=self.root)
        self.assertIn("plans (if a plan's assumption points at the topic)", reactions.out)

    def test_claude_code_runs_the_startup_when_a_window_opens(self):
        self.assertIn("scripts/sphere start", self.read(".claude/settings.json"))

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


class ScriptDeliversTest(BuildCase):
    """The script hands the AI what it needs: the startup, the reactions, a fresh manifest."""

    who: dict[str, str] = {  # noqa: RUF012  # read-only
        "GIT_AUTHOR_NAME": "Test",
        "GIT_AUTHOR_EMAIL": "test@example.com",
        "GIT_COMMITTER_NAME": "Test",
        "GIT_COMMITTER_EMAIL": "test@example.com",
    }

    def sphere(self, *args: str):
        return run([os.path.join(self.root, "scripts", "sphere"), *args], cwd=self.root, env=self.who)

    def write(self, path: str, text: str, mode: str = "w") -> None:
        with open(os.path.join(self.root, path), mode, encoding="utf-8") as handle:
            handle.write(text)

    def entry(self, focus: str) -> None:
        self.write(
            f"layers/focus/{focus}/history.md", "\n## 2026-11-20 12:00 — a change\n\n**Did:** Changed it.\n", "a"
        )

    def test_start_before_and_after_setup(self):
        self.assertIn("hasn't been set up yet", self.sphere("start").out)
        self.assertEqual(self.sphere("init", "--git").code, 0)
        alone = self.sphere("start")
        self.assertIn("f0-main open · the sphere", alone.out)
        self.assertIn("sense: focus-attached\n", alone.out)
        self.assertIn("== using the sphere: skimmed", alone.out)  # how much to explain, handed over
        self.assertIn("== you are companion", alone.out)
        self.sphere("open", "garden", "-i", "Plant a garden")
        one = self.sphere("start")
        self.assertIn("== f1-garden", one.out)  # the one open focus, attached once
        self.sphere("open", "taxes", "-i", "File the taxes")
        several = self.sphere("start")
        self.assertIn("Several are open", several.out)
        self.assertNotIn("open · foreground", several.out)

    def test_getting_started_holds_the_sphere_subject(self):
        self.sphere("init", "--git")
        opened = self.sphere(
            "open", "getting-started", "-i", "Get comfortable using the sphere", "--holds", "literacy:sphere"
        )
        self.assertEqual(opened.code, 0, opened.text)
        self.assertIn("literacy:sphere → layers/literacy/sphere", self.sphere("attach", "f1").out)
        structure = run([os.path.join(self.root, "scripts", "structure-check")], cwd=self.root)
        self.assertEqual(structure.out.strip(), "structure-check: clean")

    def test_start_names_the_human_from_their_profile(self):
        self.sphere("init", "--git")
        profile = self.read("core/user/profile.md")
        self.write(
            "core/user/profile.md", profile.replace("## In a few lines\n", "## In a few lines\n\nI'm Kane.\n", 1)
        )
        self.assertIn("== who you're working with (their profile): I'm Kane.", self.sphere("start").out)

    def test_ground_writes_its_own_entry_with_the_clocks_time(self):
        self.sphere("init", "--git")
        self.write("layers/focus/f0-main/history.md", "\n## 2099-01-01 09:00 — invented\n\n**Did:** Old.\n", "a")
        grounded = self.sphere("ground", "main", "--reacted", "--did", "Planted the tomatoes.", "--next", "Water them.")
        self.assertEqual(grounded.code, 0, grounded.text)
        self.assertEqual(
            run(["git", "log", "-1", "--format=%s"], cwd=self.root).out.strip(),
            "ground [f0-main] — Planted the tomatoes.",
        )
        top = self.read("layers/focus/f0-main/history.md").split("\n")[0]
        self.assertRegex(
            top, r"^## \d{4}-\d{2}-\d{2} \d{2}:\d{2} — grounded$"
        )  # the newest entry is first, stamped now
        self.assertIn(
            "**Next:** Water them.", self.sphere("attach", "main").out + self.read("layers/focus/f0-main/history.md")
        )

    def test_a_ground_stops_until_its_reactions_are_handled(self):
        self.sphere("init", "--git")
        self.sphere("open", "garden", "-i", "Plant a garden")
        self.entry("f1-garden")
        first = self.sphere("ground", "f1")
        self.assertEqual(first.code, 3, first.text)
        self.assertIn("sense: focus-grounding\n", first.out)
        self.assertIn("--reacted", first.err)
        second = self.sphere("ground", "f1", "--reacted")
        self.assertEqual(second.code, 0, second.text)
        self.assertIn("Grounded f1-garden", second.out)

    def test_a_ground_rebuilds_a_stale_manifest_with_the_change(self):
        self.sphere("init", "--git")
        self.write("core/protocol/lenses/principles.md", "\nAlways ask before spending money.\n", "a")
        self.entry("f0-main")
        grounded = self.sphere("ground", "main", "--reacted")
        self.assertEqual(grounded.code, 0, grounded.text)
        committed = run(["git", "show", "--name-only", "--format=", "HEAD"], cwd=self.root).out
        self.assertIn("core/manifest.md", committed)
        self.assertEqual(
            run([os.path.join(self.root, "scripts", "manifest-check")], cwd=self.root).out.strip(),
            "manifest-check: clean",
        )


if __name__ == "__main__":
    unittest.main()
