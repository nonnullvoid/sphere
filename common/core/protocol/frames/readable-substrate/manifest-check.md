---
frame: manifest-check
lens: [readable-substrate, sphere-framework]
derives_from: [readable-substrate@1, sphere-framework@1]
version: 1
version_note: First draft. The manifest and the protocol registry, checked against lenses and frames.
status: drafting
updated: 2026-11-20
sharing: public
reads: [core/protocol, core/manifest.md]
writes: []
protocol: [I-trust-what-i-read, A-check-manifest, stale-found, focus-grounding, lens-shifted]
---

# The manifest check

**Applies to:** every ground, every change to a lens or frame, and any time the human asks *"is the sphere up to date with itself?"*

The [capability manifest](../sphere-framework/capability-manifest.md) and the [protocol registry](../sphere-framework/protocol-registry.md) are written by the AI, with judgment. That's why they need a check that isn't: a deterministic comparison, in the tooling, between them and the lens and frame files on disk. *Why:* a rule that says "rebuild this at every ground" is a habit, and habits lapse without anyone noticing.

## What it checks

| Check | Confirms |
|---|---|
| **Manifest coverage** | Every lens and frame on disk has an entry, and every entry points at a file that exists |
| **Manifest freshness** | The hash in the manifest's header matches the lens and frame files now. A mismatch means something changed since it was built |
| **Lens and frame agree** | A lens's `frames:` lists exactly the frames whose `lens:` names it, both ways |
| **Frames keep up with lenses** | A frame's `derives_from` names its lens's current version. One that names an older version is behind |
| **Registry and frames agree** | Every entry in a frame's `protocol:` field has a row in the registry, and every row's frame exists |
| **The set stands alone** | Every link in a lens or frame resolves to a file inside the protocol folder. A lens and its frames describe an idea completely, so they never lean on anything outside it: not the architecture's spec, not this sphere's data |
| **Data locations exist** | Every path in a frame's `reads:` and `writes:` exists in this sphere |
| **Senses are wired** | Every sense a When/do row reacts to, or a frame fires, is in that frame's `protocol:` list; every core moment has a frame that reacts to it |
| **The manifest stays small** | It's within its size budget. It's loaded in every window, so a manifest that grows past it costs every window |

The shape of each lens and frame file (its keys, in order) is a node's shape, so the [structure-check](structure-check.md) covers it.

**The tool is `scripts/manifest-check`.** In a sphere it runs every check above. `--set <protocol folder>` checks a common set on its own, with no manifest or data locations. `--hash` prints the hash the manifest's header should carry.

## Rules

- **It reports; it never rewrites.** A stale manifest is rebuilt with `scripts/sphere manifest`; drift in the registry is rebuilt by the AI, following its frame, and the check runs again until it's clean.
- **A frame behind its lens isn't bumped.** Changing the number would hide the question. The frame is re-read against the new lens: often nothing changes and the version it names moves up; when something does, the change is proposed to the human.
- **It never blocks the ground,** and a finding isn't dropped: it's fixed this ground or put to the human.
- **A missing data location is asked about,** not created. It may be a layer this sphere doesn't have, or a frame copied from another sphere that needs adapting.

## When / do

| When | Do |
|---|---|
| `focus-grounding`, if a lens or frame changed | Run the check after the manifest and registry are rebuilt |
| Coverage or freshness fails | Fire `stale-found` for the manifest; run `scripts/sphere manifest`, then check again |
| The manifest is over its budget | Propose tightening the longest **Applies to:** lines, in sphere authoring |
| A lens and its frames disagree | Offer the one-line fix to whichever list is wrong |
| `lens-shifted` | Re-read each frame derived from it against the lens; propose any change; then move its `derives_from` up |
| A registry row has no frame, or a frame's entry has no row | Add the row, or retire it, following the protocol registry |
| A lens or frame links outside the protocol folder | Say what it needs in the file itself, or link the frame that owns it |
| A frame names a path this sphere doesn't have | Ask: adapt the frame, or create what it expects? |

## Works with

- [capability-manifest](../sphere-framework/capability-manifest.md) and [protocol-registry](../sphere-framework/protocol-registry.md): what this check confirms, and how each is rebuilt.
- [structure-check](structure-check.md): the same idea for the sphere's anatomy and nodes.
- [propose-dont-decide](../human-is-highest/propose-dont-decide.md): a frame re-derived against a changed lens is proposed, not rewritten.

## Senses

| Sense | Fires when |
|---|---|
| `stale-found` | for the manifest: it no longer matches the lens and frame files it was built from |
