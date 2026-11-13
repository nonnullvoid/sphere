---
frame: kinds-of-file
kind: guard
lens: [nodes]
derives_from: [nodes@1]
version: 1
version_note: First draft.
status: drafting
updated: 2026-11-11
sharing: public
reads: []
writes: []
protocol: [I-never-overwrite-unseen]
---

# Know a file's kind before writing it

**Applies to:** every write to a file in the sphere.

## The four kinds

| Kind | Examples | Who writes it | How |
|---|---|---|---|
| **Current state** | `work.md`, `focus.md`, a draft, a view kept by hand | **Only whoever holds it** | Rewrite in place. Anyone else offers a change to the holder |
| **History** | `progress.md`, `history.md` | Anyone | **Append only**, after re-reading. Never edit or delete an entry |
| **Reference** | knowledge topics, lenses and frames, the human's profile, principles | **Nobody directly** | Propose; apply only when the human confirms, one change at a time, re-reading first |
| **Generated** | indexes, the capability manifest, views | **Nobody** | Rebuild from sources. A hand edit is lost at the next rebuild |

**Write only to what you hold; anything else is appended, offered, proposed or rebuilt.**

## Before every write

1. **What kind is this file?** If it isn't clear, treat it as current state and find its holder.
2. **Act by kind:** rewrite only if you hold it; append if it's history; propose if it's reference; rebuild if it's generated.
3. **Re-read before writing** anything another window or device might have changed since you last read it.

*Why:* nearly every collision between several writers is two of them rewriting the same current-state file. Giving each kind one way of being shared removes that, with no locks or queues beyond the short one at ground.

## Mistakes to catch

| About to | Instead |
|---|---|
| Rewrite a file another focus holds | Offer the change to its holder |
| Edit or remove a history entry | Append a new entry that corrects it |
| Write a fact or a lens change directly | Propose it |
| Hand-edit an index or view | Change the nodes it's built from, then rebuild |

## Works with

- [node-shape](node-shape.md): every node has current state and history; this frame says how each is written.
- [focus-holds](../focus/focus-holds.md): how a focus comes to hold current state.
- [propose-dont-decide](../human-is-highest/propose-dont-decide.md): why reference is proposed, never written.
