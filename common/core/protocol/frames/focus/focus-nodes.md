---
frame: focus-nodes
kind: structural
lens: [focus, continuity]
derives_from: [focus@1, continuity@1]
version: 1
version_note: First draft. Replaces sessions-simple. The record, the verbs, liveness, the folder as registry.
status: drafting
updated: 2026-11-11
sharing: public
reads: [layers/focus, layers/work, surface/state/focus]
writes: [layers/focus, layers/work, surface/state/focus]
protocol: [I-pick-up-where-i-left-off, I-see-whats-in-focus, A-open-focus, A-attach, A-detach, A-close-focus, A-rename-focus, A-list-foci, focus-opened, focus-attached, focus-closed, focus-stale]
---

# Focus nodes

**Applies to:** every focus in the sphere: opening it, attaching to it, writing to it at ground, and closing it.

## The shape

```
layers/focus/
├── f20-kitchen-renovation/
│   ├── focus.md         intention, holds, Now                 (always)
│   └── history.md       what happened, newest first           (always)
├── f21-plumbing-quotes/
└── archived/            closed nodes, moved here whole
```

- **One folder per focus,** flat. The tree lives in `parent:`; folders never nest.
- **The folder is the registry.** Each `focus.md` holds what its focus is for; there's no separate list to drift.
- **Facts aren't stored.** When a focus last grounded and which files it touched come from git when needed.
- **Liveness isn't stored here either.** It's runtime state (below).

### `focus.md`

```yaml
---
number: f21
name: plumbing-quotes
aka: [plumbing]                    # earlier names
parent: f20                        # f0 for a top-level focus
status: open                       # open | closed
intention: Get three plumbing quotes and choose one
holds: [work:home.kitchen.plumbing, knowledge:home.kitchen]
through: [money-risk]              # lenses in the foreground
operating-mode: planning
collaboration-mode: together
persona: sage
points-at: []                      # outside things: a code repo and branch, a document
opened: 2026-11-02
---

## Now

Two quotes in, one visit booked Thursday. Waiting on the written quote.
```

- **Write the shape exactly.** Only these keys. `status` is `open` or `closed`, never free text. If something doesn't fit, ask; don't invent a key or a value. *Why:* a record that bends its own shape can't be read by the tooling or the next window.
- **Now** is rewritten at every ground: where things stand, what's next, what's open.

### `history.md`

Every ground appends an entry, newest first, never rewritten:

```markdown
## 2026-11-10 16:17 — grounded

**Did:** Called two plumbers; one quote in, one booked for Thursday.
**Decided:** Skip the third big firm: their call-out minimum is over budget.
Tried the city's licensed list first; it doesn't show availability.
**Next:** Chase the Thursday visit for a written quote.
**Pointers:** work: home.kitchen.plumbing → progress.md · commit a1b2c3d
```

- **Did** is the story. **Decided** holds the judgment calls that are expensive to re-derive, including what was tried and ruled out, so the next window doesn't try it again. **Next** is a concrete first action (*"Chase the Thursday visit"*), not a topic (*"plumbing"*).
- **Write it for a reader with no memory of this conversation.** No "as discussed", no "the thing from earlier". Name things.
- **Pointers, not copies.** Point at the work's progress and the commit; never repeat them.
- **Closing writes a last entry:** how it ended (done, or dropped) and why.

### Two records, two questions

| | The work's progress | The focus's history |
|---|---|---|
| **Answers** | "Where does this piece of work stand?" | "What was this pursuit in the middle of?" |
| **One per** | piece of work | focus |
| **Read by** | anyone picking the work up later | the next window attaching to this focus |

A focus that touches three pieces of work writes three progress entries and one history entry.

## Names

