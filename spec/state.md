# State

_Status: draft 1, for review._ How a sphere stays consistent across sessions: what a session is, what `ground` and `resume` do, and how the session system grows from simple to advanced without breaking anyone along the way.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

---

## The idea

A sphere is a **state machine**. At any moment its files are in one consistent state. A session is a bounded window of work that starts from a known state and ends by **grounding**: compacting what happened back into the sphere so the next session can pick up cold.

The human lives in real time; the sphere lives on its last grounded state. Anything not grounded is, from the sphere's point of view, not yet true. This is deliberate. It gives the human a clear moment of review before the work becomes the sphere's memory.

---

## The two verbs

### `ground` — **proven**

Ending a session, or reaching a safe point inside one, the sphere:

1. **Compacts** working state into its records: the work's journal gets what happened and what's next, and new facts or rules are *proposed* rather than written automatically (see [knowledge](knowledge.md), [guardrails](guardrails.md)).
2. **Reconciles** the session record (see [The session registry](#the-session-registry)).
3. **Commits** if git is present: stages only the files this session touched, never everything, with a message in the form `ground [scope] — summary`.

Grounding is the sphere's authorized commit. A human asking to ground is the approval; nothing else commits sphere state.

### `resume` — **proven**

Starting a session on existing work, the sphere reads that work's journal and the session record, and says where things stand and what's next. A good ground is measured by how well a cold resume works: a new session, with no memory of the last one, should be able to continue.

---

## Session levels

Sessions come in two levels. Every sphere starts at level 1. Level 2 is opt-in.

The rule behind this: **nobody meets an unfinished mechanism by accident.** Features with sharp edges only reach people who chose them.

### Level 1 — simple sessions (the default) — **proven**

- One branch, or no git at all.
- A flat **session log**: one entry per session, saying which work it touched and a one-line summary.
- `ground` = compact + log entry + commit. `resume` = read the work's journal.
- No worktrees, no branches per session, no tree vocabulary.
- At core profile, git is never mentioned. Grounding happens silently in the background, and the human only sees their work.

**Without git**, level 1 still works: ground writes the log entry and the journal, so continuity holds. What's lost is history and diffs. _(Inferred behavior; not yet exercised without git.)_

### Level 2 — the session tree (opt-in) — **advanced**

For technical users running several streams of work in parallel.

- Each session is a branch in a tree, usually with its own worktree.
- Three verbs instead of one:
  - **ground**: commit this session's state (as at level 1).
  - **sync**: merge this session's grounded state up into its parent session. Sync is **not** an ending; the child keeps going.
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

1. **Where the level-1 session log lives** in a build (`core/records/sessions.md` is the obvious candidate). Decide in the base build.
2. **Liveness rule for level 2:** "any command counts as alive" is the current practice. Confirm before it's written down as spec.
3. **Should `sync` require a ground first,** or ground implicitly? Current practice should decide this.
4. **Git-optional level 1** has not been exercised. Keep it in the spec as a design goal, or mark it unexercised until a build tries it?
