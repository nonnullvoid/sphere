"""Tests for scripts/new-sphere and the base build: a fresh sphere assembles, inits and checks clean."""

import datetime
import json
import os
import re
import shutil
import tempfile
import unittest

from sphere_testing import SCRIPTS, run

NEW_SPHERE = os.path.join(SCRIPTS, "new-sphere")
UPDATE_SPHERE = os.path.join(SCRIPTS, "update-sphere")
LINK = re.compile(r"\]\(([^)\s]+)\)")


class BuildCase(unittest.TestCase):
    """A fresh sphere, assembled from a build (base, unless a subclass says) in a temporary folder."""

    build_name: str = "base"
    base: str = ""  # set in setUp, the unittest way
    root: str = ""  # set in setUp, the unittest way

    def setUp(self):
        self.base = tempfile.mkdtemp(prefix="sphere-build-test-")
        self.root = os.path.join(self.base, "my-sphere")
        result = run([NEW_SPHERE, self.build_name, self.root], cwd=self.base)
        self.assertEqual(result.code, 0, result.text)

    def tearDown(self):
        shutil.rmtree(self.base, ignore_errors=True)

    def broken_links(self) -> list[str]:
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
        return broken

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
        self.assertEqual(self.broken_links(), [])

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
        os.makedirs(os.path.dirname(os.path.join(self.root, path)), exist_ok=True)
        with open(os.path.join(self.root, path), mode, encoding="utf-8") as handle:
            handle.write(text)

    def entry(self, focus: str) -> None:
        """A new history entry, on top: history files are newest first."""
        path = f"layers/focus/{focus}/history.md"
        self.write(path, "## 2026-11-20 12:00 — a change\n\n**Did:** Changed it.\n\n" + self.read(path))

    def test_start_before_and_after_setup(self):
        self.assertIn("hasn't been set up yet", self.sphere("start").out)
        self.assertEqual(self.sphere("init", "--git").code, 0)
        alone = self.sphere("start")
        self.assertIn("f0-main open · the sphere", alone.out)
        self.assertIn("sense: focus-attached\n", alone.out)
        self.assertRegex(alone.out, r"^== .* · \w{3} \d{4}-\d{2}-\d{2} \d{2}:\d{2}\n")  # the clock, for the greeting
        self.assertIn("== last saved here\n## ", alone.out)  # where they were, without a second read
        self.assertIn("== using the sphere: skimmed", alone.out)  # how much to explain, handed over
        self.assertIn("== you are companion", alone.out)
        self.assertIn("== you are companion; our working agreement: - I propose; you decide.", alone.out)
        self.assertNotIn("== their principles", alone.out)  # none yet: the slot is empty until they write one
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

    def test_startup_context_is_whatever_sphere_md_lists(self):
        self.sphere("init", "--git")
        self.write(
            "sphere.md",
            self.read("sphere.md").replace(
                "- **their principles:**",
                "- **what's in the kitchen:** `core/engine.md#headings`\n- **their principles:**",
            ),
        )
        out = self.sphere("start").out
        self.assertIn("== what's in the kitchen:", out)  # a line added in text, printed with no code change

    def test_ground_and_close_keep_the_views_and_index_current(self):
        self.sphere("init", "--git")
        self.write(
            "layers/work/shed/work.md",
            "---\ntitle: Build a shed\nkind: project\nstate: active\n"
            "summary: a garden shed\nupdated: 2026-11-21\n---\n",
        )
        self.write("layers/work/shed/progress.md", "## 2026-11-21 — added\n\nStarted.\n")
        self.sphere("open", "shed", "-i", "Build the shed", "--holds", "work:shed")
        grounded = self.sphere("ground", "f1", "--reacted", "--did", "Added the shed.")
        self.assertEqual(grounded.code, 0, grounded.text)
        self.assertIn("Build a shed", self.read("layers/work/index.md"))
        self.assertIn('"text": "Build a shed"', self.read("surface/projections/work/work-dashboard/data.js"))
        self.assertEqual(run(["git", "status", "--short"], cwd=self.root).out, "")  # committed with the change
        self.assertNotIn("Left for main", grounded.out)  # and not reported as left behind
        self.write(
            "layers/work/shed/work.md", self.read("layers/work/shed/work.md").replace("state: active", "state: done")
        )
        gate = self.sphere("close", "f1", "-m", "built it")
        self.assertIn("sense: node-archived\n", gate.out)  # a finished node's reactions reach the AI at close
        self.assertIn("persona (if our working agreement", gate.out)
        closed = self.sphere("close", "f1", "-m", "built it", "--reacted")
        self.assertEqual(closed.code, 0, closed.text)
        self.assertNotIn('"text": "Build a shed"', self.read("surface/projections/work/work-dashboard/data.js"))

    def test_show_names_the_page_it_opens(self):
        self.assertIn("render", self.sphere("help").out)

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


