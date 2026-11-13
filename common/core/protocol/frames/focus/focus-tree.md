---
frame: focus-tree
kind: structural
lens: [focus]
derives_from: [focus@1]
version: 1
version_note: First draft. Children, carving, reporting up, what's waiting, closing with open children.
status: drafting
updated: 2026-11-11
sharing: public
reads: [layers/focus, layers/work]
writes: [layers/focus, layers/work]
protocol: [I-delegate-and-hear-back, A-open-child, A-report-up, A-inspect, A-request, A-share, child-reported]
---

# The focus tree

**Applies to:** a focus that opens a child (the human narrowing, or a focus delegating to an agent), and every exchange between a parent and a child.

## Opening a child

**A child narrows its parent.** *"Let's go deep on the quotes"*, or *"have an agent compare cabinet options"*.

1. **Propose the child:** number, name, intention, and what it will take from the parent's hold.
2. **Carve the hold.** A hold is exclusive, so the child can't share the parent's; part of it moves to the child instead:

   | What the child takes | How it's carved |
   |---|---|
   | An item on the parent's task list | The item becomes a work node of its own, and the child holds it. The parent's line becomes a link |
   | Part of a folder the parent keeps | The child holds one file or one subfolder |
   | One file both need at once | Can't be carved. One holds it; the other offers its changes |

3. **Write the child's `focus.md`.** Its intention is the child's starter: for an agent, its task. Set its collaboration mode.
4. **Ground the parent.** The carve changed the parent's file and holds, so it's committed under the parent's name: `ground [f20-kitchen-renovation] — opened f21; carved plumbing`. It can be reverted like any ground.
5. **Tell the parent's window,** in one line: *"Opened f21-plumbing-quotes: get three quotes."*

*Why carve:* in a sphere that ran parallel sessions daily, most conflicts came from one shared task list written by a parent and several children at once. Carving gives each list item a single writer.

## Talking across an edge

**Nodes talk through their parent, never sideways.** *Why:* direct messaging between siblings was tried, and they started taking over each other's work. A tree only has parent edges. Across one edge, three verbs:

- **inspect:** read the other node.
- **request:** an ask, never a command. The other side may say no.
- **share:** offer a change to review. Never overwrite.

## Reporting up

- **A child never edits its parent's node.** At each ground it appends its own history entry, plus **one line to the parent's `history.md`**: *"f22: three cabinet options drafted; one fact pending your review."* Anyone can append to history, so this needs no hold.
- **The parent rolls up** on its next read: when it next grounds, or something next attaches to it. Generated views are rebuilt from the nodes, so the overview is current before the parent rolls up.
- **What's waiting is computed, not tracked.** Report lines and requests appended to the parent since its last ground are *waiting for you*. When the parent grounds, it rolls them into its Now, and they stop being new. Nothing marks them read.
- **An offered change lives in the sender's history.** Append an entry naming the holder and the change, in words or as the new text. The holder sees it as *waiting for you* until it appends *accepted* or *declined* to its own history. Never write into the holder's files yourself.
- **A child's work lands piece by piece,** at each of its grounds, labeled by its state (open, not closed). For a change that only makes sense whole, checkpoint first and revert by node if it goes wrong. There's no branch for it.

## Closing a child

- **Close ends it and returns its hold to the parent.** The last history entry says how it ended; the folder moves to `archived/`.
- **What it learned is already where it belongs:** in work, in knowledge, in proposals to lenses. The parent's history has its report lines.

## Closing a focus that has open children

Follow [finishing a node](../nodes/node-shape.md#finishing-a-node). For a focus: list each open child's latest **Next** and whether it has unsaved work, then ask once:

*"f20-kitchen-renovation has 2 open children: f21-plumbing-quotes (one quote left) and f22-cabinets (unsaved changes). Close them too, move them up to f20's parent, or keep f20 open?"*

- **Close them too:** each child grounds, gets its last history entry, and closes, deepest first. Then f20's last entry sums up the subtree from the report lines already in its history.
- **Move them up:** each child's `parent:` becomes f20's parent (main, for a top-level focus). Their holds stay theirs.
- **A child with a window or run attached** is never closed under it: move it up, or keep f20 open.
- **Main has no parent and never closes,** so the question never reaches it.

## Agents

- **A delegated agent is a child focus** in supervised or unattended collaboration mode. It starts with a fresh context, its `focus.md` as the task, and the tools its loadout and guardrails allow.
- **It grounds only under a standing approval** given when it's delegated (*"ground your own work as you go"*), scoped to what it holds. Its reference proposals still wait for the human.
- **To keep it going, hand it the next task on the same focus.** When the work is done, close the focus.

## When / do

| When | Do |
|---|---|
| The human narrows mid-conversation | Propose a child: name, intention, what it takes. On yes, carve, write, ground the parent, report |
| A focus delegates to an agent | Open a child in supervised or unattended mode, with the task as its intention and a standing approval to ground |
| A child grounds | Append its history entry and one line to the parent's history. Fire `child-reported` |
| A parent grounds with reports waiting | Roll them into the parent's Now |
| Offering a change to a file another focus holds | Append the offer to your own history, naming the holder |
| An offer naming this focus has no answer yet | Show it as waiting; on the human's call, apply it and append *accepted*, or append *declined* |
| A focus wants something from a sibling | Ask through the parent; never message the sibling directly |
| A child closes | Return its hold; move it to `archived/` |
| Closing a focus with open children | List them with Next and unsaved work; ask once: close them too, move them up, or keep it open |

## Works with

- [focus-holds](focus-holds.md): carving is how a hold is split.
- [focus-nodes](focus-nodes.md): a child is a focus like any other, with the same record and verbs.
- [state-machine](../continuity/state-machine.md): opening a child is a ground of the parent; undo aims by node.

## Senses

| Sense | Fires when |
|---|---|
| `child-reported` | a child appends its report line to its parent |
