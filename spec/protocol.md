# Protocol

_Status: draft 4, for review._ How a sphere holds what it understands about its human, the mechanics it derives from that understanding, and the vocabulary that invokes them.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

---

## The idea

Skills and instructions tell an AI how to do a job. They don't give the human's own thinking anywhere to live. That thinking ends up in separate notes, disconnected from the behavior it should shape. A sphere gives it a home and connects it:

- **A lens holds why something matters to this person,** in their own understanding. It's the piece skills don't have.
- **A frame holds how the sphere acts on it:** when, what it reads and writes, step by step. Every skill is a frame.

Three things follow:

1. **Understanding has a place where it operates.** It isn't just notes the AI may or may not read.
2. **Lenses are acceptance criteria for work that has no test.** An agent can loop on a goal when something can check its work: tests, a build, a benchmark. When the only measure of "good" is the human's judgment, the lens is that judgment, written down.
3. **One change cascades.** Change a belief once, and you know exactly which frames to revisit. With flat skills, the same belief is copied implicitly into several of them, and they drift apart. — **proven**

**When a plain skill is enough:** a stable, one-off procedure doesn't need a lens. The split earns its keep when the same understanding drives several behaviors, or keeps changing.

```
Lens  ›  Frame  ›  Components
why      how       what it touches (data) and how it's invoked (vocabulary)
```

---

## Lens — **proven**

A lens captures **understanding that comes from the human's own experience**: how they judge, decide and work, in a form the AI can operate on. An AI has no independent path to this. It wasn't there for the experience, and more capability doesn't change that. The point of a lens isn't that it's provisional; it's that it **could only have come from you.**

**Understanding is not knowledge.** Knowledge is facts about the world: right or wrong, checkable, and held by the human and the AI alike. Understanding is meaning: what matters, what fits, what good looks like. Only the human brings that. "The design review is on Thursdays" is a fact, and belongs in the [knowledge](knowledge.md) layer. "How I decide whether a meeting is worth my time" is a lens. When something feels like both, split it: the fact goes to knowledge, the meaning to a lens.

A lens is:

- **Authored with the human.** The AI drafts it from what the human says; the human reviews and iterates until it's true to how they work. See [Co-authoring](#co-authoring-the-method).
- **Open to suggestion from any source, but confirmed by the human.** The human, an AI proposal or an observed pattern can all suggest a lens. None of them is in force until the human has confirmed it.
- **Versioned and ongoing.** Understanding sharpens over time. A lens has a revision history, not a finished state.

_Example (generic):_ a lens on outbound communication might say: *anything that leaves the sphere under my name is me speaking; I'd rather be slow than wrong; I always want to see it first.*

## Frame — **proven**

A frame is the **operating mechanics derived from one or more lenses**: when it applies, what the sphere reads and writes, and the steps it follows.

- **A frame names the lens or lenses it derives from,** once one has been co-authored. A frame without a lens still works, but it can't be re-derived when understanding changes.
- **A frame can derive from several lenses.** This is how two understandings get reconciled into one set of mechanics. For example, how far an agent may act on its own draws on what the human holds authority over *and* on how the work is structured.
- **One lens usually yields several frames,** often of different kinds.
- **Frames compose; they don't inherit.** Several frames are active at once during any piece of work. There's no frame hierarchy. Intents, abilities and frames relate many-to-many, by reference.
- **A frame is self-sufficient to run.** Executing a frame never requires reading its lens. If it does, the frame is underspecified. The lens is consulted when the *why* is in question: judgment calls, changes, evolution. That's also what lets a sphere load frames often and lenses rarely. See [registries](registries.md).
- **Modes live inside one frame.** Different ways of running the same activity (outbound messages sent normally, sent with a "drafted by AI" disclosure, or pre-approved for one narrow case) are sections of one frame, not sibling frames.

### Components — **proven**

What a frame contains falls into two kinds, and the split is what makes sharing safe:

| Component | What it is | Travels? |
|---|---|---|
| **Data locations** | The parts of `layers/` and `surface/` this frame reads and writes | **No.** Data stays home. |
| **Protocol entries** | The intents, abilities, commands and senses this frame defines | **Yes.** Protocol travels. |

A frame declares both in its frontmatter (below). That's what lets a sphere share *how* it works, frame by frame, without exposing *what* it holds.

### Every skill is a frame; not every frame is a skill

A **skill** is portable: it has to work on its own, in any agent that loads skills. Many frames only make sense inside a sphere. Frames come in four kinds: — _taxonomy to be checked against real spheres_

| Kind | Example | A skill? | Why |
|---|---|---|---|
| **Procedure:** invoked to do a task | plan my day; draft a PR description | **Yes** | Self-contained and used on request, so portable as a skill |
| **Guard:** always applies | outbound messages are drafted, never sent without approval | No | A skill loads only when relevant; a guard must apply to every action |
| **Instinct:** triggered by a sphere event | on ground, propose new facts for the knowledge layer | No | Fires on something the sphere notices, which needs the sphere's [senses](#the-registry--proven) |
| **Structural:** mechanics of the sphere itself | how ground reconciles the session registry | No | Meaningless outside a sphere |

