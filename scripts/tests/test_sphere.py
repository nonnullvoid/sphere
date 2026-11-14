"""Tests for scripts/sphere, each in a throwaway sphere (git plus a bare remote) under the temp folder."""

import os
import shutil
import subprocess
import threading
import unittest

from sphere_testing import SHAPES_TEMPLATE, SphereCase


class InitTest(SphereCase):
    def test_init_makes_main_shapes_and_repository_lines(self):
        self.assertIn("number: f0", self.read("layers/focus/f0-main/focus.md"))
        self.assertEqual(self.field("layers/focus/f0-main/focus.md", "aka"), "[sphere]")
        self.assertIn("— opened", self.read("layers/focus/f0-main/history.md"))
        with open(SHAPES_TEMPLATE, encoding="utf-8") as template:
            self.assertEqual(self.read("core/shapes"), template.read())
        self.assertIn("history.md merge=union", self.read(".gitattributes"))
        self.assertIn("progress.md merge=union", self.read(".gitattributes"))
        self.assertIn("surface/state/", self.read(".gitignore"))
        self.assertEqual(self.subjects(), ["ground [f0-main] — sphere created"])
        self.assertIn("core/shapes", self.files_in())
        self.assertEqual(self.unsaved(), "")

    def test_init_twice_refuses(self):
        result = self.sphere("init")
        self.assertEqual(result.code, 1)
        self.assertIn("already a sphere", result.err)

    def test_new_sphere_is_in_shape(self):
        result = self.check()
        self.assertEqual(result.out.strip(), "structure-check: clean")

    def test_help(self):
        self.assertIn("usage: sphere <verb>", self.ok("--help").out)
        self.assertIn("--holds {back,release}", self.ok("close", "--help").out)


class OpenTest(SphereCase):
    def test_top_level_open_is_a_ground_of_main(self):
        result = self.ok("open", "kitchen-renovation", "-i", "Renovate the kitchen", "--holds", "work:home.kitchen")
        self.assertIn("f1-kitchen-renovation open · background · under f0-main", result.out)
        focus = "layers/focus/f1-kitchen-renovation/focus.md"
        self.assertEqual(self.field(focus, "parent"), "f0")
        self.assertEqual(self.field(focus, "holds"), "[work:home.kitchen]")
        self.assertEqual(self.field(focus, "status"), "open")
        self.assertEqual(self.subjects(), ["ground [f0-main] — opened f1-kitchen-renovation"])
        self.assertIn("opened f1-kitchen-renovation", self.read("layers/focus/f0-main/history.md"))
        self.assertEqual(self.git("rev-parse", "HEAD"), self.git("rev-parse", "origin/main"))
        self.assertEqual(self.unsaved(), "")

    def test_child_carves_an_equal_hold_out_of_its_parent(self):
        self.kitchen_and_plumbing()
        self.assertEqual(self.field("layers/focus/f1-kitchen-renovation/focus.md", "holds"), "[work:home.kitchen]")
        self.assertEqual(self.field("layers/focus/f2-plumbing-quotes/focus.md", "parent"), "f1")
        log = self.git("log", "--format=%s")
        self.assertIn(
            "ground [f1-kitchen-renovation] — opened f2-plumbing-quotes; carved work:home.kitchen.plumbing", log
        )

    def test_soft_claim_warns_but_opens(self):
        self.kitchen_and_plumbing()
        result = self.ok("open", "plumbing-install", "-i", "Get it installed", "--holds", "work:home.kitchen.plumbing")
        self.assertIn(
            "In focus already: work:home.kitchen.plumbing is already in focus in f2-plumbing-quotes", result.err
        )
        self.assertTrue(self.exists("layers/focus/f3-plumbing-install"))

    def test_attach_flag_brings_it_to_the_foreground(self):
        result = self.ok("open", "garden", "-i", "Plan the garden", "--attach")
        self.assertIn("foreground", result.out)
        self.assertTrue(self.exists("surface/state/focus/f1.json"))
        self.assertNotIn("surface/state", self.git("ls-files"))

    def test_bad_name_and_missing_intention_refused(self):
        self.assertEqual(self.sphere("open", "Kitchen Reno", "-i", "x").code, 1)
        self.assertIn("say what it's for", self.sphere("open", "kitchen").err)
        self.assertFalse(self.exists("layers/focus/f1-kitchen"))

    def test_numbers_come_from_the_folder_archived_included(self):
        self.ok("open", "one", "-i", "First")
        self.ok("open", "two", "-i", "Second")
        self.entry("f1-one", "Finished.")
        self.ok("close", "f1", "-m", "done")
        self.assertIn("f3-three open", self.ok("open", "three", "-i", "Third").out)

    def test_open_under_a_named_parent(self):
        self.ok("open", "bathroom", "-i", "Redo the bathroom")
        result = self.ok("open", "tiles", "-i", "Pick tiles", "--parent", "bathroom")
        self.assertIn("under f1-bathroom", result.out)


