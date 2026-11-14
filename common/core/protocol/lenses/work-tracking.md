---
lens: work-tracking
version: 1
version_note: First draft. One node system for work, depth as a dial; plan asserted, progress measured.
derives_from: practice in spheres in daily use, and the work design (spec/work.md)
status: drafting
updated: 2026-11-12
verified: false
sharing: public
frames: [work-breakdown, work-progress, work-registry, plans]
---

# What's changing, and how far it's got

**Work is anything the human is trying to change in the world:** a job hunt, a kitchen renovation, a health goal, a codebase. It's usually the part of a sphere that changes most, and the part a human would miss first. Tracking it means holding two things at once: **where the work is meant to go, and where it really is.**

## One node system, depth as a dial

**Every piece of work is a work node, and any node can hold other nodes.** There's no separate kind of thing for a subtask or a sub-project; it's the same node, one level down. The shape is the sphere's [node shape](nodes.md): a name, a `parent:`, a current-state file (`work.md`) and a history file (`progress.md`).

- **Depth is a dial.** A flat list of work is a tree one level deep. A node grows children only when something needs breaking down, and nothing changes shape when it does. A simple sphere never sees the word tree; a heavy one nests as deep as it needs. Moving between the two takes no migration.
- **A label says what kind of work it is, not where it sits.** *Area* (never finishes), *project* (has an end), *task* (a unit of doing). The label is a light judgment that depends on where you stand: a task to its parent can be a project in its own right. Relabeling is a one-word edit that moves nothing.
- **The tree lives in the nodes, not the folders.** Each node names its parent. Folders stay flat, so reorganizing work is editing a line.
- **Not everything starts as a node.** A checklist line is fine until it needs its own memory. Then it's promoted, and the line becomes a link.

*Why one kind of thing:* a fixed ladder of levels (stream, project, sub-project, task, subtask) forces work into a shape it doesn't have. A flat list says nothing about how work folds into work. One recursive node does both, and stays simple.

## Plan is asserted; progress is measured

- **A plan is what we believe the path is:** the direction, its phases and steps, and why this path. It's written down so *"what's next?"* comes from the plan, not a fresh judgment call in every window.
- **Progress is what actually happened, read from evidence:** children finished, steps done, things that really shipped (a sent application, a commit, a fact that changed in knowledge). **Never from how many boxes are ticked.** Marked done and actually done are different claims.
- **The gap between the two is the most useful signal the work produces.** A plan that keeps being overtaken needs replanning; work that isn't moving is stalled. Both show, instead of drifting quietly.
- **Replanning is the system working, not failing.** The first plan isn't sacred. What matters is that the change, and the reason for it, is recorded.

## The work is true at the edges

**When a window attaches and when it grounds, the work it touched is true.** In between, the sphere may update work as the human mentions changes, but it doesn't promise to. Boundaries can be checked; ambience can't.

## How it shows up

- **One line per node, anywhere.** A node's frontmatter is enough to show it in a list or a tree, so views never read bodies.
- **Paused always says why.** Blocked, waiting or on hold, and on what. Paused work without a reason quietly becomes forgotten work.
- **Some work never finishes, and that's said up front.** An area or a routine is marked ongoing, so nobody waits for it to be done, and a project that never closes stands out.
- **Finished work moves out of the way,** and stays findable by name.
- **Plans fit the model.** When the AI drafts a plan, it becomes a plan and work nodes in the sphere's shape, never a free-floating document of its own invention.

## Focus is not work

**Work is what's changing; focus is what's being attended to.** Whether a piece of work is *in focus* isn't stored on the work. It's read from the [focus](focus.md) tree: work is in focus when an open focus holds it. Many foci hold one piece of work; some hold several, or none.

## What it doesn't mean

- **Not a to-do app.** It holds the work's real state and story, not a list of checkboxes.
- **Not every thought.** A maybe isn't work until it graduates; until then it's an [idea](idea-capture.md), kept apart.
- **Not the record of a pursuit.** What a window was in the middle of lives in its focus node. What happened to the work lives with the work.
- **Not a mirror of someone else's tracker.** A sphere may push a summary out to a team's tool, but it never takes its own truth from one. See [mirrors](../../../../spec/work.md#advanced-mirrors--advanced).
- **Not a scoreboard.** Showing growth back to the human is a separate, optional witness layer. See [witness](../../../../spec/work.md#witness-optional).

## What follows from it

| Frame | Kind | In short |
|---|---|---|
| [work-breakdown](../frames/work-tracking/work-breakdown.md) | structural | The work node: labels, names, the two files, depth, promotion, templates |
| [work-progress](../frames/work-tracking/work-progress.md) | structural | States, paused and ongoing, progress from evidence, stalls, the edges |
| [work-registry](../frames/work-tracking/work-registry.md) | structural | The generated index and tree view, what's in focus, archiving |
| [plans](../frames/work-tracking/plans.md) | structural | Plans beside the work: what they hold, frontmatter, versions, following and finishing one, fitting the model |

## Revision history

- **v1:** First draft. Spec chapter [work](../../../../spec/work.md).
