---
frame: knowledge-capture
lens: [knowledge]
derives_from: [knowledge@1]
version: 1
version_note: First draft. The topic node, grades, what gets caught, offering facts at ground, where they land.
status: drafting
updated: 2026-11-13
sharing: public
reads: [layers/knowledge, layers/focus]
writes: [layers/knowledge, layers/focus]
protocol: [I-trust-what-the-sphere-knows, A-remember-fact, A-offer-facts, A-ask-what-it-knows, knowledge-captured, knowledge-grade-conflict, knowledge-domain-added]
---

# Catching facts

**Applies to:** the human saying something definite about how things are, the human correcting the sphere, *"remember …"*, *"what do you know about …?"*, and every ground.

## The topic

**A topic is one thing worth knowing about, in one file.** It's the unit of knowledge, and a node like any other: a name, current state at the top, history below.

```
layers/knowledge/
├── money.taxes.2025-return/
│   ├── topic.md        its facts, reads and history
│   ├── history.md      its history, once it outgrows topic.md
│   └── sources/        documents and research it was built from (optional)
├── home.lease/
│   └── topic.md
├── history/            narratives that span topics, append-only
└── index.md            generated
```

- **The name is the place.** Knowledge is arranged by how the world is, and that rarely moves, so a topic's place in the tree is its namespaced name: `money.taxes.2025-return`. Everything under `money` is one query. Folders stay flat, named by the full name.
- **A domain is the part of the name a topic shares with others:** `money`, `money.taxes`. Domains nest as deep as they need. A build ships a few to start (health, money, home, people); a sphere grows its own.
- **One file per topic.** Detail below a fact stays as fields on the fact, never as new files.
- **From elsewhere, refer to knowledge as `knowledge:<name>`,** down to a single fact: `knowledge:home.lease.end-date`.

### `topic.md`

```yaml
---
name: home.lease
title: The flat's lease
summary: ends in August; renewal not yet discussed
related: [money.budget, work:home.move]
fresh_for: 1y        # optional: how long its facts stay fresh
updated: 2026-11-04
---
```

Then three parts.

**Facts:** the firm end, one row each.

| Fact | Current → intended | As of | Source |
|---|---|---|---|
| `end-date` | 2027-08-31 | 2026-09-01 | **verified**: the lease, `sources/lease.pdf` |
| `rent` | 1,450 a month | 2026-09-01 | **verified**: the lease |
| `notice-period` | two months | 2026-10-12 | **stated**: the human, in conversation |

**Current → intended** is what makes a fact useful for work: the gap between the two is often where a work node comes from. Most facts only have a current value.

**Reads:** the soft end, as prose, each with its grade and how confident it is.

> **`landlord-renewal`** — _read, medium confidence, inferred_ from his last two emails: open to renewing, likely with a small rise.

**History:** how the topic got here, newest first, appended, never rewritten. A correction is a new entry next to the one it corrects. When the history starts to outweigh the facts, it moves to `history.md` beside the topic.

**`sources/`** holds what the topic was built from. Each source is linked from the facts and reads that rest on it.

**Narratives that span topics** (how a career unfolded, why a move happened) go in `layers/knowledge/history/`, append-only.

**The index is generated** from topic frontmatter, never edited by hand: every domain and topic, by name, and how they relate.

## Grades

Every fact and read carries both.

| Where it came from | Means |
|---|---|
| **verified** | Read from a primary source: the document itself, a statement, an official page |
| **reported** | From a secondary source: an article, a summary, someone else's account |
| **stated** | The human said it. Authoritative for their own life and choices; not for outside facts like prices or rules |
| **inferred** | The AI's reasoning from other facts. **Always names what it rests on** |

| How firm | Kept as | Refreshed by |
|---|---|---|
| **Fact:** single-valued, checkable | a row in Facts | re-checking the source |
| **Read:** narrative, approximate | prose in Reads, with a confidence note | revisiting as the world, or the read, changes |

**Shape follows grade.** A read sitting in the facts table, or a checkable fact buried in a read, is a mismatch. So is an inference with no inputs, or a fact with no source. Raise it; propose the fix. Fire `knowledge-grade-conflict`.

## What gets caught

**Fire only on durable, high-confidence signals. Default to silence.**

