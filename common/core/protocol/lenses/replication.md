---
lens: replication
version: 1
version_note: First draft. Data stays home, protocol travels; seeds are built from an allowlist; what arrives is untrusted until accepted; every sphere has a stable identity. Mostly unexercised.
derives_from: practice in spheres in daily use (seeding, by script); spec/replication.md
status: drafting
updated: 2026-11-13
verified: false
sharing: public
frames: [export-contract, sphere-identity]
---

# Data stays home, protocol travels

_Mostly unexercised. Seeding a new sphere from an existing one has been run by script, in a sphere in daily use. Taking things in from another sphere, comparing spheres, trusting another sphere and joining a network haven't been tried; they're written down so the design is clear before it's built._

**A sphere holds two very different kinds of thing.** Its **shape** is how it works: lenses about sphere mechanics, frames, registries, templates, the tooling that checks it. Its **substance** is the human's life: their work, knowledge, principles, history. The shape can be shared, and that's how a good idea in one sphere reaches another. The substance never leaves.

## Compose, don't prescribe

**What travels is the shape, never the filled-in form.** A sphere that receives a lens puts it to work for its own human, with its own data and its own rhythm. A lens about planning a garden brings a way of thinking about gardens, not the other sphere's garden.

- **That's also the test of how something was written.** If it only works the way its author used it, it was written as a personal artifact, not a pattern, and it won't travel.
- **If sharing something would drag data with it, it's coupled wrong.** Decouple the capability from the data. Never leak the data.

## Built from what may go, never scrubbed

**A seed is assembled from an explicit list of what may leave.** It's never made by copying the whole sphere and deleting what looks private. *Why:* copy-then-delete fails quietly. One stray file in an unexpected folder survives every cleanup pass and ships. A list can't leak what it never named.

- **History stays home by placement.** A lens or frame keeps a short changelog of what changed. Why it changed lives in the sphere's private records, which never travel. Examples in shared text use roles, not names.
- **Nothing leaves without the human seeing it.** A seed is staged where they can read exactly what will go, checked against their private patterns, and sent only on their yes.

## Every sphere knows who it is

**A sphere has a stable identity**, so anything that came from it can say which sphere, which version of it, and where that sphere itself began. Identity names the sphere and nothing about its human.

**Where a sphere began is fixed; what it resembles now is worked out.** A sphere records once what it was born from. Which published architecture it's closest to today is something a comparison can describe, whenever someone asks. **A sphere is never required to conform to an architecture.** Its human decides how it grows.

## What arrives is untrusted until accepted

**Taking something in from another sphere only ever produces proposals.** A frame from elsewhere is instructions someone else wrote, and instructions can carry things nobody here asked for.

- **Nothing in an incoming seed is run or followed while it's read.** Its scripts aren't executed; its words are content to weigh, not commands.
- **The human decides item by item:** adopt, adapt, or skip.
- **Where each item came from is kept,** so a later comparison can trace it.

## Gathering can be autonomous; changing your sphere never is

As spheres connect to each other, more can happen without the human watching: finding another sphere's offerings, reading what it publishes, pulling a capability into a staging area, inert and labeled with where it came from. **Bringing anything into the live sphere always goes through the human's yes.** The autonomy is in the gathering, never the integrating.

- **Trust between spheres starts at nothing,** is granted one specific thing at a time, is recorded, and can be revoked at once. It's one-way: being trusted grants nothing in return.
- **What a sphere shows another is limited where it's shown.** A catalog of offerings lists only what that requester may see. Nothing relies on the other side choosing not to look.

## What it doesn't mean

- **Not a platform.** A shared sphere is a starting kit, not a mold. The receiver brings the content.
- **Not forking.** A fork rebuilds your own sphere alongside the old one (see [evolution](evolution.md)). Replication moves capabilities between spheres.
- **Not proof of who's who, yet.** Nothing here proves a sphere is who it says it is. Between people who share a home or a machine, that's sound. Across a network, signing is what will make it safe, and it slots in later without changing anything else.
- **Not every lens.** A lens's sharing level decides whether it travels at all. A private one shows only as an empty slot.

## What follows from it

| Frame | Kind | In short |
|---|---|---|
| [export-contract](../frames/replication/export-contract.md) | structural | What may leave and what never does; grains; building a seed from an allowlist; provenance; taking things in; comparing |
| [sphere-identity](../frames/replication/sphere-identity.md) | structural | The sphere's id, name and version; where it began; how versions advance; signing as a swappable part |

## Revision history

- **v1:** First draft. Spec chapter [replication](../../../../spec/replication.md).