- **A number** (`f21`), stable for life and **never reused:** the next number is one more than the highest in `layers/focus/`, `archived/` included. *Why:* an old reference must never point at a new focus.
- **A name** (`plumbing-quotes`), two or three words the human would remember it by. Propose one at open; the human can change it.
- **The reference is both:** `f21-plumbing-quotes`. Match on number, name or `aka:`. A partial match (*"the kitchen one"*) shows candidates; never guess.
- **Rename when the focus shifts a little:** *"rename f21 to kitchen-upgrades."* The number stays. Rename the folder, update links (they use the number, so few change), and add the old name to `aka:`.

## The verbs

| Verb | Does | Saves? |
|---|---|---|
| **open focus** | creates the folder and `focus.md`, with a proposed name and the holds it's for. Inside a focus, opens a child (see [focus-tree](focus-tree.md)) | **Yes** (a ground of the parent; for a top-level focus, one line in main's history) |
| **attach** | brings a focus to the foreground and briefs (below). *Resume*, *continue*, *pick up* are the same verb | No |
| **detach** | grounds, then sends the focus to the background | **Yes** |
| **close focus** | grounds, writes the last history entry, sets `status: closed`, returns its hold, moves the folder to `layers/focus/archived/` | **Yes** |
| **rename** | renames, keeping the number and `aka:` | **Yes** |
| **what's in focus?** | lists open foci (below) | No |

Saving is [state-machine](../continuity/state-machine.md)'s `ground`.

### Attach runs the whole briefing

*"Resume the kitchen,"* *"continue f21,"* *"pick up where we left off on the quotes"*: **every phrasing runs the whole attach.**

1. **Find the focus.** Match number, name or `aka:`. If more than one fits, show the candidates and ask.
2. **Read** `focus.md` (intention and Now), the latest history entries, and the progress of what it holds.
3. **Brief:** where things stand, what was decided, what's next. Then carry on.

There's no lighter version. *Why:* a window that finds the focus but skips the reading carries on knowing the plan and not the story, and redoes or contradicts what the last window settled. A quick look without attaching is `peek`.

### Focus talk is a command

**Check focus-shaped phrasing against the verbs before treating it as conversation:** open, start, attach, resume, continue, pick up, detach, park, close, wrap up, rename, *a focus for…*. **Session phrasing counts too:** people will keep saying *"start a session for the website"* or *"continue that session"*; those mean open focus and attach. *Why:* read as prose, *"start a session for the website"* becomes "I'm about to work on the website", the work happens with no focus behind it, and nobody notices until the human asks where it went.

**Every change to a focus is reported in one line** (*"f21-plumbing-quotes open · foreground"*), so a focus that was meant to open and didn't shows on the very next turn. A non-technical build says it plainly, or says nothing when nothing changed.

## Main: the root focus

**`f0-main` (`aka: sphere`) is the root of the focus tree: always open, never closed, and where every window is until it attaches to something else.** Create it with the sphere. Top-level foci have `parent: f0`.

- **A window that only reads leaves nothing behind.**
- **A window that writes grounds into main:** `ground [f0-main] — summary`. Don't open a focus for it.
- **Main holds nothing.** Its ground covers touched files that no open focus holds. For a file another focus holds, offer the change to the holder.
- **Never rewrite main's `focus.md` from a quick window.** Append to its `history.md` only. Its `focus.md` changes only when the human changes what main is for.
- **No heartbeat for main.** Unsaved work no focus holds shows in `peek` as out of focus.
- **The second ground from the same window into main,** offer a focus once: *"This is turning into real work. Open f24-heat-pump-research for it?"* Accept, attach to an open focus, or keep going in main. Remember in the window that you asked; store nothing. A first ground that touches several pieces of work may be offered one too.
- **Opening a top-level focus** appends one line to main's history.
- **Attaching to main** briefs the whole sphere: what's in focus, and what needs attention (below). A window that just starts in main skips that briefing.
- **Main can't be closed, detached or moved.** *"Close focus"* in main has nothing to close; say so.

## Foreground, background, and stale

**Foreground** is open with a window or run attached; **background** is open with nothing attached; **stale** is foreground gone quiet (the window closed, the laptop crashed).

