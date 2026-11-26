---
frame: worktree-lanes
lens: [workflow]
derives_from: [workflow@1]
version: 1
version_note: First draft. A predictable home for worktrees (default layout), dev and review modes, the main lane as an option, the pre-flight before any switch, cleaning up after a merge.
status: drafting
updated: 2026-11-22
sharing: public
reads: [core/user, layers/work, layers/focus]
writes: [core/user]
protocol: []
---

# Worktree lanes

**Applies to:** setting up a branch to build on, bringing one in to review, and any switch of branch or worktree.

**Several branches in flight, across several worktrees:** how does the human work on and review each without losing track, or yanking a branch out from under another window?

## Where worktrees live (a default layout)

_A starting layout. If the human keeps worktrees elsewhere, record where in the codebase's entry in `core/user/codebases.md` and use that._

**One predictable home per repository,** beside it:

```
the-app/                 the main checkout
the-app-worktrees/       every other worktree for this repository
├── fix-login-timeout/
└── add-export/
```

The same shape for every repository makes worktrees easy to find, and easy to clean up.

## Two modes

| Mode | Sets up |
|---|---|
| **Dev** | A worktree for building on a branch: a clean tree, the right branch, ready to write code. Agent work runs here, never in the main checkout ([harness-engineering](../agentic-engineering/harness-engineering.md#run-agent-written-code-in-a-sandbox)) |
| **Review** | The branch where the human can read it in their editor, with no intent to build |

The human says which; the sphere does the worktree and branch mechanics to match.

## The main lane (an option)

_For people who keep their editor open on one checkout. Many prefer a window per worktree; then skip this._

**One checkout is the main lane,** the one the editor stays open on. To review a branch, the sphere brings it into the main lane, so the editor sees it without being re-pointed; when the review is done, the branch goes back out to its own worktree.

## The pre-flight, before every switch

**Always, whatever the mode:**

- **Uncommitted changes: stop.** Never switch over them. Show what's changed; the human decides.
- **Clean, but on a branch you didn't expect: say so and wait.** Another window may be in the middle of something there ([check-shared-state](../continuity/check-shared-state.md)).
- **Never force past a guard,** and never skip the hooks.

## Cleaning up after a merge

**Worktrees pile up, and each holds a full checkout** (often with its dependencies and build output too). When the work is done, its worktree is just disk space.

- **When a branch's pull request merges** (the human says so, the roll-up shows it, or its work item is marked done), offer to remove its worktree and its local branch, in a line.
- **At the weekly look, a sweep:** the worktrees whose branches have merged or been dropped, with how much space each takes. One yes can clear them all, or the human picks.
- **The pre-flight still holds.** A worktree with uncommitted or unpushed changes is never removed: say what's there, and leave it to the human.
- **Removing waits for a yes,** every time ([destructive-actions-ask](../human-is-highest/destructive-actions-ask.md)).

## When / do

| When | Do |
|---|---|
| *"Set me up to work on …"* | Dev mode: a clean worktree on the right branch, in the human's layout |
| *"Let me look at …"*, *"bring it in to review"* | Review mode; with a main lane, bring the branch into it |
| Any switch of branch or worktree | The pre-flight first. Stop on uncommitted changes; say so and wait on an unexpected branch |
| A branch's pull request merges, or the branch is dropped | Offer to remove its worktree and local branch. Never one with uncommitted or unpushed changes. Removing waits for a yes |
| The weekly look | List worktrees whose branches merged or were dropped, with their size; offer to clear them |

## Works with

- [pr-runbook](pr-runbook.md): review mode usually comes just before a walkthrough.
- [check-shared-state](../continuity/check-shared-state.md): why an unexpected branch means wait.
