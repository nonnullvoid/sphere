---
frame: manifest-check
kind: instinct
lens: [readable-substrate, sphere-framework]
derives_from: [readable-substrate@1, sphere-framework@1]
version: 1
version_note: First draft. The manifest and the protocol registry, checked against lenses and frames.
status: drafting
updated: 2026-11-12
sharing: public
reads: [core/protocol, core/manifest.md]
writes: []
protocol: [I-trust-what-i-read, A-check-manifest, manifest-stale]
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
| **Data locations exist** | Every path in a frame's `reads:` and `writes:` exists in this sphere |

The shape of each lens and frame file (its keys, in order) is a node's shape, so the [structure-check](structure-check.md) covers it.

## Rules

- **It reports; it never rewrites.** Drift in the manifest or the registry is rebuilt by the AI, following their own frames, and the check runs again until it's clean.
- **A frame behind its lens isn't bumped.** Changing the number would hide the question. The frame is re-read against the new lens: often nothing changes and the version it names moves up; when something does, the change is proposed to the human.
- **It never blocks the ground,** and a finding isn't dropped: it's fixed this ground or put to the human.
- **A missing data location is asked about,** not created. It may be a layer this sphere doesn't have, or a frame copied from another sphere that needs adapting.

## When / do

| When | Do |
|---|---|
| Ground, when a lens or frame changed | Run the check after the manifest and registry are rebuilt |
| Coverage or freshness fails | Fire `manifest-stale`; rebuild the entries it names, then check again |
| A lens and its frames disagree | Offer the one-line fix to whichever list is wrong |
| A frame is behind its lens | Re-read the frame against the lens; propose any change; then move its `derives_from` up |
| A registry row has no frame, or a frame's entry has no row | Add the row, or retire it, following the protocol registry |
| A frame names a path this sphere doesn't have | Ask: adapt the frame, or create what it expects? |

## Works with

- [capability-manifest](../sphere-framework/capability-manifest.md) and [protocol-registry](../sphere-framework/protocol-registry.md): what this check confirms, and how each is rebuilt.
- [structure-check](structure-check.md): the same idea for the sphere's anatomy and nodes.
- [propose-dont-decide](../human-is-highest/propose-dont-decide.md): a frame re-derived against a changed lens is proposed, not rewritten.
- [loading](../../../../../spec/loading.md#the-capability-manifest--decided-not-yet-exercised) and [protocol](../../../../../spec/protocol.md#versioning-and-drift--decided-not-yet-exercised): the manifest and versioning, in the spec.

## Senses

| Sense | Fires when |
|---|---|
| `manifest-stale` | the manifest no longer matches the lens and frame files it was built from |