| Catch | Don't catch |
|---|---|
| A definite statement about how things are | Passing status: *"the call went fine"* (that's [work](../work-tracking/work-progress.md)) |
| The human correcting something the sphere had wrong | **The AI's own conclusions.** Those are inferences, not the human's knowledge |
| A pattern the human names: *"we always book on Tuesdays"* | A passing mention with no weight behind it |
| Stable facts about people: their role, how to reach them, what they care about | Anything already in knowledge |
| A new person, when they come with real context: a decision, a view, a reason they matter | A bare first mention of a name |

**Facts about other people are kept only because the human chose to keep them.** Never build up a picture of someone from everything that passes by.

## Offering facts

**Nothing is written into knowledge without the human's say.** Knowledge is reference: changes are proposed and applied one at a time, on a yes.

1. **Note the candidate** in the focus's Now, under *Facts to offer:* the fact in the human's own words, its grade, where it came up, and where it would land. *Why the Now:* it survives the window closing, and needs no list of its own.
2. **At ground, offer them as one batch:**

   > I picked up 3 facts since the last ground:
   > - Notice period on the lease: two months (stated)
   > - The lease ends on 31 August (verified: the lease)
   > - The landlord seems open to renewing (a read, inferred from his last two emails)
   >
   > Save all, some, or none?

3. **Write what's confirmed:** re-read the topic, add or change the rows, add a history entry, set `updated`. Clear them from the Now, kept or not. Fire `knowledge-captured`.

- **The exception: a fact about to be lost.** If the topic is changing or the window is closing in a hurry, ask right then, in one line: *"Worth keeping: notice period is two months. Save it?"*
- **"Remember …" is the human's say.** Write it straight away, graded *stated*, and say where it went in one line.
- **A correction from the human** is applied the same way: fix the row, and add a history entry saying what it was and why it changed.
- **Don't ask twice** about a candidate the human said no to.

## Where it lands

- **The most specific topic wins.** A fact about the 2025 return goes in that topic, not in `money`.
- **A fact that spans domains goes to the more general one,** never copied into several. Copies drift apart.
- **Unclear placement is asked, in the offer,** never solved by storing it twice.
- **Update before adding.** A fact that fits an existing topic goes there. A new topic, or a new domain, is proposed only when a genuinely different part of the world needs modelling. A new domain fires `knowledge-domain-added`.

## Not knowledge

| It's really | Send it to |
|---|---|
| A maybe, a *"what if"* | An [idea](../idea-capture/idea-nodes.md), captured directly |
| An idea about improving the sphere | An idea tagged `sphere` |
| Something the human is doing | [Work](../work-tracking/work-breakdown.md) |
| How the human thinks, what matters to them | A lens, co-authored |

**Unsure where it belongs?** Propose a home along with the capture.

## Answering *"what do you know about …?"*

Read the index, then the topic. Answer from its facts and reads, **each with its grade and age where they matter** (see [say-how-sure](say-how-sure.md)). Say what isn't there: *"Nothing on the deposit."*

## When / do

| When | Do |
|---|---|
| The human states something durable about how things are | Note it in the focus's Now as a fact to offer |
| A fact is about to be lost | Ask now, in one line |
| *"Remember …"* | Write it, graded *stated*; say where in one line. Fire `knowledge-captured` |
| The human corrects the sphere | Fix the fact; add a history entry. Fire `knowledge-captured` |
| Ground, with facts to offer | Offer them as one batch; write what's confirmed; clear the list. Fire `knowledge-captured` |
| A grade and its shape disagree, or a fact has no source | Raise it; propose the fix. Fire `knowledge-grade-conflict` |
| A candidate fits no existing topic | Propose a topic, or a domain. Fire `knowledge-domain-added` for a new domain |
| It's really an idea, work or a lens | Send it there |
| *"What do you know about …?"* | Answer from the topic, with grades and ages |

## Works with

- [knowledge-compile](knowledge-compile.md): building topics on purpose, refreshing them, freshness.
- [say-how-sure](say-how-sure.md): how a fact is stated back to the human.
- [kinds-of-file](../nodes/kinds-of-file.md): a topic is reference; its history is appended; the index is generated.
- [node-shape](../nodes/node-shape.md): a topic is a node, its place in its name.
- [propose-dont-decide](../human-is-highest/propose-dont-decide.md): facts are offered, never written on the sphere's own say.
- [state-machine](../continuity/state-machine.md): ground is where the batch is offered.

## Senses

| Sense | Fires when |
|---|---|
| `knowledge-captured` | a fact or read is written into a topic, from conversation or a correction |
| `knowledge-grade-conflict` | a fact's grade and its shape disagree, or a fact has no source |
| `knowledge-domain-added` | a topic opens a domain the sphere didn't have |
