# State

How a sphere stays consistent: what state it's in, what each operation does to that state, why windows end and the thread survives them, and how several foci and devices share one sphere. What a focus node is, and how it's opened, attached and closed, is in [focus](focus.md).

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

---

## The idea

A sphere is a **state machine**. At any moment its files are in one consistent state, and every operation is a defined move between states. Git is the substrate underneath: it makes each move durable, reviewable and reversible. — **proven**

| State | Means |
|---|---|
| **Bootstrap** | The sphere is being created. Its structure doesn't exist yet. |
| **Working** | Changes in progress, not yet saved. |
| **Grounded** | A clean state, saved. Safe to stop and pick up cold later. Every grounded state is a commit. |

After bootstrap, a sphere moves between *working* and *grounded* for the rest of its life.

**The human lives in real time; the sphere lives on its last grounded state.** Anything not grounded is, from the sphere's point of view, not yet true. This is deliberate. It gives the human a clear moment of review before work becomes the sphere's memory.

### Two levels — _unexercised_

With several [focus nodes](focus.md) open at once, the machine has two levels:

| Level | States | Where it lives |
|---|---|---|
| **The sphere** | always grounded: its state is its latest commit | `main` |
| **Each focus node** | working ↔ grounded | its held files, and its commits |

**The sphere's state is the latest commit, never the working folder.** The folder can hold several foci's unfinished work at once. None of it is true until it's grounded. With one focus open, the two levels are the same thing, which is how a sphere has run in daily use.

---

## Why windows end, and why that's fine — **proven**

An AI's working context is finite, and it degrades as it fills: long conversations get worse at paying attention. The cure is to **close a window at a natural stopping point and attach a fresh one.** What stops people doing that is the fear of losing what the old window knew.

**The sphere is the answer to that fear.** The better a sphere captures context when it grounds, the less there is to lose by closing, and the earlier it's safe to close. *How much you hesitate to close a window is a measure of how well your sphere captures.* Windows and the sphere work as partners: windows create the pressure to capture, and the sphere pays down the cost of closing.

What carries the thread from one window to the next is the [focus node](focus.md) the window was attached to: its intention, and the memory each ground adds to it. Focus nodes also give:
- **Compartments.** One clean container per pursuit, for the human's head as much as the AI's.
- **Delegation.** A fresh context, handed one focused job, as a child focus.
- **Parallelism.** Several pursuits at once, without contaminating each other.

---

## Operations — **proven**