class GroundTest(SphereCase):
    def setUp(self):
        super().setUp()
        self.kitchen_and_plumbing()

    def test_changes_without_a_history_entry_stop(self):
        self.append("layers/work/home.kitchen.plumbing/work.md", "- two quotes in\n")
        head = self.git("rev-parse", "HEAD")
        result = self.sphere("ground", "f2", "-m", "two quotes")
        self.assertEqual(result.code, 3)
        self.assertIn("no new history entry", result.err)
        self.assertEqual(self.git("rev-parse", "HEAD"), head)

    def test_ground_commits_what_the_focus_holds_and_pushes(self):
        self.append("layers/work/home.kitchen.plumbing/work.md", "- two quotes in\n")
        self.append("layers/work/home.kitchen/work.md", "- cabinets chosen\n")
        self.entry("f2-plumbing-quotes", "Two quotes in.")
        result = self.ok("ground", "f2", "-m", "two quotes in")
        self.assertIn("Grounded f2-plumbing-quotes: 2 files", result.out)
        self.assertEqual(self.subjects(), ["ground [f2-plumbing-quotes] — two quotes in"])
        self.assertEqual(
            self.files_in(), ["layers/focus/f2-plumbing-quotes/history.md", "layers/work/home.kitchen.plumbing/work.md"]
        )
        self.assertIn("layers/work/home.kitchen/work.md", self.unsaved())
        self.assertEqual(self.git("rev-parse", "HEAD"), self.git("rev-parse", "origin/main"))

    def test_summary_defaults_to_the_entrys_did(self):
        self.entry("f2-plumbing-quotes", "Called the third plumber.")
        self.ok("ground", "f2")
        self.assertEqual(self.subjects(), ["ground [f2-plumbing-quotes] — Called the third plumber."])

    def test_out_of_focus_changes_never_stop_a_ground(self):
        self.write("notes/budget.md", "budget\n")
        self.git("add", "notes/budget.md")
        self.git("commit", "-q", "-m", "seed", "--", "notes/budget.md")
        self.write("notes/budget.md", "budget v2\n")
        self.write("scratch.txt", "scratch\n")
        self.append("layers/work/home.kitchen.plumbing/work.md", "- quote\n")
        self.entry("f2-plumbing-quotes", "A quote.")
        result = self.ok("ground", "f2")
        self.assertIn("Left for main (no open focus holds them): notes/budget.md, scratch.txt (new)", result.out)
        self.assertNotIn("notes/budget.md", self.files_in())
        # main's ground picks up the tracked one; the new file only when named
        self.entry("f0-main", "Took in the budget notes.")
        result = self.ok("ground", "-m", "took in the budget notes")
        self.assertEqual(self.files_in(), ["layers/focus/f0-main/history.md", "notes/budget.md"])
        self.assertIn("not grounded (often scratch; --also <path> to include): scratch.txt", result.out)
        self.entry("f0-main", "Kept the scratch file.")
        self.ok("ground", "--also", "scratch.txt")
        self.assertIn("scratch.txt", self.files_in())

    def test_report_adds_one_line_to_the_parent_once(self):
        self.append("layers/work/home.kitchen.plumbing/work.md", "- quote\n")
        self.assertEqual(self.sphere("ground", "f2", "--report", "two quotes in").code, 3)  # no entry yet
        self.entry("f2-plumbing-quotes", "Two quotes in.")
        self.ok("ground", "f2", "--report", "two quotes in")
        parent_history = self.read("layers/focus/f1-kitchen-renovation/history.md")
        self.assertEqual(parent_history.count("f2-plumbing-quotes: two quotes in"), 1)
        self.assertIn("layers/focus/f1-kitchen-renovation/history.md", self.files_in())
        listing = self.ok("list").out
        self.assertIn("f1-kitchen-renovation  foreground · grounded", listing)
        self.assertIn("· 1 waiting", listing)

    def test_most_specific_hold_wins(self):
        self.ok("open", "drafts", "-i", "Sort the drafts", "--parent", "f1", "--holds", "work:home.kitchen/drafts")
        self.write("layers/work/home.kitchen/drafts/a.md", "draft\n")
        self.write("layers/work/home.kitchen/plan.md", "plan\n")
        self.entry("f3-drafts", "First draft.")
        self.ok("ground", "f3")
        self.assertIn("layers/work/home.kitchen/drafts/a.md", self.files_in())
        self.assertNotIn("layers/work/home.kitchen/plan.md", self.files_in())
        self.assertEqual(self.field("layers/focus/f1-kitchen-renovation/focus.md", "holds"), "[work:home.kitchen]")

    def test_nothing_to_ground(self):
        self.assertIn("Nothing to ground in f2-plumbing-quotes.", self.ok("ground", "f2").out)

    def test_out_of_shape_focus_md_stops_the_ground(self):
        focus = "layers/focus/f2-plumbing-quotes/focus.md"
        self.write(focus, self.read(focus).replace("status: open", "status: in progress"))
        self.entry("f2-plumbing-quotes", "Something.")
        result = self.sphere("ground", "f2")
        self.assertEqual(result.code, 3)
        self.assertIn("status is 'in progress', expected one of: open closed", result.err)

    def test_ground_waits_for_the_lock(self):
        lock = self.path(".git/sphere-ground.lock")
        os.mkdir(lock)
        timer = threading.Timer(1.5, lambda: shutil.rmtree(lock))
        timer.start()
        try:
            self.entry("f2-plumbing-quotes", "Waited for the lock.")
            self.ok("ground", "f2")
        finally:
            timer.join()
        self.assertFalse(os.path.exists(lock))

    def test_ground_gives_up_on_a_held_lock(self):
        os.mkdir(self.path(".git/sphere-ground.lock"))
        self.entry("f2-plumbing-quotes", "Blocked.")
        result = self.sphere("ground", "f2")
        self.assertEqual(result.code, 1)
        self.assertIn("another ground holds the lock", result.err)

    def test_ground_takes_the_other_devices_grounds_first(self):
        other = os.path.join(self.base, "other")
        subprocess.run(["git", "clone", "-q", os.path.join(self.base, "remote"), other], check=True)
        with open(os.path.join(other, "elsewhere.md"), "w") as handle:
            handle.write("from the laptop\n")
        for args in (
            ["add", "elsewhere.md"],
            ["-c", "user.name=T", "-c", "user.email=t@example.com", "commit", "-q", "-m", "ground [f0-main] — laptop"],
            ["push", "-q"],
        ):
            subprocess.run(["git"] + args, cwd=other, check=True)
        self.entry("f2-plumbing-quotes", "After the laptop.")
        self.ok("ground", "f2")
        self.assertTrue(self.exists("elsewhere.md"))
        self.assertEqual(self.git("rev-parse", "HEAD"), self.git("rev-parse", "origin/main"))

    def test_sphere_focus_refreshes_the_heartbeat(self):
        self.ok("detach", "f2")
        self.assertFalse(self.exists("surface/state/focus/f2.json"))
        self.ok("peek", focus="f2")
        self.assertTrue(self.exists("surface/state/focus/f2.json"))


