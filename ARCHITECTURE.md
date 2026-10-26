# Sphere Architecture

_SPHERE-ARCH 1.0, draft. The overview. Each section links to the chapter in [`spec/`](spec/README.md) that holds the detail._

---

## What a sphere is

A sphere is a **structure for working with AI over time**: a folder of plain files that holds what you're doing, what's true in your world, and how you think, organized so any AI harness or agent can pick it up and work with you as if it remembered everything.

It isn't an agent, a model or an app. It runs on whatever you already use: a coding harness, a desktop assistant, an agent platform. Those are runtimes; a sphere is the structure the runtime boots into.

Three things make it different from a memory feature:

- **It's yours, and it's readable.** Every piece of it is a file you can open, read, change, version and take to another tool.
- **It holds your understanding, not just facts.** The way you judge and decide is written down with you, where it shapes what the AI does. See [lenses](spec/protocol.md#lens--proven).
- **It grows with you.** When you notice a better way of working, you and the AI capture it together, and the sphere carries it forward.

---

## Who does what

| | Role |
|---|---|
| **The human** | The authority. Brings the understanding, sets the direction, decides. |
| **The AI** | Reads the sphere, does the work, drafts changes to the sphere itself, and proposes. It never decides on the human's behalf. |
| **The sphere** | The files. Always in one consistent state, surviving every session. |

The human doesn't need to understand the structure to use it. The AI operates it; the human talks.

---

## What's in a sphere

```
my-sphere/
├── CLAUDE.md, AGENTS.md     doors: what harnesses look for first, pointing to sphere.md
├── sphere.md                the orchestrator: startup sequence and identity at a glance
├── core/
│   ├── identity.json        id, name, version, and where this sphere was born from
│   ├── trust.json           spheres this one trusts, and what each may do
│   ├── engine.md            runtime rules: senses, instincts, the state machine
│   ├── ai/personas/         who the AI is in this sphere (one or more)
│   ├── user/persona.md      who the human is
│   ├── protocol/            lenses, frames, and the protocol registry
│   ├── modes/               switchable behaviors on top of a persona
│   ├── records/sessions/    one file per session
│   ├── layers.md            layer registry
│   └── surface.md           surface registry
├── layers/
│   ├── work/                what the human is changing
│   ├── world/               what's true: subjects, facts, history
│   ├── projections/         how views are rendered
│   └── …                    whatever else this sphere needs
└── surface/                 rendered views, live state, inbox and outbox
```

Two kinds of thing live in these folders:

- **Shape:** lenses that are safe to share, frames, registries, templates, tooling. Shape can be shared, and it's how good ideas move between spheres.
- **Substance:** the human's work, knowledge, principles and history. Substance never leaves the sphere.

**Data stays home; protocol travels.** See [replication](spec/replication.md).

---

## How it runs

**Startup.** The harness opens a door file, which points to `sphere.md`, which loads a small startup set: who the human is, who the AI is, the rules, and the registries that say where everything else lives. Everything else is read only when a task needs it.

**A session** starts from the last grounded state and ends by **grounding**. Ground compacts what happened into the sphere: the work's progress, proposed facts, a session record. Then it commits, staging only what the session touched. A new session with no memory of the last one can **resume** cold. See [state](spec/state.md).

**Work** is a set of nodes, each a folder with `work.md` (what it is) and `progress.md` (what happened). They're flat on disk, nested only by reference, and indexed by a generated view. See [work](spec/work.md).

**Knowledge** is facts about the human's world, each one dated and graded by where it came from, proposed at ground and never written automatically. See [knowledge](spec/knowledge.md).

**Projections** are the views people actually look at: dashboards, maps, a home page. They're rendered from the files, honest about how fresh they are, and never the source of truth. See [projections](spec/projections.md).

---

## How it grows

A sphere separates **why** from **how**:

- A **lens** holds the human's understanding: why something matters to them, in their own terms.
- A **frame** holds the mechanics derived from it: when it applies, what the sphere does. Every skill is a frame. Frames also include always-on guards, event-triggered instincts, and the sphere's own mechanics.

Lenses and frames are **co-authored**. The human brings the understanding; the AI drafts; the human reviews and iterates; nothing is captured without the human's instruction. When understanding changes, everything derived from it is revisited. See [protocol](spec/protocol.md).

**Guardrails** grow from near-misses: each one is a rule with its reason, kept few, and always overridable except where the human has marked it hard. See [guardrails](spec/guardrails.md).

---

## Principles

These run through every chapter:

1. **The human is the authority.** The AI proposes; the human decides.
2. **Truth lives in one place.** Everything else is a view of it, and views are checked, not trusted. See [registries](spec/registries.md).
3. **Everything is readable.** Plain files, plain words. If a human can't audit it, it doesn't belong in a sphere.
4. **Promise boundaries, not ambience.** A sphere guarantees what's true at the start and end of a session, not continuous perfection in between.
5. **Honest status.** Every chapter marks what's **proven** in daily use, what's **advanced** with known sharp edges, and what's still **unexercised**.
6. **Never against the human's will.** A sphere records where it came from and can compare itself to a published architecture, but nothing forces it to conform. See [versions](spec/VERSIONS.md).

---

## The chapters

| Chapter | What it covers |
|---|---|
| [protocol](spec/protocol.md) | Lenses, frames, skills, the registry, co-authoring, sharing levels |
| [state](spec/state.md) | Sessions at two levels, ground and resume, the session registry, commits |
| [work](spec/work.md) | Work nodes, depth as a dial, the index, archiving |
| [knowledge](spec/knowledge.md) | The world layer, graded and dated facts, facts about other people |
| [registries](spec/registries.md) | How each registry is maintained, and how drift is caught |
| [projections](spec/projections.md) | Views, freshness, static and served, the stack, surface |
| [guardrails](spec/guardrails.md) | Incident-born rules, keeping them few, overrides |
| [replication](spec/replication.md) | Seeds, absorb, compare, sphere identity, trusted spheres |
| [modes](spec/modes.md) | Personas, and switchable behaviors on top of them |
| [versions](spec/VERSIONS.md) | Architecture, build and sphere versions; upgrades; what's new in 1.0 |

For how to grow a sphere well, see [BUILDING.md](BUILDING.md).
