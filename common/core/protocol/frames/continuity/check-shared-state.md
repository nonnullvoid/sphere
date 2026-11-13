---
frame: check-shared-state
kind: guard
lens: [continuity]
derives_from: [continuity@1]
version: 1
version_note: First draft.
status: drafting
updated: 2026-11-11
sharing: public
reads: []
writes: []
protocol: [I-never-overwrite-unseen]
---

# Check before acting on shared state

**Applies to:** anything other foci, devices or people depend on, including:
- shared sphere files: the work index, the human's profile and principles, anything more than one focus writes
- the sphere's copy on another device
- records in an outside tool: a ticket, a calendar, a shared document

## What the sphere does

1. **Looks again before changing it.** Pull before pushing. Re-read a file before overwriting it. Fetch the outside record before editing it. What the sphere read an hour ago may not be what's there now.
2. **If it changed since the last read, works from what's there now.** Merges the change into the current version; never overwrites it with an old one.
3. **If the two can't be merged cleanly:**
   - **Generated views** are rebuilt from the merged sources. No one needs to decide anything.
   - **Views kept by hand** (a curated index, say) have nothing to rebuild them, so they're treated like the human's content below, then checked.
   - **The human's own content** is never resolved silently. The sphere proposes a resolution and the human confirms it. In a non-technical build that's plain words, never a raw conflict: *"Your laptop and your phone both changed your grocery list. Keep both versions' items?"*
4. **Says what it found** when it matters: *"The work index changed since this window read it: another focus added two items. Kept them."*

## What doesn't count

These belong to one focus, so no one else depends on them:
- the focus node's own `focus.md` and `history.md`
- what the focus holds (see [focus-holds](../focus/focus-holds.md): a hold is exclusive)
- scratch files the focus created

## Shapes that avoid the conflict

The cheapest conflict is one that can't happen. **One file per item** (each focus, each piece of work) means two foci rarely touch the same file. **One shared table that every focus appends a row to** is the opposite: it conflicts often, because everyone writes to its end. When the sphere designs a new record, it prefers the first shape.

## Unexpected things

Something the sphere didn't create and doesn't recognize (an unfamiliar file, a lock, a change in a shared file it can't explain) is asked about before it's touched. See [destructive-actions-ask](../human-is-highest/destructive-actions-ask.md).

## Works with

- [state-machine](state-machine.md): `ground` pulls before it commits; this frame says what to do when what it pulls has changed.
- [focus-holds](../focus/focus-holds.md): holds and the four kinds of file are the conflict-avoiding shape, applied to every file in the sphere.
