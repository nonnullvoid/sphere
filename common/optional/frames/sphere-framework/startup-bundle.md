---
frame: startup-bundle
lens: [sphere-framework]
derives_from: [sphere-framework@1]
version: 1
version_note: First draft. One generated file holding everything a window reads at startup, for spheres whose startup has grown slow.
status: drafting
updated: 2026-11-19
sharing: public
reads: [core/identity.json, core/user/profile.md, core/ai/personas, core/engine.md, core/protocol, core/manifest.md]
writes: [core/startup.md]
protocol: [stale-found, focus-grounding]
---

# The startup bundle

**Applies to:** a sphere whose startup has grown slow or uneven: a fresh window takes many reads before it can answer, or two fresh windows start from different pictures of the sphere. **Not** a fresh or small sphere: there the files themselves are quick to read, and a bundle is one more thing to keep current.

Startup reads the same slices every time: who the human is, the persona, the engine, the guards, the manifest. In a young sphere that's a handful of short files. In a sphere used every day for months the guards multiply, the manifest grows and the profile gains sections, and startup becomes a dozen or more reads before the first answer. The bundle puts those slices into one file, so a fresh window reads one thing and starts from exactly the same place every time.

## What it holds

In this order, each under a heading that names its source file:

1. **Identity:** the sphere's name and version, from `core/identity.json`.
2. **The human:** the frontmatter and first section of `core/user/profile.md`. Never the whole profile.
3. **The default persona:** the persona file marked `default: true`, without its journal.
4. **The engine:** `core/engine.md`, whole.
5. **The guards:** every frame marked `always: true`, whole.
6. **The manifest:** `core/manifest.md`, whole, reactions table included.

Its first line carries the hash of everything it was built from. **Nothing goes in it that isn't already in those files.** It's a copy, never a source: no one edits it, and no rule lives only there.

## Rules

- **It's built by a script, never by the AI.** The point is a cheaper and repeatable start; an AI assembling it would cost what it saves and vary each time. A build that adopts this frame adds `scripts/build-startup`, which concatenates the slices above and writes the hash.
- **It's a machine-only cache.** `core/startup.md` is gitignored and never committed or exported. Delete it and nothing is lost: startup falls back to reading the files, which is what `sphere.md` describes anyway.
- **It's checked before it's trusted.** Startup compares the hash on the bundle's first line with the sources. On a mismatch it rebuilds, or, if it can't, reads the files directly. A stale bundle is never read.
- **Startup changes in one place.** `sphere.md` gains one line before its startup steps: *if `core/startup.md` is current, read it instead of steps 1 to 4.* The steps themselves stay as they are, as the fallback.
- **Measure before and after.** Adopt it because a cold-start count says startup is the cost, and keep it only if the count drops.

## Adopting it

In sphere authoring, with the human's yes:

1. Copy this frame into `core/protocol/frames/sphere-framework/` and add `startup-bundle` to the sphere-framework lens's `frames:`.
2. Add `scripts/build-startup` and the line in `sphere.md`. Add `core/startup.md` to `.gitignore`.
3. Rebuild the manifest; run `scripts/manifest-check`.

## When / do

| When | Do |
|---|---|
| A window starts and `core/startup.md` exists | Compare its hash with the sources; read it if current, otherwise rebuild it, or read the files |
| `focus-grounding`, if anything the bundle holds changed | Run `scripts/build-startup` after the manifest is rebuilt |
| The bundle's hash doesn't match its sources | Fire `stale-found` for the bundle; rebuild it |
| The bundle grows past what startup should carry | Look at what grew (usually the guards or the profile's first section) and propose trimming the source, not the bundle |

## Works with

- [capability-manifest](capability-manifest.md): the largest slice it carries, and rebuilt first.
- [kinds-of-file](../nodes/kinds-of-file.md): the bundle is a generated file, rebuilt and never hand-edited.
- [export-contract](../replication/export-contract.md): generated files never travel.

## Senses

| Sense | Fires when |
|---|---|
| `stale-found` | for the bundle: its hash no longer matches the files it was built from |
