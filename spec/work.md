# Work

_Status: draft 3, for review. A starting point for architecture 1.0. A more flexible work model can replace it later, behind the [same interface](#the-interface)._

How a sphere tracks what its human is doing: what a piece of work is, how work grows from a single thing into a tree, how plans give it direction, and how its real progress stays honest.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

---

## The idea

Work is anything the human is trying to change in the world: a job hunt, a kitchen renovation, a health goal, a codebase. It's usually the part of a sphere that changes most, and the part a human would miss first.

Three ideas shape everything below:

1. **One kind of thing, recursive.** Every piece of work is a **work node**, and any node can hold other nodes. A node can be a task to its parent and a project in its own right; labels are a light judgment, never a structural rule. — **proven**
2. **Plans give direction.** A plan says where the work is going and why this path, so what to do next comes from the plan, not from a fresh judgment call at every session. Plans live alongside the work, not inside it. — _decided, not yet exercised_
3. **Plan is asserted; progress is measured.** A plan is what we believe the path is. Progress is what actually happened, read from evidence, never from checkboxes. **The gap between the two is the most useful signal the work layer produces.** — **proven**

And one promise: **at the start and end of every session, the work it touched is true.** In between, the sphere may update work as you mention changes, but it doesn't promise to. Boundaries can be checked; ambience can't. — **proven**

---

## Work nodes — **proven**

### Labels are a light judgment

A node's label says what *kind* of work it is. It's a judgment about the work's nature, not a fact about its structure, and it depends on where you stand: a task to its parent can be a project in its own right.

| Kind | What it is | Usually holds |
|---|---|---|
| **area** | A part of life or work that never finishes: health, home, finances, a standing responsibility | projects, tasks |
| **project** | An effort with an end: the kitchen renovation, a job hunt | projects, tasks |
| **task** | A unit of doing: call the plumber, book the onsite | tasks (subtasks) |

- **The containment is convention, not a rule.** The sphere expects these shapes but doesn't enforce them. Any node can hold any other.
- **`kind:` is optional.** When it's absent, the sphere infers a label from context. When a task grows into an effort of its own, the sphere can suggest calling it a project. The human decides, and relabeling is a one-word edit that moves nothing.
- **The words are display only.** A human can say "to-do," "chore" or "item," and the sphere understands. Builds can rename the labels for their audience: a code build might say workstream / project / task. The structure underneath never changes.

### Naming — _decided, not yet exercised_

Every node has a **name**: unique, lowercase, and stable once given, so it can be referred to from anywhere: other nodes, plans, knowledge, a conversation. The AI picks a name that fits the context. Two default schemes work in most cases:

| Scheme | Example | Best for | Trade-off |
|---|---|---|---|
| **Namespace** | `home.kitchen.plumbing` | Stable structure, like areas and the projects inside them | The name records where the node sits. Moving it means renaming it; the tooling fixes links inside the sphere, but references written elsewhere won't follow. |
| **Prefix + number** | `TAX-20`, `dubai-trip-21` | Work that recurs or may move around the tree | Says less about where the node sits, but never changes when it moves |

The folder is named after the node (`layers/work/home.kitchen.plumbing/`), and folders stay flat whatever the scheme. In the tree view, a child is shown relative to its parent (`.plumbing`).

### On disk

```
layers/work/
├── <node>/
│   ├── work.md          what the work is, now: its context, state and quick info   (always)
│   ├── progress.md      what happened, in order                                    (always)
│   └── …                anything else this work needs                               (optional)
├── archived/
│   └── <node>/          finished work, moved out of the way
├── plans/
│   └── <plan>/
│       ├── plan.md      the plan's current version
│       └── history.md   every version, and the discussion behind it
├── templates/           starting shapes for kinds of work
└── index.md             generated: the work tree and its quick info
```

**Folders never nest.** Every node lives at `layers/work/<node>/` whatever its depth. The tree exists only in each node's `parent:` field, which names its parent, so moving work around the tree never moves a folder.

**Every node has exactly two required files.** Anything else the work needs (screenshots, a draft document, a spreadsheet, an `assets/` folder) can live in the node's folder too, but **every extra file is linked from the node's References**, so nothing in the folder goes unexplained. Templates can add extras for kinds of work.

**One rule across the sphere:** every living thing is **a current-state file plus a history file**. Work nodes have `work.md` + `progress.md`, plans have `plan.md` + `history.md`, and sessions work the same way (see [state](state.md)).

### `work.md`

**Frontmatter** carries everything needed to show a node in one line, so views never have to read the body:

```yaml
---
title: Google interview
kind: task                      # optional: area | project | task; inferred when absent
parent: jobhunt-may-2026        # a node name; absent for top-level work
state: active                   # idea | planned | active | paused | done | archived
paused:                         # when paused: blocked | waiting | on hold
waiting_on:                     # required when paused
focus: pinned                   # optional; see State and focus
ongoing: false                  # true for work that never finishes (every area, some tasks)
progress: 3/7                   # optional; see Plan vs progress
summary: onsite scheduled, phone done    # one line, refreshed at ground
plan: [jobhunt-strategy@2]      # optional; the plan(s) and version this node follows
connects-to: [interview-practice, world:career/offers]
updated: 2026-10-26
---
```

The **body** is the node's context: the distilled, current truth about this work.

- **Now:** a few scannable lines covering where things stand, what's next, what's blocking, and when it was last grounded. This is the only section with a fixed shape.
- **Context:** what the work is, why it matters, and what done looks like.
- **References:** knowledge subjects it depends on, lenses that govern it, related nodes, outside links.
- **Checklist:** small things to do that don't yet need their own node (see [Depth is a dial](#depth-is-a-dial--proven)).
- **Notes:** the discussion around the work, distilled: decisions in force, open questions, what was learned. When Notes outgrows `work.md`, it can move to its own `notes.md`, linked from References.

### `progress.md`

The node's history, in order and never rewritten. Each ground adds an entry: what happened, what was decided, highlights of the discussion, and a link to the [session file](state.md#the-session-file--proven-shape).

`work.md` holds the current understanding; `progress.md` holds the trail of how it got there. A cold resume reads both: the first for where things are, the latest entries of the second for how they got there.

---

## State and focus — two separate axes

**State: how far along.** — **proven**

| State | Means | Default mark |
|---|---|---|
| **idea** | Captured, not thought through | 💡 |
| **planned** | Thought through, not started | 📋 |
| **active** | Being worked on | 🔄 |
| **paused** | Stopped for a reason: **blocked**, **waiting**, or **on hold**. Always says on what, in `waiting_on:` | ⛔ ⏳ ⏸️ |
| **done** | Finished | ✅ |
| **archived** | Done and moved out of the way | 📦 |
| _(ongoing)_ | Never finishes: every area, and some tasks, like a practice routine | ♾️ |

Paused always says why, because paused work without a reason quietly becomes forgotten work.

**Ongoing work doesn't finish.** If someone marks an ongoing node done, the sphere asks whether it has really ended (a responsibility handed over, a routine retired) or whether something inside it finished.

**Focus: is it in view right now.** — _decided, not yet exercised_ Focus is independent of state. A paused node can stay pinned, and a fresh idea can be the focus of the week.

- **`pinned`** is the human's choice, and always wins.
- **The sphere may suggest focus** from signals: deadlines coming up, how recently and how often something was touched, the week's plan. Suggestions appear as suggestions in the Focused view. They're never written into a node as a decision.

The marks are the base build's defaults. A [witness theme](projections.md#matter-not-machinery) can replace them: a garden theme might show 🌱 → 🌿 → 🍄. The node stores the state; the theme decides how it looks.

---

## Depth is a dial — **proven**

A flat list of work is a tree that is one level deep. Nothing else changes as work grows:

- **A checklist item becomes a task** when it needs its own context or history. It's promoted into a node of its own, and its line in the checklist becomes a link.
- **Any node can gain children:** a task gets subtasks, a project gets sub-projects. Nothing is restructured; the sphere may suggest a new label when the work's nature has changed.
- **Work moves around the tree** by editing `parent:`, never by moving folders.

A simple sphere never nests and never sees the word tree. A heavy one nests as deep as it needs. Moving between the two needs no migration.

---

## Plans — _decided, not yet exercised_

A **plan** is direction a human understands: *how I'm approaching the job hunt*, *the order we're doing the kitchen in*. It isn't a list of child nodes. It's the reasoning that the work follows.

### What a plan holds

- **The direction:** the approach, and why this one over the alternatives.
- **Phases:** stretches of the plan (*research, applications, interviews, decision*).
- **Steps:** the ordered moves within each phase. Steps are where *"what's next?"* gets its answer.
- **Assumptions** it rests on. An assumption can point at a specific fact in the [knowledge](knowledge.md) layer. If that fact changes or goes stale, the plan is flagged for review, which catches plans that have quietly outlived their premises.
- **What would change it:** the signals that should trigger a replan.
- **The discussion:** options considered, trade-offs, questions still open. Months later, anyone can see why this path was chosen.

### Plans are a parallel hierarchy

- **Plans live beside the work, not inside it,** in `layers/work/plans/`. A plan can guide **any number of nodes**, in any part of the work tree.
- **Plans are always optional.** A node with no plan works fine; its next action lives in its own Now section.
- **Plans have their own tree.** A plan can hold sub-plans: *interview prep* within *the job hunt*.
- **The link lives on the node.** A node's `plan:` field names the plan and the version it follows (`jobhunt-strategy@2`). Reassigning a node to another plan, or a newer version, is a one-line edit. *Which nodes follow this plan* is computed from those links, so the truth lives in one place.

### Plans are versioned: major and minor

A plan has two files: **`plan.md`**, its current version, and **`history.md`**, every version and the discussion behind each. Replanning is the system working, not failing.

| Change | Version | What it takes |
|---|---|---|
| **A refinement:** re-ordering two steps, sharpening a phase, adding a detail | **minor** (`2.1` → `2.2`) | No approval needed. The sphere just says so in one line when it happens (*"Updated the job-hunt plan to v2.44."*), records it in `history.md`, and it can be reverted. |
| **A change of direction:** a new approach, a different sequence of phases, a dropped goal | **major** (`2.x` → `3.0`) | **A proposal until the human approves it,** the same as a lens isn't in force until it's confirmed. Then **every node following the plan is reviewed**: each is confirmed as fine, or flagged for updating. |

- **Nodes link to the major version only** (`plan: jobhunt-strategy@2`). Minor refinements reach them automatically; only a major change asks them to re-check.
- **Earlier major versions are kept in full** in `history.md`, so a node still on version 2 can read exactly what version 2 said while it's being reviewed. Minor changes are recorded as short notes.
- Fixing a typo isn't a version at all.

### Following a plan

What to do next comes from the plan's steps and the work's real progress. A session that does something different **records the deviation and its reason,** and the sphere raises it at ground: *"This session worked on the offer comparison before the onsite. The plan has it after. Update the plan, or note it as an exception?"*

---

## Plan vs progress — **proven**

- **Progress is measured from evidence:**
  - children finished
  - plan steps completed
  - things that actually shipped (commits, a sent application, a fact that changed in the knowledge layer)

  It's never inferred from how many boxes are ticked.
- **The `progress:` fraction is computed where it can be:** steps or children finished out of those planned, where finished means there's evidence. Where it can't be computed (a count of practice exercises), it's a counter set by the human or the sphere.
- **Stalls are visible.** An active node with no real movement for a while is flagged, not hidden.

---

## The index and the tree view — _decided, not yet exercised_

`index.md` is **generated from frontmatter alone** (never edited by hand) and rebuilt at ground. Because it reads only frontmatter, it stays fast even with hundreds of nodes. See [registries](registries.md).

It shows the work as a tree, one line per node:

```
[jobhunt-may-2026] Find a new job  🔄 · pinned  [2/3]  onsite next week
├── [.interview-practice] Practice coding exercises  ♾️  [3/10]  focusing on leetcode
└── [.interview] Google interview  🔄  [3/7]  onsite scheduled, phone done
```

Children show their name relative to their parent (`.interview`). The folders on disk stay flat.

| Section | What's in it |
|---|---|
| **Focused** | Pinned nodes, then suggested ones (marked as suggestions) |
| **Active** | Everything else in motion: active, paused, planned |
| **Ideas** | Captured, not yet planned |
| **Done** | Finished, not yet archived |
| **Archived** | Collapsed; listed on request |

## Archiving — _decided, not yet exercised_

Archiving **moves** a node's folder to `layers/work/archived/<node>/`, so the active work folder stays readable. **Its row stays in the index,** collapsed under Archived, so old work can still be found, referenced or revived without digging through history.

- **Subtrees archive together.** Archiving a node takes its finished children with it. Children still in progress **block** the archive until each is finished, moved under a new parent, or explicitly dropped.
- **Links are fixed by the tooling.** `parent:` fields use names, so they never break.
- **The sphere can suggest archiving** work that has been done for a while. The human decides.

---

## The boundary contract — **proven**

| Moment | What happens |
|---|---|
| **Open** | If the session is clearly about a node, the sphere notes it. It never blocks on the question. |
| **During** | When the human mentions a change ("the phone screen went well"), the sphere may update the node right away. That's done opportunistically, never promised. |
| **Ground** | Each touched node's `progress.md` gets an entry; its `summary`, `state` and Now section are refreshed; progress is re-measured; the index is rebuilt. New facts are proposed for the [knowledge](knowledge.md) layer, never written automatically. |

**Which work a session belongs to is inferred,** from what the session talks about and which nodes it touches. A session that touches two nodes writes to both. Many sessions belong to no node at all, and that's fine. The sphere only asks when it has real evidence and can't resolve it.

## Work keeps its shape — _decided, not yet exercised_

- **Templates.** Kinds of work can have a starting shape: a coding project might start with architecture notes and a folder for screenshots, and a trip might start with a packing checklist. Templates live in `layers/work/templates/`. *"Save this as a template"* lifts a well-shaped node into one.
- **Plans fit the model.** When the AI drafts a plan, its phases and steps become a plan in `plans/`, and the work becomes nodes and checklists. **It never becomes a free-floating plan document of its own invention.** A plan that doesn't fit the model is flagged and reshaped before it sets, because ad-hoc structure is painful to clean up later.

---

## Senses and commands — _decided, not yet exercised_

**Senses:**
- `work-node-added`, `work-node-moved`, `work-node-archived`
- `work-state-changed`, `work-focus-changed`
- `work-progress-measured`, `work-stalled`
- `plan-versioned`, `plan-deviation`, `plan-assumption-stale`
- `work-index-stale`

**Commands** (natural phrasing works too):
- `add [task or project] [name] under [parent]`
- `move [node] under [parent]`
- `pin` / `unpin [node]`
- `pause [node] [reason]`
- `done`
- `archive [node]`
- `what's on my plate?`
- `show the tree`
- `plan [node]`
- `replan [plan]`

---

## Advanced: mirrors — **advanced**

A **mirror** keeps a node's status in step with an outside tool, such as a team's tracker, so the human doesn't update two places.

- A mirror is **one-way by default**: the sphere pushes a summary out. It doesn't take its own truth from the outside tool.
- Everything a mirror sends passes the outbound guard: it's drafted and the human approves, unless they've given a standing approval for that mirror.
- **Only what the mirror is told to send leaves the sphere.** Private notes, progress and lenses never travel with it.

## Witness (optional)

Finished work is also evidence of growth. A build can add a **witness** layer that records completed nodes and wins and shows them back to the human over time, in a theme that resonates. Its source is the plain record of what got done, which stays true whatever theme is on top.

---

## The interface

What any replacement for this work model has to honor, so that projections, sessions, plans and other spheres keep working (see [registries](registries.md#conventions-and-swappable-parts)):

- Each node has a stable name, a `title`, an optional `kind`, a `parent`, a `state`, an optional `focus`, and a one-line `summary`.
- A generated index lists every node with those fields.
- Each node keeps a history that sessions can append to.
- Nodes can name the plan and major version they follow.
- Names are unique and stable, so any node can be referred to from anywhere.

---

## Open questions

1. **Suggested focus.** Which signals, weighted how? Learned from what the human pins over time?
2. **Grouping top-level work** (life, work, home) as an optional namespace: needed, or does the tree already do this?
