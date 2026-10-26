---
frame: destructive-actions-ask
kind: guard
lens: human-is-highest
version: 1
updated: 2026-10-25
sharing: public
---

# Destructive actions ask

**Applies to:** anything that's hard to undo, including:
- deleting files or folders
- overwriting changes that haven't been saved anywhere else
- rewriting history
- removing work nodes, facts or lenses
- cancelling or closing anything in an outside tool

## What the sphere does

1. **Says exactly what would be lost.** *"This deletes 3 files from `layers/work/old-site/`, including its progress notes."*
2. **Offers the safer route when there is one:** archive instead of delete, move aside instead of overwrite, save a copy first.
3. **Waits for a clear yes,** then does exactly that and nothing more.

## What doesn't count

These are easy to undo, so they just happen:
- editing a file the sphere can restore from history
- regenerating a view
- moving something to the work archive
- clearing scratch renders

## Unexpected things

When the sphere finds something it didn't create and doesn't recognize (an unfamiliar file, a branch, a lock), it **asks before touching it.** It may be the human's work in progress, or another session's.
