"""Tests for the agent, operating-mode, persona, projection, knowledge, literacy and library trees,
and for the history and reference kinds. Each tree: a valid node, then each rule broken once."""

import os
import sys
import unittest

from sphere_testing import SCRIPTS, SHAPES_TEMPLATE, SphereCase

sys.path.insert(0, SCRIPTS)
from sphere_shapes import read_shapes  # noqa: E402

CLEAN = "structure-check: clean"

AGENT = """\
---
agent: notes
does: Tidies the week's notes into topics
source:                        # empty when it's defined here
trust:                         # earned rung per kind of work
  tidying: unattended
  summarizing: together
tier: light
---

## What it may touch
"""

OPERATING_MODE = """\
---
operating-mode: brainstorming
persona: any
signals: ["let's brainstorm", "I have an idea"]
loadout: [idea-nodes]
adds-guardrails: []
sharing: public
---
"""

PERSONA = """\
---
persona: {name}
default: {default}
operating-mode: brainstorming
---
"""

PROJECTION = """\
---
projection: work-dashboard
title: What's in motion
namespace: work
kind: live
opens: served
lifespan: long-lived
freshness: on-open
sources: [layers/work/index.md, layers/work/*/work.md]
writes: []
home: surface/projections/work/work-dashboard/
sharing: private
template: dashboard
legacy: false
---
"""

TOPIC = """\
---
name: home.lease
title: The flat's lease
summary: ends in August
related: [money.budget, work:home.move]
fresh_for: 1y
updated: 2026-11-04
---
"""

SUBJECT = """\
---
subject: money.investing.index-funds
title: Index funds
summary: chooses between funds unaided
level: can-use
rests_on: [knowledge:money.investing]
stale:
tracked: 2026-09-14
updated: 2026-11-10
---
"""

ARTIFACT = """\
---
artifact: {name}
title: How compound interest works
type: walkthrough
subjects: [money.investing]
perspective: personalized
made_for: choosing between two savings accounts
rests_on: [knowledge:money.savings]
sharing: private
created: 2026-10-14
updated: 2026-10-14
---
"""


class LensShapeCase(SphereCase):
    use_git: bool = False  # the shape check needs no git; this keeps the tests quick

    def put(self, relative: str, text: str, old: str = "", new: str = "") -> str:
        """Write a node (changing `old` to `new` first, if given) and return the whole check's output."""
        self.write(relative, text.replace(old, new) if old else text)
        return self.check().out


class AgentShapeTest(LensShapeCase):
    file: str = "core/ai/agents/notes.md"

    def test_a_valid_agent_is_clean_and_the_index_is_skipped(self):
        self.write("core/ai/agents/index.md", "generated: no frontmatter\n")
        self.assertIn(CLEAN, self.put(self.file, AGENT))

    def test_teams_are_skipped(self):
        self.write("core/ai/agents/teams/review-panel.md", "a team: no shape yet\n")
        self.assertIn(CLEAN, self.put(self.file, AGENT))

    def test_an_empty_trust_map_is_fine(self):
        out = self.put(self.file, AGENT, "  tidying: unattended\n  summarizing: together\n", "")
        self.assertIn(CLEAN, out)

    def test_each_rule(self):
        self.assertIn(
            "agent is 'scribe', but the node is named 'notes'",
            self.put(self.file, AGENT, "agent: notes", "agent: scribe"),
        )
        self.assertIn("tier is 'huge'", self.put(self.file, AGENT, "tier: light", "tier: huge"))
        self.assertIn(
            "missing key 'does'", self.put(self.file, AGENT, "does: Tidies the week's notes into topics\n", "")
        )
        out = self.put(self.file, AGENT, "summarizing: together", "summarizing: trusted")
        self.assertIn("trust for 'summarizing' is 'trusted', expected one of: together supervised unattended", out)
        out = self.put(
            self.file, AGENT, "trust:                         # earned rung per kind of work", "trust: unattended"
        )
        self.assertIn("trust is a map", out)


class OperatingModeShapeTest(LensShapeCase):
    file: str = "core/operating-modes/brainstorming.md"

    def test_a_valid_operating_mode_is_clean(self):
        self.assertIn(CLEAN, self.put(self.file, OPERATING_MODE))

    def test_each_rule(self):
        out = self.put(self.file, OPERATING_MODE, "operating-mode: brainstorming", "operating-mode: ideas")
        self.assertIn("operating-mode is 'ideas', but the node is named 'brainstorming'", out)
        self.assertIn(
            "sharing is 'everyone'", self.put(self.file, OPERATING_MODE, "sharing: public", "sharing: everyone")
        )
        self.assertIn("missing key 'signals'", self.put(self.file, OPERATING_MODE, "signals:", "cues:"))
        out = self.put(self.file, OPERATING_MODE, "persona: any", "persona: forge")
        self.assertIn("persona 'forge' doesn't exist", out)
        self.write("core/ai/personas/forge/forge.md", PERSONA.format(name="forge", default="true"))
        self.write("core/ai/personas/forge/journal.md", "")
        self.assertNotIn("persona 'forge'", self.check().out)


