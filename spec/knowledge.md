# Knowledge

_Status: draft 2, for review._ How a sphere keeps its model of the world it operates in: the people, places, things and situations that matter to its human, held as facts and reads that are sourced, dated and readable, and kept honest about how sure they are.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

---

## The idea

A sphere holds three different kinds of thing, and keeps them apart:

| | What it is | Example | Lives in |
|---|---|---|---|
| **Understanding** | How the human thinks: meaning only they bring | *how I think about financial risk* | a [lens](protocol.md) |
| **Work** | What the human is changing | *rebalance the portfolio by March* | [work](work.md) |
| **Knowledge** | How things are: facts the human and the AI can both hold | *the brokerage account holds 60% index funds, as of Oct 1* | the knowledge layer |

**Knowledge is reference.** It aims to be correct. So it carries where it came from, it can go stale, and **when it's wrong, that's a bug: fix the fact.** A lens is different: it doesn't go wrong, it gets sharper. When something feels like both, split it: the fact goes to knowledge, the meaning to a lens. — **proven**

Knowledge has to be the most trustworthy thing in a sphere, because everything else reasons from it. A sphere that states a stale or guessed fact with confidence does more harm than one that says "I don't know."

**Knowledge informs; it never directs.** Frames consult it, plans rest on it, the human asks about it. But a corrected fact doesn't cascade the way a lens change does. It just makes the next read right. Anything that explicitly *cites* a fact (a plan's assumption, a work node's reference) is flagged when that fact changes. That's a reference being kept honest, not a cascade.

---

## Structure — **proven** (shape) · _naming decided, not yet exercised_

```
layers/knowledge/
├── <domain>/                     a domain: an area of the world (money, health, home, people…)
│   └── …                         domains can nest (money.taxes, money.investing)
├── <topic>/                      a topic: one thing worth knowing about
│   ├── topic.md                  its facts, reads and history
│   └── sources/                  research, documents, analyses it was built from (optional)
├── history/                      narratives that span topics, append-only
└── index.md                      generated: every domain and topic, and how they relate
```

**Three kinds of knowledge node:**

| Node | What it is | Example name |
|---|---|---|
| **Domain** | An area of the world. Domains nest. | `money`, `money.taxes` |
| **Topic** | One thing worth knowing about, in one file | `money.taxes.2025-return` |
| **Fact** or **read** | One piece of knowledge inside a topic | `money.taxes.2025-return.filing-status` |

