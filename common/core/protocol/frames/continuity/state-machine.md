---
frame: state-machine
kind: structural
lens: [continuity]
derives_from: [continuity@1]
version: 1
version_note: First draft.
status: drafting
updated: 2026-11-11
sharing: public
reads: [layers/focus, layers/work]
writes: [layers/focus, layers/work]
protocol: [I-pick-up-where-i-left-off, I-try-things-safely, A-ground, A-peek, A-undo, A-revert, focus-grounded, dirty-detected]
---

# State machine

**Applies to:** every change to the sphere's own files, and every operation that moves them between states.

## The states

| State | Means |
|---|---|
| **Bootstrap** | The sphere is being created; its structure doesn't exist yet. Happens once. |
| **Working** | Changes in progress, not yet saved. |
| **Grounded** | A clean, saved state. Every grounded state is a commit. |

After bootstrap, the sphere moves between *working* and *grounded* for the rest of its life.

**Two levels when several foci are open.** The sphere is always its latest commit. Each [focus node](../focus/focus-nodes.md) moves between working and grounded on its own: its held files have unsaved changes, or they don't. With one focus open, the two levels are the same thing.

## The operations

Each operation acts on one focus node and is a move with a contract. The focus verbs (*open*, *attach*, *detach*, *close*) are in [focus-nodes](../focus/focus-nodes.md); their saving step is `ground`, below.

| Operation | Moves | Saves? | Reads | Writes |
|---|---|---|---|---|
| `ground` | working → grounded. Can take a name: *"ground, call it before-restructure"* | **Yes** | this focus's changes | the focus's records, then one commit |
| `peek` | nothing | No | uncommitted changes, recent grounds | nothing |
| `undo` | this focus back to its previous grounded state | **Yes**, as a new commit | the focus's last commit | a reversing commit |
| `revert` | back to an earlier grounded state, named or recent | **Yes**, as a new commit | history | a reversing commit |

- **Read-only operations write nothing.** `peek` reports and stops. Its long form, *"what happened today?"*, lists recent grounds.
- **Composite operations declare their parts.** `detach` = ground + background. `close` = ground + end. A composite's contract is the union of its parts'. If a part fails, stop and say which.
- **There's no separate sync.** Ground is the one way state reaches the sphere. With several devices, ground pulls before it commits and pushes after.
- **Undo and revert never destroy.** They add a commit that reverses an earlier one. History stays whole, which is what makes trying things cheap.

## Ground, step by step

1. **Update the work.** Each piece of work the focus touched gets its `progress.md` entry: what happened, what's next. New facts and rules are proposed, not written.
2. **Write the focus node:** rewrite **Now** in `focus.md`, append a history entry. A child also appends one line to its parent's history. (Shapes in [focus-nodes](../focus/focus-nodes.md).)
3. **Apply confirmed reference changes** (facts, lens edits the human said yes to), one at a time, each after re-reading the file.
4. **Rebuild generated files from what's committed** plus this ground's own changes. Never from the working folder: it may hold other foci's unfinished work, and a view built from it would commit that work's shadow.
5. **Reconcile this focus.** Other changed files no focus holds are listed and left for main; nothing stops. Ask *"hold it too?"* only about files this window edited outside the holds. Questions about other foci (quiet for weeks, stale unsaved work) aren't asked here; see [focus-nodes](../focus/focus-nodes.md#reconciling-each-question-where-it-belongs). This runs in the ground tooling, not as a habit, because a step that depends on remembering eventually gets skipped.
6. **Commit under a short lock.** Two foci grounding at the same moment take turns. Pull, stage only this focus's files and appends, commit as `ground [f21-plumbing-quotes] — summary`, push.
7. **Report in one line.** *"Grounded f21: 3 files · a1b2c3d"*, or *"Saved."* in a non-technical build.

## Who may commit

- **Grounding is the sphere's authorized commit.** It counts as approved when the human asks for it, or when a standing approval the human set up runs it: a scheduled end-of-day ground, or an agent delegated to *"ground your own work as you go"*, scoped to what it holds. Nothing else commits sphere state.
- **The sphere's repository is its own.** Grounding never commits to a project being worked on. A code repository keeps its own rules and its own approvals.

## Aiming undo and revert

Commits from different foci interleave. Every commit names its node, so:
- **`undo` in a focus** reverses that focus's last ground, never another's.
- **`revert` to a focus's earlier ground** reverses that focus's commits after it.
- **Reverting the whole sphere** to a point in time reaches into every focus: every foreground focus grounds or detaches first, and the human confirms.

Each kind of file is reversed the way it's written: current state is reversed; appended history entries are never removed (an entry is appended saying what was reversed and why), though a history file created or deleted whole goes with its node; a reverted fact or lens change becomes a proposal to restore the old version; generated files are rebuilt.

## When the state isn't what was expected

- **"Clean" is scoped to the focus.** Other foci's unsaved files in the folder are normal. What stops an operation is a changed file **no open focus holds**: stop, show it, and ask: save it here, set it aside, or leave it. Never stage it along with this focus's work, and never resolve it alone. It may be the human's.
  - Show tracked files apart from new ones (new files are often scratch).
- **Only what this focus holds is staged,** plus its appends. Never everything in the folder. *Why:* staging everything is how one focus's ground quietly commits another's half-finished work, under the wrong name.
- **A failing commit check is never bypassed.** Fix the cause, or show the human. If a check really is wrong for this one case, the escape is an exception the human names and the sphere records, scoped to that check alone. A blanket skip of every check is never the way.

## When / do

| When | Do |
|---|---|
| The human asks to save, ground, or *lock it in* | Run `ground` for the focus this window is attached to. If it isn't attached to one, ground into [main](../focus/focus-nodes.md#main-the-root-focus) |
| The human asks what's changed, or what happened today | Run `peek`. Report, and write nothing |
| The human asks to undo | Say what this focus's last ground was and what undoing it reverses. Then add the reversing commit |
| The human asks to go back to an earlier point | Show the recent grounds and let the human pick one. Never guess which. Then add the reversing commit |
| An operation finds a changed file no open focus holds | Stop. Show it and ask (above). Fire `dirty-detected` |
| A commit check fails | Fix the cause, or show the human. Never skip the check |
| A composite runs (`detach`, `close`) | Run each part in order. If one fails, stop and say which, before going further |

## Works with

- [focus-nodes](../focus/focus-nodes.md) adds the verbs a human uses and what a focus writes at each ground. This frame owns the moves; that one owns the record.
- [check-shared-state](check-shared-state.md) covers what `ground` does when the pull brings changes.
- [without-git](without-git.md) covers what changes when there's no git underneath.
- [propose-dont-decide](../human-is-highest/propose-dont-decide.md) still applies inside a ground: new facts and rules are proposed, not written.

## Senses

| Sense | Fires when |
|---|---|
| `focus-grounded` | a ground commits |
| `dirty-detected` | an operation found a changed file no open focus holds |