class PersonaShapeTest(LensShapeCase):
    def persona(self, name: str, default: str = "false") -> None:
        self.write("core/operating-modes/brainstorming.md", OPERATING_MODE)
        self.write(f"core/ai/personas/{name}/{name}.md", PERSONA.format(name=name, default=default))
        self.write(f"core/ai/personas/{name}/journal.md", "## 2026-11-01 — first entry\n")

    def test_valid_personas_are_clean(self):
        self.persona("sage", "true")
        self.persona("forge")
        self.write("core/ai/personas/sage/notes/mornings.md", "no frontmatter: notes aren't nodes\n")
        self.assertIn(CLEAN, self.check().out)

    def test_the_main_file_is_named_like_the_folder(self):
        self.persona("sage", "true")
        os.rename(self.path("core/ai/personas/sage/sage.md"), self.path("core/ai/personas/sage/persona.md"))
        self.assertIn("core/ai/personas/sage: missing sage.md (current state)", self.check().out)

    def test_journal_and_keys(self):
        self.persona("sage", "true")
        os.remove(self.path("core/ai/personas/sage/journal.md"))
        self.assertIn("missing journal.md (history)", self.check().out)
        self.persona("sage", "yes")
        out = self.check().out
        self.assertIn("default is 'yes'", out)
        self.write("core/ai/personas/sage/sage.md", "---\npersona: owl\ndefault: true\n---\n")
        self.assertIn("persona is 'owl', but the node is named 'sage'", self.check().out)

    def test_the_operating_mode_names_a_file(self):
        self.persona("sage", "true")
        path = "core/ai/personas/sage/sage.md"
        self.write(path, self.read(path).replace("operating-mode: brainstorming", "operating-mode: drafting"))
        self.assertIn("operating-mode 'drafting' isn't a file in core/operating-modes/", self.check().out)
        self.write(path, self.read(path).replace("operating-mode: drafting\n", ""))
        self.assertIn("missing key 'operating-mode'", self.check().out)
        self.write(path, "---\npersona: sage\noperating-mode: brainstorming\ndefault: true\n---\n")
        self.assertIn(
            "keys out of order; the persona shape's order is: persona default operating-mode", self.check().out
        )

    def test_a_new_focus_starts_as_the_default_persona_in_its_mode(self):
        self.persona("sage", "true")
        self.persona("forge")
        self.ok("open", "kitchen", "-i", "Renovate the kitchen")
        focus = "layers/focus/f1-kitchen/focus.md"
        self.assertEqual((self.field(focus, "persona"), self.field(focus, "operating-mode")), ("sage", "brainstorming"))
        self.ok("open", "garden", "-i", "Plant the garden", "--persona", "forge", "--operating-mode", "planning")
        focus = "layers/focus/f2-garden/focus.md"
        self.assertEqual((self.field(focus, "persona"), self.field(focus, "operating-mode")), ("forge", "planning"))

    def test_exactly_one_default(self):
        self.persona("sage")
        self.persona("forge")
        self.assertIn("exactly one persona has default: true (found: none)", self.check().out)
        self.persona("sage", "true")
        self.persona("forge", "true")
        self.assertIn("(found: forge sage)", self.check().out)


