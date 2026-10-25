# Work

_Status: draft 2, for review._ How a sphere tracks the work its human is doing: what a piece of work looks like on disk, how it grows from a flat list into a tree, and what sessions promise to keep true.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

---

## The idea

Work is anything the human is trying to change in the world: a project, a goal, a task, an errand that spans days. It's usually the part of a sphere that changes most, and the part a human would miss first.

A sphere's promise about work is modest and honest: **at the start and end of every session, the work it touched is true.** In between, no promise. Continuous tracking depends on remembering mid-flow, and that fails. Boundaries can be checked. — **proven**

---

## A piece of work — **proven**

Each piece of work is a **node**: one folder, holding two files.

```
layers/work/
├── <node>/
│   ├── work.md         what and why: goal, done-when, status, next action
│   └── journal.md      what happened, session by session, and where to pick up
├── archive/
│   └── <node>/         finished work, moved out of the way
└── index.md            generated: every node, grouped by status
```

**`work.md`** is the definition. It changes rarely.

```yaml
---
status: paused          # focused | active | paused | done | archived
waiting_on: design sign-off from the client   # required when paused
parent: website-relaunch   # optional; a node name, not a path; see Depth
updated: 2026-10-25
---
```

Then, in plain words: the goal, what done looks like, and the **next action**, a single concrete step.

**`paused` always says why.** It covers both *blocked* (something is in the way) and *waiting* (someone else has to act), so a paused node carries a one-line `waiting_on:`. Without it, paused work quietly turns into forgotten work.

**`journal.md`** is the running record. Each ground adds an entry: what happened, what's next, and a link to the [session file](state.md#level-1--simple-sessions-the-default--proven). A cold `resume` reads the latest entries and can continue without anyone re-explaining.

Display names are up to the build. A life sphere might call nodes *projects*; a non-technical sphere might call them *my things*. The structure is the same.

---

## Depth is a dial — **proven**

A flat list of work is a tree that is one level deep. Nothing else changes as work grows:

- **A node becomes part of a bigger one** by setting `parent:` in its `work.md`.
- **A node is broken down** by creating child nodes that point to it.
- **Folders never nest.** Every node lives at `layers/work/<node>/` whatever its depth. The tree exists only in the `parent:` fields, which refer to node names rather than paths.

A simple sphere never nests, and never sees the word tree. A heavy sphere nests as deep as it needs to. Moving between the two needs no migration. Profiles differ in how they present work, not in how they store it.

Common shapes, as labels rather than types: a **stream** (an ongoing area), a **project** (has a finish line), a **task** (one sitting or a few). All use the same two files.

---

## The index — _decided, not yet exercised_

`index.md` is **generated, never edited by hand.** It's rebuilt at ground from every node's `work.md`:

| Section | What's in it |
|---|---|
| **Focused** | Nodes with `status: focused`: what the human has chosen to put first. Kept short on purpose. |
| **Active** | Everything else that's in motion: `active` and `paused`. |
| **Done** | `done` nodes not yet archived, collapsed. |

Why generated: an index edited by hand drifts. It goes stale the moment a node changes and nobody remembers to update the list. Each node holds its own status, once, and the index is a view of them. See [registries](registries.md).

**Focused is a human choice.** The sphere can suggest moving a node into focus or out of it, but it never decides alone.

## Archiving — _decided, not yet exercised_

Archiving **moves** a node's folder to `layers/work/archive/<node>/` and sets `status: archived`. Without it, the work folder keeps growing until a human can no longer read it, and a sphere has to stay readable by a human.

- The tooling does the move and fixes links that pointed at the old path. `parent:` fields need no fixing, because they use names.
- Archived nodes don't appear in the index. They're still searchable, and still part of history.
- If a node with active children is archived, the sphere asks first: archive the children too, or give them a new parent?
- The sphere can suggest archiving work that has been `done` for a while. The human decides.

---

## The boundary contract — **proven**

What every session does with work:

| Moment | What happens |
|---|---|
| **Open** | If the session is clearly about a node, the sphere notes it. It never blocks on the question. |
| **During** | Nothing is promised. |
| **Ground** | The node's journal gets an entry; its `status` and next action are updated if they changed; the index is rebuilt. New facts are *proposed* for the [knowledge](knowledge.md) layer, never written to it automatically. |

**Which work a session belongs to is inferred, on the fly,** from what the session talks about and which nodes' files it touches. A session that touches two nodes writes an entry to both. Many sessions belong to no node at all: a question, some research, a quick fix. They stay untracked, and that's fine. The sphere only asks when it has real evidence and can't resolve it, for example two plausible nodes and no way to choose.

---

## Advanced: mirrors — **advanced**

A **mirror** keeps a node's status in step with an outside tool, such as a team's tracker, so the human doesn't update two places.

- A mirror is **one-way by default**: the sphere pushes a summary out. It doesn't take its own truth from the outside tool.
- Everything a mirror sends passes the outbound guard: it's drafted and the human approves, unless they've given a standing approval for that mirror.
- **Only what the mirror is told to send leaves the sphere.** Private notes, journals and lenses never travel with it.

---

## Witness (optional)

Finished work is also evidence of growth. A build can add a **witness** layer that records completed nodes and wins and shows them back to the human over time. Whether it's used heavily depends on the person and the shape of their work, so it ships as a slot, never as a requirement.

---

## Open questions

1. **The second file's name.** `work.md` is settled. `journal.md` is a placeholder; `progress.md` and `handoff.md` are the candidates.
2. **When to suggest archiving.** How long should a node sit in `done` before the sphere suggests moving it? A fixed delay, or at a periodic review?
