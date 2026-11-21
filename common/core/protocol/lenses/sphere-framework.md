---
lens: sphere-framework
version: 1
version_note: First draft. The sphere as one unit that does meaningful work; anatomy in registries, convention over configuration, stable interfaces with swappable parts.
derives_from: practice in spheres in daily use; spec/registries.md, spec/protocol.md, spec/loading.md
status: drafting
updated: 2026-11-17
verified: false
sharing: public
frames: [capability-manifest, protocol-registry, reactions, structure-check, manifest-check]
---

# A framework, not a one-off

## What a sphere is

**A sphere is a unit that does meaningful work.** Humans and AIs inhabit it, and it acts as one: it holds what it knows, carries its work forward, and gets better at it over time. Neither the human alone nor the AI alone is the sphere. The human brings meaning, presence and judgment; the AI brings scale, recall and tireless execution; the sphere is what they do together.

- **The unit has an order.** The human decides; the AI amplifies their judgment and never replaces it (see [human-is-highest](human-is-highest.md)).
- **It isn't limited to one of each.** A sphere can have several personas, agents working on its behalf, and more than one person who works in it.
- **It outlives every window, model and session.** What makes it the same sphere tomorrow is what it has written down: its state, its lenses, its record of what it did. That's why the rest of this lens matters.
- **Its work and its growth are the unit's.** What it finishes, it finished together, and how well it works is something it can watch improve (see [growth-tracking](growth-tracking.md)).

## A framework, not a bespoke arrangement

**A sphere is a framework, not a bespoke arrangement of files.** Its parts have standard shapes, it writes down what it's made of, and any part can be replaced by another that keeps the same promises.

A sphere that only works because of how one person happened to wire it can't be seeded, shared or repaired by anyone else, including a fresh AI window. A framework can. Another sphere, or the same sphere a year later, recognizes its shape and knows where everything is.

## Three disciplines

- **The sphere writes down its own anatomy.** What it can do, which layers it has, how its surface is laid out: each lives in a **registry**, a short index that says what exists and where. The sphere answers *"what am I made of?"* by reading its registries, not by scanning folders. *Structure that isn't written down doesn't travel.*
- **Convention over configuration.** Every part has a shape it's assumed to have: a layer has a contract, a node has its frontmatter, a finished thing goes to `archived/`. Following the convention costs nothing; only a deviation needs configuring, and **a deviation is always explicit**, an exception the sphere knows about and can say why. When something needs special wiring to work, first ask whether it should become a convention.
- **Stable interface, swappable implementation.** What a part must promise (its interface) is written down in its registry. How it keeps that promise is free to change. A sphere can replace how it tracks work or stores knowledge with its own design and keep running, as long as the new part honors the interface. **Name the interface, or it isn't swappable.** The test: could another sphere's version slot in behind it?

## The registry pattern

Every registry is the same thing:

- **An index, not a copy.** A name, a line, a pointer. The content stays in the files it points at.
- **The explicit list.** If it isn't in the registry, the sphere treats it as not there.
- **It names the interface,** not only what exists.
- **It's checked.** However it's kept up to date, the tooling checks it against what it lists (see [readable-substrate](readable-substrate.md)).

**Truth lives in one place.** A registry is either a view of files that hold their own truth, or the only home for its items. Never both. *Why:* a fact stored twice drifts, and from then on the sphere reasons from a picture that isn't true.

**Reference, don't absorb.** A layer's contract stays with the layer; the layer registry points at it. A frame's definition stays in the frame; the manifest points at it. Each part stays whole wherever it travels.

**Structural and content registries belong to different owners.** Registries of the sphere's anatomy (layers, surface, the protocol, the capability manifest) belong to this lens. Registries of a domain's items (work, knowledge, focus) belong to that domain. Don't gather content registries here; don't scatter structural ones.

## What it gives

- **A seed that comes up working.** A new sphere started from another one follows the same conventions, so nothing needs reconfiguring. A layer lists what it `requires` (its contract, its helper scripts), so it arrives able to maintain itself. The machinery that builds registries travels; the built registries don't, because they describe someone else's sphere.
- **Self-knowledge, cheaply.** Reading a few short registries tells the sphere what it can do and where things are, without loading any of it. See [capability-manifest](../frames/sphere-framework/capability-manifest.md).
- **Room to grow its own way.** Spheres diverge in how they implement things and still work with each other, because the interfaces hold.

## How it shows up

- **A new part conforms first.** A new layer gets a contract (what it holds, its interface, what it requires); a new frame gets an entry in the manifest and its vocabulary in the protocol registry. It exists to the sphere once it's registered.
- **A registry changes in the same ground as what it lists.** A new frame and its manifest entry land together.
- **Asked "can this be swapped?",** the sphere looks for a named interface. If the registry lists only what exists, the interface is missing; say so.

## What it doesn't mean

- **Not rigid.** A sphere may deviate from any convention. It just does so on purpose, and on record.
- **Not more files.** A registry earns its place by replacing scanning or remembering. A registry nobody reads is debt; fold it away.
- **Not centralizing.** Registries point; they don't take over. Each part keeps its own definition.
- **Not the node shape.** [nodes](nodes.md) is how each part is shaped. This lens is how the parts are listed, connected and replaced.

## What follows from it

| Frame | In short |
|---|---|
| [capability-manifest](../frames/sphere-framework/capability-manifest.md) | The routing table of every lens and frame: its entries, how it's rebuilt, and how it's used |
| [protocol-registry](../frames/sphere-framework/protocol-registry.md) | The one registry of intents, abilities, commands and senses, each tied to the frame that defines it |
| [reactions](../frames/sphere-framework/reactions.md) | Senses, who produces them, and the reactions that say what follows each |
| [structure-check](../frames/readable-substrate/structure-check.md) | Shared with [readable-substrate](readable-substrate.md): the anatomy registries, node shapes, links and views, checked at ground |
| [manifest-check](../frames/readable-substrate/manifest-check.md) | Shared with [readable-substrate](readable-substrate.md): the manifest and protocol registry, checked against lenses and frames |

## Revision history

- **v1:** First draft. What a sphere is: one unit of humans and AIs doing meaningful work. Spec chapters *registries*, *protocol* and *loading*.
