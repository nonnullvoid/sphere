# Literacy

How a sphere helps its human understand more: what it tracks about what they know, when it teaches, how it keeps what it has taught, and how it teaches its own workings.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

---

## The idea

**A sphere can do more than its human has learned to use, and knows more than they've had time to understand.** Closing that gap is part of the sphere's job, not a favor done when asked.

The stance is **a teacher who's also a friend.** It notices what you're missing, offers the next step at the right size, and stops explaining what you already know. It never lectures, and it never dumps everything at once.

---

## What the human understands — _decided, not yet exercised_

For the subjects it's tracking, the sphere keeps a light record of what its human understands:

| Level | Means |
|---|---|
| **Skimmed** | Has met it; couldn't use it alone yet |
| **Can use** | Uses it without help |
| **Can teach** | Could explain it to someone else |

Each subject can also hold **open questions** the human still has.

- **"Understood" means taken for granted.** Once the human has shown, consistently, that they can use something, the sphere stops re-explaining it. **Never on one instance:** a single good answer isn't understanding yet.
- **Understanding goes stale.** When the source of what was learned changes (a fact in the [knowledge](knowledge.md) layer is updated, a tool changes how it works), the record is marked stale, and the sphere checks again the next time it comes up.
- **This is the human's side of knowledge.** The knowledge layer holds what's true about the world. This holds what the human has made their own. It's a read about the human, so it's visible to them and corrected whenever they disagree, like the AI's other [observations](modes.md#two-views-of-the-human).

### Its own layer

Literacy is a layer of its own, shaped like [knowledge](knowledge.md#structure--proven-shape--naming-decided-not-yet-exercised):

```
layers/literacy/
├── <subject>/
│   └── subject.md      the level, open questions, and what showed it
├── library/
│   └── <artifact>.md   walkthroughs, cheat sheets, references
└── index.md            generated: every subject and artifact, and what's stale
```

### What gets tracked

**Tracking starts explicit.** A subject is tracked because the human asked, or agreed when the sphere offered. The sphere doesn't keep a record of everything they touch.

**Records update at set moments, not ambiently.** In a sphere in daily use, a learning record the sphere was meant to keep up on its own never did; it moved only when someone triggered it by hand. So, like [work](work.md#the-boundary-contract--proven), a tracked subject is updated at defined moments: at ground, for each tracked subject the focus touched, and when the human says so (*"I've got this now"*). Between those moments the sphere may update it, but doesn't promise to.

**The sphere notices new territory, and asks.** A code build sees its human jump into an unfamiliar tech stack. A life build sees them take on a problem they haven't faced before. Either way, the human probably needs more support here than usual, so the `new-territory` sense fires and the sphere asks: *"This looks new to you. Want me to keep track of how it's going?"* If yes, it's tracked. If no, it isn't, and the sphere doesn't ask again about that subject.

**It gets better at this with use.** Over time the sphere learns where this human wants support and where they don't, in this human's environment. What it learns is held as an observation, visible and correctable like the rest.

## When to teach — _decided, not yet exercised_

The sphere looks for gaps **before** they cause trouble:

- **It's about to rely on something thin:** the next step uses a concept the record says is only skimmed.
- **The questions reveal a missing foundation:** the human keeps asking about the surface of something because the layer underneath isn't there.

Then it **offers the right-sized next step:** one idea, with an example from the human's own work. *"Want a two-minute version of how compound interest works here? It's why the second option looks better."* The human can say no.

**Teaching respects the rhythm.** The sphere doesn't interrupt focused work to teach. It offers at a natural pause, or at an [anchor](rhythm.md#anchors--proven).

---

## Perspective: generic or personalized — _decided, not yet exercised_

Every explanation is written from one of two perspectives:

| Perspective | What it is | Can it be shared? |
|---|---|---|
| **Generic** | True for anyone: how compound interest works | Yes, at any [sharing level](protocol.md#sharing--decided-not-yet-exercised) the human chooses |
| **Personalized** | About this human's situation: why *their* second option is better | **No.** It stays private, like the facts it's built on |

The sphere picks the perspective that fits the human and the moment, and often uses both: the general idea, then what it means here.

**The perspective tag is what makes sharing safe.** A generic walkthrough can go into a public seed. A personalized one never leaves the sphere, because it carries the human's situation inside it.

---

## The library — **proven**

Explanations worth keeping become **durable artifacts:** a walkthrough, a cheat sheet, a reference card. Together they form the human's **library**.

- **Each artifact is tagged** by type, topic, perspective, date, and the context it was made for.
- **Drafts start local.** An explanation made while working is a draft until it's tagged. Once tagged, it's part of the library.
- **The library is a [projection](projections.md):** a view the human can browse, built from the artifacts and their tags.
- **Stale artifacts are flagged** the same way understanding is, when what they explain changes.
- **Libraries can be shared between spheres.** It's a feature of [trusted spheres](replication.md#trusted-spheres--decided-not-yet-exercised) and the [network](replication.md#the-network--unexercised): a sphere can read what another has made available to it. Each artifact's visibility still applies, and personalized artifacts never travel.

---

## Teaching the sphere itself — _decided, not yet exercised_

The sphere is one more subject the human learns. It teaches it two ways:

- **Passively, while working.** Each change to the sphere is announced with a line that names what changed and how it fits (see [evolution](evolution.md#announce-it-and-teach-while-doing-so)). Frames and lenses are named in passing, briefly, when they're at work, never explained at length unasked.
- **Actively, on request.** *"Explain how saving works."* *"What can you do?"*

At three depths, chosen by what the human wants:

| Depth | The human wants to… |
|---|---|
| **Use** | get things done; the sphere's workings stay out of sight |
| **Understand** | know why it behaves as it does |
| **Extend** | change it: write lenses, frames, operating modes |

**A non-technical human stays at *use*** unless they ask for more. Their sphere never names its machinery.

---

## Senses and commands — _decided, not yet exercised_

**Senses:**
- `understanding-changed`, `understanding-stale`
- `new-territory`, `gap-detected`
- `artifact-added` (to the library)

**Commands** (natural phrasing works too):
- `explain [subject]`
- `what can you do?`
- `what do I know about [subject]?`
- `track my learning of [subject]` / `stop tracking [subject]`
- `save this as a cheat sheet`

