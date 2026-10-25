# Knowledge

_Status: draft 1, for review._ How a sphere keeps its model of the world it operates in: the people, places, things and situations that matter to its human, as facts that are sourced, dated and readable.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

---

## The idea

A sphere holds three different kinds of thing, and keeps them apart:

| | What it is | Example | Lives in |
|---|---|---|---|
| **Understanding** | How the human thinks | *how I think about financial risk* | a [lens](protocol.md) |
| **Work** | What the human is changing | *rebalance the portfolio by March* | [work](work.md) |
| **Knowledge** | How things are | *the brokerage account holds 60% index funds, as of Oct 1* | the world layer |

Knowledge is the plainest of the three: facts. It has to be the most trustworthy, because everything else reasons from it. A sphere that states a stale or guessed fact with confidence does more harm than one that says "I don't know." — **proven**

---

## Structure — **proven**

```
layers/world/
├── subjects/
│   └── <domain>/
│       └── <subject>.md     one file per subject: its items and their states
├── history/                 narrative record of the past, append-only
└── registry.md              generated: every domain and subject, how they relate
```

**Three levels, no more:** domain → subject → item.

- A **domain** is a broad area: *finance*, *people*, *home*, *health*, or, in a work sphere, *codebase*, *team*, *org*.
- A **subject** is one thing worth tracking inside it: *retirement accounts*, *the car*, *the payments service*.
- An **item** is a specific fact about a subject, kept as a row inside the subject's file.

Detail below item level goes in fields on the item, never in new files. Without that limit, a world layer turns into a maze nobody reads.

Builds rename freely. A life sphere might use its own vocabulary for subjects and items. A work sphere might split the layer into several domains. The three levels stay.

## A subject file

```yaml
---
domain: finance
related: [taxes, retirement-planning]
work: [rebalance-portfolio]      # work nodes about this subject, by name
updated: 2026-10-25
---
```

Then a table of items:

| Item | State (current → intended) | As of | Grade | Source |
|---|---|---|---|---|
| Index fund share | 60% → 70% | 2026-10-01 | verified | brokerage statement, Oct 2026 |
| Contribution rate | 10% → 15% | 2026-09-15 | stated | the human, in session |

And free notes: why the subject is tracked, what's in tension, what to watch.

**Current → intended** is what makes a fact useful for work. The gap between the two is often where a work node comes from.

## The registry — **proven**

`registry.md` is **generated** from subject frontmatter at ground, never edited by hand. It's the one small file the sphere reads to know the shape of the world before opening any subject. See [registries](registries.md).

## History — **proven**

`history/` holds the story behind the current state: how a career unfolded, why a move happened, what a long project taught. It's **append-only.** When history turns out to be wrong, a correction is appended next to it. The original is never rewritten.

---

## Grades and freshness — _decided, not yet exercised_

Every fact carries a **grade**, saying where it came from, and an **as of** date.

| Grade | Meaning |
|---|---|
| **verified** | Read from a primary source: a statement, an official page, the document itself |
| **reported** | From a secondary source: an article, a summary, someone else's account |
| **stated** | The human said it. Authoritative for their own life and choices, though not for outside facts like prices or rules. |
| **inferred** | The AI's reasoning, not yet checked |

**Facts go stale at different speeds.** A share price is stale in a day, a tax rule in a year, a birthday never. Each domain can declare how long its facts stay fresh. When the sphere is about to rely on a stale fact for a decision, it re-checks it first or says plainly that it's stale.

**Saying the grade.** When the sphere tells the human a fact that isn't verified, it says so: *"reported, not checked against the source"* or *"my inference."* A confident answer that turns out wrong costs more than an honest "I'm not sure."

---

## How facts get in — **proven**

**Facts are proposed, never written automatically.** During a session, the sphere notices facts worth keeping: something the human mentioned, something a document showed. It holds them, and at ground it offers them as one batch:

> I picked up 3 facts this session:
> - Contribution rate is now 15% (stated)
> - The lease ends in August (verified: lease PDF)
> - The client prefers async updates (inferred from the thread)
>
> Save all, some, or none?

The human decides what becomes the sphere's knowledge. A world layer fed automatically fills up with half-true guesses that every later session treats as fact.

---

## Facts about other people

A sphere inevitably holds facts about people other than its human: family, colleagues, friends. These people never agreed to be in it. So:

- **The sphere only keeps what the human chose to record.** It doesn't build profiles of people on its own, or collect everything it happens to see about someone.
- **Facts about other people never leave the sphere,** whether in exports, mirrors or published views. See [replication](replication.md).
- **The human can read everything** the sphere holds about anyone, because it's plain files.

---

## Open questions

1. **Grade names.** Are *verified / reported / stated / inferred* the right four, and the right words?
2. **Freshness windows.** Should domains declare them, or should the sphere learn them? And what's the default for a domain that declares nothing?
3. **Batch size at ground.** When a session produces many candidate facts, should the sphere offer them all, or only the most useful few and drop the rest?
4. **History vs progress.** A finished work node's `progress.md` is a kind of history. Does any of it move into `history/` when the work is archived, or does history stay narrative only?
