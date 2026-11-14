---
lens: readable-substrate
version: 1
version_note: First draft. Auditability is the floor; readability is a dial; checks keep the readable picture true.
derives_from: practice in spheres in daily use; spec/registries.md (drift checks), spec/nodes.md (the shape check)
status: drafting
updated: 2026-11-12
verified: false
sharing: public
frames: [structure-check, manifest-check]
---

# Nothing the human can't read

**Everything a sphere stores must be something its human can open, read and check.** Nothing in it is hidden from them unless they asked for that. This is the floor, and it's why a sphere can be trusted: the human never has to take the AI's word for what it knows or what it did.

## The floor and the dial

**The floor: auditable.** A format the human can't inspect on their own doesn't belong in a sphere. Opaque embeddings, proprietary binary files, and state that lives only in a remote service with no local copy are all out. No feature is worth crossing this line, and it isn't relaxed case by case. Only the human can opt into something opaque, for one named store.

**The dial: readable.** Above the floor, a format is chosen by **who reads it and how often**:

| Format | When |
|---|---|
| **Markdown** | The default, and the center. Anything a person reads regularly: lenses, frames, nodes, notes, plans. Readable raw by the human and the AI alike, and diffable |
| **JSON or YAML** | Data the AI reads and writes constantly and the human checks only now and then: counters, settings, machine records. Still plain text |
| **A diagram language** | A picture that should travel as text and render when viewed |
| **An inspectable store** | Only for a job plain files can't do, and only if the human can look inside it with ordinary tools |

**Reach past markdown only with a reason,** and say what it is. Don't force machine counters into prose for purity, and don't reach for a database when a file would do.

## Readable isn't enough; it must also be true

A file the human can read but can't trust is worse than no file. So a sphere keeps its own picture honest:

- **Every file says what it is.** Frontmatter says what a node is; a generated view says it's generated and what it was built from.
- **Structure travels with the file.** Each tree's shape is written down once, in plain text beside the tree, not in a separate schema system only tooling can read.
- **The tooling checks what the AI and the human can't keep in their heads:** that registries match what they list, that every node has its parts, that views match their sources. The checks run at ground, report in plain words and offer a fix. *A check that stops work gets switched off; a check that offers a fix gets used.*

## How it shows up

- **A screen is never the source.** A dashboard, a page or an app is a view of files kept elsewhere. It's rendered one way, from the files; editing the screen never changes the truth. See [projections](../../../../spec/projections.md).
- **Outside tools are inputs, not homes.** What matters from a ticket, a chat or a meeting is brought into the sphere, with the link kept as a citation. The sphere doesn't need the outside tool to still be there to make sense.
- **An AI tool's own memory is scaffolding.** Anything durable lives in a sphere file the human can read. If something could go either place, the sphere file wins.
- **Portable because readable.** A sphere can be copied, seeded and read by another AI because it's plain files. Anything that would tie it to one tool or one service breaks that.

## What it doesn't mean

- **Not "everything is prose."** Frontmatter, tables and structured files are all readable. Structure inside plain text is the point.
- **Not "the human must read everything."** They rarely will. What matters is that they *can*, at any time, without help.
- **Not checks that fix things by themselves.** A check reports and offers. What's fixed is decided like any other change.

## What follows from it

| Frame | Kind | In short |
|---|---|---|
| [structure-check](../frames/readable-substrate/structure-check.md) | instinct | At ground: the anatomy matches its registries, every node has its shape, links resolve, views match their sources |
| [manifest-check](../frames/readable-substrate/manifest-check.md) | instinct | At ground: the capability manifest and the protocol registry match the lenses and frames on disk |

## Revision history

- **v1:** First draft, with the checks that keep the readable picture true. Spec chapters [registries](../../../../spec/registries.md#drift-checks--proven) and [nodes](../../../../spec/nodes.md#the-shape-check--decided-not-yet-exercised).
