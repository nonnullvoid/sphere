---
frame: skill-progress
lens: [literacy-tracking]
derives_from: [literacy-tracking@1]
version: 1
version_note: First draft. The subject record, levels from evidence, tracking and stopping, updates at the edges, staleness computed.
status: drafting
updated: 2026-11-13
sharing: public
reads: [layers/literacy, layers/knowledge, layers/focus]
writes: [layers/literacy]
protocol: [I-know-where-i-stand, A-track-subject, A-stop-tracking, A-show-understanding, A-set-level, new-territory, node-archived, focus-grounding, stale-found]
---

# Where the human stands in a subject

**Applies to:** starting or stopping tracking a subject, every ground that touched a tracked subject, the human saying where they stand (*"I've got this now"*), and *"what do I know about …?"*

## The subject

**A subject is one area the human is learning,** tracked as a node in the literacy layer:

```
layers/literacy/
├── money.investing.index-funds/
│   └── subject.md      the level, open questions, and what showed it
├── code.rust/
│   └── subject.md
├── sphere/
│   └── subject.md      the sphere itself (see teaching)
├── library/            artifacts worth keeping (see library)
├── archived/           subjects no longer tracked
└── index.md            generated
```

- **Named like knowledge,** by namespace: `money.investing.index-funds`. Its place is its name; folders stay flat. From elsewhere, `literacy:<name>`.
- **Name it the way the human would.** A subject is as broad as they're learning it: *Rust*, not *Rust's borrow checker*, until the narrower thing needs its own record.
- **The current state and the history share one file.** The record is short; what showed the level belongs right next to it.

### `subject.md`

```yaml
---
subject: money.investing.index-funds
title: Index funds
summary: chooses between funds unaided; fees still fuzzy
level: can-use              # skimmed | can-use | can-teach
rests_on: [knowledge:money.investing]   # optional: what it was learned from
stale:                      # optional: why, when an outside change is known
tracked: 2026-09-14
updated: 2026-11-10
---
```

| Key | Holds |
|---|---|
| `subject` | The name; matches the folder |
| `title` | What the human would call it |
| `summary` | One line on where they stand |
| `level` | `skimmed`, `can-use` or `can-teach` |
| `rests_on` | Knowledge topics the subject was learned from. Optional. Used to tell when understanding may be stale |
| `stale` | Absent unless an outside change is known (*"the app redesigned its menus"*). A short reason |
| `tracked`, `updated` | When tracking began, and when the record last changed |

```markdown
# Index funds

## Now
Picks between funds by cost and spread without help. Next step: how fees
compound over decades, which is why the cheaper fund wins.

## Open questions
- Does rebalancing cost anything?

## Evidence
### 2026-11-10 · used
Compared two funds by expense ratio, unprompted (f24-savings-review).
### 2026-10-28 · used
Explained the difference between an index fund and an active one, correctly.
### 2026-10-02 · level
skimmed → can-use, on the human's yes.
### 2026-09-14 · taught
A two-minute version of what an index fund tracks.
```

- **Now and Open questions are current state:** where the human stands, the next step up, and what they're still unsure of.
- **Evidence is history,** newest first, appended, never rewritten. Each entry is dated, with what kind it is: **used** (did it, unprompted), **explained** (said it back correctly), **asked** (a question that showed where they are), **taught** (the sphere explained something), **stated** (the human said where they stand), **level** (the level changed, and on whose say). Point at the focus where it happened.

## Levels come from evidence

| Level | Means | Shown by |
|---|---|---|
| **skimmed** | Has met it; couldn't use it alone yet | Where every subject starts, unless the human says otherwise |
| **can-use** | Uses it without help | *used* entries, more than one, at different times, unprompted |
| **can-teach** | Could explain it to someone else | *explained* entries: they've put it in their own words, correctly, more than once |

- **Never on one instance.** One good answer isn't understanding yet.
- **Taught isn't evidence of a level.** It records that an explanation was given; only what the human does with it counts.
- **The human's word sets it.** *"I've got this now"* raises the level, recorded as *stated*. *"I don't really get this"* lowers it. Their word overrides the evidence.
- **The sphere never raises a level on its own say.** The record is a read about the human, so changes to it are proposed (see below).
- **Levels go down only on the human's say.** A long gap, or a stumble, makes the sphere check gently; it doesn't demote.

