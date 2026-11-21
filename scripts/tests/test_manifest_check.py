"""Tests for scripts/manifest-check: the registry, the manifest and the lens and frame files agree."""

import os
import shutil
import tempfile
import unittest

from sphere_testing import REPO, SCRIPTS, run

MANIFEST_CHECK = os.path.join(SCRIPTS, "manifest-check")

LENS = """---
lens: tidy
version: 2
frames: [sweep, dust]
---

# Tidy
"""

SWEEP = """---
frame: sweep
lens: [tidy]
derives_from: [tidy@2]
reads: []
writes: []
protocol: [I-clean-home, A-sweep, room-entered]
---

# Sweep

## When / do

| When | Do |
|---|---|
| *"Sweep"* | Sweep. Fire `room-entered` |

## Senses

| Sense | Fires when |
|---|---|
| `room-entered` | someone walks in |
"""

DUST = """---
frame: dust
lens: [tidy]
derives_from: [tidy@2]
reads: []
writes: []
protocol: [I-clean-home, A-dust, room-entered]
---

# Dust

## When / do

| When | Do |
|---|---|
| `room-entered`, if it's dusty | Dust |
"""

REGISTRY = """# Protocol registry

## Senses

### Core moments

| Sense | Fires when | Produced by | Reacted to by |
|---|---|---|---|
| `room-entered` | someone walks in | [sweep](frames/house/sweep.md) | [dust](frames/house/dust.md) |

## Intents

| Intent | Means | Home | Lens | Also listed by |
|---|---|---|---|---|
| `I-clean-home` | a clean home | [sweep](frames/house/sweep.md) | tidy | [dust](frames/house/dust.md) |

## Abilities

| Ability | Does | Home | Serves | Also listed by |
|---|---|---|---|---|
| `A-sweep` | sweep | [sweep](frames/house/sweep.md) | `I-clean-home` | — |
| `A-dust` | dust | [dust](frames/house/dust.md) | `I-clean-home` | — |
"""