class DetachTest(SphereCase):
    def test_detach_grounds_then_clears_the_heartbeat(self):
        self.kitchen_and_plumbing()
        self.append("layers/work/home.kitchen.plumbing/work.md", "- third plumber called\n")
        self.entry("f2-plumbing-quotes", "Called the third plumber.")
        result = self.ok("detach", "f2", "-m", "third plumber called")
        self.assertIn("f2-plumbing-quotes open · background", result.out)
        self.assertFalse(self.exists("surface/state/focus/f2.json"))
        self.assertEqual(self.subjects(), ["ground [f2-plumbing-quotes] — third plumber called"])

    def test_detach_stops_with_its_ground(self):
        self.kitchen_and_plumbing()
        self.append("layers/work/home.kitchen.plumbing/work.md", "- x\n")
        result = self.sphere("detach", "f2")
        self.assertEqual(result.code, 3)
        self.assertIn("detach stopped at its ground step", result.err)
        self.assertTrue(self.exists("surface/state/focus/f2.json"))

    def test_main_cant_be_detached(self):
        self.assertIn("main can't be detached", self.sphere("detach", "f0").err)


class CloseTest(SphereCase):
    def setUp(self):
        super().setUp()
        self.kitchen_and_plumbing()

    def test_main_is_never_closed_and_a_why_is_required(self):
        self.assertIn("main is never closed", self.sphere("close", "f0", "-m", "nope").err)
        self.assertIn("-m <why>", self.sphere("close", "f2").err)

    def test_closing_a_child_gives_its_hold_back_by_default(self):
        self.append("layers/work/home.kitchen.plumbing/work.md", "- quote A chosen\n")
        result = self.ok("close", "f2", "-m", "chose quote A")
        self.assertIn("Its hold went back to f1-kitchen-renovation (the default", result.out)
        parent = "layers/focus/f1-kitchen-renovation/focus.md"
        self.assertEqual(self.field(parent, "holds"), "[work:home.kitchen, work:home.kitchen.plumbing]")
        archived = "layers/focus/archived/f2-plumbing-quotes"
        self.assertEqual(self.field(f"{archived}/focus.md", "status"), "closed")
        self.assertIn("closed: done", self.read(f"{archived}/history.md"))
        self.assertFalse(self.exists("layers/focus/f2-plumbing-quotes"))
        self.assertFalse(self.exists("surface/state/focus/f2.json"))
        self.assertEqual(self.subjects(), ["ground [f2-plumbing-quotes] — closed (done): chose quote A"])
        files = self.files_in()
        self.assertIn(parent, files)  # the hold, in the same commit
        self.assertIn("layers/focus/f1-kitchen-renovation/history.md", files)
        self.assertIn("layers/work/home.kitchen.plumbing/work.md", files)  # the close is a ground
        self.assertEqual(self.unsaved(), "")
        self.assertIn("structure-check: clean", self.check().out)

    def test_closing_a_child_can_release_its_hold(self):
        result = self.ok("close", "f2", "-m", "dropped it", "--outcome", "dropped", "--holds", "release")
        self.assertIn("Its hold is released: work:home.kitchen.plumbing", result.out)
        self.assertEqual(self.field("layers/focus/f1-kitchen-renovation/focus.md", "holds"), "[work:home.kitchen]")
        self.assertIn("closed: dropped", self.read("layers/focus/archived/f2-plumbing-quotes/history.md"))

    def test_a_top_level_focus_releases_its_hold(self):
        self.ok("open", "garden", "-i", "Plan the garden", "--holds", "work:garden")
        result = self.ok("close", "f3", "-m", "planned")
        self.assertIn("Its hold is released: work:garden", result.out)
        self.assertEqual(self.field("layers/focus/f0-main/focus.md", "holds"), "[]")

    def test_closing_with_open_children_asks(self):
        result = self.sphere("close", "f1", "-m", "kitchen done")
        self.assertEqual(result.code, 3)
        self.assertIn("f1-kitchen-renovation has open children:", result.err)
        self.assertIn("f2-plumbing-quotes (next: Keep going.; a window is attached)", result.err)

    def test_children_up(self):
        self.ok("close", "f1", "-m", "kitchen done", "--children", "up")
        self.assertEqual(self.field("layers/focus/f2-plumbing-quotes/focus.md", "parent"), "f0")
        self.assertEqual(self.field("layers/focus/archived/f1-kitchen-renovation/focus.md", "status"), "closed")
        self.assertIn("layers/focus/f2-plumbing-quotes/focus.md", self.files_in())
        listing = self.ok("list").out
        self.assertIn("\n  f2-plumbing-quotes", listing)
        self.assertIn("structure-check: clean", self.check().out)

    def test_children_close_refused_under_an_attached_window_then_deepest_first(self):
        self.ok("open", "grout", "-i", "Choose grout", "--parent", "f2", "--holds", "work:home.kitchen.grout")
        result = self.sphere("close", "f1", "-m", "kitchen done", "--children", "close")
        self.assertEqual(result.code, 1)
        self.assertIn("f2-plumbing-quotes has a window attached", result.err)
        self.ok("detach", "f2")
        self.ok("close", "f1", "-m", "kitchen done", "--children", "close")
        self.assertEqual(sorted(os.listdir(self.path("layers/focus"))), ["archived", "f0-main"])
        subjects = self.subjects(3)
        self.assertTrue(subjects[2].startswith("ground [f3-grout] — closed (done): closed with f2-plumbing-quotes"))
        self.assertTrue(subjects[1].startswith("ground [f2-plumbing-quotes] — closed (done): closed with f1"))
        self.assertTrue(subjects[0].startswith("ground [f1-kitchen-renovation] — closed (done): kitchen done"))
        # each hold went back up the chain, and the top-level one was released
        f1 = "layers/focus/archived/f1-kitchen-renovation/focus.md"
        self.assertIn("work:home.kitchen.grout", self.field(f1, "holds"))
        self.assertEqual(self.unsaved(), "")


