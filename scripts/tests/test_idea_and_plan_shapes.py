"""Tests for the idea and plan trees in the shapes template, and for the archive being opt-in."""

import os
import unittest

from sphere_testing import SphereCase

IDEA = """\
---
idea: 20261101-quiet-hours
title: Quiet hours for notifications
captured: 2026-11-01
topics: [home, home.evenings]
stage: shaping
refinements: 2
refined: 2026-11-05
related: [20261020-evening-routine]
change: add
horizon: soon
---

Body text is never read by the check.
"""

PLAN = """\
---
plan: kitchen-spring
title: Kitchen by spring
for: [work:home.kitchen]
state: active
version: 1.2
summary: Plumbing first, then cabinets.
created: 2026-10-01
updated: 2026-11-10
---
"""


class IdeaShapeTest(SphereCase):
    use_git: bool = False  # the shape check needs no git; this keeps the tests quick

    live: str = "layers/ideas/20261101-quiet-hours.md"
    archived: str = "layers/ideas/archived/20261101-quiet-hours.md"

    def idea(self, old: str = "", new: str = "", path: str = "") -> str:
        self.write(path or self.live, IDEA.replace(old, new) if old else IDEA)
        return self.check().out

    def test_a_valid_idea_is_clean(self):
        self.assertIn("structure-check: clean", self.idea())

    def test_a_raw_idea_needs_no_refined_date(self):
        out = self.idea("stage: shaping\nrefinements: 2\nrefined: 2026-11-05\n", "stage: raw\nrefinements: 0\n")
        self.assertIn("structure-check: clean", out)
        out = self.idea(
            "stage: shaping\nrefinements: 2\nrefined: 2026-11-05\n", "stage: raw\nrefinements: 0\nrefined:\n"
        )
        self.assertIn("structure-check: clean", out)

    def test_name_and_key_formats(self):
        self.write("layers/ideas/Quiet.md", IDEA)
        out = self.check().out
        self.assertIn("name 'Quiet' doesn't match", out)
        self.assertIn("idea is '20261101-quiet-hours', but the node is named 'Quiet'", out)
        out = self.idea("captured: 2026-11-01", "captured: 2026-13-01")
        self.assertIn("captured is '2026-13-01', expected a date", out)
        out = self.idea("topics: [home, home.evenings]", "topics: [Home, home..x]")
        self.assertIn("topics has items that don't match", out)
        self.assertIn("Home home..x", out)
        self.assertIn("refinements is 'two'", self.idea("refinements: 2", "refinements: two"))
        self.assertIn("horizon is 'later'", self.idea("horizon: soon", "horizon: later"))
        self.assertIn("change is 'rewrite'", self.idea("change: add", "change: rewrite"))

    def test_empty_topics_are_fine(self):
        self.assertIn("structure-check: clean", self.idea("topics: [home, home.evenings]", "topics: []"))

    def test_captured_matches_the_name(self):
        out = self.idea("captured: 2026-11-01", "captured: 2026-11-02")
        self.assertIn("captured is '2026-11-02', but the name starts with 20261101", out)

    def test_raw_exactly_when_unrefined(self):
        out = self.idea("stage: shaping", "stage: raw")
        self.assertIn("stage is raw, so refinements should be 0 (it's 2)", out)
        out = self.idea("refinements: 2\nrefined: 2026-11-05\n", "refinements: 0\n")
        self.assertIn("refinements is 0, so stage should be raw (it's shaping)", out)
        out = self.idea("refined: 2026-11-05\n", "")
        self.assertIn("needs 'refined'", out)

    def test_keys_in_order(self):
        out = self.idea(
            "title: Quiet hours for notifications\ncaptured: 2026-11-01\n",
            "captured: 2026-11-01\ntitle: Quiet hours for notifications\n",
        )
        self.assertIn("keys out of order; the idea shape's order is: idea title captured", out)

    def test_outcome_exactly_when_archived(self):
        out = self.idea("horizon: soon\n", "horizon: soon\noutcome: parked not now\n")
        self.assertIn("'outcome' belongs only to archived nodes", out)
        self.write(self.archived, IDEA)
        out = self.check("--archive").out
        self.assertIn("archived, so it needs 'outcome'", out)

    def test_outcome_forms(self):
        def archived_with(outcome: str) -> str:
            self.write(self.archived, IDEA.replace("change: add", f"outcome: {outcome}\nchange: add"))
            return self.check("--archive").out

        self.assertIn("structure-check: clean", archived_with("graduated work:home.quiet-hours"))
        self.assertIn("structure-check: clean", archived_with("parked waiting on the new router"))
        self.assertIn("graduated <tree:name>", archived_with("graduated"))
        self.assertIn("parked <reason>", archived_with("parked"))
        self.assertIn(
            "outcome is 'shelved for now', expected one of: graduated parked", archived_with("shelved for now")
        )

    def test_the_archive_is_opt_in(self):
        self.write(self.archived, "# no frontmatter\n")
        self.assertIn("structure-check: clean", self.check().out)
        self.assertIn("no frontmatter", self.check("--archive").out)
        self.assertIn("no frontmatter", self.check(self.archived).out)  # a named node is always checked