class ProjectionShapeTest(LensShapeCase):
    file: str = "layers/projections/work-dashboard.md"
    folder: str = "layers/projections/work-dashboard"

    def test_a_file_projection_is_clean_and_registry_and_templates_are_skipped(self):
        self.write("layers/projections/registry.md", "generated\n")
        self.write("layers/projections/templates/dashboard/template.md", "no frontmatter\n")
        self.assertIn(CLEAN, self.put(self.file, PROJECTION))

    def test_a_folder_projection_reads_its_same_named_main_file_only(self):
        self.write(f"{self.folder}/chapters.md", "not a node\n")
        self.assertIn(CLEAN, self.put(f"{self.folder}/work-dashboard.md", PROJECTION))
        os.remove(self.path(f"{self.folder}/work-dashboard.md"))
        self.assertIn("missing work-dashboard.md (current state)", self.check().out)
        out = self.put(f"{self.folder}/work-dashboard.md", PROJECTION, "projection: work-dashboard", "projection: wd")
        self.assertIn("projection is 'wd', but the node is named 'work-dashboard'", out)

    def test_each_rule(self):
        for key, bad in [
            ("kind: live", "kind: cached"),
            ("opens: served", "opens: emailed"),
            ("lifespan: long-lived", "lifespan: forever"),
            ("freshness: on-open", "freshness: weekly"),
            ("sharing: private", "sharing: secret"),
            ("legacy: false", "legacy: maybe"),
        ]:
            self.assertIn(f"{bad.split(':')[0]} is '{bad.split(': ')[1]}'", self.put(self.file, PROJECTION, key, bad))
        out = self.put(
            self.file,
            PROJECTION,
            "title: What's in motion\nnamespace: work\n",
            "namespace: work\ntitle: What's in motion\n",
        )
        self.assertIn("keys out of order", out)
        self.assertIn(
            "'retired' belongs only to archived nodes",
            self.put(self.file, PROJECTION, "legacy: false\n", "legacy: false\nretired: 2026-11-01 replaced\n"),
        )

    def test_archived_projections_need_retired(self):
        archived = "layers/projections/archived/launch-tracker.md"
        text = PROJECTION.replace("work-dashboard", "launch-tracker")
        self.assertIn(CLEAN, self.put(archived, text))  # the archive is opt-in
        self.assertIn("archived, so it needs 'retired'", self.check("--archive").out)
        self.write(archived, text.replace("legacy: false\n", "legacy: false\nretired: 2026-11-01 the launch is done\n"))
        self.assertIn(CLEAN, self.check("--archive").out)


class KnowledgeShapeTest(LensShapeCase):
    file: str = "layers/knowledge/home.lease/topic.md"

    def test_a_valid_topic_is_clean_and_history_is_skipped(self):
        self.write("layers/knowledge/history/2026.md", "narratives, not a topic\n")
        self.write("layers/knowledge/index.md", "generated\n")
        self.assertIn(CLEAN, self.put(self.file, TOPIC))
        self.assertIn(CLEAN, self.put(self.file, TOPIC, "related: [money.budget, work:home.move]\nfresh_for: 1y\n", ""))
        self.assertIn(CLEAN, self.put(self.file, TOPIC, "fresh_for: 1y", "fresh_for: never"))

    def test_each_rule(self):
        self.assertIn(
            "name is 'lease', but the node is named 'home.lease'",
            self.put(self.file, TOPIC, "name: home.lease", "name: lease"),
        )
        self.assertIn(
            "fresh_for is '1 year', expected to match", self.put(self.file, TOPIC, "fresh_for: 1y", "fresh_for: 1 year")
        )
        self.assertIn("updated is 'Nov 4'", self.put(self.file, TOPIC, "updated: 2026-11-04", "updated: Nov 4"))
        self.assertIn("missing key 'summary'", self.put(self.file, TOPIC, "summary: ends in August\n", ""))
        self.assertIn("missing topic.md", self.put("layers/knowledge/money.budget/notes.md", "loose\n"))


class LiteracyShapeTest(LensShapeCase):
    file: str = "layers/literacy/money.investing.index-funds/subject.md"

    def test_a_valid_subject_is_clean_and_the_library_is_skipped(self):
        self.write("layers/literacy/library/x.md", ARTIFACT.format(name="x"))
        self.assertIn(CLEAN, self.put(self.file, SUBJECT))
        self.assertIn(CLEAN, self.put(self.file, SUBJECT, "rests_on: [knowledge:money.investing]\nstale:\n", ""))

    def test_each_rule(self):
        self.assertIn("level is 'expert'", self.put(self.file, SUBJECT, "level: can-use", "level: expert"))
        self.assertIn(
            "subject is 'funds'", self.put(self.file, SUBJECT, "subject: money.investing.index-funds", "subject: funds")
        )
        self.assertIn(
            "tracked is 'September'", self.put(self.file, SUBJECT, "tracked: 2026-09-14", "tracked: September")
        )
        self.assertIn("missing key 'tracked'", self.put(self.file, SUBJECT, "tracked: 2026-09-14\n", ""))