class UndoRevertTest(SphereCase):
    def setUp(self):
        super().setUp()
        self.kitchen_and_plumbing()

    def ground_line(self, ref: str, line: str, number: str) -> None:
        self.append("layers/work/home.kitchen.plumbing/work.md", line + "\n")
        self.entry(ref, line)
        self.ok("ground", number, "-m", line)

    def test_undo_shows_first_then_reverses_only_this_focus(self):
        self.ground_line("f2-plumbing-quotes", "- two quotes in", "f2")
        self.append("layers/work/home.kitchen/work.md", "- cabinets chosen\n")
        self.entry("f1-kitchen-renovation", "Chose cabinets.")
        self.ok("ground", "f1")
        shown = self.ok("undo", "f2")
        self.assertIn("Run again with --yes", shown.out)
        self.assertIn("ground [f2-plumbing-quotes] — - two quotes in", shown.out)
        self.ok("undo", "f2", "--yes")
        self.assertTrue(self.subjects()[0].startswith("undo [f2-plumbing-quotes] — reverses"))
        self.assertNotIn("two quotes in", self.read("layers/work/home.kitchen.plumbing/work.md"))
        self.assertIn("cabinets chosen", self.read("layers/work/home.kitchen/work.md"))
        history = self.read("layers/focus/f2-plumbing-quotes/history.md")
        self.assertIn("— undone", history)
        self.assertIn("**Did:** - two quotes in", history)  # appended history stays
        self.assertIn("Reverses: ", self.git("log", "-1", "--format=%B"))
        self.assertEqual(self.unsaved(), "")

    def test_repeated_undo_walks_back(self):
        self.ground_line("f2-plumbing-quotes", "- first", "f2")
        self.ground_line("f2-plumbing-quotes", "- second", "f2")
        self.ok("undo", "f2", "--yes")
        self.ok("undo", "f2", "--yes")
        work = self.read("layers/work/home.kitchen.plumbing/work.md")
        self.assertNotIn("first", work)
        self.assertNotIn("second", work)

    def test_undo_refuses_over_unsaved_changes(self):
        self.ground_line("f2-plumbing-quotes", "- first", "f2")
        self.append("layers/work/home.kitchen.plumbing/work.md", "- wip\n")
        result = self.sphere("undo", "f2", "--yes")
        self.assertEqual(result.code, 1)
        self.assertIn("unsaved changes", result.err)
        self.assertIn("- wip", self.read("layers/work/home.kitchen.plumbing/work.md"))

    def test_undo_a_close(self):
        self.ok("close", "f2", "-m", "done")
        self.ok("undo", "f2", "--yes")
        self.assertTrue(self.exists("layers/focus/f2-plumbing-quotes/focus.md"))
        self.assertFalse(self.exists("layers/focus/archived/f2-plumbing-quotes"))
        self.assertEqual(self.field("layers/focus/f1-kitchen-renovation/focus.md", "holds"), "[work:home.kitchen]")
        self.assertIn("structure-check: clean", self.check().out)

    def test_revert_lists_then_goes_back_to_a_point(self):
        mark = self.git("rev-parse", "--short", "HEAD")
        self.ground_line("f2-plumbing-quotes", "- quote A accepted", "f2")
        self.ground_line("f2-plumbing-quotes", "- install booked", "f2")
        listing = self.ok("revert", "f2")
        self.assertIn("pick the point to go back to", listing.out)
        self.assertIn("install booked", listing.out)
        self.ok("revert", "f2", "--to", mark, "--yes")
        self.assertTrue(self.subjects()[0].startswith(f"revert [f2-plumbing-quotes] — back to {mark} (reverses 2)"))
        self.assertEqual(self.read("layers/work/home.kitchen.plumbing/work.md"), "# Plumbing\n")

    def test_reference_files_are_proposed_never_reversed(self):
        self.ok("open", "notes", "-i", "Keep notes", "--holds", "layers/knowledge/kitchen.md")
        self.write("layers/knowledge/kitchen.md", "fact\n")
        self.entry("f3-notes", "Wrote a fact.")
        self.ok("ground", "f3")
        result = self.ok("undo", "f3", "--yes")
        self.assertIn(
            "Not reversed (reference; propose restoring the old version): layers/knowledge/kitchen.md", result.out
        )
        self.assertTrue(self.exists("layers/knowledge/kitchen.md"))

    def test_revert_sphere_refused_while_a_focus_is_foreground(self):
        mark = self.git("rev-parse", "--short", "HEAD")
        self.ground_line("f2-plumbing-quotes", "- later", "f2")
        result = self.sphere("revert", "--sphere", "--to", mark, "--yes")
        self.assertEqual(result.code, 1)
        self.assertIn("Ground or detach these first", result.err)
        self.ok("detach", "f1")
        self.ok("detach", "f2")
        self.assertIn("Confirm with --yes", self.ok("revert", "--sphere", "--to", mark).out)
        self.ok("revert", "--sphere", "--to", mark, "--yes")
        self.assertEqual(self.read("layers/work/home.kitchen.plumbing/work.md"), "# Plumbing\n")
        self.assertTrue(self.subjects()[0].startswith(f"revert [f0-main] — sphere back to {mark}"))

    def test_revert_sphere_takes_a_whole_focus_away_history_and_all(self):
        mark = self.git("rev-parse", "--short", "HEAD")
        self.ok("open", "heat-pump", "-i", "Research heat pumps", "--holds", "work:home.heat")
        self.entry("f3-heat-pump", "Read about heat pumps.")
        self.ok("detach", "f3")
        self.ok("detach", "f1")
        self.ok("detach", "f2")
        self.ok("revert", "--sphere", "--to", mark, "--yes")
        self.assertFalse(self.exists("layers/focus/f3-heat-pump"))
        self.assertEqual(self.unsaved(), "")
        self.assertIn("structure-check: clean", self.check().out)

    def test_a_reused_number_after_a_revert(self):
        mark = self.git("rev-parse", "--short", "HEAD")
        self.ok("open", "heat-pump", "-i", "Research heat pumps")
        self.entry("f3-heat-pump", "Read about heat pumps.")
        self.ok("detach", "f3")
        self.ok("detach", "f1")
        self.ok("detach", "f2")
        self.ok("revert", "--sphere", "--to", mark, "--yes")
        # the number comes back: the sphere is a state machine
        self.assertIn("f3-solar open", self.ok("open", "solar", "-i", "Look at solar").out)
        self.assertIn("Nothing to undo in f3-solar.", self.ok("undo", "f3").out)

    def test_undo_never_reaches_an_older_focus_with_the_same_number_and_name(self):
        self.ok("open", "heat-pump", "-i", "Research heat pumps", "--holds", "work:home.heat")
        self.write("layers/work/home.heat/notes.md", "old notes\n")
        self.entry("f3-heat-pump", "Read about heat pumps.")
        self.ok("ground", "f3")
        self.ok("undo", "f0", "--yes")  # reverses main's last ground: the opening of f3
        self.assertFalse(self.exists("layers/focus/f3-heat-pump"))
        self.assertTrue(self.exists("layers/work/home.heat/notes.md"))  # that older f3's ground is still in effect
        self.ok("open", "heat-pump", "-i", "Research heat pumps, again")
        self.assertIn("Nothing to undo in f3-heat-pump.", self.ok("undo", "f3").out)


