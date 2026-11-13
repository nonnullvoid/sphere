# Nodes

_Status: draft 1, for review._ The one shape a sphere is built from, and how to design with it. Every other chapter describes a tree made of this shape; this chapter describes the shape itself.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

---

## The idea

Sphere began by borrowing from things that organize themselves well: nature, the cosmos, living organisms, systems, ant colonies. Building spheres in daily use, the same pattern kept turning up underneath. Work, knowledge, plans, sessions and the protocol each arrived at the same small unit, arranged the same way. **That shape captures reality well, and it works for both people and AI:** a person can read it in a folder, and a model can walk it without loading everything.

It's also a very old shape in computing: a **node**, joined to others in a **tree**, with links across trees making a **map**. A sphere names it once, here, so that every part follows it on purpose rather than by accident, and so that **new parts of a sphere are designed by asking how they fit the shape** before inventing anything new. — _the shape **proven** in work, knowledge and sessions; named as one model, decided, not yet exercised_

| | Is | In a sphere |
|---|---|---|
| **Node** | one thing, with its own folder and its own memory | a piece of work, a knowledge topic, a focus, a lens |
| **Tree** | nodes joined by one parent each, from broad to narrow | area → project → task |
| **DAG** | a tree where a node may have more than one parent, and nothing loops back | lens → frame |
| **Map** | links from a node in one tree to nodes in another | a focus that holds a piece of work and some knowledge |

---

## A node

Every node has:

| Part | What it is |
|---|---|
| **A name** | Stable, and unique within its tree, so anything can refer to it from anywhere |
| **A place in its tree** | a `parent:` field, or a namespaced name (below) |
| **A flat folder** | named after the node. Folders never nest, whatever the depth |
| **One-line frontmatter** | enough to show the node in one line of a list or a tree view: name, title, state, a one-line summary |
| **Current state** | what's true now, rewritten in place |
| **History** | what happened, appended, never rewritten |

**Every living thing is a current-state file plus a history file.** — **proven** Current state answers "where does it stand?"; history answers "how did it get here?" A cold reader reads the first for now and the latest entries of the second for the story. Keeping them apart means current state stays short, and history stays true.

**Where the shape already appears:**

| Tree | Node | Current state | History | Place in tree |
|---|---|---|---|---|
| [Work](work.md) | area → project → task | `work.md` | `progress.md` | `parent:` |
| [Plans](work.md#plans--decided-not-yet-exercised) | plan → phase → step | `plan.md` | `history.md` | inside the plan |
| [Knowledge](knowledge.md) | domain → topic | a topic's facts and reads | its history section, or its own `history.md` once long | namespaced name |
| [Literacy](literacy.md) | subject | the level and open questions, in `subject.md` | what showed the level, in the same file | namespaced name, as knowledge |
| [Focus](focus.md) | sphere → pursuit → narrower pursuit | `focus.md` | `history.md` | `parent:` |
| [Understanding](protocol.md) | lens → frame (a DAG) | the lens or frame | its revision history | a frame's `lens:` |
| [Agents](agent-trust.md) | agent | `core/ai/agents/<agent>.md` | `core/records/agents/<agent>.md` | — |

The variations are deliberate, and they're few: history can be a section of the same file while it stays short (a knowledge topic), or a separate file kept apart by placement when it must stay private (an agent's runs).

**History that grows long gets its own file.** When a node keeps its history as a section and that section starts to outweigh what's true now, move it to a `history.md` beside the node's file. Current state stays short enough to read in one go; the history keeps every entry. A knowledge topic is where this happens first.

### Where the tree lives

The tree is never in the folders. It's in one of two places:

- **In `parent:`, for things that move.** Work and focus get reorganized as they grow, so the parent is a field: moving a node is editing one line, and nothing on disk moves.
- **In the name, for things that rarely move.** Knowledge is arranged by how the world is, so its place is its name: `money.taxes.2025-return`. Everything under `money` is one query.