class LibraryShapeTest(LensShapeCase):
    top: str = "layers/literacy/library/compound-interest.md"
    grouped: str = "layers/literacy/library/math.infinite-series/convergence-tests.md"

    def test_valid_artifacts_at_the_top_and_in_a_group(self):
        self.write(self.top, ARTIFACT.format(name="compound-interest"))
        self.assertIn(CLEAN, self.put(self.grouped, ARTIFACT.format(name="convergence-tests")))

    def test_a_draft_may_leave_out_its_tags(self):
        draft = ARTIFACT.format(name="compound-interest")
        for line in ("type: walkthrough\n", "subjects: [money.investing]\n", "perspective: personalized\n"):
            draft = draft.replace(line, "")
        self.assertIn(CLEAN, self.put(self.top, draft))

    def test_groups_are_one_level_only(self):
        self.write("layers/literacy/library/math/series/deep.md", "no frontmatter\n")
        self.assertIn(CLEAN, self.check().out)

    def test_each_rule(self):
        text = ARTIFACT.format(name="compound-interest")
        self.assertIn(
            "perspective is 'mine'", self.put(self.top, text, "perspective: personalized", "perspective: mine")
        )
        self.assertIn("artifact is 'ci'", self.put(self.top, text, "artifact: compound-interest", "artifact: ci"))
        self.assertIn("created is '14 Oct'", self.put(self.top, text, "created: 2026-10-14", "created: 14 Oct"))
        out = self.put(self.top, text, "sharing: private", "sharing: public")
        self.assertIn(
            "sharing is public, but only a generic artifact can be opened up (perspective: personalized)", out
        )
        generic = text.replace("perspective: personalized", "perspective: generic")
        self.assertIn(CLEAN, self.put(self.top, generic, "sharing: private", "sharing: protected"))

    def test_names_are_unique_across_groups(self):
        self.write(self.top, ARTIFACT.format(name="compound-interest"))
        self.write(
            "layers/literacy/library/money.basics/compound-interest.md", ARTIFACT.format(name="compound-interest")
        )
        self.assertIn(
            "name 'compound-interest' is already used by layers/literacy/library/compound-interest.md", self.check().out
        )


LENS = """\
---
lens: nodes
version: 1
version_note: First.
derives_from: []
status: active
updated: 2026-11-01
verified: true
sharing: public
frames: [node-shape]
---
"""

FRAME = """\
---
frame: node-shape
kind: structural
lens: nodes
derives_from: [nodes@1]
version: 1
version_note: First.
status: active
updated: 2026-11-01
sharing: public
reads: []
writes: []
protocol: []
---
"""


class SharingUntilTest(LensShapeCase):
    """`until:` is an optional end date right after `sharing:`, only when sharing is more open than private."""

    def nodes(self) -> list[tuple[str, str, str]]:
        """(path, frontmatter, its sharing line) for every tree that has sharing."""
        return [
            ("core/protocol/lenses/nodes.md", LENS, "sharing: public"),
            ("core/protocol/frames/nodes/node-shape.md", FRAME, "sharing: public"),
            ("core/operating-modes/brainstorming.md", OPERATING_MODE, "sharing: public"),
            ("layers/projections/work-dashboard.md", PROJECTION, "sharing: private"),
            (
                "layers/literacy/library/compound-interest.md",
                ARTIFACT.format(name="compound-interest").replace("perspective: personalized", "perspective: generic"),
                "sharing: private",
            ),
        ]

    def test_each_tree_takes_until_after_an_open_sharing(self):
        for path, text, line in self.nodes():
            with self.subTest(path=path):
                self.assertIn(CLEAN, self.put(path, text))
                self.assertIn(CLEAN, self.put(path, text, line, "sharing: protected\nuntil: 2026-12-31"))
                self.assertIn(CLEAN, self.put(path, text, line, "sharing: public\nuntil: 2026-12-31"))
                os.remove(self.path(path))

    def test_each_rule_once_per_tree(self):
        for path, text, line in self.nodes():
            with self.subTest(path=path):
                out = self.put(path, text, line, "sharing: private\nuntil: 2026-12-31")
                self.assertIn("until only goes with sharing protected or public (sharing is private)", out)
                out = self.put(path, text, line, "sharing: protected\nuntil: end of year")
                self.assertIn("until is 'end of year', expected a date", out)
                out = self.put(path, text, line, "until: 2026-12-31\nsharing: protected")
                self.assertIn("keys out of order", out)
                self.assertIn(CLEAN, self.put(path, text, line, "sharing: private\nuntil:"))  # empty is no end date
                os.remove(self.path(path))


class HistoryAndReferenceKindsTest(unittest.TestCase):
    def test_history_by_name_folder_and_pattern_and_history_wins_over_reference(self):
        shapes = read_shapes(SHAPES_TEMPLATE)
        self.assertTrue(shapes.is_history("layers/focus/f1-x/history.md"))
        self.assertTrue(shapes.is_history("core/records/agents/notes.md"))
        self.assertTrue(shapes.is_history("core/records/absorbed.md"))
        self.assertTrue(shapes.is_history("core/ai/personas/sage/journal.md"))
        self.assertFalse(shapes.is_history("core/ai/personas/sage/sage.md"))
        self.assertTrue(shapes.is_reference("core/ai/personas/sage/sage.md"))
        self.assertTrue(shapes.is_reference("core/ai/agents/notes.md"))
        self.assertFalse(shapes.is_reference("core/ai/personas/sage/journal.md"))


if __name__ == "__main__":
    unittest.main()
