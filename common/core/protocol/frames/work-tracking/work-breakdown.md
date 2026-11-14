---
frame: work-breakdown
kind: structural
lens: [work-tracking]
derives_from: [work-tracking@1]
version: 1
version_note: First draft. The work node, labels, names, the two files, depth and promotion, templates.
status: drafting
updated: 2026-11-12
sharing: public
reads: [layers/work]
writes: [layers/work]
protocol: [I-work-as-one-tree, A-add-work, A-move-work, A-relabel-work, A-promote-item, A-save-work-template, work-node-added, work-node-moved]
---

# Breaking work down

**Applies to:** creating a work node, adding children, moving work around the tree, relabeling it, and promoting a checklist line.

## The work node

Every piece of work is a node at `layers/work/<name>/`, **whatever its depth.** Folders never nest. The tree lives only in each node's `parent:` field.

| File | Kind | Holds |
|---|---|---|
| `work.md` | current state | What the work is, now: frontmatter, then the body below. Rewritten in place by whoever holds it |
| `progress.md` | history | What happened, newest first, never rewritten. Each ground that touched the work adds an entry |
| anything else | as fits | Drafts, screenshots, a spreadsheet. **Every extra file is linked from References,** so nothing in the folder goes unexplained |

**Frontmatter** carries everything needed to show the node in one line, and nothing else:

```yaml
---
title: Get plumbing quotes
kind: task                 # optional: area | project | task; inferred when absent
parent: home.kitchen       # a node name; absent for top-level work
state: active              # see work-progress
summary: two quotes in, one visit Thursday
plan: [kitchen-order@2]    # optional; see plans
connects-to: [knowledge:home.kitchen]
updated: 2026-11-12
---
```

The full key list, and what each may hold, is the work tree's declared shape in [the spec](../../../../../spec/work.md#workmd). **Write it exactly:** no invented keys, no free text in fields with fixed values.

**The body:**
- **Now:** a few scannable lines: where it stands, what's next, what's blocking. The only section with a fixed shape, because views read it.
- **Context:** what the work is, why it matters, what done looks like.
- **References:** knowledge it depends on, lenses that govern it, related nodes, outside links, and every extra file in the folder.
- **Checklist:** small things to do that don't need their own node yet.
- **Notes:** decisions in force, open questions, what was learned. Moves to its own `notes.md`, linked from References, when it outgrows `work.md`.

**Creating a node:** pick the name, write `work.md` with exact frontmatter and a Now, and start `progress.md` with one entry saying why the work exists.

## Labels

| Label | Is | Usually holds |
|---|---|---|
| **area** | A part of life that never finishes: health, home, money | projects, tasks |
| **project** | An effort with an end: the kitchen, a job hunt | projects, tasks |
| **task** | A unit of doing: call the plumber | tasks |

- **A label is a judgment about the work's nature, not a rule about structure.** Any node can hold any other. The containment above is what to expect, not what to enforce.
- **The question that matters: will it ever be done?** Never, it's an area (or an ongoing task). It has an end, it's a project or a task. *Why:* that's the call that sets what to expect: watch it, close it, or do it.
- **`kind:` is optional.** When it's absent, infer the label from context. When a task has grown into an effort of its own, suggest calling it a project; the human decides.
- **The words are for display.** The human can say to-do, chore or item. A build can rename the labels for its audience. The structure underneath never changes.

## Names

Every node has a **name**: lowercase, unique in the work tree, and stable once given. Pick one that fits:

| Scheme | Example | Use for | Trade-off |
|---|---|---|---|
| **Namespace** | `home.kitchen.plumbing` | Stable structure: areas, and the projects inside them | Moving it means renaming it. The tooling fixes links inside the sphere; links written elsewhere won't follow |
| **Prefix and number** | `taxes-20`, `trip-21` | Work that recurs, or may move around the tree | Says less about where it sits, but never changes when it moves |

From another tree, refer to work as `work:<name>`. In a tree view, a child shows relative to its parent (`.plumbing`).

## Depth is a dial

- **Add a child only when something needs breaking down.** A task gets subtasks, a project gets sub-projects. Nothing is restructured.
- **Promote a checklist line when it needs its own context or history.** It becomes a node with `parent:` set to the node it came from, and its checklist line becomes a link to it.
- **Move work by editing `parent:`,** never by moving folders. Under the namespace scheme, moving also renames.
- **Relabel by editing `kind:`.** Children don't move; nothing else changes.

## Templates

**Kinds of work can start from a shape.** A coding project might start with architecture notes and a folder for screenshots; a trip might start with a packing checklist. Templates live in `layers/work/templates/`.

- **New work of a known kind starts from its template,** if there is one. Otherwise, from the two files alone.
- **"Save this as a template"** lifts a well-shaped node into one, keeping its structure and leaving out its content.
- **A template only adds.** It can add sections, a checklist or extra files; it never changes the two files' frontmatter.

## When / do

| When | Do |
|---|---|
| New work to track | Name it, set `parent:`, write `work.md` and a first `progress.md` entry. Start from a template if one fits. Fire `work-node-added` |
| Something needs breaking down | Add child nodes under it |
| A checklist line needs its own memory | Promote it; leave a link in its place |
| Work belongs under a different parent | Edit `parent:` (and the name, under the namespace scheme). Fire `work-node-moved` |
| A task has grown into an effort of its own | Suggest calling it a project; on yes, edit `kind:` |
| A file is added to a node's folder | Link it from References |
| A node's shape is worth reusing | Offer to save it as a template |
| Unsure whether it's work at all | If it's a maybe, capture it as an [idea](../idea-capture/idea-nodes.md) |

## Works with

- [node-shape](../nodes/node-shape.md): the shape every work node follows.
- [kinds-of-file](../nodes/kinds-of-file.md): `work.md` is current state, `progress.md` is history.
- [work-progress](work-progress.md): what goes in `state:`, and what each ground writes.
- [work-registry](work-registry.md): the tree view drawn from `parent:`.
- [plans](plans.md): direction lives beside the work, not in its checklist.
- [focus-tree](../focus/focus-tree.md): carving a parent's checklist item for a child focus is a promotion.

## Senses

| Sense | Fires when |
|---|---|
| `work-node-added` | a work node is created |
| `work-node-moved` | a work node's `parent:` changes |
