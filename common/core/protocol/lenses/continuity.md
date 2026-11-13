---
lens: continuity
version: 1
version_note: First draft. Reworked 2026-11-11 for focus nodes.
derives_from: practice in spheres in daily use
status: drafting
updated: 2026-11-11
verified: false
sharing: public
frames: [state-machine, check-shared-state, without-git]
---

# The thread survives the window

**An AI forgets when its window closes. The sphere doesn't.** Work with a sphere happens in windows, and windows end. What carries the thread from one to the next is **grounding**: at a safe point, the sphere writes down where things stand and saves it. The next window, with no memory of this one, picks the thread up from there.

Continuity is what makes everything else in the sphere worth building. A lens, a fact or a plan that doesn't survive the window might as well not exist.

## Why windows end, and why that's fine

- **An AI's working context degrades as it fills.** Long conversations get worse at paying attention. The cure is to close a window at a natural stopping point and attach a fresh one.
- **What stops people closing is the fear of losing what the old window knew.** So windows run on past their best, and get worse.
- **The sphere is the answer to that fear.** The better it captures at each ground, the less a close costs, and the earlier it's safe to close. *How much you hesitate to close a window is a measure of how well your sphere captures.* Windows put pressure on the sphere to capture; the sphere pays down the cost of closing.

## What carries the thread

The thread is held by a **[focus node](focus.md)**: what the human is pursuing with the model, and the memory of pursuing it. A window attaches to a focus, works it, grounds, and can close at any time without losing anything, because the memory is the node's, not the window's. That's also why a sphere doesn't belong to any one AI tool: any tool can attach to a focus. *Swap in a different tool's name. If a frame breaks, it's leaking an assumption.*

This lens is about the state underneath: how the sphere's files move between saved and unsaved, how each move is made safe, and what happens when more than one window or device touches the same sphere. The [focus](focus.md) lens is about what's being pursued.

## The sphere is a state machine

Underneath, the sphere's files are always in one of two states: **working** (changes in progress) or **grounded** (a clean, saved state). Every operation is a defined move between them, with a contract: what it changes, whether it saves, what it keeps. Git is the substrate. It makes every move durable, reviewable and reversible, so the sphere doesn't reinvent any of that.

- **Grounded is what's true.** The human lives in real time; the sphere lives on its last grounded state. Anything not grounded isn't yet the sphere's memory. That gap is deliberate: it's the moment of review before work becomes memory.
- **With several foci open, there are two levels.** The sphere is always its latest commit. Each focus node moves between working and grounded on its own, and its ground commits only what it holds.
- **Reversal is cheap, so trying things is cheap.** Every grounded state is a checkpoint. Undo and revert add a new change that reverses an old one; nothing is destroyed. Safe experimentation is built into the structure, not left to care.
- **The model is precise; the words are the human's.** Inside, *ground* means "move to grounded and commit". A human may say *save*, or *lock it in*, and hear back *"Saved."* The precision is for the sphere, not a vocabulary the human has to learn.

## How it shows up

- **Ground often, ground well.** A good ground is judged by the next window, not this one: could a fresh window, with no memory of this conversation, carry on?
- **Nothing is lost silently.** Changes nobody can account for stop the sphere and get a question. A window that went quiet with unsaved work is recovered, never discarded. A failing check is fixed, never skipped.
- **A ground saves only what its focus touched.** Other changes may be another focus's, or the human's own.
- **Look again before changing what others depend on.** What the sphere read an hour ago may not be what's there now.
- **No git, less safety, said plainly.** A sphere can run without git, but then it runs one focus at a time and can't undo, and the human is told so.

## What it doesn't mean

- **Not saving after every message.** Grounds come at safe points: a finished step, a decision, a natural pause.
- **Not recording every window.** A quick question or a scratch experiment never grounds, so it leaves nothing behind.
- **Not the work's own history, or the focus's.** What happened to a piece of work lives with that work; what a pursuit did lives in its focus node. Continuity makes sure both get written and saved.
- **Not how the sphere grows or travels.** How it learns new abilities is [evolution](../../../../spec/evolution.md); how it's shared with other spheres is [replication](../../../../spec/replication.md). Continuity is only about state surviving from one window to the next.

## What follows from it

| Frame | Kind | In short |
|---|---|---|
| [state-machine](../frames/continuity/state-machine.md) | structural | The states, the operations and their contracts, and ground step by step |
| [check-shared-state](../frames/continuity/check-shared-state.md) | guard | Before changing what others depend on, look again first |
| [without-git](../frames/continuity/without-git.md) | structural | Running with no git: one focus at a time, and what's lost |

## Revision history

- **v1 (2026-11-10):** First draft, written fresh after an idea-by-idea pass against the source lenses and frames in a sphere in daily use. Simple sessions only.
  - _Reworked 2026-11-11, still v1 (never shipped):_ sessions replaced by focus nodes as what carries the thread; the session frame moved to the focus lens; `without-git` added.
