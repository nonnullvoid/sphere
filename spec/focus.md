# Focus

What the human is focusing on with the model, and how that focus is held, worked, narrowed and closed. Sessions and agents are two ways of working on a focus node.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice). A focus tree one level deep, one focus per thread of work side by side, has run daily in one sphere, so those parts carry **proven**. The deeper tree, holds and carving are **unexercised**._

---

## The idea

A sphere is made of trees, and every tree is made of the same unit, a [node](nodes.md): a name, a `parent:`, a flat folder, frontmatter that shows it in one line, and a current-state file plus a history file.

| Tree | Answers | Example |
|---|---|---|
| [Understanding](protocol.md) | How does the human think? | lens → frame |
| [Knowledge](knowledge.md) | How are things? | domain → topic → fact |
| [Work](work.md) | What's changing? | area → project → task |
| **Focus** | **What is the human focusing on, with the model?** | sphere → kitchen → plumbing quotes |

**A focus node is what the human is focusing on, with the model: an intention plus the memory of pursuing it.** Focus is co-created. The sphere has no focus of its own, apart from the human's.

**It answers a question every sphere needs answered.** A sphere is a large collection of files and nodes. *"What's in focus right now?"* has a clear answer: the focus node a window or a run is attached to, and what that node holds.

### What a node keeps, and what it doesn't

| | Kept by the node? | |
|---|---|---|
| **Intention** | **yes** | why the node exists: its charge |
| **Memory** | **yes** | what was done, decided and learned while pursuing it |
| **Context** | no, built each time | made at each attach from the intention, the memory and the loadout. It fills the window and is lost when the window closes |
| **Ability** | no, borrowed | lives in the protocol (lenses and frames). The node borrows it through its loadout and operating mode |

**A node is an intention plus the memory of pursuing it.** That's exactly what a good ground writes down, and exactly what survives a window closing.

A focus node also links the other trees into one sentence: *focus node X, for work Y, using knowledge Z, through lens W.*

