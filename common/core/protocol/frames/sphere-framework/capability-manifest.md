---
frame: capability-manifest
lens: [sphere-framework]
derives_from: [sphere-framework@1]
version: 1
version_note: First draft. Entries, rebuilding, and use at startup. Built by script from Applies-to lines; no reactions table; size budget.
status: drafting
updated: 2026-11-20
sharing: public
reads: [core/protocol]
writes: [core/manifest.md]
protocol: [I-know-what-it-can-do, A-build-manifest, floor-grew, focus-grounding, sphere-authoring-started, sphere-authoring-ended]
---

# The capability manifest

**Applies to:** every window at startup, and every change to a lens or frame.

The manifest, `core/manifest.md`, is the sphere's routing table: one short file that says everything the sphere can do and when each thing applies, so nothing else has to be read until it's needed. It's the [registry pattern](../../lenses/sphere-framework.md#the-registry-pattern) applied to capabilities.

## What's in it

| Part | Says |
|---|---|
| **Always on** | every guard marked `always: true`, with what it covers |
| **Lenses** | each lens's name and title: why the sphere works as it does |
| **Frames** | grouped by folder, each frame's name and its **Applies to:** line, cut to one sentence |

A header says it's generated, when, and carries a hash over the lens and frame files. That hash is what the [manifest-check](../readable-substrate/manifest-check.md) compares.

**No mechanics, and no reactions.** What follows a sense is computed from the frames when it fires (see [reactions](reactions.md)), so the manifest only has to say what exists and when it applies. That keeps it small enough to load whole in every window: it has a size budget, and the check reports a manifest over it.

## How it's used

- **Loaded at startup,** whole. A tool that imports files (Claude Code, through `CLAUDE.md`) has it in context before the first word; others read it in the startup batch. Lens and frame text stays unread.
- **Stop at the shallowest depth that answers.** "Is there a frame for this?" is answered by the manifest. Only "do it" opens the frame. The lens opens only when the *why* is in question.
- **If it isn't in the manifest, it doesn't exist.** The sphere doesn't go looking through `frames/` for abilities. A frame that should be used has to be listed.

## How it's built

- **By a script, never by hand or by the AI:** `scripts/sphere manifest`. The same lens and frame files always give the same manifest. *Why:* the judgment a good line needs was made once, when the frame's **Applies to:** was written. Rebuilding it by hand in every ground would cost a window's attention and drift with each rewrite.
- **To improve a line, improve the frame.** A vague or overlong entry is fixed in the frame's **Applies to:**, in sphere authoring, and the manifest rebuilt.
- **Rebuilt whenever a lens or frame changes,** by `sphere ground` itself, in the same commit as the change. `sphere start` rebuilds it too if it's found stale.
- **Checked by the tooling, every ground.** See [manifest-check](../readable-substrate/manifest-check.md).
- **Committed.** It's a view a person reads: opening it is how the human sees what their sphere knows how to do.
- **Built fresh in every sphere.** A new sphere is assembled with one; a seed carries the script, never a built manifest.

## When / do

| When | Do |
|---|---|
| A window starts | Have the manifest in context (imported, or read in the startup batch); open nothing else until a task points at it |
| A task might need a capability | Look it up in the manifest; open the frame only to run it |
| `focus-grounding`, if a lens or frame was added, changed or retired | Nothing to do: `sphere ground` rebuilds it and commits it with the change |
| `sphere-authoring-started` | Load the deeper engine mechanics: how evolution runs, how replication works, how registries rebuild |
| `sphere-authoring-ended` | Drop the deeper engine mechanics again |
| Something is added to the floor | Say so in a line; reflection asks whether it earns its place. Fire `floor-grew` |
| The manifest-check says it's stale or missing | Run `scripts/sphere manifest` |
| The manifest is over its budget | Propose tightening the longest **Applies to:** lines; never trim the manifest itself |
| Someone edited the manifest by hand | Ask where the change belongs; put it in that lens or frame and rebuild |

## Works with

- [reactions](reactions.md): what follows a sense, computed when it fires rather than listed here.
- [manifest-check](../readable-substrate/manifest-check.md): the check that keeps the manifest true to its sources.
- [kinds-of-file](../nodes/kinds-of-file.md): the manifest is generated; nobody writes it directly.

## Senses

| Sense | Fires when |
|---|---|
| `floor-grew` | something was added to the floor. Worth a second look |
