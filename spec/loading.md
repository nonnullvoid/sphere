# Loading

How a sphere decides what to read, and when, so that it stays fast and sharp as it grows: a small core that always loads, a manifest that says what else exists, and everything else read only when a task needs it.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

---

## The idea

A sphere that has been used for a year holds hundreds of lenses, frames, work nodes and topics. If every window read all of it, two things would go wrong:

- **It gets expensive.** Every window pays for the whole sphere, whatever the task.
- **It gets worse.** This is the bigger problem. A model given a very large context attends to it unevenly: what's in the middle gets less weight than what's at the start and end. Loading everything doesn't make the sphere better informed. It makes it *worse at the question in front of it.*

So loading is about quality first and cost second. — **proven**

**The scaling invariant:** _a window's cost scales with the breadth of the task, not the size of the sphere._ A narrow question in a large sphere should cost about what it costs in a small one. Three things make that hold:

1. **Bodies load on demand.** The text of a lens or frame is read only when it's used.
2. **The index is hierarchical, not flat.** The sphere sees a short list of what exists, and opens a level deeper only where the task points.
3. **Discovery shifts from loading to searching.** As a sphere grows, it finds things by looking them up rather than by having read them in advance.

_The evidence so far:_ one sphere cut its always-loaded engine from about 19 KB to about 5.5 KB by splitting it this way, with no loss in what it could do. The invariant hasn't yet been tested on a very large sphere.

### Measured for every build — _decided, not yet exercised_

What matters is the **cold-start context**: what a fresh window has read before it gives its first answer. Every build is measured on it:

1. Take the build's sample sphere at three sizes: as shipped, about ten times larger and about fifty times larger (filled with generated nodes).
2. Run the same set of narrow tasks on each, every one in a fresh window: *"when does the lease end?"*, *"capture an idea about X"*, *"resume the move focus"*.
3. Count what each window read before its first answer: startup files plus every read.

The build passes when the largest sphere costs about the same as the smallest, within a fifth more. A build that fails has let something grow onto the floor or into startup.

### An index, once a layer is big — _decided, not yet exercised_

Plain text search over files is fast; reading is what costs. So a layer that grows large gets an **index**: one generated file, one line per node (name, title, summary, path, last updated), built from frontmatter the nodes already carry. Search reads the index first and opens only what matches. A very large index splits by name prefix.

- **It arrives when it's needed,** not from the start: when a layer passes a few hundred nodes, or a search starts opening too many files. Because it's built entirely from frontmatter, adding it later costs nothing.
- **It's the one generated file that follows the nodes.** Ground updates only the lines for the nodes it touched (see [registries](registries.md)).
- **A faster cache is a swappable part.** At very large sizes a build may add a database, such as an SQLite file with full-text search, for ranked and structured queries. It's only ever a **cache**: kept out of git, rebuilt from the files at any time, never the source. Delete it and nothing is lost; search falls back to the files.

### A startup bundle, once startup is slow — _decided, not yet exercised_

Startup reads the same slices in every window: identity, the first section of the profile, the default persona, the engine, the guards and the manifest. In a young sphere that's a few short reads. In one used daily for months, the guards and the manifest have grown and it can be a dozen or more, and two windows can start from slightly different pictures depending on what each read.

The fix is a **startup bundle**: one generated file holding exactly those slices, in a fixed order, with a hash of its sources on its first line. A fresh window reads one file and starts from the same place every time.

- **It arrives when it's needed:** when the cold-start measure above shows startup is the cost, or windows start unevenly. A fresh sphere doesn't have one.
- **It's a cache, never a source.** Built by a script (not the AI, which would cost what it saves), gitignored, never exported. A stale bundle is never read: startup checks the hash and falls back to the files. Delete it and nothing is lost.
- **It's an optional frame,** not part of the common set: [startup-bundle](../common/optional/frames/sphere-framework/startup-bundle.md) says what it holds and how a sphere adopts it.

_The real test is a sphere in daily use for six months or more._ A fresh sphere's startup is short by construction, so a new build's first run can't show whether the bundle is needed.

---

## Four tiers — _decided, partly exercised_

| Tier | What | When it loads | How often |
|---|---|---|---|
| **1. Identity core** | Who the human is, who the AI is, the rules, the kernel of the engine | Every window, at startup | Always |
| **2. Capability manifest** | One line per lens: its job and when to load it; under each, its frames' scope and triggers; then the reactions table: for each sense, who reacts, when and how, in a line | Every window, at startup | Always |
| **3. Frame text** | The full mechanics of a frame | When the frame is invoked | Often |
| **4. Lens text** | The full understanding behind a set of frames | When the *why* is in question: a judgment call, a change, evolution | Rarely |

**Eager loading carries knowing-what; lazy loading carries knowing-how.** At startup, the sphere knows *what it can do* and *when each thing applies*. It learns *how* only when it's about to do it.

This works because **a frame is self-sufficient to run** (see [protocol](protocol.md)). If running a frame required reading its lens, tier 4 would collapse into tier 3, and the lazy tiers would stop paying for themselves.

### The kernel split — _decided, partly exercised_

The core is split too. A small **kernel** loads in every window: the state machine and every frame marked `always: true` (the guards). The **deeper engine mechanics** (how evolution runs, how replication works, how the registries rebuild) load only when the sphere is being worked on, not when it's being used.

### The floor is governed — _decided, not yet exercised_

What loads in every window is the **floor**, and floor creep is the one real per-window cost of a large sphere. Every addition seems small, and together they undo the whole model. So:

