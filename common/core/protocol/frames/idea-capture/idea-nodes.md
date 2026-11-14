---
frame: idea-nodes
kind: structural
lens: [idea-capture]
derives_from: [idea-capture@1]
version: 1
version_note: First draft. One file per idea, capture with its conversation, refining, collections by topic, looking into an idea, graduating or parking.
status: drafting
updated: 2026-11-12
sharing: public
reads: [layers/ideas, layers/focus]
writes: [layers/ideas, layers/work]
protocol: [I-never-lose-an-idea, A-capture-idea, A-refine-idea, A-check-ideas, A-investigate-idea, A-settle-idea, idea-captured, idea-refined, idea-investigated, idea-graduated, idea-parked]
---

# Ideas, one file each

**Applies to:** an idea coming up in conversation, anything said with *"idea:"* or *"what if…"*, coming back to an idea to work on it, listing ideas, looking into one, and deciding what becomes of it.

## One file per idea

**Every idea is its own file,** in one flat folder:

```
layers/ideas/
├── 20260925-interview-friends-about-finances.md
├── 20261104-heat-pump-grant.md
├── 20261112-plan-steps-as-nodes.md
└── archived/
    └── 20260610-cycle-to-work.md     an idea that graduated or was parked
```

- **The name is the file's name:** the date it was captured, compact, then a short hyphenated slug. `20260925-interview-friends-about-finances`. The date keeps names unique and in order; the slug says what it's about. The name never changes, even when the idea's title does.
- **Folders never nest.** Topics are a field, not a place (see [Collections](#collections)).
- **An idea is a node kept in one file:** its current shape at the top, its history below, like a short knowledge topic. *Why one file:* an idea is small, and the conversation that sparked it belongs right next to what it's become. A folder per idea would be ceremony.

## Frontmatter

Enough to show the idea in one line, so a list never reads a body:

```yaml
---
idea: 20260925-interview-friends-about-finances
title: Ask friends how they actually handle money
captured: 2026-09-25
topics: [money]
stage: shaping                # raw | shaping | ready
refinements: 2
refined: 2026-10-14
related: [20261002-shared-budget-sheet, knowledge:money.budgeting]
outcome:                      # once settled: graduated <tree:name>, or parked <why>
---
```

| Key | Holds |
|---|---|
| `idea` | The name; matches the file name |
| `title` | One line saying what the idea is now. Rewritten as it's refined |
| `captured` | The date it came. Matches the date in the name |
| `topics` | Zero or more topic names, namespaced like knowledge: `home`, `money.taxes`, `sphere` |
| `stage` | `raw` until first refined, `shaping` while being refined, `ready` when the human says so |
| `refinements` | How many refinement entries the file has |
| `refined` | The date of the latest one. Absent while raw |
| `related` | Other ideas by name, and links into other trees as `tree:name` |
| `outcome` | Absent while open. Once settled: `graduated work:home.heat-pump`, or `parked the grant is closed until spring` |

**`refinements` and `refined` are a count and a date of what the body already says.** They're in frontmatter so a list can show them without reading bodies, and a check confirms they match the entries.

**Ideas in the `sphere` topic may add two keys:** `change:` (add, refactor or drop) and `horizon:` (now, soon or someday). Neither is ever required.

## The body

```markdown
# Ask friends how they actually handle money

What the idea is now, rewritten each time it's refined. A few lines for a
simple idea; for a complex one, whatever structure it has grown into.

## Findings

What looking into it found, if anyone has. (See below.)

## Captured

2026-09-25, while sorting out the monthly budget.

> what if I just asked a few friends how they do this, like actually sat
> down and interviewed them, I bet everyone has some trick, or maybe not,
> maybe nobody knows what they're doing either

Before this: we'd been going through why the shared budget sheet keeps
falling behind. After: back to the sheet; no decision.

## Refinements

### 2026-10-14
Narrowed to three questions, and to friends who'd be comfortable talking about it.

### 2026-10-02
Split out the budget sheet idea; linked it as related.
```

- **The top is current state.** The title, the idea in its current shape, and any findings. Rewritten as the idea is refined.
- **Captured and Refinements are history,** kept forever. **The capture is verbatim:** the human's words exactly as they came, however vague, repetitive or half-formed. Around it, the conversation it came out of: the human's own words where they fit, a short summary otherwise. *Why:* an idea out of context is often unreadable a month later. What was being talked about is what brings it back.
- **Refinements are dated entries, newest first.** Each says what changed in the idea and, where it matters, why.

## Capture

**Capture has no friction.** When the human names an idea, write the file straight away: name, title, `captured`, `stage: raw`, a guess at `topics` (or none), the verbatim words and the conversation around them. No proposal, no confirmation. Say so in a few words: *"Caught it: interview friends about finances."*

- **When the sphere notices one in passing,** a real maybe and not a remark, offer in one line: *"Catch that as an idea?"* On yes, write it. Don't ask twice about the same one.
- **Never stop to ask about topics.** A missing topic is fine; tagging it later is a one-word edit.
- **Capture is a new file, so any focus can do it** without holding anything. A new file has one writer, so nothing collides.
- **If it's clearly part of an idea already caught,** offer to add it there as a refinement instead of starting a second file. If unsure, capture it new and link the two in `related`.
- **Don't capture what belongs elsewhere:** a fact about how things are is a knowledge proposal; something the human is already doing is work.

## Refining

**Ideas come in spurts and get clearer over time.** A refinement is a session of working on one: reshaping it, cutting what's redundant, giving it structure, splitting it, merging it with another.

- **Refining is co-authored,** like a lens. The AI proposes the new shape; the human decides what it says. Never refine the human's idea into something they didn't mean.
- **Each refinement** rewrites the top, adds an entry at the top of Refinements, adds one to `refinements`, sets `refined`, and moves `stage` from `raw` to `shaping` the first time.
- **`ready` is the human's call.** The sphere can say an idea looks ready to settle; it never marks it so.
- **Refining rewrites the top, so it's done by a focus that holds the idea** (`holds: [idea:20260925-interview-friends-about-finances]`). Anyone else offers a change to it, or appends to its history.
- **Splitting** makes a new idea file for the part that's leaving, with its own capture pointing back. Both list each other in `related`. **Merging** settles one into the other: `outcome: graduated idea:<the other>`.

## Collections

**A collection is every open idea that shares a topic,** found by reading `topics:`. It's computed, never a folder or a list to keep up. An idea can be in two collections; one with no topics is in none, and still shows in every list.

- **"Check my ideas"** lists open ideas, newest first, one line each: title, topics, stage, and whether it has findings. **It's a read; nothing happens.** *"Check my home ideas"* lists one collection.
- **At an [anchor](../../../../../spec/rhythm.md#anchors--proven)** (the morning, the weekly look), offer them in a line, never as a pile: *"6 open ideas, 1 ready, 2 untouched for a month. Look now?"*
- **An idea untouched for a long time** is worth one question at an anchor: refine it, or park it?

## The sphere's own collection

**Ideas tagged `sphere` are about the sphere itself:** a lens to sharpen, a frame that's awkward, a tool to add. It's where [evolution](../../../../../spec/evolution.md#evolution-as-work--decided-not-yet-exercised) keeps what it noticed but hasn't acted on.

- **Evolution reviews the collection when evolution comes up.** Each idea is done on the spot, graduates, or is parked.
- **Graduating from `sphere` means a proposed sphere change,** approved by the human like any other.

## Looking into an idea

An idea can be **investigated:** researched by the sphere or an agent, often without the human.

- **It runs as a child focus that holds the idea,** usually delegated to an agent. See [focus-tree](../focus/focus-tree.md#agents).
- **Its findings go in the idea's Findings section:** what it would take, what it's up against, whether it holds up, and a suggested end (graduate into what, or park, and why). The investigation adds a refinement entry saying so. It reports up in one line, like any child.
- **Investigating produces understanding, not action.** Findings never create work, write a fact, or change the sphere, and they don't change the idea's shape on their own. The human decides what they mean.

## Every idea graduates or is parked

| End | What happens |
|---|---|
| **Graduates into work** | On the human's yes, a [work node](../work-tracking/work-breakdown.md) is created. Its first `progress.md` entry and its References point at the idea |
| **Graduates into a fact** | It's proposed to knowledge, like any capture. It's graduated only once confirmed |
| **Graduates into a sphere change** | It's proposed through evolution. Nothing in the sphere changes until approved |
| **Graduates into another idea** | A merge: the other idea takes it in as a refinement |
| **Parked** | With a reason: *"the grant's closed until next spring"* |

**Either way:** set `outcome`, add a last refinement entry saying how it ended, and **move the file to `layers/ideas/archived/`.** It's still findable by name, and `related` links still resolve. *Why move it:* the live folder holds only what's still a maybe, so a list never wades through what's settled.

- **Graduating doesn't wait for `ready`.** If the human wants to act on a raw idea, that's their call.
- **A parked idea can come back.** Move it back, clear `outcome`, and add a refinement entry saying why now.

## When / do

| When | Do |
|---|---|
| The human names an idea | Write its file: verbatim words, the conversation around it, `stage: raw`. Say so in a line. Fire `idea-captured` |
| An idea comes up in passing | Offer to catch it, once; on yes, write it |
| It's really a fact or work | Send it there instead |
| It's part of an idea already caught | Offer to add it there as a refinement |
| The human works on an idea | Propose the new shape; they decide. Rewrite the top, add a refinement entry, update the count and date. Fire `idea-refined` |
| An idea looks ready | Say so; `ready` is the human's to set |
| *"Check my ideas"* | List open ideas, newest first, one line each; act on nothing |
| An anchor, with ideas open | Offer them in one line |
| Evolution comes up | Review the `sphere` collection |
| *"Look into that idea"* | Open a child focus holding it; it writes Findings and reports up. Fire `idea-investigated` |
| Findings suggest an end | Put it to the human: graduate into what, or park |
| An idea graduates | Create or propose where it went; set `outcome`; archive the file. Fire `idea-graduated` |
| An idea is parked | Set `outcome` with the reason; archive the file. Fire `idea-parked` |
| A parked idea comes back | Move it back, clear `outcome`, say why now in a refinement |

## Works with

- [work-breakdown](../work-tracking/work-breakdown.md): what an idea becomes when it graduates into work.
- [node-shape](../nodes/node-shape.md): an idea is a node kept in one file; settling it is finishing it.
- [kinds-of-file](../nodes/kinds-of-file.md): capture is a new file; refining rewrites the top, so only the holder does it; history is appended.
- [focus-holds](../focus/focus-holds.md): refining and investigating hold the idea.
- [focus-tree](../focus/focus-tree.md): investigating is a child focus that reports up.
- [propose-dont-decide](../human-is-highest/propose-dont-decide.md): refinement is proposed; graduating into a fact or a sphere change is a proposal.

## Senses

| Sense | Fires when |
|---|---|
| `idea-captured` | a new idea file is written |
| `idea-refined` | an idea gets a refinement entry |
| `idea-investigated` | an idea's Findings are written |
| `idea-graduated` | an idea becomes work, a fact, a sphere change or part of another idea, and is archived |
| `idea-parked` | an idea is parked and archived |
