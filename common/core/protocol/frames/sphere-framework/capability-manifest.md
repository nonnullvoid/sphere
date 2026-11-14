---
frame: capability-manifest
kind: structural
lens: [sphere-framework]
derives_from: [sphere-framework@1]
version: 1
version_note: First draft. Entries, rebuilding, and use at startup.
status: drafting
updated: 2026-11-12
sharing: public
reads: [core/protocol]
writes: [core/manifest.md]
protocol: [I-know-what-it-can-do, A-build-manifest, manifest-built]
---

# The capability manifest

**Applies to:** every window at startup, and every change to a lens or frame.

The manifest, `core/manifest.md`, is the sphere's routing table: one short file that says everything the sphere can do and when each thing applies, so nothing else has to be read until it's needed. It's the [registry pattern](../../../../../spec/registries.md#the-registry-pattern--proven) applied to capabilities.

## What's in it

**One entry per lens; under it, one line per frame.**

| Part | Says |
|---|---|
| **Lens line** | its name and its job, in one line |
| **When to load** | the topics or situations that make this lens relevant |
| **Frame line** | its name, its scope in one line, and its trigger: the command or sense that brings it in |

A header at the top says it's generated, when it was built, which files it was built from, and a hash over them. That hash is what the [manifest-check](../readable-substrate/manifest-check.md) compares.

**An entry is a pointer, never a copy.** If a line needs more than a sentence, the detail belongs in the frame.

## How it's used

- **Read at startup,** with the identity core. Lens and frame text stays unread.
- **Stop at the shallowest depth that answers.** "Is there a frame for this?" is answered by the manifest. Only "do it" opens the frame. The lens opens only when the *why* is in question.
- **If it isn't in the manifest, it doesn't exist.** The sphere doesn't go looking through `frames/` for abilities. A frame that should be used has to be listed.

## How it's built

- **The AI writes the entries.** A good "when to load" line takes judgment, so it isn't a blind copy of frontmatter. It's drawn from each lens's and frame's frontmatter, its opening lines, and its rows in the [protocol registry](protocol-registry.md).
- **Nobody edits it by hand.** It's a generated file: change the lens or frame and rebuild. A hand edit is caught at the next check and moved into the file it belongs to.
- **Rebuilt in the same ground as the change.** A lens or frame added, renamed, retired or reworded means its entries are rebuilt before the ground commits. Untouched entries are left as they are.
- **Checked by the tooling, every ground.** See [manifest-check](../readable-substrate/manifest-check.md).
- **Committed.** It's a view a person reads: opening it is how the human sees what their sphere knows how to do.
- **Built fresh in every sphere.** A seed carries the frames and scripts that build a manifest, never a built one. A new sphere builds its own on first start.

## When / do

| When | Do |
|---|---|
| A window starts | Read the manifest with the identity core; open nothing else until a task points at it |
| A task might need a capability | Look it up in the manifest; open the frame only to run it |
| A lens or frame is added, changed or retired | Rebuild its entries in the same ground; fire `manifest-built` |
| The manifest-check reports drift | Rebuild the entries it names, then check again |
| Someone edited the manifest by hand | Ask where the change belongs; put it in that lens or frame and rebuild |
| A new sphere starts from a seed | Build its manifest from its own lenses and frames |

## Works with

- [protocol-registry](protocol-registry.md): the manifest's triggers come from the vocabulary registered there.
- [manifest-check](../readable-substrate/manifest-check.md): the check that keeps the manifest true to its sources.
- [kinds-of-file](../nodes/kinds-of-file.md): the manifest is generated; nobody writes it directly.
- [loading](../../../../../spec/loading.md): the tiers this manifest sits in, and why bodies load late.

## Senses

| Sense | Fires when |
|---|---|
| `manifest-built` | the manifest was rebuilt |