class SeeingTest(SphereCase):
    def setUp(self):
        super().setUp()
        self.kitchen_and_plumbing()

    def test_peek_groups_by_focus(self):
        self.append("layers/work/home.kitchen.plumbing/work.md", "- quote\n")
        self.write("scratch.txt", "x\n")
        out = self.ok("peek", focus="f2").out
        self.assertIn("f2-plumbing-quotes (this focus)\n  changed: layers/work/home.kitchen.plumbing/work.md", out)
        self.assertIn("Out of focus (main's)\n  new: scratch.txt", out)
        self.assertIn("Unsaved: 1 in focus · 1 out of focus", out)
        self.assertIn("Recent grounds:", out)
        self.assertIn("Today:", self.ok("peek", "--today").out)

    def test_list_shows_the_tree(self):
        out = self.ok("list").out
        self.assertIn("What's in focus: 2 open", out)
        self.assertIn("f0-main  the sphere", out)
        self.assertIn("\n  f1-kitchen-renovation  foreground · grounded · last ground", out)
        self.assertIn("\n    f2-plumbing-quotes  foreground · grounded · last ground", out)
        self.assertIn("next: Keep going.", out)

    def test_list_needs_attention(self):
        self.set_heartbeat_age("f2", 120)
        self.append("layers/work/home.kitchen.plumbing/work.md", "- wip\n")
        self.ok("detach", "f1")
        self.append("layers/work/home.kitchen/work.md", "- wip\n")
        out = self.ok("list").out
        self.assertIn("Needs attention", out)
        self.assertIn("! f2-plumbing-quotes: unsaved changes, and its window went quiet", out)
        self.assertIn("! f1-kitchen-renovation: unsaved changes with no window attached. Ground them?", out)
        attach = self.sphere("attach", "f1")
        self.assertIn("! f2-plumbing-quotes has unsaved changes and its window went quiet", attach.err)

    def test_list_quiet_for_weeks(self):
        self.ok("open", "shed", "-i", "Fix the shed")
        history = "layers/focus/f3-shed/history.md"
        self.write(history, self.read(history).replace(self.read(history)[3:13], "2026-01-01", 1))
        out = self.ok("list").out
        self.assertRegex(out, r"\? f3-shed: quiet for \d+ days")

    def test_saved_but_stale(self):
        self.set_heartbeat_age("f2", 120)
        self.assertIn("· f2-plumbing-quotes: its window went quiet after saving", self.ok("list").out)

    def test_attach_prints_the_briefing(self):
        self.write("layers/work/home.kitchen/progress.md", "## 2026-11-01 — started\n\nMeasured.\n")
        out = self.ok("attach", "kitchen-renovation").out
        self.assertIn("== f1-kitchen-renovation · working · parent f0-main", out)  # progress.md is unsaved
        self.assertIn("intention: Renovate the kitchen by spring", out)
        self.assertIn("== latest history", out)
        self.assertIn("work:home.kitchen → layers/work/home.kitchen", out)
        self.assertIn("    Measured.", out)
        self.assertIn("== open children: f2-plumbing-quotes", out)
        self.assertIn("f0-main open · the sphere", self.ok("attach", "main").out)

    def test_names_resolve_and_ambiguity_says_so(self):
        self.assertIn("f2-plumbing-quotes", self.ok("attach", "2").out)
        self.assertIn("f2-plumbing-quotes", self.ok("attach", "plumbing-quotes").out)
        self.ok("open", "plumbing-install", "-i", "Install")
        result = self.sphere("attach", "plumbing")
        self.assertEqual(result.code, 2)
        self.assertIn("Did you mean: f2-plumbing-quotes f3-plumbing-install?", result.err)


