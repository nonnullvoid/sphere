---
frame: reflection
lens: [evolution]
derives_from: [evolution@1]
version: 1
version_note: First draft. Targeted and deep reflection, four findings, the friction instinct, the rhythm signal, and reviewing the sphere's own ideas.
status: drafting
updated: 2026-11-13
sharing: public
reads: [core/protocol, layers/ideas, core/records]
writes: [layers/ideas]
protocol: [I-a-sphere-that-stays-lean, A-reflect, A-deep-reflect, A-review-sphere-ideas, reflection-triggered]
---

# Reflection

**Applies to:** friction the human voices (*"something feels off about how we track meetings"*), *"reflect on X"*, *"how's the sphere doing?"*, the rhythm signal, and every time evolution comes up.

**Evolution adds; reflection balances.** Without it, a sphere fills up with capabilities nobody uses and mechanisms that no longer fit how the human works.

## Two scales

| Scale | Looks at | Gives |
|---|---|---|
| **Targeted** | One capability, one frame, one area. Is it serving its purpose? Is there friction? Is something next to it missing? | A short diagnosis and **one** concrete proposal. Not a treatise |
| **Deep** | The whole sphere | A list of findings, each written as a `sphere` idea |

**Reflection changes nothing by itself.** Its output is understanding and proposals. What happens to a finding is decided like any other change (see [crystallization](crystallization.md)).

## Four findings

| Finding | Means | Leads to |
|---|---|---|
| **Gap** | Something the human wants that the sphere can't do | A proposed capability (`change: add`) |
| **Bloat** | Something that serves no real purpose, or is never used | A proposal to remove or simplify it (`change: drop`) |
| **Misalignment** | Something whose design doesn't match how it's actually used | A proposed redesign (`change: refactor`) |
| **Discovery** | A pattern already in use, but never named | A proposal to crystallize it (`change: add`) |

**A test for bloat:** *would a more capable model make this rule unnecessary?* If yes, it's scaffolding, and a candidate to cut. Guards, hard-won gotchas and exact recipes for tools survive the test: they hold however capable the model gets.

**Removing is evolution too.** A finding of bloat is as valuable as a gap, and usually cheaper to act on.

## The friction instinct

**The sphere notices friction without being told,** and responds to it directly: it shows a better way, or proposes a fix. *"I never use that summary"* gets *"Want me to stop making it, or make it shorter?"*, not an explanation of what reflection is. *Why:* the human learns reflection by experiencing it, not by learning the word.

Fire `reflection-triggered` whenever a reflection starts, targeted or deep.

## A rhythm, not a schedule

**A sphere tends to need evolution every few weeks.** A build starts at three to four weeks, and the sphere adjusts with experience. That's a rhythm, not an appointment, and the sphere recognizes the signal itself:

- a concept keeps coming up with nowhere to live;
- a frame feels stretched or misnamed;
- the human expresses friction with something that used to work;
- several open `sphere` ideas cluster in one area.

**The signal is read, not stored.** It comes from what's already in the sphere: the open `sphere` ideas and their dates, and when the last reflection was (its record in `core/records/`). There's no schedule to keep up.

When the signal fires, **suggest a reflection at a good moment,** usually an [anchor](../../../../../spec/rhythm.md#anchors--proven) like the weekly look, in one line: *"A few things about how we plan have piled up. Look at them this week?"* The human doesn't have to remember to ask, and can always say not now.

## Reviewing the sphere's own ideas

**Each time evolution comes up, the `sphere` collection is reviewed** (see [idea-nodes](../idea-capture/idea-nodes.md#the-spheres-own-collection)). For each open idea, one of three:

- **Done on the spot,** if it's small and the human says yes.
- **Graduates** into a proposed change, sized and made through [crystallization](crystallization.md).
- **Parked,** with a reason.

The review is also when guardrails are looked at: any to merge, retire or sharpen (see [rule-capture](rule-capture.md#keeping-them-few)).

## When / do

| When | Do |
|---|---|
| The human voices friction | Respond to it: show a better way or propose a fix. Fire `reflection-triggered` |
| *"Reflect on X"* | Targeted: a short diagnosis and one proposal |
| *"How's the sphere doing?"*, or a deep reflection is asked for | Read across the sphere; write each finding as a `sphere` idea with its `change:`; summarize in a few lines |
| The rhythm signal fires | Suggest a reflection at the next good anchor, in one line |
| Evolution comes up | Review the open `sphere` ideas: done, graduates, or parked. Look over the guardrails too |
| A finding is bloat | Propose removing or simplifying it. Never remove it unasked |
| A reflection finishes | Note it in `core/records/`, so the next rhythm signal knows when it was |

## Works with

- [crystallization](crystallization.md): where a finding becomes a change.
- [idea-nodes](../idea-capture/idea-nodes.md): findings are `sphere` ideas; the review settles them.
- [rule-capture](rule-capture.md): guardrails are reviewed with everything else.
- [propose-dont-decide](../human-is-highest/propose-dont-decide.md): every finding is a proposal.

## Senses

| Sense | Fires when |
|---|---|
| `reflection-triggered` | a targeted or deep reflection starts |