- **Heartbeat:** any sphere command updates `surface/state/focus/<number>.json` with `last_seen` and the client label. One file per focus, never committed; if it's lost, rebuild it. Foreground while `last_seen` is within 30 minutes.
- **Ground before detaching,** so a focus rests grounded in the background, never working in the background.

Crossing stage with liveness gives a quick read of any focus. Three cells are where a healthy focus rests; the rest are passing, or need attention:

| stage ↓ · liveness → | background | foreground | stale |
|---|---|---|---|
| **working** (unsaved changes) | Orphaned: ask, offer to ground | **Normal work** | Crashed mid-work: offer to recover, highest priority |
| **grounded** | **Held**: attach any time | Just grounded, carrying on | Window died after saving: clear the heartbeat |
| **closed** | **Done** | A window outlived the close: detach it | Leftover record: clear the heartbeat |

- **How serious a stale focus is depends on unsaved work, not on how long it's been quiet.** With unsaved work: offer to recover it, never discard it. Clean: clear the heartbeat.

## Listing what's in focus

*"What's in focus?"* reads only the top level of `layers/focus/`, never `archived/`, and shows the tree: each focus's reference, foreground or background, last ground and latest **Next**. Foci that need attention come first: stale with unsaved work, then open but quiet for a long time. Archived foci are history, found by number or name when something refers to them.

## Reconciling: each question where it belongs

Reconciliation runs in the tooling, never from memory. **But a ground asks only about its own focus;** questions about other foci go where the human is already looking.

| Question | Ask it |
|---|---|
| *"This touched the budget sheet, which f21 doesn't hold. Hold it too?"* | At this focus's ground. Never in main, which covers whatever isn't held |
| *"f17 has unsaved changes and its window has gone quiet. Recover them?"* | In *"what's in focus?"*, when attaching to main, and in one line when a window starts, only while it's true |
| *"f12-newsletter has been quiet for three weeks. Keep it in the background, or close it?"* | In *"what's in focus?"* and when attaching to main. Never at another focus's ground |

- **Quiet is measured from a focus's latest history entry.** *"Keep it"* appends a line to its history, so the question doesn't return for another three weeks. Nothing else is stored.
- **Most grounds ask nothing.**

## When / do

| When | Do |
|---|---|
| *"Open a focus for…"*, *"start a session for…"* | Open focus: propose number, name and holds; one-line report; fire `focus-opened` |
| Any phrasing of resume or attach | The whole attach: find, read, brief. Fire `focus-attached` |
| More than one focus matches | Show candidates; ask |
| The human says they're stopping, or *park it* | Detach: ground, then background |
| *"Close focus"*, *"we're done with this"* | Close: ground, last history entry, `status: closed`, return the hold, move to `archived/`. Fire `focus-closed` |
| The intention has drifted a little | Suggest a rename |
| It drifted out, old intention unfinished | Suggest a child ([focus-tree](focus-tree.md)) |
| It drifted out, old intention finished | Suggest closing and opening a new focus |
| A window not attached to a focus writes and grounds | Ground into main; append to main's history |
| The same window grounds into main a second time | Offer a focus once |
| Grounding any focus | Ask only about this focus's own touched files |
| A window starts while some focus has stale unsaved work | Say so in one line; offer to recover |
| A focus's heartbeat lapses with unsaved work | Fire `focus-stale`; offer to recover at the next chance |

## Works with

- [state-machine](../continuity/state-machine.md) owns `ground`, `peek`, `undo` and `revert`; this frame owns the record and the focus verbs.
- [focus-holds](focus-holds.md) says what a focus may write.
- [focus-tree](focus-tree.md) covers children, carving and reporting up.

## Senses

| Sense | Fires when |
|---|---|
| `focus-opened` | a focus's folder is created |
| `focus-attached` | an attach finishes its briefing |
| `focus-closed` | close finishes and the folder has moved |
| `focus-stale` | a focus with unsaved work has gone quiet for more than 30 minutes |

`focus-grounded` and `dirty-detected` come from [state-machine](../continuity/state-machine.md).
