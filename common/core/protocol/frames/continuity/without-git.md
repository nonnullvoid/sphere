---
frame: without-git
kind: structural
lens: [continuity]
derives_from: [continuity@1]
version: 1
version_note: First draft. The gitless fallback from spec/state.md.
status: drafting
updated: 2026-11-11
sharing: public
reads: [layers/focus, layers/work, surface/state/focus]
writes: [layers/focus, layers/work, surface/state/focus]
protocol: [I-pick-up-where-i-left-off, A-ground, gitless-lock-held]
---

# Without git

**Applies to:** a sphere whose folder has no git repository, or where git can't run (a locked-down machine, a phone, a shared drive).

Git is the default because it gives history, undo and merges. Without it, a sphere still works: it remembers, it grounds, and windows can attach cold. What it loses is the safety net, so it runs more carefully and says so.

## What's lost

| Edge case | What goes wrong without git |
|---|---|
| Two foci in the foreground at once | Last writer wins on shared files; the other focus's changes are lost silently |
| One sphere synced to two devices through a cloud folder | The sync service makes conflict copies, or picks one version |
| A crash halfway through a ground | Some files written, some not, with no record of which |
| A bad ground | No history, so it can't be undone |
| The human edits a file while a window is attached | The window's next write overwrites the edit |

## How it runs

- **Tell the human once,** when the sphere starts without git: *"There's no version history here, so I can't undo, and only one thing can be in focus at a time. Want me to set up git?"* If they say no, don't ask again unless something goes wrong.
- **One focus in the foreground at a time.** When a window attaches, write a lock file at `surface/state/focus/LOCK` naming the focus and the time. A second window that finds the lock opens **read-only**, says so, and offers to wait or take over.
- **A stale lock** (older than the liveness threshold, with no heartbeat) may be from a crash. Ask before taking it over; never clear it silently. Fire `gitless-lock-held` when a window is turned away.
- **Ground writes the same records** (work progress, the focus node's Now and history) with no commit. It still reports in one line.
- **Re-read before every write** to a file the human might edit. If it changed since this window read it, merge, or ask (see [check-shared-state](check-shared-state.md)). Never overwrite unseen.
- **`undo` and `revert` aren't available.** If the human asks, say so plainly.
- **Cloud-synced folders:** if the sync service makes conflict copies (`file (1).md`, `file-conflict.md`), treat each as an unexpected file: show it and ask which version to keep.

## When / do

| When | Do |
|---|---|
| The sphere starts and finds no git | Say what's lost, once, and offer to set up git |
| A window attaches and no lock exists | Write the lock; carry on |
| A window attaches and finds a live lock | Open read-only; say which focus holds it |
| A window finds a stale lock | Ask before taking it over |
| The human asks to undo | Say it isn't available without git |
| A sync conflict copy appears | Show both versions; the human picks |

## Works with

- [state-machine](state-machine.md): the same states and operations, minus the commit, undo and revert.
- [check-shared-state](check-shared-state.md): matters more here, because nothing catches an overwrite afterwards.
