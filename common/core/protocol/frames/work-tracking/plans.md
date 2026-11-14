---
frame: plans
kind: structural
lens: [work-tracking]
derives_from: [work-tracking@1]
version: 1
version_note: First draft. Plans beside the work, their frontmatter, versions, following a plan, archiving, and plans fitting the model.
status: drafting
updated: 2026-11-12
sharing: public
reads: [layers/work, layers/knowledge]
writes: [layers/work]
protocol: [I-know-whats-next, A-plan-work, A-replan, A-archive-plan, plan-versioned, plan-deviation, plan-assumption-stale, plan-archived]
---

# Plans

**Applies to:** drafting a plan, changing one, deciding what's next on work that follows one, finishing one, and any time the AI is about to write down phases or steps.

## A plan is direction

A plan is **direction the human understands:** *how I'm approaching the job hunt*, *the order we're doing the kitchen in*. It isn't a list of child nodes. It's the reasoning the work follows.

| Part | Holds |
|---|---|
| **Direction** | The approach, and why this one over the alternatives |
| **Phases** | Stretches of the plan: *research, quotes, build, finish* |
| **Steps** | The ordered moves within each phase. Where *"what's next?"* gets its answer |
| **Assumptions** | What it rests on. An assumption can point at a fact in knowledge (`knowledge:home.kitchen`) |
| **What would change it** | The signals that should trigger a replan |
| **Discussion** | Options considered, trade-offs, open questions. So anyone can see later why this path was chosen |

## Plans live beside the work

```
layers/work/plans/<plan>/
├── plan.md       the current version
└── history.md    every version, and the discussion behind each
layers/work/plans/archived/<plan>/   a plan that's done or dropped
```

- **A plan can guide any number of nodes,** anywhere in the work tree.
- **The link lives on the node:** `plan: [kitchen-order@2]` names the plan and the major version it follows. *Which nodes follow this plan* is computed from those links. Reassigning a node is a one-line edit.
- **Plans are always optional.** A node with no plan works fine; its next action lives in its own Now.
- **A plan can hold sub-plans** (*interview prep* within *the job hunt*), named by `parent:` like any node.
- **Steps finish with their phase.** They're not nodes; they don't archive on their own. A step that needs its own memory becomes work, and the step links to it.

## Plan frontmatter

At the top of `plan.md`, enough to show the plan in one line:

```yaml
---
plan: kitchen-order
title: The order we're doing the kitchen in
parent:                       # a plan name, for a sub-plan; absent at the top
for: [work:home.kitchen]      # the work it was made for
state: active                 # active | done | dropped
version: 2.4                  # the current version, major.minor
summary: plumbing before cabinets; quotes nearly in
created: 2026-09-02
updated: 2026-11-10
---
```

| Key | Holds |
|---|---|
| `plan` | The name; matches the folder. What nodes put before `@` in `plan:` |
| `title` | One line saying what the plan is for |
| `parent` | The plan this one sits within. Absent for a top-level plan |
| `for` | The work it was drafted for, as `work:` links. One or more |
| `state` | `active` while it guides work; `done` when it has nothing left to guide; `dropped` when it was given up, with why in `history.md` |
| `version` | The current version. Its major number is what nodes link to |
| `summary` | One line on where the plan stands, refreshed when it changes |
| `created`, `updated` | When it was first written, and last changed |

- **`for:` is what the plan was made for; who follows it is still computed.** Any node may follow a plan through its own `plan:` link, and that list is never stored on the plan. The two usually overlap; they're different facts.
- **Plans use the same states as work, minus the ones they don't need.** A plan isn't planned (it *is* the plan) and isn't paused (the work is).

## Versions: minor and major

**Replanning is the system working, not failing.** Every change is recorded in `history.md`.

| Change | Version | What it takes |
|---|---|---|
| **A refinement:** reordering two steps, sharpening a phase, adding a detail | **minor** (`2.3` → `2.4`) | No approval. Say so in one line when it happens (*"Updated the kitchen plan to 2.4: plumbing before cabinets."*), record it, and it can be reverted |
| **A change of direction:** a new approach, a different sequence of phases, a dropped goal | **major** (`2.x` → `3.0`) | **A proposal until the human approves it.** Then review every node that follows the plan: each is confirmed fine on the new version, or flagged for updating |

