# State

_Status: draft 3, for review._ How a sphere stays consistent across sessions: what state it's in, what each operation does to that state, what a session is and why it exists, and how sessions grow from simple to advanced without breaking anyone along the way.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

---

## The idea

A sphere is a **state machine**. At any moment its files are in one consistent state, and every operation is a defined move between states. Git is the substrate underneath: it makes each move durable, reviewable and reversible. — **proven**

| State | Means |
|---|---|
| **Bootstrap** | The sphere is being created. Its structure doesn't exist yet. |
| **In session** | Work in progress: uncommitted changes, a conversation shaping the sphere. |
| **Grounded** | A clean state, saved. Safe to stop and pick up cold later. Every grounded state is a commit. |

After bootstrap, a sphere moves between *in session* and *grounded* for the rest of its life.

**The human lives in real time; the sphere lives on its last grounded state.** Anything not grounded is, from the sphere's point of view, not yet true. This is deliberate. It gives the human a clear moment of review before work becomes the sphere's memory.

---

## Why sessions exist — **proven**

An AI's working context is finite, and it degrades as it fills: long conversations get worse at paying attention. The cure is to **close a session at a natural stopping point and start fresh.** What stops people doing that is the fear of losing what the old session knew.

**The sphere is the answer to that fear.** The better a sphere captures context when it grounds, the less there is to lose by closing, and the earlier it's safe to close. *How much you hesitate to close a session is a measure of how well your sphere captures.* Sessions and the sphere work as partners: sessions create the pressure to capture, and the sphere pays down the cost of closing.

Sessions also give:
- **Compartments.** One clean container per thread of work, for the human's head as much as the AI's.
- **Delegation.** A fresh context, handed one focused job.
- **Parallelism.** Several streams of work at once, without contaminating each other.

### A session is not a window

Two things are easy to confuse:

| | What it is | Lasts |
|---|---|---|
| **Sphere-session** | An engagement with the work: its intention, its progress, its record | Until it's closed. It survives any window. |
| **Session window** | The app or terminal you're attached through right now | Until you close it |

It's like a terminal multiplexer over a remote connection: the session lives on, and windows attach and detach. A window whose context has degraded can be closed and a fresh one attached to the same session, with nothing lost. This is also why a sphere is **independent of any one AI tool:** the session is the sphere's, and any harness can attach to it.

### Work is the line; sessions are the dots

A piece of [work](work.md) is a straight line from start to finish. Sessions are dotted lines along it, each one picking up some of the work and putting it down. One session can touch several pieces of work, and one piece of work spans many sessions.

---

## Operations — **proven**

Every operation is a transition with a contract: what it changes, whether it commits, what it preserves.

| Operation | Moves | Commits? |
|---|---|---|
| `ground` | in session → grounded | **Yes** |
| `resume` | opens work and briefs where it stands | No |
| `peek` | nothing (read-only status) | No |
| `close` / `park` | grounds, then takes the work out of focus | **Yes** (grounds first, so nothing is left dirty) |
| `checkpoint` | saves the current state as a named point | **Yes** |
| `history` | nothing (shows recent transitions) | No |
| `revert` | back to an earlier grounded state | **Yes**, as a new commit |
| `undo` | back to the previous grounded state | **Yes**, as a new commit |

- **Read-only operations change nothing** and make no commit.
- **Composite operations declare their parts.** `resume` = open + orient. `close` = ground + unfocus. The composite's contract is the union of its parts.

### Safe experimentation — **proven**

Every grounded state is a checkpoint, so **trying something is cheap: undoing it is cheap.** `revert` and `undo` never destroy anything. They add a new commit that reverses an earlier one, and the history stays whole. This is one of the main reasons a sphere uses git at all.

### When the state isn't clean — **proven**

If an operation expects a clean state and finds uncommitted changes it didn't make, it **stops, shows them, and asks:** commit them, set them aside, or abort. It never resolves this on its own. The changes may be the human's, or another session's.

A failing commit check is never bypassed. The sphere fixes the cause, or surfaces it to the human.

### `ground` — **proven**

Ending a session, or reaching a safe point inside one, the sphere:

