# Protocol

How a sphere holds what it understands about its human, the mechanics it derives from that understanding, and the vocabulary that invokes them.

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

- **Authored with the human.** The AI drafts it from what the human says; the human reviews and iterates until it's true to how they work. See [Co-authoring](#co-authoring-the-method--proven).
- **Open to suggestion from any source, but confirmed by the human.** The human, an AI proposal or an observed pattern can all suggest a lens. None of them is in force until the human has confirmed it.
- **Versioned and ongoing.** Understanding sharpens over time. A lens has a revision history, not a finished state.

_Example (generic):_ a lens on outbound communication might say: *anything that leaves the sphere under my name is me speaking; I'd rather be slow than wrong; I always want to see it first.*

## Frame — **proven**

A frame is the **operating mechanics derived from one or more lenses**: when it applies, what the sphere reads and writes, and the steps it follows.

- **A frame names the lens or lenses it derives from,** once one has been co-authored. A frame without a lens still works, but it can't be re-derived when understanding changes.
- **A frame can derive from several lenses.** This is how two understandings get reconciled into one set of mechanics. For example, how far an agent may act on its own draws on what the human holds authority over *and* on how the work is structured.
- **One lens usually yields several frames,** each doing a different job.
- **Frames compose; they don't inherit.** Several frames are active at once during any piece of work. There's no frame hierarchy. Intents, abilities and frames relate many-to-many, by reference.
- **A frame is self-sufficient to run.** Executing a frame never requires reading its lens. If it does, the frame is underspecified. The lens is consulted when the *why* is in question: judgment calls, changes, evolution. That's also what lets a sphere load frames often and lenses rarely. See [loading](loading.md).
- **A frame composes the gates it uses; it isn't their child.** A skill that passes through approval steps (a review runbook, say) names the guards it uses. Filing it under one of their lenses would flatten it into a detail of that lens.
- **Variants live inside one frame.** Different ways of running the same activity (outbound messages sent normally, sent with a "drafted by AI" disclosure, or pre-approved for one narrow case) are sections of one frame, not sibling frames.

### Components — **proven**

What a frame contains falls into two kinds, and the split is what makes sharing safe:

| Component | What it is | Travels? |
|---|---|---|
| **Data locations** | The parts of `layers/` and `surface/` this frame reads and writes | **No.** Data stays home. |
| **Protocol entries** | The intents, abilities, commands and senses this frame defines | **Yes.** Protocol travels. |

A frame declares both in its frontmatter (below). That's what lets a sphere share *how* it works, frame by frame, without exposing *what* it holds.

### Every skill is a frame; not every frame is a skill

A **skill** is portable: it has to work on its own, in any agent that loads skills. Many frames only make sense inside a sphere: a rule that must hold on every action, a reaction to something the sphere notices, the mechanics of a registry.

**The test:** if it still works with the sphere taken away, it's a skill. Otherwise it's a frame that lives only inside the sphere.

**Frames aren't sorted into kinds.** One frame often does several jobs: a rule, a way of doing something, a reaction to an event. Splitting it to fit a category would help no one. A frame declares only what changes how it's used:

