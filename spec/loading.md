# Loading

_Status: draft 1, for review._ How a sphere decides what to read, and when, so that it stays fast and sharp as it grows: a small core that always loads, a manifest that says what else exists, and everything else read only when a task needs it.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

---

## The idea

A sphere that has been used for a year holds hundreds of lenses, frames, work nodes and topics. If every session read all of it, two things would go wrong:

- **It gets expensive.** Every session pays for the whole sphere, whatever the task.
- **It gets worse.** This is the bigger problem. A model given a very large context attends to it unevenly: what's in the middle gets less weight than what's at the start and end. Loading everything doesn't make the sphere better informed. It makes it *worse at the question in front of it.*

So loading is about quality first and cost second. — **proven**

**The scaling invariant:** _a session's cost scales with the breadth of the task, not the size of the sphere._ A narrow question in a large sphere should cost about what it costs in a small one. Three things make that hold:

1. **Bodies load on demand.** The text of a lens or frame is read only when it's used.
2. **The index is hierarchical, not flat.** The sphere sees a short list of what exists, and opens a level deeper only where the task points.
3. **Discovery shifts from loading to searching.** As a sphere grows, it finds things by looking them up rather than by having read them in advance.

_The evidence so far:_ one sphere cut its always-loaded engine from about 19 KB to about 5.5 KB by splitting it this way, with no loss in what it could do. The invariant hasn't yet been tested on a very large sphere.

---

## Four tiers — _decided, partly exercised_

| Tier | What | When it loads | How often |
|---|---|---|---|
| **1. Identity core** | Who the human is, who the AI is, the rules, the kernel of the engine | Every session, at startup | Always |
| **2. Capability manifest** | One line per lens: its job and when to load it; under each, its frames' scope and triggers | Every session, at startup | Always |
| **3. Frame text** | The full mechanics of a frame | When the frame is invoked | Often |
| **4. Lens text** | The full understanding behind a set of frames | When the *why* is in question: a judgment call, a change, evolution | Rarely |

**Eager loading carries knowing-what; lazy loading carries knowing-how.** At startup, the sphere knows *what it can do* and *when each thing applies*. It learns *how* only when it's about to do it.

This works because **a frame is self-sufficient to run** (see [protocol](protocol.md)). If running a frame required reading its lens, tier 4 would collapse into tier 3, and the lazy tiers would stop paying for themselves.

### The kernel split — _decided, partly exercised_

The core is split too. A small **kernel** loads every session: the state machine, the guards, the instincts that must always be on. The **deeper engine mechanics** (how evolution runs, how replication works, how the registries rebuild) load only when the sphere is being worked on, not when it's being used.

### The floor is governed — _decided, not yet exercised_

What loads every session is the **floor**, and floor creep is the one real per-session cost of a large sphere. Every addition seems small, and together they undo the whole model. So:

- **Admission to the floor is rare.** A thing earns its place by being needed in nearly every session, not by being important.
- **Admission is reversible.** Anything on the floor can be moved back to on-demand. Evolution's reflection looks at the floor's size and asks whether each item still earns its place.
- **The floor's size is visible.** The startup check reports it, so growth is noticed.

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

## work_tracking: how the human's work is held and moved forward
_Load when: adding, planning, reviewing or archiving work._
- `work_breakdown`: splitting a node into children. Trigger: "break this down", a node too big to act on.
- `work_progress`: measuring progress from what shipped. Trigger: "how's it going?", ground.
- `work_registry`: the work index. Trigger: a node added, moved or archived.
```

- **One entry per lens:** its job, and when to load it. **Under it, each frame:** its scope and its trigger.
- **If it isn't in the manifest, it doesn't exist.** The sphere doesn't go looking for capabilities by scanning folders. A lens or frame that should be used has to be in the manifest. This is the [registry pattern](registries.md#the-registry-pattern--proven) applied to capabilities.
- **It's AI-maintained, with a deterministic check.** Writing a good "when to load" line takes judgment, so the AI writes and updates the entries. The tooling checks the result: every lens and frame on disk has an entry, every entry points at a file that exists, and the content hash over the source files matches. A mismatch means the manifest is stale. See [registries](registries.md#three-ways-a-registry-is-maintained).
- **It's rebuilt at ground and whenever the sphere evolves.** A new frame isn't usable until the manifest knows about it.
- **It's markdown, in `core/manifest.md`, and it's committed.** It's a human-facing view: reading it is how a person sees what their sphere knows how to do.

### The machinery travels; the caches don't

A seed carries the **scripts and frames that build** the manifest and the startup bundle, never the built files. A new sphere builds its own on first start, from its own lenses and frames. A copied manifest would describe someone else's sphere.

---

## Discipline — _decided, partly exercised_

### At startup: the handshake slice

Startup reads only the **handshake slice** of each file it needs: the focused section, a status line, the frontmatter. Never the whole document. The full file loads on the command that needs it.

_An example already in the spec:_ the [work tree view](work.md) is built from node frontmatter alone. Opening the sphere shows every node's state without reading a single node's body.

### Mid-session

- **Don't re-read what's already loaded.** If a file was read this session and hasn't changed, use what's in context.
- **Stop at the shallowest depth** that answers the need (see [progressive disclosure](#progressive-disclosure--decided-not-yet-exercised)).
- **Prefer pointers to payloads.** Refer to a file by name instead of quoting it back. Summarize a long result instead of carrying all of it forward.
- **Let ground compact.** A long session doesn't have to carry everything it ever read. Ground saves what matters to files, and the next session starts clean from them.

---

## Session type — _decided, not yet exercised_

A session can carry a **type**: coding, brainstorming, planning, meeting review, research, sphere authoring. The type is a **hint for what to load up front, never a gate.** Everything stays reachable. If a coding session suddenly needs the meeting frames, they load on demand at the cost of one extra read.

The type is declared by the human (preferred), inferred from how the session opens, and changeable at any time. Which frames each type warms up is learned from use. _(Moved here from [state](state.md).)_

---

## Senses — _decided, not yet exercised_

- `lens-loaded`, `frame-loaded`: a body was read. Counted, so reflection can see what's actually used.
- `manifest-built`, `manifest-stale`: the manifest was rebuilt, or its hash no longer matches its sources.
- `startup-trimmed`: something was moved off the floor.
- `floor-grew`: something was added to the floor. Worth a second look.

---

## For a non-technical human

None of this is visible. They notice only that the sphere is quick, stays on topic, and doesn't slow down as it learns more about them.

---

## Open questions

1. **Measuring the invariant.** What's the test that shows a session's cost tracks the task, not the sphere? Probably a fixed set of narrow tasks, run against the same sphere at different sizes.
2. **Search at scale.** When discovery shifts to searching, is plain text search enough, or does a large sphere need an index built for it?
3. **Floor budget.** Should a build ship a size budget for the floor, or only report its size?
4. **Learned warm-up.** How does a sphere learn which frames a session type should warm up, without loading them all to find out?