class ExtendsBase(BuildCase):
    """Checks every build that extends base passes. Not run on its own: each build's case sets build_name."""

    who: dict[str, str] = {  # noqa: RUF012  # read-only
        "GIT_AUTHOR_NAME": "Test",
        "GIT_AUTHOR_EMAIL": "test@example.com",
        "GIT_COMMITTER_NAME": "Test",
        "GIT_COMMITTER_EMAIL": "test@example.com",
    }

    def sphere(self, *args: str):
        return run([os.path.join(self.root, "scripts", "sphere"), *args], cwd=self.root, env=self.who)

    def test_inits_and_checks_clean(self):
        self.assertEqual(self.sphere("init", "--git").code, 0)
        structure = run([os.path.join(self.root, "scripts", "structure-check")], cwd=self.root)
        self.assertEqual(structure.out.strip(), "structure-check: clean")
        manifest = run([os.path.join(self.root, "scripts", "manifest-check")], cwd=self.root)
        self.assertEqual(manifest.out.strip(), "manifest-check: clean")
        self.assertIn("== anchors this sphere keeps:", self.sphere("start").out)  # its own startup lines

    def test_links_inside_the_sphere_resolve(self):
        self.assertEqual(self.broken_links(), [])


class LifesphereBuildTest(ExtendsBase):
    """lifesphere extends base: base's files, then its own on top."""

    build_name: str = "lifesphere"

    def test_assembles_over_base(self):
        for path in [
            "AGENTS.md",  # from base
            "core/init.md",  # from base
            "core/build.md",
            "core/protocol/lenses/philosophy.md",
            "core/protocol/lenses/values.md",
            "core/protocol/lenses/worldview.md",
            "core/protocol/frames/philosophy/realizations.md",
            "layers/philosophy/realizations.md",
            "layers/projections/life.md",
            "surface/projections/me/life/index.html",
            "surface/projections/me/today/index.html",  # from base
        ]:
            self.assertTrue(os.path.isfile(os.path.join(self.root, path)), path)
        self.assertIn('"build": "lifesphere"', self.read("core/build.json"))
        self.assertIn('name: "life"', self.read("surface/projections/assets/registry.js"))
        self.assertFalse(os.path.exists(os.path.join(self.root, "README.md")))

    def test_the_life_page_follows_its_rules(self):
        self.sphere("init", "--git")

        def work(name: str, title: str, kind: str, parent: str, ongoing: str) -> None:
            os.makedirs(os.path.join(self.root, "layers/work", name))
            with open(os.path.join(self.root, "layers/work", name, "work.md"), "w", encoding="utf-8") as handle:
                handle.write(
                    f"---\ntitle: {title}\nkind: {kind}\nparent: {parent}\nstate: active\n"
                    f"ongoing: {ongoing}\nsummary: s\nupdated: 2026-11-22\n---\n"
                )

        work("health", "Health", "area", "", "true")
        work("health.sleep", "Sleep before eleven", "project", "health", "true")
        work("home.shelves", "Put up shelves", "project", "", "false")
        self.sphere("render")
        life = self.read("surface/projections/me/life/data.js")
        panels = {line.split('"')[1]: line for line in life.split("\n") if line.strip().startswith("{ title:")}
        areas, habits, going = panels["Areas"], panels["Habits"], panels["On the go"]
        self.assertIn("Health", areas)
        self.assertIn("Sleep before eleven", habits)
        self.assertNotIn("Health", habits)  # an area isn't a habit
        self.assertIn("Put up shelves", going)
        self.assertNotIn("Sleep before eleven", going)  # a habit isn't on the go


class UpdateSphereTest(BuildCase):
    """An existing sphere gets the repo's tools; nothing it wrote changes."""

    who: dict[str, str] = ScriptDeliversTest.who

    def update(self):
        return run([UPDATE_SPHERE, self.root], cwd=self.base, env=self.who)

    def git(self, *args: str):
        return run(["git", "-C", self.root, *args], cwd=self.root, env=self.who)

    def init(self) -> None:
        result = run([os.path.join(self.root, "scripts", "sphere"), "init", "--git"], cwd=self.root, env=self.who)
        self.assertEqual(result.code, 0, result.text)

    def append(self, path: str, text: str) -> None:
        with open(os.path.join(self.root, path), "a", encoding="utf-8") as handle:
            handle.write(text)

    def test_refreshes_only_the_tools_and_commits_them(self):
        self.init()
        self.append("scripts/sphere", "# an older copy\n")
        self.append("core/protocol/lenses/principles.md", "\nTheir own principle.\n")
        self.git("commit", "-qam", "an older sphere")
        before = self.git("rev-list", "--count", "HEAD").out.strip()

        result = self.update()
        self.assertEqual(result.code, 0, result.text)
        self.assertIn("Updated 1 of the sphere's tools: sphere.", result.out)
        with open(os.path.join(SCRIPTS, "sphere"), encoding="utf-8") as handle:
            self.assertEqual(self.read("scripts/sphere"), handle.read())
        self.assertIn("Their own principle.", self.read("core/protocol/lenses/principles.md"))
        self.assertEqual(self.git("status", "--porcelain").out.strip(), "")
        self.assertEqual(int(self.git("rev-list", "--count", "HEAD").out), int(before) + 1)
        self.assertIn("already up to date", self.update().out)

    def test_unsaved_edits_to_a_tool_stop_it(self):
        self.init()
        self.append("scripts/shapes", "# a local edit\n")
        result = self.update()
        self.assertEqual(result.code, 3)
        self.assertIn("# a local edit", self.read("scripts/shapes"))

    def test_refuses_a_folder_that_isnt_a_sphere(self):
        self.assertEqual(run([UPDATE_SPHERE, self.base], cwd=self.base).code, 2)


