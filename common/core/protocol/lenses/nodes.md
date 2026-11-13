---
lens: nodes
version: 1
version_note: First draft. The one shape, and designing with it.
derives_from: the shape found across spheres in daily use; spec/nodes.md draft 1
status: drafting
updated: 2026-11-11
verified: false
sharing: public
frames: [node-shape, kinds-of-file]
---

# One shape, all the way down

**Everything that lives in a sphere is the same shape: a node, in a tree, linked across trees into a map.** A piece of work, a knowledge topic, a focus, a lens: each is a folder with a name, a place, a one-line summary, what's true now, and what happened.

Sphere started by borrowing from things that organize themselves well: nature, the cosmos, living organisms, systems, ant colonies. What turned up underneath, again and again, was this one shape. It captures reality well, a person can read it in a folder, and a model can walk it without loading everything. It's also one of the oldest shapes in computing, which is part of why it works: nobody, human or AI, has to learn it.

## What the shape gives

- **One way to read anything.** Open a folder: the frontmatter says what it is in a line, current state says where it stands, history says how it got there. That holds for every node in every tree.
- **Growth without redesign.** Depth is a dial. A flat list is a tree one level deep; a node grows children only when something needs breaking down, and nothing changes shape when it does.
- **Several writers without collisions.** Every file is one of four kinds, and each kind has one way of being shared. Write only to what you hold; anything else is appended, offered, proposed or rebuilt.
- **One sentence across the sphere.** Links between trees let the whole thing read as one thought: *focus X, for work Y, using knowledge Z, through lens W.*
- **Less to keep in sync.** A fact lives in one node; links are stored once, at one end; everything else is computed or generated.

## Designing with it

This is a lens about how the sphere itself is built and grows. **When a new part is needed, fit it to the shape before inventing anything.** What's the node? Which tree, or is it really a new one? What's current state, what's history? What does it link to? What's computed instead of stored? Where does it go when it's finished?

**A design that needs a queue, a second registry or a sync step is usually missing the shape.** The shape, a computed fact, or a plain rule is almost always simpler, and simpler is better. When the shape really doesn't fit, say so and record why; an honest exception is how the shape gets better.

Expect new parts of a sphere to mirror it. That's not a constraint to work around; it's what makes a new part feel like it was always there.

## What it doesn't mean

- **Not everything must be a node from the start.** A line in a list is fine until it earns its own memory. Promotion is the dial turning one step.
- **Not folders inside folders.** The tree lives in a field or a name; folders stay flat.
- **Not always one parent.** A frame can serve several lenses, so understanding is a DAG rather than a tree. The frame is listed under each lens; nothing else changes.
- **Not one tree for everything.** Each tree answers its own question (how the human thinks, how things are, what's changing, what's in focus). The shape is shared; the trees stay separate.

## What follows from it

| Frame | Kind | In short |
|---|---|---|
| [node-shape](../frames/nodes/node-shape.md) | structural | A node's parts, where the tree lives, links, depth, archiving, and the design questions |
| [kinds-of-file](../frames/nodes/kinds-of-file.md) | guard | Know a file's kind before writing it; write only what you hold |

## Revision history

- **v1 (2026-11-11):** First draft. Named as the sphere's meta lens; spec chapter [nodes](../../../../spec/nodes.md).
