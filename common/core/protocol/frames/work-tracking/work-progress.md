---
frame: work-progress
kind: structural
lens: [work-tracking]
derives_from: [work-tracking@1]
version: 1
version_note: First draft. States, paused and ongoing, progress from evidence, stalls, and what's true at each edge.
status: drafting
updated: 2026-11-12
sharing: public
reads: [layers/work, layers/knowledge]
writes: [layers/work]
protocol: [I-honest-progress, A-set-work-state, A-measure-progress, work-state-changed, work-progress-measured, work-stalled]
---

# Where the work really is

**Applies to:** every change to a work node's state, every ground that touched work, and every answer to *"how far along is it?"*

## States

| State | Means | Default mark |
|---|---|---|
| **planned** | Thought through, not started | 📋 |
| **active** | Being worked on | 🔄 |
| **paused** | Stopped for a reason: blocked, waiting, or on hold | ⛔ ⏳ ⏸️ |
| **done** | Finished | ✅ |
| **dropped** | Ended without finishing; the last entry says why | ✖️ |

**Archived is where a node is, not a state.** Done or dropped work moves to `archived/`; its state stays what it ended as. See [work-registry](work-registry.md#archiving).

- **Paused always says why and on what:** `paused:` is blocked, waiting or on hold, and `waiting_on:` names the person, date or thing. *Why:* paused work without a reason quietly becomes forgotten work.
- **`ongoing: true` marks work that never finishes:** every area, and some tasks, like a practice routine. It shows ♾️ alongside its state. **If someone marks ongoing work done, ask** whether it has really ended (a responsibility handed over, a routine retired) or whether something inside it finished. Usually it's the second: make that a child and finish it.
- **Done means finished, with evidence.** Not marked, not nearly.
- **The marks are display only.** The node stores the state. A [witness theme](../../../../../spec/work.md#witness-optional) can show it differently; the state underneath doesn't change.
- **State is not focus.** A paused node can be in focus; a planned one can be what the week is about. Focus is read from the focus tree, never stored here. See [work-registry](work-registry.md#whats-in-focus).

## Progress is measured from evidence

**Evidence is something that happened in the world:**
- children finished
- plan steps completed
- things that actually shipped: a sent application, a commit, a fact that changed in the knowledge layer

**Never infer progress from ticked boxes.** "3 of 5 marked done" isn't 60%. A box records a claim; evidence records what happened.

- **`progress:` is computed where it can be:** steps or children finished, out of those planned, where finished means there's evidence. It's rewritten at ground, never hand-set when it can be computed.
- **Where it can't be computed** (practice sessions done this month), it's a counter the human or the sphere sets, and it says so.
- **Leave `progress:` out** when there's nothing to count. Most tasks don't need it.

## Stalls show

**An active node with no evidence of movement for a while is stalled.** "A while" depends on the work: a week for a task, longer for a project. The sphere surfaces it, once, at the next ground or anchor that sees it: *"The insurance claim has been active for three weeks with nothing new. Pause it, or is something happening that isn't recorded?"*

- **A project that never closes is the same signal, slower.** If a project has been open far longer than its plan expected, ask whether it's really an area. Relabel, or close it.
- **Never pause or close stalled work on the sphere's own say-so.** Surface it; the human decides.

## True at the edges

| Moment | What happens |
|---|---|
| **Open** | A focus names the work it's for in `holds:`. If that isn't clear, propose it; never block on the question |
| **During** | When the human mentions a change (*"the plumber came"*), the sphere may update the node right away. Opportunistic, never promised |
| **Ground** | Each touched node gets a `progress.md` entry; its `state`, `summary` and Now are refreshed; progress is re-measured; generated views are rebuilt. New facts are proposed to knowledge, never written |

**A `progress.md` entry** says what happened, what was decided, and what's next, and points at the focus that did it. **Pointers, not copies:** it names the focus and the commit; it never repeats the focus's history.

**A focus that touched three pieces of work writes three progress entries and one history entry.** If this window edited work outside the focus's holds, ground asks once whether to hold it too (see [focus-holds](../focus/focus-holds.md)).

## When / do

| When | Do |
|---|---|
| Work starts, stops or finishes | Set `state:`. Fire `work-state-changed` |
| Work stops for a reason | `paused`, with `paused:` and `waiting_on:` both set |
| Ongoing work is marked done | Ask: has it really ended, or did something inside it finish? |
| Grounding work a focus touched | Progress entry, refresh state, summary and Now, re-measure. Fire `work-progress-measured` |
| Asked how far along something is | Answer from evidence; say where the count is a claim, not a measure |
| An active node shows no movement | Surface it once; ask the human. Fire `work-stalled` |
| A project has run far past its plan | Ask whether it's really an area |
| The human mentions a change in passing | Update the node if it's clear; otherwise leave it for ground |

## Works with

- [work-breakdown](work-breakdown.md): the node these fields live on.
- [plans](plans.md): steps completed are evidence; the gap between plan and progress is the signal.
- [work-registry](work-registry.md): views show state; archiving is the last state change.
- [state-machine](../continuity/state-machine.md): ground updates the work first, then commits.
- [propose-dont-decide](../human-is-highest/propose-dont-decide.md): stalls and relabels are surfaced, never acted on alone.

## Senses

| Sense | Fires when |
|---|---|
| `work-state-changed` | a work node's `state:` changes |
| `work-progress-measured` | ground re-measures progress on a touched node |
| `work-stalled` | an active node has shown no evidence of movement for longer than its work suggests |