class PlanShapeTest(SphereCase):
    use_git: bool = False

    folder: str = "layers/work/plans/kitchen-spring"

    def plan(self, old: str = "", new: str = "", folder: str = "") -> str:
        folder = folder or self.folder
        self.write(f"{folder}/plan.md", PLAN.replace(old, new) if old else PLAN)
        self.write(f"{folder}/history.md", "## 2026-10-01 — created\n")
        return self.check("--archive").out

    def test_a_valid_plan_is_clean(self):
        self.assertIn("structure-check: clean", self.plan())

    def test_plan_files_and_formats(self):
        self.plan()
        os.remove(self.path(f"{self.folder}/history.md"))
        self.assertIn("missing history.md (history)", self.check().out)
        self.assertIn(
            "plan is 'kitchen', but the node is named 'kitchen-spring'",
            self.plan("plan: kitchen-spring", "plan: kitchen"),
        )
        self.assertIn("for needs at least one item", self.plan("for: [work:home.kitchen]", "for: []"))
        self.assertIn("for has items that don't match", self.plan("for: [work:home.kitchen]", "for: [home.kitchen]"))
        self.assertIn("version is '1'", self.plan("version: 1.2", "version: 1"))
        self.assertIn("state is 'paused'", self.plan("state: active", "state: paused"))
        self.assertIn("missing key 'summary'", self.plan("summary: Plumbing first, then cabinets.\n", ""))

    def test_dates(self):
        self.assertIn(
            "updated (2026-09-01) is before created (2026-10-01)",
            self.plan("updated: 2026-11-10", "updated: 2026-09-01"),
        )
        self.assertIn("created is 'October'", self.plan("created: 2026-10-01", "created: October"))

    def test_state_by_place(self):
        self.assertIn(
            "state is done, so it belongs in layers/work/plans/archived/", self.plan("state: active", "state: done")
        )
        archived = "layers/work/plans/archived/kitchen-spring"
        self.write(f"{self.folder}/plan.md", PLAN)
        out = self.plan(folder=archived)
        self.assertIn("archived, so state should be done or dropped (it's active)", out)
        self.assertIn("structure-check: clean", self.plan("state: active", "state: dropped", folder=archived))

    def test_parent_plan(self):
        out = self.plan("title:", "parent: cabinets\ntitle:")
        self.assertIn("keys out of order", out)
        out = self.plan("for:", "parent: cabinets\nfor:")
        self.assertIn("parent plan 'cabinets' doesn't exist", out)
        self.write("layers/work/plans/archived/cabinets/plan.md", PLAN)
        self.assertNotIn("parent plan", self.check().out)  # the archived parent is found by its folder alone
        self.assertIn("isn't its own parent", self.plan("for:", "parent: kitchen-spring\nfor:"))


if __name__ == "__main__":
    unittest.main()
