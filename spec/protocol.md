# Protocol

_Status: draft 3, for review._ How a sphere holds what it understands about its human, the mechanics it derives from that understanding, and the vocabulary that invokes them.

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

---

## Lens — **proven**

A lens captures **understanding that comes from the human's own experience**: how they judge, decide and work, in a form the AI can operate on. An AI has no independent path to this. It wasn't there for the experience, and more capability doesn't change that. The point of a lens isn't that it's provisional; it's that it **could only have come from you.**

A lens is:

- **Authored with the human.** The AI drafts it from what the human says; the human reviews and iterates until it's true to how they work. See [Co-authoring](#co-authoring-the-method).
- **Human-verified.** A lens isn't in force until the human has confirmed it.
- **Versioned and ongoing.** Understanding sharpens over time. A lens has a revision history, not a finished state.
- **About meaning, not facts.** "How I decide whether a meeting is worth my time" is a lens. "The design review is on Thursdays" is a fact, and belongs in the [knowledge](knowledge.md) layer.

_Example (generic):_ a lens on outbound communication might say: *anything that leaves the sphere under my name is me speaking; I'd rather be slow than wrong; I always want to see it first.*

## Frame — **proven**

A frame is the **operating mechanics derived from a lens**: when it applies, what the sphere reads and writes, and the steps it follows.

- A frame names the lens it derives from, once one has been co-authored. A frame without a lens still works, but it can't be re-derived when understanding changes.
- One lens usually yields several frames, often of different kinds.
- Frames are where the sphere gets precise; lenses are where it stays honest about why.

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

`protocol.md` is the single registry of the sphere's vocabulary. Each row is tagged with the lens and frame it comes from.

| Term | What it is |
|---|---|
| **Intent** | Something the human wants, stable over time ("know what's on my plate") |
| **Ability** | A capability that serves an intent ("plan my day") |
| **Command** | The words the human says to invoke an ability |
| **Instinct** | An ability that runs without being invoked, on a sense |
| **Sense** | An event the sphere notices (`session-started`, `work-grounded`, `decision-point`…) |

Builds ship a small core sense vocabulary (around 15 events). Spheres add their own as they grow.

---

## Layout

```
core/protocol/
├── README.md          the vocabulary, in plain words
├── protocol.md        the registry
├── lenses/
│   └── <lens>.md
└── frames/
    └── <lens-family>/
        ├── <frame>.md          guard, instinct or structural frame
        └── <skill-name>/
            └── SKILL.md        procedure frame, in the open Agent Skills format
```

Frames are grouped by the lens family they come from. — **proven** Procedure frames use the [Agent Skills format](https://agentskills.io/specification) as-is: a folder named after the skill (lowercase letters, numbers and hyphens), holding a `SKILL.md`. Skills a human imports before any lens exists go in `frames/_unattached/`. — _decided, not yet exercised_

At **core profile** this structure is present but never shown. A non-technical human never sees the words lens or frame. They see the sphere behave the way they asked. See [profiles](profiles.md).

## Frontmatter — _draft; confirm fields against current practice_

Lens:

```yaml
lens: outbound-comms
version: 3
updated: 2026-10-24
verified: true          # the human has confirmed this version
sharing: public         # public | protected | private
frames: [comms-guard, draft-message, unsent-drafts]
```

Guard, instinct or structural frame:

```yaml
frame: comms-guard
kind: guard             # guard | instinct | structural
lens: outbound-comms
version: 2
updated: 2026-10-24
```

Procedure frame. This is standard Agent Skills frontmatter. The sphere's fields go inside `metadata`, which the standard provides for exactly this, so the file stays a valid skill everywhere:

```yaml
name: draft-message
description: Drafts outbound messages in the human's voice for review. Use when preparing any email, comment or post.
metadata:
  sphere-lens: outbound-comms
  sphere-version: "2"
```

---

## Cascade — **proven**

Changes flow downward, and only as far as they need to:

| What changed | What gets re-evaluated |
|---|---|
| A lens | Every frame derived from it |
| A frame | The abilities, commands and instincts it defines |
| An ability or command | Nothing beyond itself |

Re-evaluating means checking that the frame still follows from the lens. Often nothing changes. When something does, the sphere proposes the change and the human confirms it, like any other edit.

## Governance — **proven**

**Prefer updating to adding, at every level.** Before creating a new lens, frame, ability or command, check whether an existing one should grow instead. A sphere that adds freely becomes hard to read and starts contradicting itself.

The ladder, from lightest to heaviest:

1. **One-off:** just do the thing. Nothing is recorded.
2. **Command:** a new way to invoke an existing ability.
3. **Ability:** a new capability inside an existing frame.
4. **Frame:** new mechanics under an existing lens.
5. **Lens:** new understanding. The heaviest step, because everything below it derives from it.

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

**A frame can't be more open than its lens** unless the human explicitly says so. A frame derived from a private lens often restates that lens's content in its mechanics, so it inherits the lens's level by default.

A private lens still shows up in an export as an **empty slot**. Another sphere can see *that* this sphere has a principles lens, never *what's in it*. Data stays home; protocol travels. See [replication](replication.md).

See [replication](replication.md).

---

## Open questions

1. **The four frame kinds.** Check them against a sphere in real use: does every frame fit one kind, or is there a fifth? (This replaces the earlier "frames wrap skills" idea. A procedure frame now *is* a skill, with no wrapper.)
2. **Optional commands.** _Under trial, not part of this spec._ Abilities invoked purely by intent matching, with fixed commands proposed only after a phrase repeats. The human decides whether to add one. To be trialed before inclusion.
3. **Names.** "Lens" may be renamed, along with the category sphere belongs to. Pending a dedicated naming session.
4. **Frontmatter fields.** The fields above are a first proposal. Confirm them against how lenses and frames are versioned in practice.