| What it declares | How | What follows |
|---|---|---|
| It must apply in every window | `always: true` | It loads in the [kernel](loading.md), before any action. Frames like this are called **guards** |
| It reacts to something the sphere notices | senses in its `protocol:` list | The sphere wires it to those [senses](#the-registry--proven) |
| It works without the sphere | written as a skill, a `SKILL.md` | It can travel as a plain skill |

Everything else loads when a focus needs it.

_Example (generic):_ one lens on outbound communication (*anything that leaves under my name is me speaking; I'd rather be slow than wrong*) yields a **guard** (nothing is sent without approval), a **skill** (how to draft a message the way I write) and a frame that **reacts at ground** (flag drafts left unsent). One understanding drives all three, a link skills alone can't express.

### Framing a skill

**Framing** a skill makes it part of the sphere's protocol. A human can say *"frame this skill,"* or just *"learn this skill"* or *"import this skill."* Nobody needs to know the word frame. The sphere then:

1. **Copies the skill in unchanged** as a skill frame. It keeps working as a skill everywhere.
2. **Registers what it can do:** its abilities, and its commands if the human uses any, in the registry.
3. **Offers to attach a lens,** co-authored as always: *"This skill assumes you always want to review a draft first. Want to capture why?"* The human can say no. An unattached skill is a complete frame.

Going the other way, a skill frame **exports as a plain skill** with no translation. Other agents ignore the lens link. Every other frame travels only through sphere [replication](replication.md). — _unexercised_

---

## The registry — **proven**

`protocol.md` is the single registry of the sphere's vocabulary. Each row is tagged with the frame (and through it, the lens) it comes from.

| Term | What it is |
|---|---|
| **Intent** | Something the human wants, stable over time ("know what's on my plate") |
| **Ability** | A capability that serves an intent ("plan my day") |
| **Command** | The words the human says to invoke an ability |
| **Reaction** | What a frame does when a sense fires, without being asked: a When/do row that starts with the sense |
| **Sense** | A moment or condition the sphere notices (`focus-opened`, `focus-grounding`, `waiting-on-human`…) |

**Commands are optional** — _decided, not yet exercised_. Asking in plain words always works: the sphere matches what the human says to an ability through its intents, so nobody has to learn a command to use one. A fixed command is only a shortcut. When the human uses the same phrase for the same ability a third time, the sphere offers to keep it as a command (*"You've asked 'what's on my plate' a few times. Keep that as a shortcut?"*); the human decides. A sphere can run its whole life with no commands at all, which is how a non-technical build starts.

Builds ship a small core of senses; spheres add their own as they grow. The protocol itself contributes two: `lens-shifted` and `frame-shifted` (see [Cascade](#cascade--proven)). How senses work is below.

---

## Senses and reactions — _decided, not yet exercised_

A sphere has no event bus. A **sense** is the name of a moment the AI is told to watch for, and what follows it is a lookup, not a load. The full mechanics are in the [reactions](../common/core/protocol/frames/sphere-framework/reactions.md) frame.

**Who produces a sense:**

| Producer | Examples |
|---|---|
| **The `sphere` script** prints it | `focus-opened`, `focus-attached` |
| **A check** reports it: a finding is the condition | `stale-found`, `check-failed`, `dirty-detected` |
| **The AI, as it begins something** | `focus-grounding`, `focus-closing`, `day-wrapped`, `reflection-started` |
| **The AI's judgment** (best effort; the manifest's trigger line tells it to look) | `waiting-on-human`, `work-stalled`, `gap-detected` |

A ground's reactions run before its commit, so what they write lands with the work that caused them. That's why the sense is `focus-grounding`, not *grounded*.

**Three kinds of thing get confused with each other:**

| Kind | What it is | Is it a sense? |
|---|---|---|
| **Moment** | A point in the sphere's life many frames hook: a focus opens, a ground begins, the day starts | Yes: the **core moments**, about a dozen, that every build has |
| **Condition** | Something one frame notices that needs action: stale, conflicting, unsafe | Yes, living in that frame |
| **Record** | Something the sphere did: an idea captured, a template extracted | **No.** The history entry, ledger line or commit is the record; growth and reflection read records |

**The reactions table.** A frame reacts in its When/do table: the When cell starts with the sense in backticks, and whatever follows is a guard (`` `focus-grounding`, with facts to offer ``). The AI gathers these rows into the [manifest](loading.md#the-capability-manifest--decided-not-yet-exercised) as a **reactions table**, one block per sense. When a sense fires, the AI reads its block (already in context), skips rows whose guard doesn't apply, and does each one-line action, opening a frame only when it needs that frame's mechanics.

**Conditions find their frame by tree.** A condition about a node carries its [link](../common/core/protocol/frames/nodes/node-names.md#links): `stale-found knowledge:money.taxes` reaches the rows for `stale-found knowledge`, and `stale-found projection:monthly-budget` reaches the projection rows. One word to learn, eight kinds of stale, no guessing from context. A gap (a kind a check can produce with no row) is a manifest-check finding.

**Common sense grows out of reactions.** A habit the human repeats at the same moment three times is offered as a reaction; reactions several frames share become one row; reactions found in many spheres are what the common set ships. Nothing adopts itself: the sphere offers, the human decides.

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
    │   ├── <frame>.md             a frame
    │   └── <skill-name>/
    │       └── SKILL.md           a skill frame, in the open Agent Skills format
    └── _unattached/               skills imported before any lens exists
```

**Grouping rules** — **proven**

1. **A frame's identity is its name, not its path.** References use the bare name. Finding a frame means searching `frames/` for that name at any depth, so moving a frame into a cluster breaks nothing.
2. **Group by lens family.** A cluster folder holds frames derived from the same lens, or from tightly coupled lenses.
3. **Cluster at three.** A frame stays flat at `frames/<name>.md` until at least three related frames exist.
4. **Lenses rarely group.** There's roughly one lens per concept. Keep them flat until a real family forms.
5. **Grouping is organization only.** It never changes a frame's lens, its cascade, or what it exports.

Skill frames use the [Agent Skills format](https://agentskills.io/specification) as-is: a folder named after the skill (lowercase letters, numbers and hyphens), holding a `SKILL.md`. — _decided, not yet exercised_

For a **non-technical human**, this structure is present but never shown. They never see the words lens or frame. They see the sphere behave the way they asked. How plainly a sphere talks about itself is set by its [persona and modes](modes.md).

## Frontmatter — **proven** (shape) · _field names decided, not yet exercised_

**One shape for every lens and frame,** in every sphere and every build, the common set included. The first key says what the file is and names it: `lens:` in a lens, `frame:` in a frame. Inside a frame, `lens:` names the lens or lenses it derives from.

Lens:

```yaml
lens: outbound-comms
version: 3
version_note: Added the exception for notes to myself.
derives_from: conversation 2026-10-24; a near-miss with an unreviewed reply
status: active               # active | drafting | deprecated
updated: 2026-10-24
verified: true               # the human has confirmed this version
sharing: public              # public | protected | private; optional until: <date>
frames: [comms-guard, draft-message, unsent-drafts]
```

Any other frame:

```yaml
frame: comms-guard
always: true                 # optional: applies in every window (a guard)
lens: [outbound-comms]       # one or more
derives_from: [outbound-comms@3]
version: 2
version_note: Standing approvals now name their scope.
status: active
updated: 2026-10-24
sharing: public              # defaults to its lens's level, never more open unless the human says so
reads: [layers/work]         # data locations: stay home
writes: []
protocol: [I-trust-what-leaves, A-review-outbound, draft-left-unsent]   # intents, abilities, senses: travel
```

- **Data locations** (`reads`, `writes`) are paths. They never travel; an exported frame keeps the fields and drops the values.
- **Protocol entries** (`protocol`) travel. Intents are `I-…`, abilities `A-…`, and senses go by their own event names (`focus-grounding`). Each entry is defined in the registry, `protocol.md`.
- **Empty is explicit.** A guard that reads and writes nothing says `reads: []`, so "touches no data" is a statement, not an omission.

Skill frame. This is standard Agent Skills frontmatter. The same fields go inside `metadata`, prefixed `sphere-`, which the standard provides for exactly this, so the file stays a valid skill everywhere. Its values are strings, so lists are comma-separated:

```yaml
name: draft-message
description: Drafts outbound messages in the human's voice for review. Use when preparing any email, comment or post.
metadata:
  sphere-lens: outbound-comms
  sphere-derives-from: outbound-comms@3
  sphere-version: "2"
  sphere-version-note: Learned the short-reply form.
  sphere-status: active
  sphere-updated: "2026-10-24"
  sphere-sharing: public
  sphere-reads: layers/work
  sphere-writes: ""
  sphere-protocol: I-trust-what-leaves, A-draft-message
```

### Versioning and drift — _decided, not yet exercised_

- **Bump `version` on a substantive change:** a sharpening, a change of scope, a rename. Not for typos. `version_note` says what changed in this version.
- **A frame records the lens version it was derived against** (`derives_from: [outbound-comms@3]`). When the lens moves to version 4, the frame is behind, and a [drift check](registries.md#drift-checks--proven) can say so without reading either file's prose.
- **Full history lives in git.** A lens or frame file may carry a short changelog of *what* changed. **The story of *why* (the incidents, the people, the dates) lives privately in `core/records/`,** with a pointer in the file. Placement keeps it private: a lens can be shared without the story of how it came to be, and nothing needs scrubbing first. See [replication](replication.md#history-stays-home-by-placement).

---

## Cascade — **proven**

Changes flow downward, and only as far as they need to:

| What changed | What gets re-evaluated | Sense |
|---|---|---|
| A lens | Every frame derived from it, and their components | `lens-shifted` |
| A frame | The abilities, commands and reactions it defines | `frame-shifted` |
| An ability or command | Nothing beyond itself | — |

Re-evaluating means checking that the frame still follows from the lens. Often nothing changes. When something does, the sphere proposes the change and the human confirms it, like any other edit.

## Governance — **proven**

**Prefer updating to adding, at every level.** Before creating a new lens, frame, ability or command, check whether an existing one should grow instead. A sphere that adds freely becomes hard to read and starts contradicting itself.

- **A new lens** only when the understanding is genuinely distinct from every existing lens: not a sharpening, not a downstream rule, not a variation.
- **A new frame** only when its mechanics are structurally separate from every existing frame. A new *way* of doing the same activity is a variant inside the existing frame.
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

**Time-bound sharing.** Any level more open than private can carry an end date, `until: 2026-12-31`. After that date the lens reverts to private, and exports and catalogs stop including it. It's useful for publishing something for a while: alongside a talk, or for a trial with a collaborator.

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

_None open._
