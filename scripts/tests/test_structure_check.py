"""Tests for scripts/structure-check: it reports, never fixes, and blocks only with --strict."""

import os
import sys
import unittest

from sphere_testing import REPO, SHAPES_TEMPLATE, STRUCTURE_CHECK, SphereCase, run


class StructureCheckTest(SphereCase):
    focus: str  # pyright: ignore[reportUninitializedInstanceVariable]  # set in setUp, the unittest way

    def setUp(self):
        super().setUp()
        self.ok("open", "kitchen", "-i", "Renovate the kitchen")
        self.focus = "layers/focus/f1-kitchen/focus.md"

    def bend(self, old: str, new: str) -> None:
        self.write(self.focus, self.read(self.focus).replace(old, new))

    def test_clean(self):
        result = self.check()
        self.assertEqual((result.code, result.out.strip()), (0, "structure-check: clean"))

    def test_reports_but_never_fixes_or_blocks(self):
        self.bend("status: open", "status: in progress")
        before = self.read(self.focus)
        result = self.check()
        self.assertEqual(result.code, 0)
        self.assertIn("status is 'in progress', expected one of: open closed", result.out)
        self.assertIn("structure-check: 1 to look at", result.out)
        self.assertEqual(self.read(self.focus), before)
        self.assertEqual(self.check("--strict").code, 1)

    def test_keys(self):
        self.bend("persona:\n", "mood: good\naka: [again]\n")
        out = self.check().out
        self.assertIn("key 'mood' isn't in the focus shape", out)
        self.assertIn("key 'aka' appears twice", out)
        self.assertIn("missing key 'persona'", out)

    def test_unclosed_and_missing_frontmatter(self):
        self.write(self.focus, self.read(self.focus).replace("opened:", "opened-x:").split("\n---\n")[0])
        self.assertIn("frontmatter isn't closed with ---", self.check().out)
        self.write(self.focus, "# no frontmatter\n")
        self.assertIn("no frontmatter", self.check().out)

    def test_focus_tree_rules(self):
        self.bend("parent: f0", "parent: f9")
        self.assertIn("parent f9 doesn't exist", self.check().out)
        self.bend("parent: f9", "parent: f0")
        self.bend("status: open", "status: closed")
        self.assertIn("closed but not moved to archived/", self.check().out)
        self.bend("status: closed", "status: open")
        self.bend("name: kitchen", "name: bathroom")
        self.assertIn("name 'bathroom' doesn't match the folder", self.check().out)
        os.rename(self.path("layers/focus/f1-kitchen"), self.path("layers/focus/Kitchen"))
        self.assertIn("folder isn't named f<number>-<name>", self.check().out)

    def test_missing_history(self):
        os.remove(self.path("layers/focus/f1-kitchen/history.md"))
        self.assertIn("missing history.md (history)", self.check().out)

    def test_repository_lines(self):
        self.write(".gitattributes", "")
        self.write(".gitignore", "")
        out = self.check().out
        self.assertIn("no union merge for history.md", out)
        self.assertIn("surface/state/ isn't ignored", out)

    def test_only_named_nodes(self):
        self.bend("status: open", "status: maybe")
        result = self.check("layers/focus/f1-kitchen")
        self.assertIn("status is 'maybe'", result.out)
        self.assertNotIn("structure-check:", result.out)
        self.assertIn("not in any declared tree", self.check("notes/x.md").out)

    def test_reads_core_shapes_from_the_sphere(self):
        self.append("core/shapes", "\ntree note\nnodes file notes\nkeys title\n")
        self.write("notes/a.md", "---\ntitle: A\n---\n")
        self.write("notes/b.md", "---\ntopic: B\n---\n")
        out = self.check().out
        self.assertIn("notes/b.md: missing key 'title'", out)
        self.assertNotIn("notes/a.md", out)
        os.remove(self.path("core/shapes"))
        result = self.check()
        self.assertEqual(result.code, 2)
        self.assertIn("no shapes file at core/shapes", result.err)
        self.assertIn("clean", self.check("--shapes", SHAPES_TEMPLATE).out)


class RepositoryCommonTest(unittest.TestCase):
    def test_the_repos_lenses_and_frames_are_in_shape(self):
        result = run(
            [sys.executable, STRUCTURE_CHECK, "--root", os.path.join(REPO, "common"), "--shapes", SHAPES_TEMPLATE], REPO
        )
        self.assertEqual(result.out.strip(), "structure-check: clean", result.text)


if __name__ == "__main__":
    unittest.main()
