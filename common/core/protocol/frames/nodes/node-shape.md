---
frame: node-shape
kind: structural
lens: [nodes]
derives_from: [nodes@1]
version: 1
version_note: First draft. Understanding as a DAG; long history gets its own file; the shape check; finishing a node.
status: drafting
updated: 2026-11-11
sharing: public
reads: [layers]
writes: []
protocol: [I-one-way-to-read-anything, A-design-check]
---

# Node shape

**Applies to:** creating any node, reading any node, and designing any new part of the sphere.

## A node's parts

| Part | Rule |
|---|---|
| **Name** | Stable and unique in its tree. Referred to from other trees as `tree:name` |
| **Place in the tree** | `parent:` for things that move (work, focus); a namespaced name for things that rarely do (knowledge, literacy). Understanding is a DAG: a frame lists every lens it derives from |
| **Folder** | Named after the node. **Flat:** never nested, whatever the depth |
| **Frontmatter** | Enough for one line in a list or tree: name, title, state, one-line summary, plus the tree's own fields |
| **Current state** | Rewritten in place. Short: where it stands now |
| **History** | Appended, newest first, never rewritten. Can be a section of the same file while it stays short; moves to its own `history.md` once it outweighs current state |

**Reading a node:** frontmatter first (what is it?), then current state (where does it stand?), then the latest history entries only if the story matters. Never load a whole history to answer "where does it stand?"

**Creating a node:** create the folder at the top level of its tree, write frontmatter in the tree's exact shape (no invented keys, no free text in fields with fixed values), write current state, and start the history with one entry saying why it exists.

## Links

- Write links as `tree:name` (`work:home.kitchen.plumbing`). Within the same tree, the bare name is enough.
- **Store a link once, at the end that makes it.** The reverse direction is computed when needed. *Why:* a link stored at both ends drifts.
- Views (indexes, tree views, maps) are generated from nodes and links. Never edit a view to change what it shows; change the nodes.
- **A node with several parents** (a frame with several lenses) is listed under each of them.

## Depth and promotion

- **A flat list is a tree one level deep.** Add a child only when something needs breaking down.
- **Promote when something earns its own memory:** a checklist line that needs its own history becomes a node; an idea that graduates becomes work. The original line becomes a link.

## Checking the shape

The shape check ([structure-check](../readable-substrate/structure-check.md)) reads each tree's declared frontmatter shape from `core/shapes` and reports any node missing a part or using a key its tree doesn't declare. **Changing a tree's frontmatter means changing its declaration in the same commit;** otherwise the check reports every node in that tree.

## Finishing a node

Set the final state, write the last history entry (how it ended, and why), and move the folder into `archived/` beside where it lived. References use names, so they still resolve. Listing what's live reads only the top level.

**Before it ends, look both ways:**
- **Down:** list live children, each with where it stands, and ask once: finish them too, move them up to this node's parent, or keep this one open.
- **Across:** look up live nodes in other trees that link to it (a focus holding it, work citing it), and say so.

Rules:
- **Never end a child silently.** Unsaved work grounds first. A child with a window or run attached is moved up or left open.
- **Finishing them too:** each child gets its own last entry first; the parent's last entry then sums up the subtree from what's already in its history.
- **What a node held is settled when it ends:** ask once, back to the parent (default) or released; write the answer into the parent. Released at the top.
- **Retiring a lens** retires only frames with no other lens; a shared frame stays.

## Designing something new

When the human (or the sphere, in [sphere authoring](../../../../../spec/modes.md)) designs a new part, ask in order, and show the answers:

1. What's the node: the one thing with its own memory? If nothing, it's a field or a list line.
2. Which tree? A new tree only if it answers a question no tree answers.
3. Where does its tree live: `parent:` or its name?
4. What's its current state; what's its history?
5. What does it link to, and which end stores each link?
6. What kind is each file it writes (see [kinds-of-file](kinds-of-file.md))?
7. What's computed instead of stored?
8. Where does it go when finished?

**If the design needs a queue, a second registry, a sync step or a new daemon,** stop and look for the shape, a computed fact or a plain rule first. Propose machinery only when those don't fit, and say why.

## When / do

| When | Do |
|---|---|
| Creating a node | Top-level folder, exact frontmatter, current state, a first history entry |
| Asked where something stands | Frontmatter and current state; history only if the story is needed |
| Linking across trees | `tree:name`, stored at the end that makes the link |
| A list item needs its own memory | Promote it to a node; leave a link behind |
| A history section outweighs current state | Move it to `history.md` beside the node's file |
| Changing a tree's frontmatter | Update its declared shape in the same commit |
| A node is finished | Look down (live children) and across (live links into it); ask once. Then final state, last history entry, move to `archived/` |
| Designing a new part | Walk the eight questions; prefer shape over machinery |
| Retiring a lens | Retire only the frames that have no other lens |
| The shape doesn't fit | Say so, record why, and propose the exception to the human |

## Works with

- [kinds-of-file](kinds-of-file.md): what may be written, by whom.
- [propose-dont-decide](../human-is-highest/propose-dont-decide.md): a new tree or a recorded exception is a change to the sphere's structure, proposed to the human.