**Names that carry identity** use a number, when a node shifts over time and its name will change: `f21-plumbing-quotes`. The number stays; the words can be renamed. See [work](work.md#naming--decided-not-yet-exercised) and [focus](focus.md#names-a-number-and-a-memorable-name).

**Understanding is a DAG, not a tree.** A frame can derive from several lenses, so it can have more than one parent. Nothing loops back: lenses are never children of frames. It's the one exception, and it's kept, because a frame that serves two understandings is better than two copies of it. **A view lists the frame under each of its lenses;** nothing more is needed.

### Depth is a dial — **proven**

A flat list is a tree one level deep. A node grows children only when something needs to be broken down, and nothing changes shape when it does: the same files, the same frontmatter, one more `parent:`. A sphere that never nests anything still follows the shape. See [work](work.md#depth-is-a-dial--proven).

**Not everything starts as a node.** A quick list is fine until an item in it earns a folder: an idea sits as a line in the [idea queue](work.md#ideas-come-before-work--proven) until it graduates, and a task sits as a checklist line until it needs its own memory. Promotion is the dial turning one step.

### Finishing a node — _decided, not yet exercised_

A finished node gets a final state, a last history entry saying how it ended, **and moves**, folder and all, into an `archived/` folder beside where it lived. The live folder holds only what's still in play, so the sphere scans less. References use names, not paths, so they still resolve. See [registries](registries.md#conventions-and-swappable-parts).

**Before it ends, look both ways:**

| Direction | What's still live | The sphere |
|---|---|---|
| **Down** | children still open or in progress | lists them, each with where it stands, and asks once: **finish them too**, **move them up** (to this node's parent: one `parent:` edit), or **keep this one open** |
| **Across** | live nodes in other trees that link to it (a focus that holds it, work that cites it) | says so: *"f21 still holds this work. Close f21 too, or let it keep going?"* |

- **Never end a child silently.** A child with unsaved work grounds first. A child in the foreground (a window or run attached) is moved up or left open, never ended under it.
- **Finishing them too** gives each child its own last entry first. The parent's last entry then sums up the subtree, built from what's already in its history.
- **Moving up** keeps the children going, unchanged but for one line.
- **What a node held goes up a level** when it ends: a child's holds to its parent; a top-level node's are released.
- **In a DAG,** retiring a lens retires only the frames that have no other lens. A frame shared with another lens stays, with one parent fewer.
- **Across-links are found at this moment, not kept.** Links are stored at the end that makes them, so finding who links here is a computed lookup, run once, when a node ends.

*Why:* a finished node with live parts leaves orphans: work nobody's pursuing, a focus holding work that's done. One question at the moment of finishing costs less than finding the orphans later.

How each tree applies it: [work](work.md#archiving--decided-not-yet-exercised) (archiving), [focus](focus.md#the-tree) (closing). Steps end with their phase in a plan. Knowledge topics rarely finish: retiring a domain moves or renames its topics, never archives them unseen. Retiring an agent definition while runs of it are open puts the across question to those runs.

---

## Maps

**A map is links from a node in one tree to nodes in another.** They're written as `tree:name`, so a link says which tree it points into:

```yaml
holds: [work:home.kitchen.plumbing, knowledge:home.kitchen]   # a focus node
related: [money.investing, work:TAX-20]                        # a knowledge topic
through: [money-risk]                                          # lenses a focus works through
```

- **Links let the trees read as one sentence:** *focus X, for work Y, using knowledge Z, through lens W.*
- **A link is meaning, stored once, in the node that makes it.** The reverse direction (which foci hold this work?) is computed, never stored twice. A link stored at both ends drifts.
- **Views draw the map.** An index, a tree view, a dashboard or a visual map is [generated](projections.md) from the nodes and their links. Nobody edits the map itself.

---

## Four kinds of file — _unexercised_

What goes wrong when several writers share a sphere is **two writers on one file that's rewritten in place.** Every file in a sphere is one of four kinds, and each kind has one way of handling several writers:

| Kind | Examples | With several writers |
|---|---|---|
| **Current state** (rewritten in place) | `work.md`, `focus.md`, a draft document, a view kept by hand | **One writer: whoever holds it.** Others offer changes |
| **History** (append-only) | `progress.md`, `history.md` | Anyone appends, after re-reading. Never claimed |
| **Reference** (changed only with the human's yes) | knowledge topics, lenses and frames, the human's profile, principles | Nobody holds it. Changes are proposed, and applied one at a time when confirmed |
| **Generated** | indexes, the capability manifest, views | Nobody writes it. Rebuilt from its sources |

**The rule in one line: write only to what you hold; anything else is appended, offered, proposed or rebuilt.** How a focus comes to hold something is in [focus](focus.md#what-a-focus-node-holds).

---

## Designing with the shape

A sphere grows new parts: a new layer, a new kind of record, a new feature. **Before inventing structure, fit it to the shape.** Ask, in order:

1. **What's the node?** What is the one thing that has its own memory? If nothing does, it's probably a field on an existing node, or a line in a list.
2. **Which tree is it in, or is it a new one?** A new tree answers a question no other tree does (*how does the human think, how are things, what's changing, what's in focus*). Most new things are nodes in an existing tree.
3. **Where does its tree live:** in `parent:` (it'll move) or in its name (it won't)?
4. **What's its current state, and what's its history?**
5. **What does it link to,** in which other trees, and which end of each link stores it?
6. **What kind is each file it writes:** current state, history, reference or generated?
7. **What's computed rather than stored?** Facts that git or other nodes already know stay out of the frontmatter.
8. **Where does it go when it's finished?**

**A design that can't answer these is usually reaching for machinery** (a queue, a second registry, a sync step) that the shape would make unnecessary. Prefer the shape, a computed fact, or a rule, over new state or new tooling.

**When the shape really doesn't fit,** say so and record why. A deviation is explicit, as with every [convention](registries.md#conventions-and-swappable-parts), and an honest exception is how the shape itself gets better.

---

## What isn't a node

- **Runtime state** (heartbeats, which window is attached) is disposable and never committed. It's state about nodes, not a node.
- **Generated views** draw nodes; they aren't nodes.
- **The sphere's own scaffolding** (the door file, `sphere.md`, the registries of layers and surface) is the frame the trees hang on.

---

## The shape check — _decided, not yet exercised_

A small check confirms that every node has its parts: a name, a place in its tree, frontmatter in its tree's shape, current state, and history. It works like the [drift checks](registries.md#drift-checks--proven): it runs in the tooling, reports what's missing, and never fixes anything or blocks.

**It evolves with the frontmatter.** Each tree's frontmatter shape (its keys, and the values fixed keys may take) is declared once, and the check reads that declaration rather than hard-coding it. When a tree's frontmatter changes, its declaration changes in the same commit, and the check follows.

---

## Settled for 1.0

_Answered 2026-11-12._

1. **Knowledge's history** moves to its own `history.md` once it grows long, rather than cluttering the topic file. See [A node](#a-node).
2. **Understanding as a DAG.** Listing a frame under each of its lenses is enough. See [Where the tree lives](#where-the-tree-lives).
3. **A shape check** is worth having, as long as it evolves with each tree's frontmatter. See [The shape check](#the-shape-check--decided-not-yet-exercised).