class OffersTest(SphereCase):
    """An offer is `## <date> — offer to fNN` in the sender's own history; it waits until answered."""

    def setUp(self):
        super().setUp()
        self.kitchen_and_plumbing()
        self.write_offer()

    def write_offer(self):
        history = "layers/focus/f1-kitchen-renovation/history.md"
        self.write(
            history, "## 2026-11-01 10:00 — offer to f2\n\nI have a plumber's number; want it?\n\n" + self.read(history)
        )

    def waiting_line(self):
        return [line for line in self.ok("list").out.split("\n") if "f2-plumbing-quotes  " in line][0]

    def test_an_offer_waits_for_the_focus_it_names(self):
        self.assertIn("· 1 waiting", self.waiting_line())
        attach = self.ok("attach", "f2").out
        self.assertIn("== waiting for you: 1", attach)
        self.assertIn("offer from f1-kitchen-renovation (2026-11-01 10:00)", attach)
        self.assertIn("waiting for you: 1", self.ok("peek").out)

    def test_accepted_answers_it(self):
        self.entry("f2-plumbing-quotes", "Accepted f1's offer of the plumber's number.", date="2026-11-02 09:00")
        self.assertNotIn("waiting", self.waiting_line())

    def test_declined_answers_it(self):
        self.entry("f2-plumbing-quotes", "Declined the offer from f1: already have three.", date="2026-11-02 09:00")
        self.assertNotIn("waiting", self.waiting_line())

    def test_an_answer_must_name_the_sender_and_come_after(self):
        self.entry("f2-plumbing-quotes", "Accepted a quote.", date="2026-11-02 09:00")
        self.assertIn("· 1 waiting", self.waiting_line())
        self.entry("f2-plumbing-quotes", "Accepted f1's offer.", date="2026-10-01 09:00")
        self.assertIn("· 1 waiting", self.waiting_line())


