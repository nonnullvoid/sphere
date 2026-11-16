---
frame: sphere-identity
kind: structural
lens: [replication]
derives_from: [replication@1]
version: 1
version_note: First draft. A UUID v7 id made once, a display name, a version that advances with the protocol and is tagged in git, lineage fixed at birth; signing later, as a new version of this frame.
status: drafting
updated: 2026-11-13
sharing: public
reads: [core/identity.json]
writes: [core/identity.json]
protocol: [I-know-where-it-came-from, A-show-identity, A-name-sphere, A-advance-version, sphere-versioned]
---

# Sphere identity

**Applies to:** init, naming or renaming a sphere, any change to its protocol, every export, and *"which sphere is this?"*

_Decided, not yet exercised._

## Who a sphere is

Every sphere has a stable identity, so provenance always names spheres the same way:

| Field | Is | Example |
|---|---|---|
| **id** | A UUID v7, made once at init and never changed. Practically unique, and sortable by when the sphere was born | `01933b7e-8f2a-7c41-9d3e-5b6a2f0c1e88` |
| **name** | A display name the human chooses. Unique where possible, never guaranteed | `ridgeline-worksphere` |
| **version** | A tag for the sphere's shape, which moves when its protocol changes | `2026.10.3` |
| **born_from** | Where the sphere began: a published architecture and build, or a parent sphere | `{ "architecture": "1.0", "build": "base-sphere 1.0.0" }` |

It lives in its own small file, `core/identity.json`, so tooling can read it without parsing anything else, and provenance copies it exactly:

```json
{
  "id": "01933b7e-8f2a-7c41-9d3e-5b6a2f0c1e88",
  "name": "ridgeline-worksphere",
  "version": "2026.10.3",
  "born_from": { "architecture": "1.0", "build": "base-sphere 1.0.0" }
}
```

**It names the sphere and nothing about its human.** That's why it can travel in every export.

## Born once

**At init, the sphere makes its id and records where it began.**

- **The id is new.** A sphere started from a seed is a new sphere, so it never takes its parent's id.
- **`born_from` is lineage: fixed, written once.** It names the published architecture and build the sphere started from, or the parent sphere it was seeded from, by that sphere's id, name and version. A sphere that has grown its own way since is still truly described by where it began.
- **What a sphere resembles today is worked out, not declared.** A [comparison](export-contract.md#comparing) can report the closest published architecture and how the sphere differs, whenever someone asks. **A sphere is never required to conform to an architecture.**

## The name

- **The human chooses it.** The sphere can suggest one: two plain words and what the sphere is for (`ridgeline-worksphere`, `harbor-homesphere`).
- **A name travels in every export,** so the sphere suggests names that don't include the human's own, and the leak scan checks it like anything else.
- **Renaming changes the name only.** The id stays, so everything that came from the sphere can still be traced to it. A rename isn't a new version.

## Version

**The default scheme is the year, the month, and a count:** `2026.10.3` is the third version in October 2026.

- **It advances when the protocol changes:** a lens or frame lands, changes or retires (see [crystallization](../evolution/crystallization.md#make-the-change)). Work, knowledge and every other kind of data never move it. *Why:* the version describes the sphere's shape, which is what travels and what another sphere compares against.
- **Each version is a git tag, `sphere-<version>`, on the ground that made it.** Any past shape of the sphere can be looked at again, and a [fork](../evolution/crystallization.md#fork-build-alongside-switch-once) tags its before and after with these.
- **The next version is computed, not counted by hand.** It's this month's highest tag plus one, or `.1` in a new month. The value in `core/identity.json` is a copy for tooling that reads without git; if the two disagree, the tag wins.
- Fire `sphere-versioned` when the version moves.

## A swappable part

**The interface is fixed; the scheme isn't.** Every sphere has `core/identity.json` with these four fields, and an id that never changes. How names are suggested, and how versions advance (by date, by count, at every protocol change or only at exports), is this frame. A sphere that wants a different scheme swaps this frame for its own, and nothing else changes.

## Signing, later

**Nothing here proves a sphere is who it says it is.** True uniqueness and authenticity need signing, with public and private keys, and that's more machinery than spheres need until many of them are out in the world exchanging seeds.

**When that happens, signing arrives as a new version of this frame.** The public key joins `core/identity.json`; the private key never travels. Exports and provenance carry a signature. Nothing else in the architecture has to change. Until then, trust between spheres rests on how their humans set up access, which is sound between people who share a home or a machine.

## When / do

| When | Do |
|---|---|
| Init | Make a new UUID v7; record `born_from`; ask the human for a name, with a suggestion; set the first version |
| *"Which sphere is this?"* | Answer from `core/identity.json`: name, version, where it began |
| The human renames the sphere | Change `name` only; the id stays |
| A lens or frame lands, changes or retires | Compute the next version; write it; tag the ground `sphere-<version>`. Fire `sphere-versioned` |
| Data changes | Nothing. The version follows the protocol only |
| An export is built | Copy the identity exactly into its provenance |
| `core/identity.json` and the tags disagree | The tag wins; correct the file |
| Someone asks which architecture the sphere follows | Compare and describe. Never declare it, and never require conforming |

## Works with

- [export-contract](export-contract.md): provenance carries the identity; init creates it.
- [crystallization](../evolution/crystallization.md): the step that changes the protocol moves the version.
- [state-machine](../continuity/state-machine.md): the version's tag sits on a ground.
- [versions](../../../../../spec/VERSIONS.md#a-spheres-own-version--decided-not-yet-exercised): a sphere's own version beside the architecture's and the build's.

## Senses

| Sense | Fires when |
|---|---|
| `sphere-versioned` | the sphere's version moves to a new tag |
