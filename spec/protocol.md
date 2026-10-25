# Protocol

_Status: draft 1, for review._ How a sphere holds what it understands about its human, the mechanics it derives from that understanding, and the vocabulary that invokes them.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

---

## The idea

Most AI setups give the model instructions: do this, never do that. A sphere separates two things that instructions mix together:

- **Why something matters to this person**, in their own understanding. This is a **lens**.
- **How the sphere acts on it**: when, what it reads and writes, step by step. This is a **frame**.

Keeping them apart is what lets a sphere grow without turning into a pile of rules. When the understanding changes, the mechanics are re-derived from it. When the mechanics break, the understanding they serve is still there to rebuild from. — **proven**

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

- Every frame names the lens it derives from. A frame without a lens is a rule with no reason, and it can't be re-derived when things change.
- One lens usually yields several frames.
- Frames are where the sphere gets precise; lenses are where it stays honest about why.

_Example (generic):_ from the outbound-communication lens above, an `external_comms` frame: *any message, comment or post the sphere prepares is drafted and shown to the human; nothing is sent without explicit approval; drafts are kept with the work they belong to.*

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
        └── <frame>.md
```

Frames are grouped by the lens family they come from. — **proven**

At **core profile** this structure is present but never shown. A non-technical human never sees the words lens or frame. They see the sphere behave the way they asked. See [profiles](profiles.md).

## Frontmatter — _draft; confirm fields against current practice_

Lens:

```yaml
lens: external_comms
version: 3
updated: 2026-10-24
verified: true          # the human has confirmed this version
frames: [external_comms]
```

Frame:

```yaml
frame: external_comms
lens: external_comms
version: 2
updated: 2026-10-24
reads: [layers/work]
writes: [layers/work]
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

## What travels — **unexercised** beyond one export

The protocol is the part of a sphere that can be shared; the human's data never is. Data stays home, protocol travels.

- **Mechanism lenses** (how projections work, how sessions ground) can be shared and published.
- **Self-lenses** (a person's principles, rhythms, how they position themselves) never travel. Builds ship them as empty **slots**, to be co-authored in each sphere.

See [replication](replication.md).

---

## Open questions

1. **Frames wrapping skills.** _Under trial, not part of this spec._ The frame would keep the why and the when, and a portable skill file would hold the how where it's stable. To be trialed on one real frame before inclusion.
2. **Optional commands.** _Under trial, not part of this spec._ Abilities invoked purely by intent matching, with fixed commands proposed only after a phrase repeats. The human decides whether to add one. To be trialed before inclusion.
3. **Names.** "Lens" may be renamed, along with the category sphere belongs to. Pending a dedicated naming session.
4. **Frontmatter fields.** The fields above are a first proposal. Confirm them against how lenses and frames are versioned in practice.
