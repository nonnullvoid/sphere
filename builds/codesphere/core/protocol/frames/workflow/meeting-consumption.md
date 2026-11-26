---
frame: meeting-consumption
lens: [workflow]
derives_from: [workflow@1, human-rhythm@1]
version: 1
version_note: First draft. Consume (confirmed first), a curated record, extract signals, propose, the human fills the gaps, assimilate on confirm; never automatic.
status: drafting
updated: 2026-11-22
sharing: public
reads: [layers/workflows/meetings, layers/knowledge, layers/work]
writes: [layers/workflows/meetings, layers/knowledge, layers/work]
protocol: []
---

# Turning a meeting into knowledge

**Applies to:** the human pointing the sphere at a meeting's notes or transcript (pasted, a file, a link from a notes tool), or mentioning a meeting that just happened.

**A meeting happened where the sphere was blind.** Archiving the notes isn't enough. What matters is that the meeting changes what the sphere knows and where the work stands, with the human supplying what the notes couldn't.

## The runbook

1. **Consume.** Read the source. Say which meeting it is and what it'll touch (which work, which knowledge). **Confirm before going on.**
2. **Keep a record.** A curated record in `layers/workflows/meetings/records/<date>-<name>.md`: who, what it was about, the threads worth pulling on, links to the work and knowledge it touched. The raw notes stay as the source; nothing is lost.
3. **Extract the signals,** out of the noise: decisions, commitments (whose, by when), facts about the world, risks, changes in people or roles, shifts in where work stands.
4. **Propose,** never apply:
   - facts → knowledge topics, graded and sourced to the record ([knowledge-capture](../knowledge/knowledge-capture.md));
   - where work stands → the work items it touched ([work-progress](../work-tracking/work-progress.md));
   - follow-ups → the agenda ([meeting-readiness](meeting-readiness.md)).
5. **The human fills the gaps.** Notes capture what was said, not what mattered: the room, what went unsaid, *what this really meant*. Ask, in a line, whether there's anything the notes missed. What they add folds into the proposals. **This step is the point,** not a formality.
6. **Assimilate,** on the human's yes: the facts are written (graded, sourced to the record), the work items updated, the record linked from each.

**People are private.** What a meeting says about colleagues goes into the `people` domain only as the human wants it kept, and never into anything sent ([outbound-guard](../human-is-highest/outbound-guard.md)).

## When / do

| When | Do |
|---|---|
| A meeting's notes are pasted, dropped in, or linked | Offer to take the meeting in; say what it'll touch. Nothing happens until the human says yes |
| The human mentions a meeting that just happened | Offer once to take it in, if there are notes |
| Proposals are ready | Show them grouped by where they'd go, and ask what the notes missed |
| The human adds context | Fold it in; show the changed proposals |
| The human confirms | Write the facts and the work updates, each linked to the record. Save with the next ground |

## Works with

- [meeting-readiness](meeting-readiness.md): the before-the-meeting half.
- [knowledge-capture](../knowledge/knowledge-capture.md): how facts are graded and sourced.
- [say-how-sure](../knowledge/say-how-sure.md): a fact from someone's remark in a meeting is *stated*, not *verified*.