**The test:** if it still works with the sphere taken away, it's a skill. Otherwise it's a frame that lives only inside the sphere.

_Example (generic):_ one lens on outbound communication (*anything that leaves under my name is me speaking; I'd rather be slow than wrong*) yields a **guard** (nothing is sent without approval), a **procedure** (how to draft a message the way I write) and an **instinct** (at ground, flag drafts left unsent). One understanding drives three kinds of mechanics, a link skills alone can't express.

### Framing a skill

**Framing** a skill makes it part of the sphere's protocol. A human can say *"frame this skill,"* or just *"learn this skill"* or *"import this skill."* Nobody needs to know the word frame. The sphere then:

1. **Copies the skill in unchanged** as a procedure frame. It keeps working as a skill everywhere.
2. **Registers what it can do:** its abilities, and its commands if the human uses any, in the registry.
3. **Offers to attach a lens,** co-authored as always: *"This skill assumes you always want to review a draft first. Want to capture why?"* The human can say no. An unattached skill is a complete frame.

Going the other way, a procedure frame **exports as a plain skill** with no translation. Other agents ignore the lens link. The other three kinds travel only through sphere [replication](replication.md). — _unexercised_

---

## The registry — **proven**

`protocol.md` is the single registry of the sphere's vocabulary. Each row is tagged with the frame (and through it, the lens) it comes from.

| Term | What it is |
|---|---|
| **Intent** | Something the human wants, stable over time ("know what's on my plate") |
| **Ability** | A capability that serves an intent ("plan my day") |
| **Command** | The words the human says to invoke an ability |
| **Instinct** | An ability that runs without being invoked, on a sense |
| **Sense** | An event the sphere notices (`session-started`, `work-grounded`, `decision-point`…) |

Builds ship a small core sense vocabulary (around 15 events). Spheres add their own as they grow. The protocol itself contributes two: `lens-shifted` and `frame-shifted` (see [Cascade](#cascade--proven)).

---

## Layout

```
core/protocol/
├── README.md          the vocabulary, in plain words
├── protocol.md        the registry
├── lenses/
│   └── <lens>.md
└── frames/
    ├── <frame>.md                 a frame that doesn't belong to a cluster yet
    ├── <lens-family>/
    │   ├── <frame>.md             guard, instinct or structural frame
    │   └── <skill-name>/
    │       └── SKILL.md           procedure frame, in the open Agent Skills format
    └── _unattached/               skills imported before any lens exists
```

**Grouping rules** — **proven**

1. **A frame's identity is its name, not its path.** References use the bare name. Finding a frame means searching `frames/` for that name at any depth, so moving a frame into a cluster breaks nothing.
2. **Group by lens family.** A cluster folder holds frames derived from the same lens, or from tightly coupled lenses.
3. **Cluster at three.** A frame stays flat at `frames/<name>.md` until at least three related frames exist.
4. **Lenses rarely group.** There's roughly one lens per concept. Keep them flat until a real family forms.
5. **Grouping is organization only.** It never changes a frame's lens, its cascade, or what it exports.

Procedure frames use the [Agent Skills format](https://agentskills.io/specification) as-is: a folder named after the skill (lowercase letters, numbers and hyphens), holding a `SKILL.md`. — _decided, not yet exercised_

For a **non-technical human**, this structure is present but never shown. They never see the words lens or frame. They see the sphere behave the way they asked. How plainly a sphere talks about itself is set by its [persona and modes](modes.md).

## Frontmatter — **proven** (shape) · _field names decided, not yet exercised_

Lens:

```yaml
type: lens
name: outbound-comms
version: 3
version_note: Added the exception for notes to myself.
derives_from: conversation 2026-10-24; a near-miss with an unreviewed reply
status: active               # active | drafting | deprecated
updated: 2026-10-24
verified: true               # the human has confirmed this version
sharing: public              # public | protected | private
frames: [comms-guard, draft-message, unsent-drafts]
```

Guard, instinct or structural frame:

```yaml
type: frame
name: comms-guard
kind: guard                  # guard | instinct | structural
lens: [outbound-comms]       # one or more
derives_from: [outbound-comms@3]
version: 2
version_note: Standing approvals now name their scope.
status: active
updated: 2026-10-24
reads: [layers/work]         # data locations: stay home
writes: []
protocol: [I-trust-what-leaves, A-review-outbound]   # protocol entries: travel
```

Procedure frame. This is standard Agent Skills frontmatter. The sphere's fields go inside `metadata`, which the standard provides for exactly this, so the file stays a valid skill everywhere. Its values are strings, so lists are comma-separated:

```yaml
name: draft-message
description: Drafts outbound messages in the human's voice for review. Use when preparing any email, comment or post.
metadata:
  sphere-lens: outbound-comms
  sphere-derives-from: outbound-comms@3
  sphere-version: "2"
  sphere-reads: layers/work
```

### Versioning and drift — _decided, not yet exercised_

- **Bump `version` on a substantive change:** a sharpening, a change of scope, a rename. Not for typos. `version_note` says what changed in this version.
- **A frame records the lens version it was derived against** (`derives_from: [outbound-comms@3]`). When the lens moves to version 4, the frame is behind, and a [drift check](registries.md#drift-checks--proven) can say so without reading either file's prose.
- **Full history lives in git.** A longer narrative history can be kept privately in `core/records/`, so a lens can be shared without the story of how it came to be.

---

## Cascade — **proven**

Changes flow downward, and only as far as they need to:

| What changed | What gets re-evaluated | Sense |
|---|---|---|
| A lens | Every frame derived from it, and their components | `lens-shifted` |
| A frame | The abilities, commands and instincts it defines | `frame-shifted` |
| An ability or command | Nothing beyond itself | — |

Re-evaluating means checking that the frame still follows from the lens. Often nothing changes. When something does, the sphere proposes the change and the human confirms it, like any other edit.

## Governance — **proven**

**Prefer updating to adding, at every level.** Before creating a new lens, frame, ability or command, check whether an existing one should grow instead. A sphere that adds freely becomes hard to read and starts contradicting itself.

- **A new lens** only when the understanding is genuinely distinct from every existing lens: not a sharpening, not a downstream rule, not a variation.
- **A new frame** only when its mechanics are structurally separate from every existing frame. A new *way* of doing the same activity is a mode inside the existing frame.
- **When in doubt,** surface the candidate to the human and let them decide.

How a change is sized, proposed, made and announced is in [evolution](evolution.md).

---

## Co-authoring: the method — **proven**

Lenses and frames are written by the AI from the human's input, review, feedback and iteration. Neither side can produce them alone. This is the method, not a shortcut around it:

1. **The human brings the understanding,** in their own words, ideally anchored in a concrete case: "last week I almost sent that before checking; I never want that again."
2. **The AI drafts** the lens or frame and says where it's guessing.
3. **The human reviews:** what's wrong, what's missing, what doesn't sound like them.
4. **Iterate** until it's true to how they work. Some take one pass; mechanics that touch tooling can take many rounds of trial and error.
5. **Crystallize only on concrete instruction.** The AI may notice a repeated pattern and *ask* whether to capture it. It never writes a lens or frame on its own initiative.

The human stays the authority throughout. The AI proposes; the human decides.

---

## Sharing — _decided, not yet exercised_

Every lens carries a **sharing level**, set when it's created:

| Level | Who can receive it | Typical lenses |
|---|---|---|
| **public** | anyone: published builds, open repositories | how projections should behave; why grounding matters |
| **protected** | recipients the human chooses when sharing | a team's working agreements; a family's routines |
| **private** | no one; it never leaves this sphere | the human's principles, rhythms, how they see themselves |

When a lens is created, the sphere **proposes a level as a best guess and confirms it with the human.** If it can't tell, it asks. If nobody answers, the lens is **private**. Moving a lens to a more open level later is an outbound decision, and the human approves it.

**A frame can't be more open than its lens** unless the human explicitly says so. A frame derived from a private lens often restates that lens's content in its mechanics, so it inherits the lens's level by default. A frame derived from several lenses inherits the most restrictive level among them.

A private lens still shows up in an export as an **empty slot**. Another sphere can see *that* this sphere has a principles lens, never *what's in it*. Data stays home; protocol travels. See [replication](replication.md).

---

## For an AI reading this sphere from outside — _unexercised_

A sphere's protocol is meant to be readable by another AI, such as another sphere's, without access to anything else. An AI given this folder should:

1. Read `README.md` for the vocabulary.
2. Read `protocol.md` for every intent, ability and command.
3. Read `lenses/` to see the understanding the sphere works from (shared lenses only; private ones appear as empty slots).
4. Read `frames/` to see how that understanding becomes mechanics.
5. **Not expect `layers/` or `surface/`.** Those hold the human's life and are never part of what's shared.

The protocol is enough to understand *how* a sphere operates. What it operates *on* stays home. This is what makes [spheres working with spheres](replication.md#trusted-spheres--decided-not-yet-exercised) possible without either one giving anything up.

---

## Open questions

1. **The four frame kinds.** Check them against a sphere in real use: does every frame fit one kind, or is there a fifth?
2. **Optional commands.** _Under trial, not part of this spec._ Abilities invoked purely by intent matching, with fixed commands proposed only after a phrase repeats. The human decides whether to add one. To be trialed before inclusion.
3. **Names.** "Lens" may be renamed, along with the category sphere belongs to. Pending a dedicated naming session.
4. **Lists in skill metadata.** The Agent Skills `metadata` map holds strings, so multi-lens procedure frames use comma-separated values. Confirm this reads well, or keep procedure frames single-lens.