Every operation is a transition with a contract: what it changes, whether it commits, what it preserves. Each one acts on one focus node; the verbs people use for them are in [focus](focus.md#opening-attaching-and-closing).

| Operation | Moves | Commits? | Reads | Writes |
|---|---|---|---|---|
| `ground` | working → grounded. Can name the point (*"ground, call it before-restructure"*) | **Yes** | this focus's changes | its records, then one commit |
| `attach` (resume) | brings a focus to the foreground and briefs where it stands | No | the node, its history, what it holds | nothing |
| `peek` | nothing: shows what's changed and unsaved, and recent history | No | uncommitted changes, recent grounds | nothing |
| `detach` | grounds, then sends the focus to the background | **Yes** (the ground step) | as `ground` | as `ground` |
| `close` | grounds, then ends the focus | **Yes** (the ground step) | as `ground` | as `ground`, plus the node's status and its move to `archived/` |
| `undo` | back to this focus's previous grounded state | **Yes**, as a new commit | the focus's last commit | a reversing commit |
| `revert` | back to an earlier grounded state, named or recent | **Yes**, as a new commit | history | a reversing commit |

- **Read-only operations change nothing** and make no commit.
- **Composite operations declare their parts.** `attach` = find + orient. `detach` = ground + background. `close` = ground + end. The composite's contract is the union of its parts. If a part fails, the composite stops and says which.
- **There's no separate sync.** Ground is the one way state reaches the sphere. With several devices, ground pulls before committing and pushes after, so devices catch up as part of grounding. Merging a child into its parent isn't a step either: a child reports up as part of its own ground.

### The words are the human's — _decided, not yet exercised_

The operation names are the spec's. What the human says and hears belongs to the build and to them, as with [work's labels](work.md#labels-are-a-light-judgment):

| Build | Says | Hears back |
|---|---|---|
| **Technical** (code, sphere authoring) | *ground* | *"Grounded: 3 files · a1b2c3d"* |
| **Non-technical** (life, family) | *save* | *"Saved."* |

- **The human can add their own words,** like *"lock it in."* A phrase they keep using is proposed as a command, and they decide (see [optional commands](protocol.md)).
- **Only words that clearly mean ground, and that the human has confirmed, become ground.** *"Save this idea"* is idea capture, not a ground. An ambiguous phrase gets a question, never a guess, and every ground reports in one line, so a mistaken one shows on the next turn.

### `peek`: what's unsaved — _decided, not yet exercised_

*"What's unsaved?"* or *"what's changed?"* shows the working state without touching it, grouped by focus (see [peek across foci](focus.md#peek-across-foci)). A non-technical build says it in a line: *"You have 2 unsaved changes. One other file changed outside any focus."* The longer form, *"what happened today?"*, lists recent grounds.

### Safe experimentation — **proven**

Every grounded state is a checkpoint, so **trying something is cheap: undoing it is cheap.** `revert` and `undo` never destroy anything. They add a new commit that reverses an earlier one, and the history stays whole. This is one of the main reasons a sphere uses git at all.

### Reverts by node, and by kind — _unexercised_

Commits from different foci interleave: f31, f32, f31. **Every commit names its node** (`ground [f31-…]`), so a revert can be aimed:

| Operation | Does |
|---|---|
| **undo** (in a focus) | reverses **this node's** last ground, never another node's. Another node's later commits are untouched |
| **revert to** a node's earlier ground | reverses that node's commits after it |
| **revert the sphere** to a point in time | reverses everything after it. Every foreground focus grounds or detaches first, and the human confirms, because it reaches into every node |

A revert treats each [kind of file](focus.md#several-writers-four-kinds-of-file) the way that kind is written:
- **Current state:** reversed. The node held those files, so no other node's change is caught up in it.
- **History:** appended entries are never removed. A revert **appends** an entry saying what was reversed and why, which keeps the history true. A history file that was created, deleted or moved **whole** goes with its node: reverting past a focus's opening removes the focus, history file and all (git still has it).
- **Reference:** a reverted fact or lens change becomes a **proposal to restore the old version**, confirmed like any other reference change.
- **Generated:** rebuilt afterwards.

### When the state isn't clean — **proven**

If an operation expects a clean state and finds changes it didn't make, it **stops, shows them, and asks:** save them, set them aside, or abort. It never resolves this on its own. The changes may be the human's, or another focus's.

- **"Clean" is scoped to the node.** Other foci's unfinished files in the folder are normal. What stops an operation is a changed file that **no open focus holds**: *"The budget sheet changed, and it isn't in any focus. Yours? Save it here, set it aside, or leave it?"* — _unexercised_
- **Show tracked files apart from new ones** (new files are often scratch).

A failing commit check is never bypassed. The sphere fixes the cause, or shows the human. If a check really is wrong for this one case, the escape is an exception the human names and the sphere records, scoped to that check alone.

### `ground` — **proven**

At a safe point, or before detaching or closing, the sphere:

1. **Compacts** working state into the records of what the focus holds. Each piece of work touched gets its `progress.md` entry: what happened, what's next. New facts and rules are *proposed* rather than written (see [knowledge](knowledge.md), [guardrails](guardrails.md)).
2. **Writes the focus node:** rewrites **Now** in `focus.md` and appends a history entry (Did, Decided, Next, Pointers; see [focus](focus.md#historymd)). A child also appends one line to its parent's history.
3. **Applies confirmed reference changes,** one at a time, each after re-reading the file. — _unexercised_
4. **Rebuilds generated files from what's committed** plus this ground's own changes, never from the working folder, which may hold other foci's unfinished work. — _unexercised_
5. **Reconciles this focus:** other changed files no focus holds are listed and left for main, never a stop; the AI asks *"hold it too?"* only about files its own window edited. Questions about other foci are asked elsewhere (see [the focus folder is the registry](focus.md#the-focus-folder-is-the-registry)).
6. **Commits under a short lock:** pull, stage only what this focus touched, commit as `ground [f21-name] — summary`, push.
7. **Reports in one line.**

**Every commit is a sane state.** Each ground commits one node's held files, its appends and its confirmed reference changes. Holds are exclusive, so nothing in it depends on another node's unfinished work: every commit is a consistent grounded state of the whole sphere. — _unexercised_

Grounding is the sphere's authorized commit. Two things count as approval: the human asking to ground, or a **standing approval** the human set up, such as a scheduled end-of-day ground or an agent delegated to *"ground your own work as you go."* Nothing else commits sphere state.

### `attach` — **proven**

Attaching to a focus reads its node, its latest history and what it holds, and says where things stand and what's next (see [focus](focus.md#attaching-runs-the-whole-briefing--proven)). **A good ground is measured by how well a cold attach works:** a fresh window, with no memory of the last one, should be able to continue.

---

## Sharing one sphere

### Same machine

Several windows share one working folder and can see each other's unsaved edits. Ground stages only what *this* focus touched, so it never commits another focus's half-finished work. **Ground holds a short lock while it commits,** so two foci grounding at the same moment take turns instead of colliding. — **proven** (staging) · _lock decided, not yet exercised_

### Several devices

Each device has its own copy of `main`. Ground pulls before committing and pushes after. A conflict between devices is handled as described in [Conflicts](#conflicts--decided-not-yet-exercised).

### Shapes that avoid conflicts — _decided, not yet exercised_

**One file per item takes most writes:** each focus node's files, each work node's `progress.md`. Two foci rarely touch the same file. **One shared table that every focus appends a row to** is the opposite: it conflicts often, because everyone writes to its end. When the sphere designs a new record, it prefers the first shape. Shared files that remain (the work index, principles, the human's profile) are written only at ground, after re-reading them, so nothing is overwritten unseen.

### Without git — fallback only

Git is the default because it gives history, undo and merges. Without git, these edge cases have no safety net:

| Edge case | What goes wrong |
|---|---|
| Two foci in the foreground at once | Last writer wins on shared files; the other focus's changes are lost silently |
| One sphere synced to two devices through a cloud folder | The sync service creates conflict copies or picks one version |
| A crash halfway through a ground | Some files written, some not, with no record of which |
| A bad ground | No history, so it can't be undone |
| The human edits a file while a window is attached | The window's next write overwrites the edit |

A gitless sphere is supported only as **one focus in the foreground at a time**. Ground writes the files and the history entry, with no commit. A lock file is written when a window attaches, and a second window opens read-only with a warning. Locks can go stale after a crash, and they reach other devices slowly through cloud sync. Undo and revert aren't available. Main takes part in the same one-at-a-time lock. With no commits, "unsaved" can only be approximated: a file changed after its focus's last history entry. That's why this is a documented fallback, not the default. — _unexercised_

---

## Commits

- **Stage only what the focus holds.** Never stage everything in the folder. Unrelated changes may belong to another focus or to the human. Git can't tell which window changed a file, so ownership is by holds alone; two foci that both hold a node (a soft claim answered "both") each stage it at their own ground. — **proven** (as "only what this window touched")
- **One sphere repo, separate from code repos.** Sphere state has its own history; grounding the sphere never commits to the project being worked on. — **proven**
- **Generated files never cause merge pain.** Machine-only caches (like the startup bundle) are rebuilt when needed and never committed. Human-facing views (like the work index) are committed so people can read them. See [registries](registries.md#committed-views-and-caches--decided-not-yet-exercised). — _decided, not yet exercised_
- **Ground commits the source; views follow.** Ground commits the sphere's source files once. Surface views are refreshed from them, never committed as a second, coupled change.
- **History files merge by union** (one `.gitattributes` line), so two devices appending to one history keep both sides. — _unexercised_
- **Commit subjects are part of the contract,** because undo and revert find a focus's commits by them. — _decided, not yet exercised_

  | Commit | Subject |
  |---|---|
  | A ground | `ground [f21-plumbing-quotes] — summary` |
  | Opening a child (a ground of the parent) | `ground [f20-kitchen-renovation] — opened f21-plumbing-quotes; carved plumbing` |
  | A close (the child's own last ground) | `ground [f21-plumbing-quotes] — closed (done): why` |
  | Undo | `undo [f21-plumbing-quotes] — …`, with a `Reverses: <commit>` line |
  | Revert of a focus | `revert [f21-plumbing-quotes] — back to <commit>` |
  | Revert of the sphere | `revert [f0-main] — sphere back to <commit>` |

  A focus's undo history starts at its `opened` commit, so a number reused after a revert never reaches an older focus's commits.
- **A remote with no upstream branch** isn't pushed to, and ground says so in its one-line report each time (*"not pushed: no upstream"*), so a sphere never silently stops backing up.

## Conflicts — _decided, not yet exercised_

Three kinds, handled differently:

- **Generated views** are **rebuilt** from the merged sources, automatically. No human needed.
- **Views kept by hand** have nothing to rebuild them, so they're resolved like content, then checked.
- **Content** (the human's own files: their work, their knowledge, their lenses) is **never resolved silently.** The AI proposes a resolution and the human confirms it. For a non-technical human that happens in plain words, never as a raw conflict: *"Your laptop and your phone both changed your grocery list. Keep both versions' items?"*

---

## Open questions

1. **Git inside cloud-synced folders.** A git repository inside a cloud-synced folder can be damaged when the sync service rewrites files under `.git/`. Decide whether builds warn about this or keep git data outside the synced folder.