- **Admission to the floor is rare.** A thing earns its place by being needed in nearly every window, not by being important.
- **Admission is reversible.** Anything on the floor can be moved back to on-demand. Evolution's reflection looks at the floor's size and asks whether each item still earns its place.
- **The floor's size is visible.** The startup check reports it, so growth is noticed.
- **No size budget.** A sphere's files are small text. What matters is the cold-start context, and that's [measured for every build](#measured-for-every-build--decided-not-yet-exercised).

---

## Progressive disclosure — _decided, not yet exercised_

Anything the sphere might read has three depths:

| Depth | What it is | Example |
|---|---|---|
| **Stub** | One line: name and job | a manifest entry |
| **Index** | The next level of structure | a lens's list of frames; a domain's list of topics |
| **Full** | The whole text | the frame file itself |

**Stop at the shallowest depth that answers the need.** "Is there a frame for this?" is answered by a stub. "Which of these frames applies?" is answered by an index. Only "do it" needs the full text.

---

## The capability manifest — _decided, not yet exercised_

The manifest is the sphere's routing table: how it knows, at startup, everything it can do without reading any of it.

```markdown
<!-- Built 2026-10-27 at ground. Sources: core/protocol/lenses/**, core/protocol/frames/**.
     Hash: 3f9a1c… Do not edit by hand; change the lens or frame and it will be rebuilt. -->

## work-tracking: how the human's work is held and moved forward
_Load when: adding, planning, reviewing or archiving work._
- `work-breakdown`: splitting a node into children. Trigger: "break this down", a node too big to act on.
- `work-progress`: measuring progress from what shipped. Trigger: "how's it going?", ground.
- `work-registry`: the work index. Trigger: a node added, moved or archived.

## Reactions
focus-grounding
  knowledge-capture   with facts to offer             offer them as one batch
  work-registry       if it touched work              rebuild the index
stale-found knowledge
  plans               if a plan's assumption points at it   flag the plan for review
```

- **One entry per lens:** its job, and when to load it. **Under it, each frame:** its scope and its trigger.
- **Then the reactions table:** for each sense, the frames that react, each with its guard and a one-line action, keyed by tree for conditions about nodes. Built from the frames' When/do rows; see [senses and reactions](protocol.md#senses-and-reactions--decided-not-yet-exercised).
- **If it isn't in the manifest, it doesn't exist.** The sphere doesn't go looking for capabilities by scanning folders. A lens or frame that should be used has to be in the manifest. This is the [registry pattern](registries.md#the-registry-pattern--proven) applied to capabilities.
- **It's AI-maintained, with a deterministic check.** Writing a good "when to load" line takes judgment, so the AI writes and updates the entries. The tooling checks the result: every lens and frame on disk has an entry, every entry points at a file that exists, and the content hash over the source files matches. A mismatch means the manifest is stale. See [registries](registries.md#three-ways-a-registry-is-maintained).
- **It's rebuilt at ground and whenever the sphere evolves.** A new frame isn't usable until the manifest knows about it.
- **It's markdown, in `core/manifest.md`, and it's committed.** It's a human-facing view: reading it is how a person sees what their sphere knows how to do.

### The machinery travels; the caches don't

A seed carries the **frames and scripts that build** the manifest (and the startup bundle, where a sphere has one), never the built files. A new sphere builds its own on first start, from its own lenses and frames. A copied manifest would describe someone else's sphere.

---

## Discipline — _decided, partly exercised_

### At startup: the handshake slice

Startup reads only the **handshake slice** of each file it needs: the focused section, a status line, the frontmatter. Never the whole document. The full file loads on the command that needs it.

_An example already in the spec:_ the [work tree view](work.md) is built from node frontmatter alone. Opening the sphere shows every node's state without reading a single node's body.

### While working

- **Don't re-read what's already loaded.** If a file was read in this window and hasn't changed, use what's in context.
- **Stop at the shallowest depth** that answers the need (see [progressive disclosure](#progressive-disclosure--decided-not-yet-exercised)).
- **Prefer pointers to payloads.** Refer to a file by name instead of quoting it back. Summarize a long result instead of carrying all of it forward.
- **Let ground compact.** A long-running window doesn't have to carry everything it ever read. Ground saves what matters to files, and the next window attaches clean from them.
- **Hand off before the window degrades.** — **proven** When a window's context is well past half full, the sphere offers to ground and attach a fresh window to the same focus, while it can still write a good handoff. Waiting until attention has already slipped makes the handoff worse (see [why windows end](state.md#why-windows-end-and-why-thats-fine--proven)).

---

## Operating mode loadout — _decided, not yet exercised_

Every [operating mode](modes.md#operating-modes--decided-not-yet-exercised) (coding, brainstorming, planning, research…) carries a **loadout**: the frames worth warming up front for that kind of work. The floor always loads. The loadout is the only part that varies. It's **a hint, never a gate**: everything stays reachable, and if a coding focus suddenly needs the meeting frames, they load on demand at the cost of one extra read.

The operating mode is declared by the human (preferred), inferred from how the work opens, and changeable at any time.

**Which frames a loadout warms is learned from use.** A build starts each operating mode with a best guess. When a focus closes, the frames it read are noted in its history, along with its operating mode. Over time that shows how often each frame is needed in each mode. A frame read in most focuses of a mode (a build sets the share, say seven in ten) is offered for that mode's loadout; one that sits unused is offered for removal. This is low priority: any frame can load on demand anyway, so a missing warm-up costs one extra read.

---

## Senses — _decided, not yet exercised_

- `floor-grew`: something was added to the floor. Worth a second look.
- `stale-found` for the manifest: its hash no longer matches its sources.

What gets loaded isn't a sense: the frames a focus used are recorded when it closes, which is what loadouts learn from. A rebuilt manifest or a trimmed floor is a record in the ground that did it.

---

## For a non-technical human

None of this is visible. They notice only that the sphere is quick, stays on topic, and doesn't slow down as it learns more about them.

---

## Open questions

_None open._