class CodesphereBuildTest(ExtendsBase):
    """codesphere extends base: base's files, then its own on top."""

    build_name: str = "codesphere"

    def test_assembles_over_base(self):
        for path in [
            "AGENTS.md",  # from base
            "core/init.md",  # from base
            "core/build.md",
            "core/user/channels.md",
            "core/user/codebases.md",
            "core/protocol/lenses/agentic-engineering.md",
            "core/protocol/lenses/workflow.md",
            "core/protocol/frames/workflow/pr-runbook.md",
            "core/protocol/frames/workflow/code-gates.md",
            "layers/knowledge/eng/topic.md",
            "layers/workflows/meetings/agenda.md",
            "surface/projections/me/today/index.html",  # from base
        ]:
            self.assertTrue(os.path.isfile(os.path.join(self.root, path)), path)
        self.assertIn('"build": "codesphere"', self.read("core/build.json"))
        self.assertFalse(os.path.exists(os.path.join(self.root, "README.md")))

    def test_ships_no_page_or_work_of_its_own(self):
        # Base's pages only, and an empty work tree: how work and reviews are tracked is the human's call.
        self.assertNotIn('name: "engineering"', self.read("surface/projections/assets/registry.js"))
        self.assertNotIn("reviews", os.listdir(os.path.join(self.root, "layers/work")))


class HomesphereBuildTest(ExtendsBase):
    """homesphere extends base: plain words, saving that just happens, Home and My things over base's pages."""

    build_name: str = "homesphere"

    def test_assembles_over_base(self):
        for path in [
            "AGENTS.md",  # from base
            "core/init.md",  # from base
            "core/build.md",
            "core/operating-modes/non-technical.md",
            "core/operating-modes/everyday.md",  # from base
            ".claude/settings.json",
        ]:
            self.assertTrue(os.path.isfile(os.path.join(self.root, path)), path)
        self.assertIn('"build": "homesphere"', self.read("core/build.json"))
        self.assertIn("operating-mode: non-technical", self.read("core/ai/personas/companion/companion.md"))
        registry = self.read("surface/projections/assets/registry.js")
        self.assertIn('title: "Home"', registry)
        self.assertIn('title: "My things"', registry)
        self.assertFalse(os.path.exists(os.path.join(self.root, "README.md")))

    def test_the_sphere_tools_are_pre_approved(self):
        settings = json.loads(self.read(".claude/settings.json"))
        self.assertIn("Bash(scripts/sphere *)", settings["permissions"]["allow"])
        self.assertEqual(settings["permissions"]["defaultMode"], "acceptEdits")
        self.assertIn("scripts/sphere start", json.dumps(settings["hooks"]))  # base's hook kept

    def test_init_gives_the_sphere_its_id_once(self):
        self.sphere("init", "--git")
        made = json.loads(self.read("core/identity.json"))["id"]
        self.assertRegex(made, r"^[0-9a-f]{8}-[0-9a-f]{4}-7[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$")

    def test_home_shows_wins_from_the_growth_record(self):
        self.sphere("init", "--git")
        today = datetime.date.today()
        old = today - datetime.timedelta(days=40)
        with open(
            os.path.join(self.root, "layers/witness/ledger", f"{today.year}.md"), "w", encoding="utf-8"
        ) as handle:
            handle.write(
                f"# {today.year}\n\n### {today.isoformat()} · health\nFirst 10k run.\nevidence: the human said so\n\n"
                f"### {old.isoformat()} · home\nFixed the sink.\nevidence: the human said so\n"
            )
        self.sphere("render")
        page = self.read("surface/projections/me/today/data.js")
        panels = {line.split('"')[1]: line for line in page.split("\n") if line.strip().startswith("{ title:")}
        self.assertIn("First 10k run.", panels["Done lately"])
        self.assertNotIn("Fixed the sink.", panels["Done lately"])  # older than two weeks
        self.assertIn('title: "Home"', page)


del ExtendsBase  # shared checks only; run through each build's case


if __name__ == "__main__":
    unittest.main()