**Every knowledge node has a namespaced name**, so any piece of knowledge can be referred to from anywhere, as `knowledge:money.taxes.2025-return.filing-status`. Its whole place in the tree is right there in the name. Knowledge rarely moves, so this scheme suits it (work nodes, which do move, can also use number-based names; see [work](work.md#naming--decided-not-yet-exercised)).

- **Folders stay flat.** Each domain or topic is a folder named by its full namespace (`layers/knowledge/money.taxes.2025-return/`). The tree lives in the names, and the index groups by them.
- **Domains nest as deep as they need**, and the namespace keeps it all queryable ("everything under `money`"). **A topic is the unit:** one file. Detail below a fact stays as fields on the fact, never as new files.
- **Builds ship starting domains.** A life build might start with health, money, home, people, travel; a work build with domain, engineering and org. A sphere grows its own.
- **Spheres can add their own facets.** A topic's frontmatter can carry fields a sphere cares about, like a life sphere tagging topics with the part of life they serve.

### A topic file

```yaml
---
name: money.taxes.2025-return
related: [money.investing, work:TAX-20]
updated: 2026-10-25
---
```

Then three parts.

**Facts:** the firm end, kept structured so they can be relied on and queried:

| Fact | Current → intended | As of | Source |
|---|---|---|---|
| `filing-status` | married filing jointly | 2026-10-01 | **verified**: last year's return |
| `estimated-payments` | 2 of 4 → 4 of 4 | 2026-10-15 | **stated**: the human, in session |

**Current → intended** is what makes a fact useful for work. The gap between the two is often where a work node comes from.

**Reads:** the soft end, kept as prose because nuance matters more than structure here:

> **`preparer-availability`** — _read, medium confidence, inferred_ from two late replies in October: the preparer is stretched this season, so book early.

**History:** how this topic got to where it is, appended to, never rewritten. When an earlier entry turns out to be wrong, a correction is appended next to it.

`sources/` holds what the topic was built from: research notes, documents, analyses. Each source is linked from the facts and reads that rely on it.

**Cross-topic narratives** (how a career unfolded, why a move happened) live in `layers/knowledge/history/`, also append-only.

### The index — _decided, not yet exercised_

`index.md` is **generated by tooling** from topic frontmatter, never by habit. A registry that's "rebuilt every ground" by instruction alone can go months without being rebuilt. See [registries](registries.md).

---

## Grades and freshness — _decided, not yet exercised_

Every fact and read carries **two grades**, because they answer different questions:

**Where it came from:**

| Grade | Means |
|---|---|
| **verified** | Read from a primary source: a statement, an official page, the document itself |
| **reported** | From a secondary source: an article, a summary, someone else's account |
| **stated** | The human said it. Authoritative for their own life and choices, though not for outside facts like prices or rules. |
| **inferred** | Derived: the AI's reasoning from other facts. **Always cites what it was derived from,** so a guess never passes as ground truth. |

**How firm it is:**

| | Hard (a **fact**) | Soft (a **read**) |
|---|---|---|
| Nature | Single-valued, checkable | Narrative, approximate, often inferred |
| Kept as | A row in the facts table | Prose, with a confidence note |
| Refreshed by | Re-checking the source | Revisiting as the world, or the read, changes |

It's a spectrum, so the point is to **declare where a piece sits.** A soft read stored as a hard fact misleads; a hard fact buried in prose can't be relied on or queried. Either mismatch is flagged.

**A read is still knowledge, not a lens.** *"My manager tends to favor revenue work"* is a low-certainty fact about the world, not the human's meaning. This is the boundary most often confused.

**Facts go stale at different speeds.** A share price is stale in a day, a tax rule in a year, a birthday never. Each domain can declare how long its facts stay fresh. **Staleness is a visible state:** a fact past its window, or whose source is known to have changed, is marked *suspected stale* until it's refreshed. When the sphere is about to rely on a stale fact for a decision, it refreshes it first or says plainly that it's stale.

**Saying the grade.** When the sphere tells the human something that isn't verified, it says so: *"reported, not checked against the source,"* or *"that's my read."* A confident answer that turns out wrong costs more than an honest "I'm not sure."

**An uncited fact is suspect.** A fact with no source is flagged until it gets one, or is marked as inferred, with its inputs.

---

## How knowledge gets in — **proven**

Three ways, and one rule across all of them: **nothing is written into knowledge without the human's say.**

### 1. Captured in conversation

As the human talks, the sphere notices facts worth keeping. **It fires only on durable, high-confidence signals, and defaults to silence:**

| Captures | Doesn't capture |
|---|---|
| Definite statements about how things are | Passing status ("the call went fine"); work tracking handles that |
| The human correcting something the sphere had wrong | **The AI's own conclusions.** Those are inferences, not the human's knowledge. |
| A pattern the human names ("we always book flights on Tuesdays") | Passing mentions with no weight behind them |
| Stable facts about people: their role, how to reach them, what they care about | Anything already captured |
| A new person, when they come with real context (a decision, a view, a reason they matter) | A bare first mention of a name |

Candidates go into a **proposal list** for the domain they belong to, each with the fact in the human's own words, where it came up, and where it would land. At ground, the sphere offers them as one batch:

> I picked up 3 facts this session:
> - Estimated tax payments: 2 of 4 made (stated)
> - The lease ends in August (verified: lease PDF)
> - The landlord seems open to renewing (a read, inferred from his last email)
>
> Save all, some, or none?

**The exception:** when a fact is about to be lost (the topic is changing, or the session is ending in a hurry), the sphere asks right then, in one line: *"Worth keeping: the lease ends in August. Save it?"*

### 2. Compiled from sources

Sometimes knowledge is built on purpose: *"compile what we know about the new house from the inspection report and the listing."* That's a deliberate pass:
1. read the sources
2. extract the facts and reads
3. grade each one
4. note where each came from
5. put the sources in the topic's `sources/` folder

The result is offered to the human like any capture.

*"Refresh what you know about my taxes"* reconciles a topic against its sources: confirm, update or correct each fact, clear its stale mark, and re-date it.

### 3. Routed elsewhere

Not everything that sounds like knowledge is:
- **A speculative idea** goes to idea capture, which takes it directly with no review, because ideas are maybes by nature.
- **An idea about improving the sphere itself** goes to the [evolution](evolution.md) queue.
- **When it's unclear where something belongs,** the sphere proposes a home along with the capture.

### Where it lands

- **The most specific domain wins.** A fact about the 2025 return goes in that topic, not in `money`.
- **Facts that span domains go to the more general one,** instead of being copied into several.
- **Ambiguous placement is surfaced, never stored twice.** Duplicated facts drift apart.
- **Update before adding.** A new domain is created only when a genuinely different part of the world needs modeling. A fact that fits an existing topic goes there.

---

## Facts about other people

A sphere inevitably holds facts about people other than its human: family, colleagues, friends. These people never agreed to be in it. So:

- **The sphere only keeps what the human chose to record.** It doesn't build profiles of people on its own, or collect everything it happens to see about someone.
- **Facts about other people never leave the sphere,** whether in exports, mirrors or published views. See [replication](replication.md).
- **The human can read everything** the sphere holds about anyone, because it's plain files.

## Knowledge stays home — **proven**

Knowledge is the sphere's model of *its human's* world, and it's private. It never travels with an export. Two spheres can share how they work without either showing what it knows. See [replication](replication.md).

---

## Senses and commands — _decided, not yet exercised_

**Senses:**
- `knowledge-captured`, `knowledge-compiled`, `knowledge-refreshed`
- `knowledge-stale`
- `knowledge-grade-conflict`
- `knowledge-domain-added`

**Commands** (natural phrasing works too):
- `what do you know about [topic]?`
- `remember [fact]`
- `compile [topic] from [sources]`
- `refresh [topic or domain]`
- `is [topic] still current?`

---

## Open questions

1. **Freshness windows.** Should domains declare them, or should the sphere learn them? And what's the default for a domain that declares nothing?
2. **Batch size at ground.** When a session produces many candidates, should the sphere offer them all, or only the most useful few?
3. **Finished work into history.** When a work node is archived, does any of its `progress.md` belong in the knowledge layer's history, or does history stay narrative only?
4. **Domain overview files.** Should a domain folder hold a short overview of itself, or is the generated index enough?