- **Nodes link to the major version only.** Minor changes reach them automatically; only a major one asks them to re-check.
- **Earlier major versions stay in full** in `history.md`, so a node still on version 2 can read exactly what version 2 said. Minor versions are a short note each.
- **A typo isn't a version.**

## Following a plan

- **What's next comes from the plan's steps and the work's real progress,** not a fresh judgment call. Steps completed count as evidence (see [work-progress](work-progress.md)).
- **Doing something different is fine; doing it silently isn't.** A focus that departs from the plan records what it did and why, and ground raises it: *"This worked on cabinets before the plumbing quotes. The plan has them after. Update the plan, or note it as an exception?"*
- **An assumption that goes stale flags the plan.** When a fact an assumption points at changes or goes stale in knowledge, the plan is flagged for review. *Why:* that's how plans that have quietly outlived their premises get caught.
- **Watch the gap.** A plan the work keeps overtaking needs a replan; a plan with no movement against it is stalled work.

## Finishing a plan

**A plan ends `done` when its work is done or it has nothing left to guide, and `dropped` when it's given up** (for another plan, or because the goal went away). Either way it's archived like a work node: the folder moves to `layers/work/plans/archived/<plan>/`.

This is [finishing a node](../nodes/node-shape.md#finishing-a-node) for plans. **Look both ways and ask once:**

- **Down:** sub-plans still active. Finish them too, move them up, or keep this plan open.
- **Across:** live work whose `plan:` still points here. *"Two nodes still follow the kitchen plan. Move them to another plan, drop their plan link, or keep it open?"*

Then set `state`, write the last `history.md` entry (how it ended, and why), and move the folder.

- **Archiving the work it was for raises the plan.** When the last live node in `for:` is archived, ask once whether the plan is done too.
- **Links keep working.** `plan: kitchen-order@2` names a plan, not a path.
- **Reviving** moves the folder back and sets `state: active`, with a history entry saying why.

## Plans fit the model

**When the AI drafts a plan, its phases and steps become a plan in `plans/`, and the work it needs becomes nodes and checklist lines. It never becomes a free-floating plan document of the AI's own invention,** in a node's Notes or anywhere else.

- **Before writing phases or steps anywhere, ask where they belong:** direction and order go in a plan; things to do go in nodes and checklists.
- **A plan that doesn't fit is flagged and reshaped before it sets.** *Why:* ad-hoc structure is cheap to write and painful to clean up later, and a tree full of private formats stops being readable by the next window.

## When / do

| When | Do |
|---|---|
| Work needs direction across several nodes or phases | Propose a plan: direction, phases, steps, assumptions, what would change it |
| About to write phases or steps | Put them in a plan and nodes, never a free-form document |
| A small refinement | Minor version: change it, say so in one line, record it. Fire `plan-versioned` |
| A change of direction | Propose a major version. On approval, review each following node. Fire `plan-versioned` |
| *"What's next?"* on planned work | The next step not yet evidenced as done |
| A focus departs from the plan | Record the departure and the reason; raise it at ground. Fire `plan-deviation` |
| A fact an assumption points at changes or goes stale | Flag the plan for review. Fire `plan-assumption-stale` |
| A step needs its own memory | Make it a work node; link the step to it |
| A plan's work is done, or the plan is given up | Look down and across; ask once. Then state, last entry, move. Fire `plan-archived` |
| The last work in a plan's `for:` is archived | Ask whether the plan is done too |

## Works with

- [work-breakdown](work-breakdown.md): the nodes a plan guides.
- [work-progress](work-progress.md): progress against the plan is measured, never assumed.
- [work-registry](work-registry.md): plans archive the way work does.
- [node-shape](../nodes/node-shape.md): finishing a node, which archiving a plan applies.
- [propose-dont-decide](../human-is-highest/propose-dont-decide.md): a major version is a proposal until approved.
- [check-shared-state](../continuity/check-shared-state.md): re-read a plan before changing one other foci follow.

## Senses

| Sense | Fires when |
|---|---|
| `plan-versioned` | a plan gets a new minor or major version |
| `plan-deviation` | a focus does something its plan has elsewhere or later |
| `plan-assumption-stale` | a knowledge fact a plan assumption points at changes or goes stale |
| `plan-archived` | a plan's folder moves to `plans/archived/` |