class ManifestCheckCase(unittest.TestCase):
    root: str = ""  # set in setUp, the unittest way

    def setUp(self):
        self.root = tempfile.mkdtemp(prefix="manifest-check-test-")
        self.write("core/protocol/lenses/tidy.md", LENS)
        self.write("core/protocol/frames/house/sweep.md", SWEEP)
        self.write("core/protocol/frames/house/dust.md", DUST)
        self.write("core/protocol/protocol.md", REGISTRY)

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def write(self, path: str, text: str) -> None:
        full = os.path.join(self.root, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as handle:
            handle.write(text)

    def bend(self, path: str, old: str, new: str) -> None:
        with open(os.path.join(self.root, path), encoding="utf-8") as handle:
            text = handle.read()
        self.assertIn(old, text)
        self.write(path, text.replace(old, new, 1))

    def check(self, *args: str) -> str:
        return run([MANIFEST_CHECK, "--root", self.root, *args], cwd=self.root).out

    def check_set(self) -> str:
        return self.check("--set", os.path.join(self.root, "core/protocol"))

    def manifest(self, reactions: str = "room-entered\n  dust   if it's dusty   dust\n") -> None:
        digest = self.check("--hash").strip()
        self.write(
            "core/manifest.md",
            f"<!-- Built at ground. Hash: {digest} -->\n\n## tidy\n- `sweep`: sweep.\n- `dust`: dust.\n\n"
            f"## Reactions\n{reactions}",
        )


class CommonSetTest(unittest.TestCase):
    def test_the_common_set_passes_its_own_check(self):
        out = run([MANIFEST_CHECK, "--set", "common/core/protocol"], cwd=REPO).out
        self.assertEqual(out.strip(), "manifest-check: clean")


class SetTest(ManifestCheckCase):
    def test_clean(self):
        self.assertEqual(self.check_set().strip(), "manifest-check: clean")

    def test_an_entry_with_no_row(self):
        self.bend(
            "core/protocol/protocol.md", "| `A-dust` | dust | [dust](frames/house/dust.md) | `I-clean-home` | — |\n", ""
        )
        self.assertIn("no row for 'A-dust' (listed by dust)", self.check_set())

    def test_a_row_no_frame_lists(self):
        self.bend("core/protocol/frames/house/dust.md", "A-dust, ", "")
        self.assertIn("'A-dust' isn't in any frame's protocol: list", self.check_set())

    def test_a_row_that_links_to_nothing(self):
        self.bend(
            "core/protocol/protocol.md",
            "| [dust](frames/house/dust.md) | `I-clean-home`",
            "| [dust](frames/house/mop.md) | `I-clean-home`",
        )
        self.assertIn("'A-dust' links to frames/house/mop.md, which doesn't exist", self.check_set())

    def test_a_reaction_the_frame_doesnt_list(self):
        self.bend("core/protocol/frames/house/dust.md", ", room-entered]", "]")
        out = self.check_set()
        self.assertIn("a When/do row reacts to `room-entered`, which isn't in its protocol: list", out)

    def test_a_fired_sense_the_frame_doesnt_list(self):
        self.bend("core/protocol/frames/house/sweep.md", "Sweep. Fire `room-entered`", "Sweep. Fire `room-swept`")
        self.assertIn("fires `room-swept`, which isn't in its protocol: list", self.check_set())

    def test_a_core_moment_nothing_reacts_to(self):
        self.bend("core/protocol/frames/house/dust.md", "| `room-entered`, if it's dusty |", "| Dusty |")
        self.assertIn("core moment 'room-entered' has no frame that reacts to it", self.check_set())

    def test_a_frame_never_links_outside_the_set(self):
        link = "Sweep (see [spec](../../../../spec/tidy.md)). Fire"
        self.bend("core/protocol/frames/house/sweep.md", "Sweep. Fire", link)
        self.assertIn("links to ../../../../spec/tidy.md, outside the protocol set", self.check_set())

    def test_a_frame_link_to_a_missing_file(self):
        self.bend("core/protocol/frames/house/sweep.md", "Sweep. Fire", "Sweep (see [mop](mop.md#how)). Fire")
        self.assertIn("links to mop.md, which isn't in this set", self.check_set())

    def test_lens_and_frame_disagree(self):
        self.bend("core/protocol/lenses/tidy.md", "frames: [sweep, dust]", "frames: [sweep]")
        self.assertIn("lens tidy's frames: doesn't list dust", self.check_set())

    def test_a_frame_behind_its_lens(self):
        self.bend("core/protocol/lenses/tidy.md", "version: 2", "version: 3")
        self.assertIn("derives from tidy@2; the lens is at 3", self.check_set())

    def test_a_set_has_no_manifest_or_data_checks(self):
        self.bend("core/protocol/frames/house/dust.md", "reads: []", "reads: [layers/attic]")
        self.assertNotIn("manifest", self.check_set().replace("manifest-check:", ""))


class SphereTest(ManifestCheckCase):
    def test_clean_with_a_fresh_manifest(self):
        self.manifest()
        self.assertEqual(self.check().strip(), "manifest-check: clean")

    def test_no_manifest_yet(self):
        self.assertIn("no manifest yet", self.check())

    def test_a_stale_manifest(self):
        self.manifest()
        self.bend("core/protocol/frames/house/dust.md", "| Dust |", "| Dust, then polish |")
        self.assertIn("core/manifest.md: stale: built from", self.check())

    def test_a_manifest_over_its_budget(self):
        self.manifest(reactions="x" * 13 * 1024 + "\n")
        self.assertIn("over the 12 KB budget", self.check())

    def test_every_lens_and_frame_has_an_entry(self):
        self.manifest()
        self.bend("core/manifest.md", "- `dust`: dust.\n", "")
        self.assertIn("no entry for 'dust'", self.check())

    def test_a_data_location_the_sphere_doesnt_have(self):
        self.manifest()
        self.bend("core/protocol/frames/house/dust.md", "reads: []", "reads: [layers/attic]")
        self.manifest()
        self.assertIn("names 'layers/attic', which this sphere doesn't have", self.check())

    def test_reports_but_never_blocks_unless_strict(self):
        result = run([MANIFEST_CHECK, "--root", self.root], cwd=self.root)
        self.assertEqual(result.code, 0)
        self.assertEqual(run([MANIFEST_CHECK, "--root", self.root, "--strict"], cwd=self.root).code, 1)


if __name__ == "__main__":
    unittest.main()