**Moving down the focus tree narrows the focus.** The root is [main](#main-the-root-focus--decided-not-yet-exercised), the sphere itself, always open. Its children are the broad things in view, such as the kitchen renovation or this week. Their children are specific pursuits, such as getting three plumbing quotes.

### Focus is not work

Many focus nodes will hold exactly one piece of work, and that can look like duplication. It isn't: **work is what's changing in the world; focus is what's being attended to.** A focus node can hold several pieces of work, only knowledge (*"read up on heat pumps"*), or the sphere itself (*"restructure my lenses"*). And a piece of work is attended to by many focus nodes over its life.

**Work is the line; focus nodes are the dots.** A piece of work runs from start to finish. Focus nodes are dotted lines along it, each picking some of it up and putting it down.

---

## Windows, sessions and agents

Three things are easy to confuse:

| | What it is | Lasts |
|---|---|---|
| **Focus node** | The pursuit: its intention and its memory | Until it's closed. It survives any window |
| **Window** | The app, terminal or run attached to it right now | Until it's closed, or its context degrades |
| **Session or agent** | *How* a window works on the node: who chooses each step | As long as that window works that way |

**A window is not the focus.** It's like a terminal multiplexer over a remote connection: the focus lives on, and windows attach and detach. A window whose context has degraded can be closed and a fresh one attached to the same focus, with nothing lost. That's also why a sphere is **independent of any one AI tool:** the focus is the sphere's, and any harness can attach to it. — **proven**

**What separates a session from an agent is who chooses the next step.** In agentic systems, an agent is a model working in a loop: it picks its next action, uses tools, looks at the result, and goes again until it's done. In a chat, the human picks, turn by turn. In a sphere that difference already has a name, the [collaboration mode](modes.md#collaboration-modes--decided-not-yet-exercised):

| | Who chooses each step | The intention | Collaboration mode |
|---|---|---|---|
| **Session** | the human, turn by turn | drifts with each turn, taking on whatever the turn needs | together |
| **Agent** | the model, with the human checking at gates or afterwards | usually fixed by its `focus.md`, which acts as its starter | supervised or unattended |

The first column is the definition. A fixed intention is common for agents, but it isn't what makes one.

**So a session and an agent aren't two kinds of thing. They're two ways of working on a focus node.** Whatever attaches brings the loop; the node holds the intention and the memory. Three things follow:

- **Memory belongs to the focus, not to the agent.** An agent's memory is usually its context window, plus whatever its product stores. In a sphere, it's the node's history, in files the human can read. Any window or run that attaches gets the same memory, and loses nothing when it ends.
- **A delegated agent is a child focus node.** It starts with a fresh context, its `focus.md` as the task, and the tools its loadout and guardrails allow. It hands back one report: a history entry, and one line to the parent. That's how subagents in agentic tools work today, with one change: the report lands in the sphere, not only in the parent's context.
- **To keep an agent going, hand it the next task on the same node.** When the work is done, close the node. Either way, what it learned stays with the focus.

**Who, what, and how.** A [persona](modes.md#the-persona--proven-one-persona) is *who* the AI is. A focus is *what* the human is pursuing. A collaboration mode is *who chooses each step*. An agent's own definition, what it may do and how far it's trusted, is a fourth thing, kept in [agent-trust](agent-trust.md); a run of that agent is a window attached to a focus node. A character that only chats is a persona with no focus. A product agent that runs errands for days is a long-lived focus worked unattended, with its memory kept where the human can't read it. A sphere keeps these apart, and keeps the memory with the human.

### When to close, or open a child

**When the intention has drifted out of the node, the work belongs somewhere else.** The sphere notices and asks: *"This has moved from plumbing quotes to the cabinet budget. Open that as its own focus?"* The human decides. Closing stops being a matter of feel, or of the window wearing out.

**Drift decides between rename, child and close:**
- the intention shifted *a little* → suggest a **rename** (below);
- it drifted *out*, and the old intention isn't finished → suggest a **child**;
- it drifted out, and the old intention is finished → suggest **closing** it and opening a new focus.

---

## Foreground and background

**Every open focus node is something the sphere is holding in focus for the human.** They differ only in whether it's in view right now:

| | Means | Example |
|---|---|---|
| **Foreground** | open, with a window or a run attached | a session drafting the quote request; an agent comparing cabinet options |
| **Background** | open, with nothing attached: not in view, but held | this week; work waiting on someone |

- **Foreground means the model is attending, not that the human is.** An unattended run is in the foreground, in unattended collaboration mode.
- **Attaching** brings a background node to the foreground at once. Nothing reloads from scratch: the sphere remembers where it stands. **Detaching** grounds and sends it back.
- **Liveness is how recent the focus is.** Something in the foreground can go quiet and turn **stale**: the window closed, or the laptop crashed. Nothing is lost; the focus stays held.
- **Only closing ends a focus.** Until then the sphere remembers it and can return to it at once. That's how a person works too: one thing in hand, several in mind.

**Foreground and background are runtime state, never committed.** They're computed from heartbeats (below). Whether a node is open or closed is meaning, and lives in the node. Each fact is in [exactly one place](#the-focus-folder-is-the-registry).

### Stage and liveness

A node's **stage** is whether its held files have unsaved changes: **working** (unsaved changes) or **grounded** (clean), until it's **closed**. **Liveness** is foreground, background or stale. Crossing them gives a quick read of any node — **proven** (in a tree one level deep):

| stage ↓ · liveness → | background | foreground | stale |
|---|---|---|---|
| **working** | Orphaned: unsaved work with nothing attached. Ask; offer to ground | **Normal work** | Crashed mid-work: offer to recover, highest priority |
| **grounded** | **Held**: attach any time | Just grounded, carrying on | Window died after saving: clear the heartbeat |
| **closed** | **Done** | A window outlived the close: detach it | Leftover record: clear the heartbeat |

- **Ground before detaching,** so a node rests *grounded in the background*, never *working in the background*.
- **How serious a stale node is depends on unsaved work, not on how long it's been quiet.** Stale with unsaved work: offer to recover it, never discard it. Stale and clean: clear the heartbeat.
- **Closing ends attachment.** `close focus` detaches any window still attached.

**Heartbeats** — _decided, not yet exercised_. Each foreground node has a heartbeat file at `surface/state/focus/<number>.json` holding `last_seen` and the window's client label. Any sphere command updates it; there's no list of which commands count. The window says which focus it's in (the reference tooling reads `SPHERE_FOCUS`). **Heartbeats are per device** and never committed, so a focus in the foreground on another device looks background here; a close or a sphere revert can't see that window, and the human is the check. A node counts as foreground while `last_seen` is within 30 minutes. One file per node, so heartbeats never contend. If the file is lost, the tooling rebuilds it.

### Focus in the other chapters

- **Work's focus axis** comes from focus nodes, not from a guess. A piece of [work](work.md#state-and-focus--two-separate-axes) is **in focus** when an open focus node, foreground or background, holds it. `pinned` is a background focus node the human keeps open on purpose. Suggestions from signals (deadlines, the week's plan) are suggestions to open a focus node.
- **[Rhythm](rhythm.md):** a day or a week can be a long-lived background focus node, brought to the foreground by the morning and evening routines.

---

## A focus node

```
layers/focus/
├── f20-kitchen-renovation/
│   ├── focus.md         the intention, what it holds, where it stands      (always)
│   └── history.md       what happened, newest first                        (always)
├── f21-plumbing-quotes/
│   ├── focus.md
│   └── history.md
└── archived/            closed nodes, moved here whole
```

**Folders never nest.** The tree lives in `parent:`, as with work. **Focus lives with the other trees,** in `layers/focus/` beside work and knowledge, because it's the human's focus, not something internal to the sphere.

**Closed nodes move to `layers/focus/archived/`,** folder and all, so the top level holds only what's open and listing it stays cheap. Archived nodes are still found by number or name when something refers to them. See [finished things move out of the way](registries.md#conventions-and-swappable-parts).

### Names: a number and a memorable name

Every focus node has **both**:
- **A number** (`f21`): the shorthand. Stable for the node's whole life. The next number is one more than the highest in `layers/focus/`, `archived/` included. If a revert removes a focus, its number may be used again; the sphere is a state machine, and undo or revert aimed at a focus only looks at commits since that focus opened. `f0` is always [main](#main-the-root-focus--decided-not-yet-exercised).
- **A name** (`kitchen-renovation`): two or three words that match how the human would remember it. The AI proposes one when the node opens, and the human can change it.

Together they make the reference: **`f21-kitchen-renovation`**. People use whichever comes to mind: *"attach to f21"*, *"resume the kitchen renovation"*, *"close focus"*. A partial or plain-words match (*"the kitchen one"*) shows candidates rather than guessing. This is the prefix-and-number scheme from [work](work.md#naming--decided-not-yet-exercised), with the number carrying identity, because focus moves around the tree and shifts over time.

**Renaming keeps a focus alive as it evolves.** When the focus shifts a little, rename it rather than living with a name that misleads: *"rename f21 to kitchen-upgrades."* The number stays, so everything that refers to `f21` still resolves.
- The folder is renamed, and links inside the sphere are updated. Links use the number, so very little changes.
- **Old names are kept** in `focus.md` under `aka:`, so *"the renovation one"* still finds it.
- Commits keep the name they were made under. They all start `[f21-`, so a node's whole history is found by its number.

### `focus.md`

```yaml
---
number: f21
name: plumbing-quotes              # the reference is f21-plumbing-quotes
aka: [plumbing]                    # earlier names, still findable
parent: f20                        # f0 for a top-level focus
status: open                       # open | closed
intention: Get three plumbing quotes and choose one
holds: [work:home.kitchen.plumbing, knowledge:home.kitchen]   # nodes, never a list of files
through: [money-risk]              # lenses in the foreground
operating-mode: planning
collaboration-mode: together
persona: sage
points-at: []                      # outside things it works in: a code repo and branch, a document
opened: 2026-11-02
---
```

- **Write the shape exactly.** These keys only; `status` is `open` or `closed`, never free text. If something doesn't fit, ask; don't invent a key or a value. A record that bends its own shape can't be read by the tooling or by the next window.
- The body holds **Now**: where things stand, what's next, what's open. It's rewritten at every ground.

### `history.md`

The node's memory, never rewritten. **Every ground adds an entry at the top**, newest first — **proven** (shape):

```markdown
## 2026-11-10 16:17 — grounded

**Did:** Called two plumbers; one quote in, one booked for Thursday.
**Decided:** Skip the third big firm: their minimum call-out is over budget. Tried the
city's licensed list first, but it doesn't show availability.
**Next:** Chase the Thursday visit for a written quote.
**Pointers:** work: home.kitchen.plumbing → progress.md
```

- **Did** is the story. **Decided** holds the judgment calls that are expensive to re-derive, including what was tried and ruled out. **Next** is the single most useful line for a cold start: a concrete first action, not a topic.
- **Write it for a reader with no memory of this conversation.** Name things; no "as discussed".
- **Pointers, not copies.** An entry points at the work's progress, never repeats it. The commit isn't named: it doesn't exist yet when the entry is written, and it's found by its `[f21-` subject.
- **Many windows over many days write to the same history,** because they all attached to the same pursuit.
- **Closing writes a last entry** saying how it ended: done, or dropped, and why.

**Two records, two questions.** A focus node's history and a work node's `progress.md` are separate axes:

| | The work's progress | The focus node's history |
|---|---|---|
| **Answers** | "Where does this piece of work stand?" | "What was this pursuit in the middle of?" |
| **One per** | piece of work | focus node |
| **Read by** | anyone picking the work up later | the next window attaching to this focus |

A focus that touches three pieces of work writes three progress entries and one history entry.

---

## What a focus node holds

**`holds:` is the node's scope: the nodes it's pursuing, never a list of files.** A node held covers everything in its folder. Name the most specific node that covers the work: `work:home.kitchen.plumbing`, not each file inside it, and not all of `work:home`. For something outside any node, name its folder.

**Git can't tell which window changed a file,** so a ground goes by holds, never by guesses. It commits what the focus holds and lists, in one line, any other changed file no open focus holds: *"Also changed, not in any focus: budget.md (left for main)."* Nothing stops; main's next ground picks those files up. **The "hold it too?" question is the AI's,** asked only about a file its own window edited while in this focus: *"I also changed the budget sheet. Hold budget work in f21 too?"*

**The most specific hold wins.** If f20 holds `work:home` and its child f21 holds `work:home.kitchen.plumbing`, plumbing's files are f21's. So a child rarely needs to edit its parent's holds.

Scope does three jobs:

1. **Loadout.** What a node holds, plus the lenses it works through, decides what's warmed when something attaches. Its operating mode adds the rest. See [loading](loading.md).
2. **Writing.** A focus node writes directly only to what it holds, plus its own two files. Everything else follows the rules for its kind, below. This extends a proven rule: stage only what this window touched.
3. **Seeing overlap early.** When a second open node tries to hold something already held, the overlap shows up **when it's claimed, not later as a merge conflict.** The question goes through the parent: *"Plumbing is already in focus in f20-kitchen-renovation. Ask it, or just read?"*

**Say "in focus", not "held".** To the human, something is **in focus** when an open focus node holds it, and **out of focus** when none does. "Hold" is the spec's word for the mechanism.

**Claims are soft.** A claim warns and asks; it never refuses. The human can always say "both," and the overlap is then handled like any content conflict: proposed, never silent.

**Reading is never claimed.** Any node can read anything.

---

## Several writers: four kinds of file

What goes wrong with several writers is never really parent and child. It's **two writers on one file that gets rewritten in place.** Every file in a sphere is one of [four kinds](nodes.md#four-kinds-of-file--unexercised) (current state, history, reference, generated), each with one way of handling several writers. **The rule in one line: write only to what you hold; anything else is appended, offered, proposed or rebuilt.** Below is how that plays out with focus nodes.

### Current state: carving the hold

**A hold is exclusive.** So when a parent opens a child, the child can't share the parent's hold. Instead, **opening a child carves part of the parent's hold out and hands it to the child.** The parent's hold shrinks by that much. When the child closes, that part returns to the parent.

| What the child takes | How it's carved |
|---|---|
| An item on the parent's task list | The item becomes a node of its own (see [depth is a dial](work.md#depth-is-a-dial--proven)), and the child holds it. The parent's line becomes a link |
| Part of a folder the parent keeps (a design folder, a set of drafts) | The child holds one file or one subfolder |
| One file both need at once | It can't be carved. One holds it, and the other **offers** its changes |

**The parent rolls up.** A child marks its own node done and reports up in one line. It never edits the parent's node. The parent picks up what its children did on its next read: when it next grounds, or something next attaches to it. Generated views are rebuilt from the nodes, so the overview is current even before the parent rolls up.

### Reference: confirming, one at a time

Knowledge can't follow the focus tree. It's arranged by how the world is (domain → topic → fact), not by who's working on what, so two sibling foci can both learn something about the same topic. It can't be carved finely either: a topic is one file.

**It doesn't need to be carved, because reference is never written directly.** [Nothing is written into knowledge without the human's say](knowledge.md#how-knowledge-gets-in--proven), and lenses change only in [sphere authoring](modes.md#sphere-authoring-changing-the-sphere-itself--decided-not-yet-exercised). The confirmation step serializes writes:

1. **Each focus node keeps its proposals in its own folder.** Two children proposing facts about one topic never touch the same file.
2. **At ground, under the ground lock,** confirmed changes are applied one at a time, each after re-reading the file.
3. **Two proposals about the same fact** are a real disagreement, not a file conflict, and the human sees them as one: *"f31 says the estimated payments are 2 of 4; f32 says 3 of 4. Which is right?"*

**Work avoids contention by dividing; reference avoids it by confirming.**

**One exception: compiling.** *"Compile what we know about the house from the inspection report"* produces a large batch for one topic. **A compile holds its topic for as long as it runs**, so a second compile into the same topic gets the soft-claim question before it starts.

### Where overlap really happens

One sphere ran parallel lines of work, each on its own git branch, daily for six months. Its merge history:
- **About 1 in 6 merges** had two live lines of work writing the same file.
- **About 1 in 20** conflicted.
- **Most of it was one pattern:** a shared task list, written by a parent and several of its children at the same time.
- **The registry of open work, one file per line of work, never conflicted.**

That pattern is two writers on one current-state file, a problem of which way writes flow, not of branching. Carving the hold removes it, and history appends never contend. Soft claims are left for the rare real overlap. _Expectation, not yet measured._

---

## The tree

- **Opening a child** narrows a focus: the human mid-conversation (*"let's go deep on the quotes"*), or a node delegating to an agent. **The child's `focus.md` is its starter,** and the child takes its carved part of the parent's hold. The parent is told: *"Opened f21-plumbing-quotes: get three quotes."*
- **Opening a child is a ground of the parent.** The carve changes the parent's file (a checklist line becomes a link) and its holds, so it's committed under the parent's name (`ground [f20-kitchen-renovation] — opened f21; carved plumbing`), and can be reverted like any other ground.
- **Nodes talk through their parent, never sideways.** — **proven** (as a lesson: direct messaging between siblings was tried, and they started taking over each other's work). A tree only has parent edges. Across one edge, three verbs: **inspect** (read the other node), **request** (an ask, never a command), **share** (offer a change to review, never overwrite).
- **Reporting up** is a history entry in the child, plus **one short entry at the top of the parent's `history.md`** at ground, headed `## <date> — f22 reported`: *"f22: three cabinet options drafted; one fact pending your review."* Anyone can append to history, so this keeps the child out of the parent's current-state files. There's no merge.
- **What's waiting is computed, not tracked.** Report lines and requests appended to a parent since its last ground are what's *waiting for you*. When the parent grounds, it rolls them into its Now, and they stop being new. Nothing marks them read.
- **An offered change lives in the sender's history.** The sender adds an entry headed `## <date> — offer to f21`, naming the file and the change it offers, in words or as the new text. The heading is what lets the tooling count it as waiting. The holder sees it as *waiting for you* until it answers, by appending *accepted* or *declined* to its own history. Nothing is written into the holder's files until it accepts.
- **Closing a child** ends it and asks, once, about what it held: *"f21 held plumbing. Give it back to f20, or release it?"* Giving it back is the default. The answer is written into the parent's `holds:` in the **close commit, which is the child's last ground**, so `undo` on the child reverses the whole close, holds included. The AI asks before closing and passes the answer to the tooling, which can't ask on its own. Nothing about holds is computed from archived children afterwards. Its history stays, and what it learned is already where it belongs: in work, in knowledge, in proposals to lenses.
- **When children close with their parent,** the AI writes each child's real last entry first, then the parent's summary of the subtree; the tooling only adds a plain `closed with f20` entry where none was written. **Moving children up** edits each child's `parent:` inside the parent's close commit.
- **Closing a focus that still has open children** follows [finishing a node](nodes.md#finishing-a-node--decided-not-yet-exercised): list each child's latest **Next** and whether it has unsaved work, and ask once: *"f20 has 2 open children: f21 (one quote left) and f22 (unsaved changes). Close them too, move them up, or keep f20 open?"* Closing them too goes deepest first, and f20's last entry sums up the subtree. A child with a window or run attached is never closed under it.

**Depth is a dial.** A sphere that never opens a child has a focus tree one level deep: one focus per thread of work, side by side, which is how one sphere has run daily. The tree only gets deeper when someone opens a child. Nothing changes shape when it does.

**Subtrees are also the grain of sharing.** A focus node and its children can be exported together, as one pursuit. See [replication](replication.md).

---

## Opening, attaching and closing

| Verb | Does | Commits? |
|---|---|---|
| **open focus** | starts a focus, or a child if you're inside one | **yes** (a ground of the parent; for a top-level focus, one line in main's history) |
| **attach** | brings a focus to the foreground (*resume*, *continue*, *pick up* mean the same) | no |
| **ground** | commits this focus's changes into the sphere. Can name the point | **yes** |
| **detach** | grounds, then sends the focus to the background | yes |
| **close focus** | grounds, writes the last history entry, ends the focus, gives its hold back to the parent or releases it (asked once), moves it to `archived/` | yes |
| **peek** | what's changed and unsaved, by focus; recent history | no |
| **undo** / **revert** | reverses this focus's last ground, or goes back to an earlier one | yes, as a new commit |

The state contracts behind these verbs are in [state](state.md).

- **Other words people use:** *start a session* means open focus; *park* means detach; *checkpoint* is a named ground; *history* is peek's longer form.
- **The words belong to the build and the human,** as in [state](state.md#the-words-are-the-humans--decided-not-yet-exercised). People say focus references short: *"attach to f21"*, *"close focus"*.

### Attaching runs the whole briefing — **proven**

Every phrasing (*"resume the kitchen"*, *"continue f21"*, *"pick up where we left off on the quotes"*) runs the full attach:

1. **Find the node.** Match the number, name or `aka:`. If more than one fits, show the candidates and ask; never guess.
2. **Read** its `focus.md` (intention and Now), the latest history entries, and the progress of what it holds.
3. **Brief:** where things stand, what was decided, what's next. Then carry on.

There's no lighter version that finds the node and skips the reading. A window that does that carries on knowing the plan and not the story, and redoes or contradicts what the last window settled. A quick look without attaching is `peek`.

### Main: the root focus — _decided, not yet exercised_

Not everything deserves a focus. *"Remind me how these projects fit together,"* *"what did we decide about the cabinets?"*, *"take in these meeting notes"*: quick windows, some only reading, some writing once and leaving. They still need somewhere to ground, without opening a node for every one.

**`f0-main` is the root of the focus tree: always open, never closed, and where any window is until it attaches to something else.** It's the sphere itself, as a focus (`aka: sphere`, so *"attach to sphere"* works too). Every sphere has it from the start.

- **A window that only reads leaves nothing behind.** A quick question isn't a focus, and needs no step to stay out of the tree.
- **A window that writes grounds into main:** `ground [f0-main] — took in the design review notes`. No node is opened for it.
- **Main holds nothing.** A ground in main covers the files it touched that **no open focus holds**. A file another focus holds becomes an offer to that holder, as anywhere else. Reference changes are proposed as usual.
- **Quick windows never rewrite main's `focus.md`.** They only append to its `history.md`, so any number of them can use main at once with nothing to collide on beyond the short lock at ground. Main's history becomes the record of quick work. Its `focus.md` says what main is for and changes only when the human changes that.
- **Main's `focus.md`** has the same shape as any focus, with no parent:
  ```yaml
  number: f0
  name: main
  aka: [sphere]
  parent:
  status: open
  intention: Anything not in another focus; the sphere as a whole
  holds: []
  ```
- **Main has no heartbeat.** It can't go stale. Unsaved work no focus holds already shows in `peek` as out of focus, which is main's.
- **Real work gets offered a focus once.** When a window grounds into main a second time, it's probably not quick: *"This is turning into real work. Open f24-heat-pump-research for it?"* The human can accept, attach to an open focus, or keep going in main. The window knows it grounded before; nothing is stored. (A first ground that touches several pieces of work can be offered one too.)
- **Opening a top-level focus** appends one line to main's history (*"opened f24-heat-pump-research"*). Top-level foci have `parent: f0`.
- **Attaching to main briefs the whole sphere:** what's in focus, and what needs the human's attention (see [the focus folder is the registry](#the-focus-folder-is-the-registry)). A window that simply starts in main doesn't run that briefing; quick windows stay quick.

*Why a root focus rather than "no focus":* an unattached window that grounds otherwise has nowhere to put its record, so every quick write turns into a question. Main gives it a home that's still a node, with the same shape, verbs and history as every other focus.

### Focus talk is a command — **proven**

**Focus phrasing is a command, not prose.** *"Open a focus for the kitchen"* means open one. It doesn't mean "I'm about to work on the kitchen." The same goes for session words people use: *"start a session for…"*, *"continue that session"*. The sphere checks focus-shaped and session-shaped phrasing against its commands before reading it as conversation. Missing this once meant several turns of work done outside any record, unnoticed until the human asked where it went.

**Every change to a focus node reports back in one line** (*"f21-plumbing-quotes open · foreground"*), so a focus that was meant to open but didn't shows on the very next turn. A non-technical build says it plainly, or says nothing when nothing changed.

### `peek` across foci

Holds make it possible to say whose change is whose:

```
f21-plumbing-quotes (this focus)
  changed: plumbing/work.md · 1 fact proposed
f22-cabinet-options (agent, running)
  changed: cabinets/options.md
f20-kitchen-renovation (background)
  waiting for you: 1 offered change (budget sheet) · 2 reports from children
Out of focus
  changed: notes/scratch.md   → yours? save it here, set it aside, or leave it
```

A non-technical build says it in a line: *"You have 2 unsaved changes here. The cabinet agent is still working. The kitchen has 1 change waiting for you."*

---

## The focus folder is the registry

Three kinds of truth, each with exactly one home:

| Kind | Examples | Home | Who writes it |
|---|---|---|---|
| **Facts** | the node exists, when it last grounded, what it touched | git and the folder | computed when needed, never stored |
| **Meaning** | intention, holds, status, modes, why it's a child of its parent | `focus.md` frontmatter | the AI drafts it, the human confirms |
| **Runtime** | foreground or background, which window, last seen | `surface/state/focus/`, never committed | the tooling |

**Why three homes:** a fact stored in two places drifts. Storing facts only in git and meaning only in the node shrinks what can drift to a few cases, and each surfaces as a question — **proven**.

**Reconciliation runs in the tooling, not as a habit,** because a step that depends on remembering eventually gets skipped. But **each question is asked where it belongs, not at every ground:**

| Question | About | Asked |
|---|---|---|
| *"I also changed the budget sheet. Hold it in f21 too?"* | this window's own edits | by the AI at this focus's ground, only for files its window edited. Other changed files are listed, never asked about |
| *"f17 has unsaved changes and its window has gone quiet. Recover them?"* | another focus | in *"what's in focus?"*, when attaching to main, and once when a window starts |
| *"f12-newsletter has been quiet for three weeks. Keep it in the background, or close it?"* | another focus | in *"what's in focus?"* and when attaching to main |

- **A ground asks only about its own focus.** Most grounds ask nothing. A ground into main asks nothing of this kind, since main covers whatever isn't held.
- **An answer sticks.** *"Keep it in the background"* appends a line to that focus's history, and quiet is measured from its latest history entry, so the question doesn't come back for another three weeks. Nothing new is stored.
- **Stale unsaved work is the one sphere-wide item that interrupts:** one line when a window starts, and only while it's true, because it's the one case where waiting can lose work.

**Listing open foci** (*"what's in focus?"*) reads only the top level of `layers/focus/`, never `archived/`, and shows each node's reference, foreground or background, last ground and latest **Next** line, as a tree. Nodes that need attention come first: stale with unsaved work, or open but quiet for a long time.

---

## How it runs

- **One branch.** Every focus node commits to `main`. Git holds history, undo, and sync between devices. **Branches aren't how focus nodes are kept apart; holds are.** A branch per line of work was tried in daily use; most of its sharp edges came from the branches themselves (silent fallback to the main line, a detached checkout, a startup file that conflicted on merge, worktree limits), not from parallel work. — _one branch decided; tree unexercised_

  | Branches gave | Focus nodes use instead |
  |---|---|
  | Separation | **Holds.** A node writes only what it holds |
  | Review before landing | **Ground** is already the review |
  | Throwing a line of work away | **Revert by node:** every commit names its node |
  | Catching overlap, at merge | **Catching it at claim time,** through the parent |

- **Ground holds a short lock** while it applies confirmed changes, rebuilds generated files and commits, so two nodes grounding at once take turns. The lock works within one device. Across devices, ordering comes from the merge.
- **An unattended run grounds only under a standing approval,** given when it's delegated (*"ground your own work as you go"*), and **scoped to what it holds.** Its reference proposals still wait for the human, and anything it would offer to another node waits on that node.
- **Commits name their node:** `ground [f21-plumbing-quotes] — summary`, `undo [f21-plumbing-quotes] — …` and `revert [f21-plumbing-quotes] — …`. A reversal names what it reverses in a `Reverses:` line, so a second undo walks one step further back.
- **Outside branches stay outside.** A code repo's branches, worktrees and pull requests belong to the code. A focus node only points at them (`points-at:`), and grounding the sphere never commits to the code repo. — **proven**
- **Devices still merge.** Each device has its own copy. Ground pulls before committing and pushes after, and the [conflict rules](state.md#conflicts--decided-not-yet-exercised) apply. Holds keep current-state files apart, so they merge cleanly. **A node can be in the foreground on two devices;** its hold keeps their writes on the same files, so it's the one case where a device merge can still conflict.
- **History merges by union.** When two devices both append to one history file, git would report a conflict. History files are marked for git's built-in union merge (one `.gitattributes` line), which keeps both sides. Entries are never re-sorted afterwards: that would rewrite an append-only file. Each is dated, so readers order them.
- **Without git,** only one focus can be in the foreground at a time. See [state](state.md#without-git--fallback-only).

---

## Design notes

1. **Whether the rules remove overlap in use** is still to be seen. The evidence so far is one sphere's merge history ([Where overlap really happens](#where-overlap-really-happens)): it shows where the sharp edge is, not how common it is. Carved holds and append-only history are first used in 1.0.
2. **Changes that only make sense whole get no branch of their own,** not even opt-in. A branching model needs real machinery to get right, and nothing needs it yet. For a large restructure: checkpoint first, and revert by node if it goes wrong. When a real case needs more, a better model can be designed then.
3. **Offered changes wait in the sender's own `history.md`.** See [What's waiting](#the-tree). If that ever gets hard to follow, a single `offers.md` listing what's still unsettled is the next step; not before.
4. **The liveness threshold** is 30 minutes.