1. **Compacts** working state into its records. The work's `progress.md` gets what happened and what's next. New facts and rules are *proposed* rather than written automatically (see [knowledge](knowledge.md), [guardrails](guardrails.md)).
2. **Writes the session file** (see [The session file](#the-session-file--proven-shape)), creating it on the session's first ground.
3. **Reconciles** the session record (see [The session registry](#the-session-registry)).
4. **Commits,** staging only the files this session touched, with a message in the form `ground [scope] — summary`.

Grounding is the sphere's authorized commit. Two things count as approval: the human asking to ground, or a **standing approval** the human set up, such as a scheduled end-of-day ground. Nothing else commits sphere state.

### `resume` — **proven**

Starting a session on existing work, the sphere reads that work's `progress.md` and the latest session file, and says where things stand and what's next. **A good ground is measured by how well a cold resume works:** a new session, with no memory of the last one, should be able to continue.

---

## Session levels

Sessions come in two levels. Every sphere starts at level 1. Level 2 is opt-in.

The rule behind this: **nobody meets an unfinished mechanism by accident.** Features with sharp edges only reach people who chose them.

### Level 1 — simple sessions (the default) — **proven**

- **One branch for the whole sphere**, shared by every session: all sessions commit to `main`. (Branches per session are what level 2 adds.) Git is always present, but for a non-technical human it's **invisible**: the tooling makes every commit and the human never sees the word.
  - **Same machine:** sessions share one working folder and can see each other's uncommitted edits. Ground stages only what *this* session touched, so it never commits another session's half-finished work.
  - **Several devices:** each device has its own copy of `main`. Ground pulls before committing and pushes after. A conflict between devices is handled as described in [Conflicts](#conflicts--decided-not-yet-exercised).
- **One file per session** in `core/records/sessions/`, named `YYYY-MM-DD-HHMM-<slug>.md`. Two sessions never write the same file, so the log can't conflict. The folder listing is the registry.
- **A session record is created at its first ground.** A window that never grounds (a quick question, a scratch experiment) leaves nothing behind. **Throwaway windows aren't sessions,** and at level 1 that happens by construction, with no promotion step. — _decided, not yet exercised_
- No worktrees, no branches per session, no tree vocabulary.

#### The session file — **proven** (shape)

The session file is the session's handoff to its own future self. Each ground appends a short checkpoint, newest first:

```markdown
## 2026-10-24 16:17 — grounded

**Did:** Drafted the state chapter; resolved the two conflicts with the human.
**Decided:** Session records are created at first ground; content conflicts are proposed, never silent.
**Next:** Fidelity pass on the work chapter.
**Pointers:** work: sphere-v2 → progress.md · commit a1b2c3d
```

- **Did, Decided, Next, Pointers.** *Decided* holds the judgment calls that are expensive to re-derive. *Next* is the single most useful line for a cold start.
- **Pointers, not copies.** The session file points at the work's `progress.md` and the commit. It never duplicates them.
- **Two axes, complementary.** A work's `progress.md` is the *work's* history ("what happened to the website relaunch"). The session file is the *session's* handoff ("what was this session in the middle of"). A session that touches three pieces of work writes three progress entries and one session file.

#### Conflict-avoiding layout — _decided, not yet exercised_

Concurrent sessions are normal: two windows, or a laptop and a phone. The layout keeps them out of each other's way:

- **Per-session and per-work files** take most writes: session files and each work's `progress.md`.
- **Shared files** (the work index, principles, the human's persona) are only written at ground, and only after re-reading them, so a session never overwrites changes it hasn't seen.

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

For technical users running several streams of work in parallel. Each session is a branch in a tree, with its own worktree.

**Starting sessions explicitly.** At level 2 a session is started on purpose (`start session …`), because a branch is cut up front. Windows that are never started as sessions stay untracked.

**References.** Each session gets a short reference made of a number and a keyword or two from its intention: `S12-payments-rev`, never a bare `S12`. A human can attach with the exact reference, or with plain words ("continue the payments one"). An ambiguous match shows the candidates rather than guessing.

**Two ways a child session is born:**

| | When | Who runs it |
|---|---|---|
| **Spawn** | A session seeds a child with a *starter prompt*, to be picked up later, or by an agent | Whoever resumes it, cold |
| **Open a sub-session** | The human, mid-session, opens a new window to go deep on a slice | The human, now |

Both write the same parent ↔ child link, and **the parent is told:** *"Child S12-rounding-bug opened: chase the rounding bug."*

**Attaching is resuming.** "Resume," "attach" and "continue session" are one operation. Every phrasing runs the full cold start: switch to the session's branch and worktree, load its intention, starter prompt and last state, read its session file, register the window. There's no lighter path that identifies a session without loading it.

**Three verbs:**
- **ground:** commit this session's state, on its own branch.
- **sync:** ground, then merge this session's state up into its parent. **Not an ending.** The session and its branch stay alive.
- **close:** merge up and finish. Only on an explicit signal that *this* session is done. **When it's unclear whether the human means sync or close, sync.** Closing is the one step that isn't casually reversible.

**After a clean close,** the sphere asks once, right then, whether to delete the merged branch and its worktree. It uses a safe delete that refuses to remove unmerged work. On a merge conflict, it doesn't ask; it surfaces the conflict first.

**Branch names are part of the contract.** A child's branch is its parent's full branch name plus its own reference, joined with a dot (`session/S4-launch.S5-rev-fix`), so the branch list reads as the tree. A dot, unlike a slash, lets a name sit beside its parent's in git without nesting under it.

**Sessions talk through their parent, never sideways.** A child that needs something from a sibling asks the parent, which relays. Direct sibling messaging was tried and caused sessions to take over each other's work. Across a parent ↔ child link, three verbs:

| Verb | Does | Changes the other session? |
|---|---|---|
| **inspect** | Read the other session's record | No |
| **request** | Ask it to ground, close or hand over its window | Only if accepted. **A request is an ask, never a command.** Today, only reversible requests exist. |
| **share** | Offer it a change | Adds it as a reviewable change; never overwrites |

How far an unattended agent-session may act on requests by itself is a question of autonomy, deferred to a later version.

Level 2 ships with its known sharp edges documented, not hidden. See [Known sharp edges](#known-sharp-edges-level-2).

### Hidden until needed

Nested sessions, parent/child sync and cross-session asks are **off by default** and absent from the default documentation path. When the sphere sees a need, for example the human working on two separate pieces of work in parallel, it proposes turning level 2 on and explains what changes. The human decides.

### No migration between levels

A level-1 session file is a valid depth-1 node of a session tree. Moving to level 2 only turns features on; nothing is rewritten. Moving back means simply not opening child sessions. _(Same principle as work tracking: depth is a dial. See [work](work.md).)_

---

## Session lifecycle and liveness — **proven**

A sphere has no birth and death. A session does:

```
ready ──attach──▶ working ──ground──▶ grounded ──close──▶ closed
                     ▲                    │
                     └────── resume ──────┘
```

| Stage | Means |
|---|---|
| **ready** | Created and seeded (intention, starter prompt), never attached. Level 2 only. |
| **working** | Attached; changes in progress. |
| **grounded** | Clean and saved. Safe to detach and resume cold. |
| **closed** | Done, merged up, archived. |

**Liveness is separate from stage.** Stage belongs to the session. Liveness belongs to the windows attached to it: **live** (recently active), **stale** (gone quiet: the window closed or the laptop crashed), or **detached** (no window, which is normal for a grounded session waiting to be resumed).

The rules that fall out:

- **Ground before detaching.** A window should ground before it goes away, so a session rests *grounded and detached* (parked, safe), never *working and detached* (orphaned).
- **How serious a stale session is depends on dirtiness, not on how long it's been quiet.** A stale *working* session may have uncommitted work at risk: offer to recover it, never discard it. A stale *grounded* or *closed* session is harmless bookkeeping: just clear the window entry.
- **Closing ends attachment.** `close` detaches any window still attached.

**Heartbeats** — _decided, not yet exercised_. Each running session has a heartbeat file at `surface/state/sessions/<id>.json` holding `last_seen`. Any sphere command updates it, and a session counts as live while `last_seen` is within a threshold (30 minutes as a starting point). It's one file per session, so heartbeats never contend. At ground, reconciliation cross-checks heartbeats against git activity: *"S41's heartbeat says live, but it hasn't touched anything in 3 days. Still running?"*

## Recognizing session commands — **proven**

**Session phrasing is a command, not prose.** "Start a new session for the website" means *start a session*. It doesn't mean "I'm about to work on the website." The sphere checks session-shaped phrasing against its command vocabulary before reading it as conversation. Missing this once meant several turns of work done outside any session.

**Every write to a session record reports back in one line** (*"session S12-payments-rev working"*), so a session that was meant to start but didn't is visible on the very next turn, not several turns later. For a non-technical human, the same tripwire is a plain phrase, or silence when nothing changed.

---

## The session registry

The record of which sessions exist and what they're for. Three kinds of truth, each with exactly one home:

| Kind | Examples | Home | Who writes it |
|---|---|---|---|
| **Facts** | the session exists, its branch, its parent, when it last grounded | git (and, at level 1, the session files) | computed when needed, never duplicated |
| **Meaning** | what the session is for, the work it touches, its starter prompt, its status (paused, abandoned, done), why it's linked to another | the registry | the AI drafts it, the human confirms |
| **Runtime state** | is it live right now, what's mounted where | a disposable state file, never committed | the tooling |

**Why three homes:** when a fact is stored in two places, they drift apart. Storing facts only in git, and only meaning in the registry, shrinks what can drift to two cases, and both surface as questions at ground:

> S41 has grounds but no registry entry. Add it — what's it for?
> S38 is marked active, but its branch is gone. Closed, or abandoned?

**Reconciliation runs in the `ground` tooling, not as a habit.** A step that depends on someone remembering to do it will eventually be skipped. Mismatches are batched into one short prompt per ground.

At level 1 the session files *are* the registry, and reconciliation is a single check: *"this ground has no session note. Add one?"*

**Closed sessions move to an archive** record, so the live list stays short. Their session files stay where they are, as history, and their references keep meaning something.

**Runtime state is never committed.** Committing fast-changing state causes merge conflicts and makes the committed record disagree with reality. If the state file is deleted, the tooling rebuilds it.

## Session type — _decided, not yet exercised_

A session can carry a **type**: coding, brainstorming, planning, meeting review, research, sphere authoring. The type is a **hint for what to load up front, never a gate.** Everything stays reachable. If a coding session suddenly needs the meeting frames, they load on demand at the cost of one extra read. The type is declared by the human (preferred), inferred from how the session opens, and changeable at any time. Which frames each type warms up is learned from use. _(Belongs with loading efficiency; it moves there when that chapter exists.)_

---

## Commits

- **Stage only what the session touched.** Never stage everything in the folder. Unrelated changes may belong to another session or to the human. — **proven**
- **One sphere repo, separate from code repos.** Sphere state has its own history; grounding the sphere never commits to the project being worked on. — **proven**
- **Generated files never cause merge pain.** Machine-only caches (like the startup bundle) are rebuilt when needed and never committed. Human-facing views (like the work index) are committed so people can read them. See [registries](registries.md#committed-views-and-caches--decided-not-yet-exercised). — _decided, not yet exercised_
- **Ground commits the source; views follow.** Ground commits the sphere's source files once. Surface views are refreshed from them, never committed as a second, coupled change.
- **Flatspace surface** — **advanced**: rendered views can live on a separate, always-latest branch that every session sees, so a view never depends on which session branch you're on. A single-timeline sphere doesn't need this, and pays nothing for it.

## Conflicts — _decided, not yet exercised_

Two kinds, handled differently:

- **Conflicts in views** (generated or AI-maintained files) are **rebuilt**, from the merged sources, automatically. No human needed, since the merged sources produce the right view.
- **Conflicts in content** (the human's own files: their work, their knowledge, their lenses) are **never resolved silently.** The AI proposes a resolution and the human confirms it. For a non-technical human that happens in plain words, never as a raw conflict: *"Your laptop and your phone both changed your grocery list. Keep both versions' items?"*

---

## Known sharp edges (level 2)

Documented so people who opt in know what they're choosing. Each will be addressed by the session tooling before level 2 ships.

| Sharp edge | What happens | Planned fix |
|---|---|---|
| Silent fallback to main | a session meant for its own worktree ends up working on the main branch, and its branch silently goes stale | the shared root is never checked out to a session branch; a commit guard refuses session work committed straight to main; a narrow, audited override exists for deliberate exceptions, instead of bypassing checks |
| Surface inside worktrees | the always-latest surface can only be checked out once | each session worktree links to the one real surface instead of checking out its own |
| Registry drift | sessions exist in git with no registry entry, or entries outlive their branches | three homes + reconciliation at ground |
| Detached HEAD | grounds land on no branch and can be lost | ground refuses or repairs before committing |
| Generated-file conflicts | a committed startup bundle conflicts on nearly every sync | caches aren't committed; committed views are rebuilt on conflict |
| Worktree shell limits | some harnesses restrict multi-line shell inside worktree sessions | under investigation; root cause first, not workarounds |

---

## Open questions

1. **The liveness threshold.** 30 minutes is a starting point; tune it from real use.
2. **Git inside cloud-synced folders.** A git repository inside a cloud-synced folder can be damaged when the sync service rewrites files under `.git/`. Decide whether builds warn about this or keep git data outside the synced folder.
3. **The session type list.** Is the starter set right, and should a sphere learn its own types?