class PushReportTest(SphereCase):
    def ground_once(self, text: str) -> str:
        self.write("layers/focus/f0-main/note.md", text)
        self.entry("f0-main", text)
        return self.ok("ground", "-m", text).out

    def test_pushed_says_nothing(self):
        out = self.ground_once("pushed")
        self.assertNotIn("not pushed", out)
        self.assertEqual(self.git("rev-parse", "HEAD"), self.git("rev-parse", "origin/main"))

    def test_a_remote_without_upstream_says_so_every_time(self):
        self.git("branch", "--unset-upstream")
        for text in ("first", "second"):
            out = self.ground_once(text)
            self.assertRegex(out, r"Grounded f0-main: \d+ files · [0-9a-f]+ · not pushed: no upstream")

    def test_no_remote_says_nothing(self):
        self.git("remote", "remove", "origin")
        self.assertNotIn("not pushed", self.ground_once("local only"))


class WithoutGitTest(SphereCase):
    use_git: bool = False

    def test_without_git(self):
        self.assertFalse(self.exists(".git"))
        self.ok("open", "garden", "-i", "Plan the spring garden", "--attach")
        self.assertTrue(self.read("surface/state/focus/LOCK").startswith("f1-garden"))
        result = self.sphere("attach", "f0", client="phone")
        self.assertEqual(result.code, 4)
        self.assertIn("Read-only: f1-garden is in the foreground", result.err)
        self.ok("attach", "f1")
        self.write("seeds.md", "seeds\n")
        self.assertIn("Saved f1-garden (no git", self.ok("ground", "f1").out)
        self.assertIn("isn't available without git", self.sphere("undo", "f1").err)
        self.assertIn("(no git:", self.ok("peek").out)
        self.ok("detach", "f1")
        self.assertFalse(self.exists("surface/state/focus/LOCK"))
        self.ok("attach", "f0")
        self.ok("ground", "-m", "quick")
        self.assertIn("take over", self.sphere("attach", "f1").err.lower())
        self.ok("attach", "f1", "--take-over")
        self.ok("close", "f1", "-m", "planted")
        self.assertTrue(self.exists("layers/focus/archived/f1-garden/focus.md"))


class OutsideTest(unittest.TestCase):
    def test_not_inside_a_sphere(self):
        import sys
        import tempfile

        from sphere_testing import SPHERE, run

        with tempfile.TemporaryDirectory() as folder:
            result = run([sys.executable, SPHERE, "list"], folder)
        self.assertEqual(result.code, 1)
        self.assertIn("not inside a sphere", result.err)


if __name__ == "__main__":
    unittest.main()
