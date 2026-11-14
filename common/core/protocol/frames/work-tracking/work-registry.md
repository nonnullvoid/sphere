---
frame: work-registry
kind: structural
lens: [work-tracking]
derives_from: [work-tracking@1]
version: 1
version_note: First draft. The generated index and tree view, focus read from the focus tree, archiving.
status: drafting
updated: 2026-11-12
sharing: public
reads: [layers/work, layers/focus]
writes: [layers/work]
protocol: [I-whats-on-my-plate, A-show-work, A-archive-work, work-node-archived, work-index-stale]
---

# What work exists

**Applies to:** showing work (*"what's on my plate?"*, *"show the tree"*), rebuilding the work index, and archiving finished work.

## The index is generated

`layers/work/index.md` is **built from each node's frontmatter alone,** never edited by hand, and rebuilt at ground. It adds nothing of its own: delete it, and the next rebuild brings it back. *Why frontmatter alone:* it stays fast with hundreds of nodes, and it's why everything a view needs lives in frontmatter.

It shows the work as a tree, one line per node:

```
[home.kitchen] Kitchen renovation  🔄  [2/5]  cabinets ordered
├── [.plumbing] Get plumbing quotes  ⏳ waiting on the Thursday visit  two quotes in
└── [.budget] Kitchen budget  🔄  over by 8%, trimming fixtures
[health.running] Running  ♾️  [9/12]  three runs a week since October
```

Children show their name relative to their parent. Folders on disk stay flat.

| Section | What's in it |
|---|---|
| **Focused** | Work an open focus holds, then suggestions (marked as suggestions) |
| **Active** | Everything else in motion: active, paused, planned |
| **Done** | Finished, not yet archived |
| **Archived** | Collapsed; listed on request |

- **Reverse links are computed here, not stored.** Children are found from `parent:`; which nodes follow a plan, from `plan:`; which foci hold a node, from their `holds:`.
- **If the index disagrees with the nodes, the nodes win.** Rebuild it; never fix the index by hand. Fire `work-index-stale` if it was found out of date outside a ground.

## What's in focus

**Work is in focus when an open [focus](../focus/focus-nodes.md) holds it,** foreground or background. That's read from the focus tree, never stored on the work.

- **Keeping something in view on purpose** (what other tools call pinning) is keeping a focus that holds it open in the background. Closing that focus takes it out of view. Nothing on the work changes.
- **The sphere may suggest focus** from signals: a deadline coming up, how recently and often something was touched, the week's plan. A suggestion is a suggestion to open a focus, shown in Focused and marked as one. It's never written into a node.
- **Asking live** (*"what's in focus?"*) reads the open foci directly. The index's Focused section is as of its last rebuild.

## What's on my plate

Answer from the index, in this order: Focused, then paused work whose `waiting_on:` may have resolved, then the rest of Active. **One line each,** from frontmatter. Read a node's Now only when the human asks about it. Never load bodies or history to draw a list.

## Archiving

**Archiving moves a node's folder** to `layers/work/archived/<name>/`, so the live folder holds only what's in play. **Its row stays in the index,** collapsed under Archived, so old work can be found, cited or revived without digging through git.

This is [finishing a node](../nodes/node-shape.md#finishing-a-node) for work. Before it moves, **look both ways and ask once:**

- **Down:** list live children, each with its state and Now. *"The kitchen has 2 children still going: plumbing (waiting on a visit) and budget (active). Finish them too, move them up to home, or keep the kitchen open?"*
  - **Finish them too:** each gets its last `progress.md` entry and moves, deepest first. The parent's last entry sums up the subtree from what's already in its progress.
  - **Move them up:** each child's `parent:` becomes this node's parent.
  - **Finished children archive with their parent.** Subtrees move together.
- **Across:** name any open focus that holds it, or any live work that cites it. *"f21 still holds this. Close f21 too, or let it keep going?"*

Then set the final state, write the last `progress.md` entry (how it ended, and why), and move the folder.

- **Dropped work is archived too,** straight from whatever state it was in: `state: dropped`, with a last entry saying why. It isn't marked done.
- **Links keep working.** `parent:` and `tree:name` links use names, not paths.
- **The sphere can suggest archiving** work that has been done for a while. The human decides.
- **Reviving** moves the folder back and sets a live state, with a progress entry saying why.

## When / do

| When | Do |
|---|---|
| *"What's on my plate?"* | Focused, then paused work that may be unblocked, then Active. One line each, from the index |
| *"Show the tree"* | The index's tree. Archived only if asked |
| A ground touched work | Rebuild the index from committed frontmatter plus this ground's changes |
| The index disagrees with the nodes | Rebuild it. Fire `work-index-stale` if found outside a ground |
| The human wants something kept in view | Open a focus that holds it, or keep its focus open |
| Signals suggest something deserves attention | Show a suggestion to open a focus; write nothing to the node |
| Archiving work | Look down and across; ask once. Then last state, last entry, move. Fire `work-node-archived` |
| Work is dropped | Last entry saying why; archive it |
| Work has been done for a while | Suggest archiving it |

## Works with

- [work-breakdown](work-breakdown.md): the frontmatter the index is built from.
- [work-progress](work-progress.md): the states the index shows.
- [focus-holds](../focus/focus-holds.md): `holds:` is where *in focus* comes from.
- [node-shape](../nodes/node-shape.md): finishing a node, which archiving applies.
- [kinds-of-file](../nodes/kinds-of-file.md): the index is generated; nobody writes it.

## Senses

| Sense | Fires when |
|---|---|
| `work-node-archived` | a work node's folder moves to `archived/` |
| `work-index-stale` | the work index is found out of date with the nodes outside a ground |
