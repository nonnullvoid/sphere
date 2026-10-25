# State

_Status: draft 2, for review._ How a sphere stays consistent across sessions: what a session is, what `ground` and `resume` do, and how the session system grows from simple to advanced without breaking anyone along the way.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

---

## The idea

A sphere is a **state machine**. At any moment its files are in one consistent state. A session is a bounded window of work that starts from a known state and ends by **grounding**: compacting what happened back into the sphere so the next session can pick up cold.

The human lives in real time; the sphere lives on its last grounded state. Anything not grounded is, from the sphere's point of view, not yet true. This is deliberate. It gives the human a clear moment of review before the work becomes the sphere's memory.

---

## The two verbs

### `ground` — **proven**

Ending a session, or reaching a safe point inside one, the sphere:

1. **Compacts** working state into its records: the work's `progress.md` gets what happened and what's next, and new facts or rules are *proposed* rather than written automatically (see [knowledge](knowledge.md), [guardrails](guardrails.md)).
2. **Reconciles** the session record (see [The session registry](#the-session-registry)).
3. **Commits** if git is present: stages only the files this session touched, never everything, with a message in the form `ground [scope] — summary`.

Grounding is the sphere's authorized commit. Two things count as approval: the human asking to ground, or a **standing approval** the human set up, such as a scheduled end-of-day ground. Nothing else commits sphere state.

### `resume` — **proven**

Starting a session on existing work, the sphere reads that work's `progress.md` and the session record, and says where things stand and what's next. A good ground is measured by how well a cold resume works: a new session, with no memory of the last one, should be able to continue.

---

## Session levels

Sessions come in two levels. Every sphere starts at level 1. Level 2 is opt-in.

The rule behind this: **nobody meets an unfinished mechanism by accident.** Features with sharp edges only reach people who chose them.

### Level 1 — simple sessions (the default) — **proven**

- **One branch for the whole sphere**, shared by every session: all sessions commit to `main`. (Branches per session are what level 2 adds.) Git is always present, but at core profile it's **invisible**: the tooling makes every commit and the human never sees the word.
  - **Same machine:** sessions share one working folder and can see each other's uncommitted edits. Ground stages only what *this* session touched, so it never commits another session's half-finished work.
  - **Several devices:** each device has its own copy of `main`. Ground pulls before committing and pushes after. If two devices changed the same shared file, the conflict surfaces there and is resolved by the tooling or the AI, never shown raw at core profile.
- A **session log** with one file per session in `core/records/sessions/`, named `YYYY-MM-DD-HHMM-<slug>.md`. Each file says which work the session touched and summarizes what happened.
- `ground` = compact + session file + commit. Ground also adds a one-line pointer from the work's `progress.md` to the session file. `resume` = read the work's `progress.md`.
- No worktrees, no branches per session, no tree vocabulary.

**Why one file per session:** two sessions never write the same log file, so the log can't conflict, with or without git. The folder listing is the registry.

#### Conflict-avoiding layout — _decided, not yet exercised_

Concurrent sessions are normal: two windows, or a laptop and a phone. The layout keeps them out of each other's way:

- **Per-session and per-work files** take most writes: session files and each work's `progress.md`.
- **Shared files** (the work index, principles, profile) are only written at ground, and only after re-reading them, so a session never overwrites changes it hasn't seen.
- When a conflict still happens, **the tooling or the AI resolves it**. At core profile a raw merge conflict never reaches the human.

#### Without git — fallback only

Git is the default because it gives history, undo and merges. Without git, these edge cases have no safety net:

| Edge case | What goes wrong |
|---|---|
| Two sessions open at once | Last writer wins on shared files; the other session's changes are lost silently |
| One sphere synced to two devices through a cloud folder | The sync service creates conflict copies or picks one version |
| A crash halfway through a ground | Some files written, some not, with no record of which |
| A bad ground | No history, so it can't be undone |
| The human edits a file while a session is open | The session's next write overwrites the edit |

A gitless sphere is supported only as **one session at a time**. A lock file is written at session start, and a second session opens read-only with a warning. Locks can go stale after a crash, and they reach other devices slowly through cloud sync. That's why this is a documented fallback, not the default. — _unexercised_

### Level 2 — the session tree (opt-in) — **advanced**

For technical users running several streams of work in parallel.

- Each session is a branch in a tree, usually with its own worktree.
- Three verbs instead of one:
  - **ground**: commit this session's state (as at level 1).
  - **sync**: ground, then merge this session's state up into its parent session. Sync is a superset of ground, and it's **not** an ending: the child keeps going.
  - **close**: finish the session. Its final state merges up and it leaves the active tree.
- A parent session can hold many children and act as the integration point for their work.
- **Sessions talk through their parent, never sideways.** A child that needs something from a sibling asks the parent, which relays. Direct sibling messaging was tried and caused sessions to take over each other's work.

Level 2 ships with its known sharp edges documented, not hidden. See [Known sharp edges](#known-sharp-edges-level-2).

### Hidden until needed

Nested sessions, parent/child sync and cross-session asks are **off by default** and absent from the default documentation path. When the sphere sees a need, for example the human working on two separate pieces of work in parallel, it proposes turning level 2 on and explains what changes. The human decides.

### No migration between levels

A level-1 log entry is a valid depth-1 node of a session tree. Moving to level 2 only turns features on; nothing is rewritten. Moving back means simply not opening child sessions. _(Same principle as work tracking: depth is a dial. See [work](work.md).)_

---

## The session registry

The record of which sessions exist and what they're for. Three kinds of truth, each with exactly one home:

| Kind | Examples | Home | Who writes it |
|---|---|---|---|
| **Facts** | the session exists, its branch, its parent, when it last grounded | git | computed when needed, never stored in the registry |
| **Meaning** | what the session is for, its status (paused, abandoned, done), why it's linked to another | the registry | the AI drafts it, the human confirms |
| **Runtime state** | is it running right now, what's mounted where | a disposable state file, never committed | the tooling |

**Where liveness lives (level 2):** each running session has a heartbeat file at `surface/state/sessions/<id>.json` holding `last_seen`. Any sphere command updates it, and a session counts as alive while `last_seen` is within a threshold (30 minutes as a starting point). It's one file per session, so heartbeats never contend. At ground, reconciliation cross-checks heartbeats against git activity: "S41's heartbeat says alive, but it hasn't touched anything in 3 days. Still running?" — _decided, not yet exercised_

**Why three homes:** when a fact is stored in two places, they drift apart. Storing facts only in git, and only meaning in the registry, shrinks what can drift to two cases, and both surface as questions at ground:

> S41 has grounds but no registry entry. Add it — what's it for?
> S38 is marked active, but its branch is gone. Closed, or abandoned?

**Reconciliation runs in the `ground` tooling, not as a habit.** A step that depends on someone remembering to do it will eventually be skipped. Mismatches are batched into one short prompt per ground.

At level 1 the session log *is* the registry, and reconciliation is a single check: "this ground has no session note. Add one?"

**Runtime state is never committed.** Committing fast-changing state causes merge conflicts and makes the committed record disagree with reality. If the state file is deleted, the tooling rebuilds it.

---

## Commits

- **Stage only what the session touched.** Never stage everything in the folder. Unrelated changes may belong to another session or to the human. — **proven**
- **One sphere repo, separate from code repos.** Sphere state has its own history; grounding the sphere never commits to the project being worked on. — **proven**
- **Generated files are caches.** Anything that can be regenerated (for example a startup bundle) is rebuilt when needed rather than committed, so it can't conflict on merge. — _decided, not yet exercised_
- **Flatspace surface** — **advanced**: rendered views (projections) can live on a separate branch that every session sees at its latest version, so a view never depends on which session branch you're on.

---

## Known sharp edges (level 2)

Documented so people who opt in know what they're choosing. Each will be addressed by the session tooling before level 2 ships.

| Sharp edge | What happens | Planned fix |
|---|---|---|
| Silent fallback to main | a session meant for a worktree ends up working on the main branch | tooling refuses to start the session instead of falling back |
| Registry drift | sessions exist in git with no registry entry, or entries outlive their branches | three homes + reconciliation at ground |
| Detached HEAD | grounds land on no branch and can be lost | ground refuses or repairs before committing |
| Generated-file conflicts | a committed startup bundle conflicts on nearly every sync | treat it as a cache: regenerate, don't commit |
| Worktree shell limits | some harnesses restrict multi-line shell inside worktree sessions | under investigation; root cause first, not workarounds |

---

## Open questions

1. **The liveness threshold.** 30 minutes is a starting point; tune it from real use.
2. **Conflict resolution at core profile.** What the tooling resolves by itself, and what it hands to the AI. To be designed with the session tooling.
3. **Git inside cloud-synced folders.** A git repository inside a cloud-synced folder can be damaged when the sync service rewrites files under `.git/`. Decide whether builds warn about this or keep git data outside the synced folder.
