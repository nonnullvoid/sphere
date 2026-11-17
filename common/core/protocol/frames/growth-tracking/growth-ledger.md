---
frame: growth-ledger
lens: [growth-tracking]
derives_from: [growth-tracking@1]
version: 1
version_note: First draft. The plain ledger, what it tracks, its entries and lanes, what writes them, the plain view, and exports.
status: drafting
updated: 2026-11-13
sharing: public
reads: [layers/witness, layers/work, layers/literacy, layers/focus, core/ai, core/records]
writes: [layers/witness]
protocol: [I-see-myself-grow, A-record-win, A-show-growth, A-export-record, growth-recorded, record-exported]
---

# The growth ledger

**Applies to:** every ground that finished something, the wrap and the weekly look back, the human naming a win (*"log a win: ran my first 10k"*), *"how am I doing?"*, and any request to export a record of what got done.

## The witness layer

```
layers/witness/
├── ledger/
│   ├── 2026.md       this year's entries, newest first
│   └── 2025.md
├── lanes.md          what this sphere tracks, and its lanes
└── <theme>/          a theme's own records, if there is one (see growth-themes)
```

- **The ledger is history:** appended, never rewritten. One file per year keeps each file short. A correction is a new entry pointing at the old one.
- **`lanes.md` is reference:** one line saying what the sphere tracks (see below), then a short list of lanes, each a name and a line on what counts. The sphere proposes a starting set; the human decides. Changing it is a proposal.
- **There's no current-state file.** What's true now (this month's wins, a lane gone quiet) is computed from the ledger. *Why:* a running total kept beside the entries is a second truth that drifts.

## What it tracks

The first line of `lanes.md` says whose growth this sphere keeps (the [lens](../../lenses/growth-tracking.md#whose-growth-it-tracks) explains each):

```markdown
tracks: unit          # unit | apart | human | world
```

| `tracks` | Which entries are kept | `by:` on an entry |
|---|---|---|
| `unit` | everything the sphere got done | left out |
| `apart` | the human's wins and abilities, and the sphere's own effectiveness | `human`, `sphere` or `together`, on every entry |
| `human` | the human's achievements and milestones | left out |
| `world` | outcomes in the world, whoever made them | left out |

- **`apart` adds a `sphere` lane** for the sphere's own effectiveness. Its entries point at records the sphere already keeps: an agent trusted with more (`trust-changed`), a rule captured after a mistake, a sphere change that landed, a stretch of grounds with no correction.
- **Changing what's tracked never rewrites the ledger.** Old entries stay as they were; the views read what's there.

## An entry

```markdown
### 2026-11-12 · home
Kitchen plumbing sorted: three quotes compared, one booked.
evidence: work:home.kitchen.plumbing (done)

### 2026-11-10 · learning
Index funds: can use.
evidence: literacy:money.investing.index-funds (level)

### 2026-11-09 · health
First 10k run, in under an hour.
evidence: the human said so
```

In a sphere that tracks `apart`, each entry also says who:

```markdown
### 2026-11-12 · sphere
The research agent now runs literature searches unattended.
by: sphere
evidence: core/records/agents/research.md (trust changed)
```

| Part | Holds |
|---|---|
| **Date and lane** | When it happened, and which lane it counts in. One lane per entry; the most fitting one |
| **What** | One line, in plain words. What the human would say if asked what they did |
| **By** | Only when the sphere tracks `apart`: `human`, `sphere` or `together` |
| **Evidence** | A link to where it's recorded (`work:`, `literacy:`, a commit, an outbound receipt), or *the human said so* |

- **Pointers, not copies.** An entry names the node and what happened to it. The node's own history holds the story.
- **The human saying so is evidence.** It's their life; a win they name counts.
- **Never an entry without evidence.** If there's nothing to point at and the human didn't say it, it isn't recorded.

## What writes an entry

| Source | Becomes an entry |
|---|---|
| **A work node finished** (`done`) | At the ground that finished it, quietly. Tasks too small to matter are left out by the lane's own line on what counts |
| **A subject reached a new level** | At the ground that confirmed it, quietly. In the learning lane |
| **The sphere changed** (`sphere-evolved`) | One entry for the change, in the sphere's own lane, if it keeps one |
| **An agent earned more trust** (`trust-changed`, upward) | One entry in the sphere's lane, when the sphere tracks `apart` |
| **The human names a win** | Straight away; they said so. Say it in one line: *"Recorded: first 10k."* |
| **The wrap** | Offer once, in a line: *"Anything worth recording today?"* Never more than once |

- **Quiet by default.** Entries from finished work and levels go in without comment, listed in the ground's one-line summary at most. **A milestone is the exception:** it gets a line of celebration (see [growth-themes](growth-themes.md#milestones)).
- **Dropped work isn't a win.** Neither is a node merely archived.
- **The sphere never decides a win on its own say** beyond what's already evidenced. A *"that seemed like a big deal, record it?"* is an offer.

## The plain view

**Without a theme, growth is shown plainly,** built from the ledger alone:

> **This week:** 4 things done. Home: kitchen plumbing sorted. Learning: index funds, can use. Health: first 10k. Work: the quarterly report sent.
> **Quiet lane:** friends, nothing since October.

- **"How am I doing?"** answers with this, for the week, or the period asked about. In a sphere that tracks `apart`, *"how is the sphere doing?"* shows the sphere's half the same way.
- **The weekly look back** offers it, in a line, as one of the anchor's offers.
- **A quiet lane is named, gently,** never as a reproach. It's information, not a nudge.
- **A witness view** (a page the human can open) is a [projection](../../../../../spec/projections.md#matter-not-machinery) of the ledger. It deserves care: for many people it's the warmest thing a sphere shows them.

## Exports are views of the ledger

**Evidence for a review, a portfolio, a status report, a look back at the year:** each is built from the ledger, following its evidence links into the nodes for detail. **Exports read the ledger, never a theme.** A score means nothing outside the game.

- **Draft it, show it, wait.** An export meant for anyone else passes the [outbound guard](../human-is-highest/outbound-guard.md).
- **Facts about other people stay out,** unless the human puts them in.
- **The ledger stays the truth.** An export is a copy for a purpose; it isn't kept in step.

Fire `record-exported`.

## When / do

| When | Do |
|---|---|
| A ground finished a work node | Append an entry pointing at it, quietly. Fire `growth-recorded` |
| A ground confirmed a new level | Append an entry in the learning lane, quietly. Fire `growth-recorded` |
| The human names a win | Append it; say so in a line. Fire `growth-recorded` |
| The wrap | Offer once: anything worth recording? |
| The weekly look back | Offer the plain view in a line |
| *"How am I doing?"* | The plain view for the period, or the theme's view if there is one |
| A lane goes quiet for a long while | Name it gently in the plain view; nothing more |
| An export is asked for | Build it from the ledger; draft it; outbound guard if it leaves. Fire `record-exported` |
| An entry was wrong | Append a correction pointing at it |

## Works with

- [growth-themes](growth-themes.md): what a theme makes of each entry.
- [work-progress](../work-tracking/work-progress.md): *done* means finished, with evidence; that's what an entry points at.
- [skill-progress](../literacy-tracking/skill-progress.md): a confirmed level is an entry in the learning lane.
- [kinds-of-file](../nodes/kinds-of-file.md): the ledger is history, `lanes.md` is reference, views are generated.
- [outbound-guard](../human-is-highest/outbound-guard.md): exports that leave the sphere.

## Senses

| Sense | Fires when |
|---|---|
| `growth-recorded` | an entry is appended to the ledger |
| `record-exported` | an export is built from the ledger |