## Tracking starts explicit

- **Track a subject when the human asks** (*"keep track of how I'm doing with Rust"*), **or says yes when offered.** Write `subject.md` at `skimmed` (or the level the human gives), with a first evidence entry saying why it's tracked.
- **Offer when the sphere notices new territory:** the human takes on an unfamiliar stack, tool or kind of problem and needs more help than usual. Ask once: *"This looks new to you. Want me to keep track of how it's going?"* Fire `new-territory`. If no, don't ask again about that subject.
- **Stopping** (*"stop tracking Rust"*) finishes the node: a last evidence entry, then the folder moves to `layers/literacy/archived/`. Asked to track it again, it moves back, record intact.
- **The sphere learns where this human wants support,** and where they don't, over time. That's an observation about the human, kept with the AI's other observations, visible and correctable.

## Updated at the edges

**The record is true at ground and at the human's word.** In between, the sphere may note things, but doesn't promise to.

| Moment | What happens |
|---|---|
| **Ground** | For each tracked subject the window touched, append the evidence it produced. Then offer any change to the level, Now or open questions, **one line per subject:** *"Index funds: skimmed → can use? You compared two funds unprompted twice this week."* Write what's confirmed |
| **The human says where they stand** | Set the level; add a *stated* entry. |
| **During** | Notice evidence as it happens; leave the writing for ground |

- **The top is reference, the evidence is history.** Any ground can append evidence. The level, Now and open questions change only on the human's yes. *Why:* it's the sphere's read of the human, and they're the authority on themselves.
- **Offer level changes in the ground batch,** alongside facts to keep, never as a separate interruption.

## Staleness is computed

**Understanding may be stale when what it was learned from has changed.**

- **Inside the sphere:** a topic in `rests_on` updated after the subject's latest evidence makes it *suspected stale*. The index computes this; nobody marks it.
- **Outside the sphere:** a tool or a rule known to have changed sets `stale:` with a short reason, with the human's yes.
- **Stale means check, not demote.** Next time it comes up, check lightly that the human's picture still holds, and say what changed. Fresh evidence clears it.

## The index

`layers/literacy/index.md` is **generated** from subject and artifact frontmatter: every tracked subject with its level and summary, which are stale and why, and the library's artifacts. Never edited by hand.

*"What do I know about index funds?"* answers from the subject: the level, the summary, open questions, and the last few pieces of evidence. *"How am I doing?"* lists tracked subjects, one line each.

## When / do

| When | Do |
|---|---|
| *"Track my learning of …"* | Write `subject.md`; first evidence entry |
| The human takes on unfamiliar ground | Offer to track it, once. Fire `new-territory` |
| `focus-grounding`, if it touched a tracked subject | Append evidence; offer level, Now and question changes in one line per subject |
| The human confirms a change | Write it; a *level* entry for a level change. |
| *"I've got this now"* | Set the level; a *stated* entry. |
| `stale-found knowledge`, if a tracked subject rests on the topic | Mark the subject stale: check lightly next time |
| An outside change is known | Offer to set `stale:` with the reason |
| *"Stop tracking …"* | Last entry; move to `archived/`. Fire `node-archived` |
| *"What do I know about …?"* | Level, summary, open questions, recent evidence |

## Works with

- [adapt-to-level](adapt-to-level.md): what the level is for.
- [teaching](teaching.md): gaps, and the *taught* entries.
- [library](library.md): artifacts tagged with the subjects they explain.
- [knowledge-capture](../knowledge/knowledge-capture.md): the topics a subject rests on.
- [kinds-of-file](../nodes/kinds-of-file.md): the top is reference, the evidence is history, the index is generated.
- [node-shape](../nodes/node-shape.md): stopping tracking is finishing the node.
- [propose-dont-decide](../human-is-highest/propose-dont-decide.md): a level is proposed, never set on the sphere's say.

## Senses

| Sense | Fires when |
|---|---|
| `new-territory` | the human takes on unfamiliar ground that isn't tracked |
| `node-archived` | for a subject: tracking stops |
