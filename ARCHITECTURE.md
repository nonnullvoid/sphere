# Sphere Architecture

_Deep reference for how Sphere works. This document is for two audiences: **curious power users** who want to understand what's happening under the hood, and **contributors and builders** who want to extend, fork, or build on top of Sphere. For an introduction, start with [README.md](README.md)._

---

## Boot Sequence

When you open a sphere, the AI reads three files in order. Everything else follows from this.

```
CLAUDE.md  →  sphere.md  →  core/
```

**`CLAUDE.md`** is the door. A single instruction pointing to `sphere.md`. Nothing else lives here — it exists because most AI tools look for `CLAUDE.md` as the entry point.

**`sphere.md`** is the orchestrator. It runs a startup sequence: reads the user's profile, principles, and persona, then reads the core instruction files. Ends by announcing the sphere is ready. It also holds the identity block (sphere name, personality, layer registry) and optionally a project table for WorkSphere variants.

**`core/`** is the engine room. Three files the AI reads every session:

| File | Role | What it contains |
|------|------|-----------------|
| `engine.md` | HOW | Runtime rules: layer discovery, senses, state machine, instincts, evolution protocol |
| `protocol.md` | WHAT + WHY | User intents as a compact table, abilities as command registries |
| `init.md` | SETUP | Onboarding conversation guide — triggered when profile is still placeholder content |

The AI reads `init.md` only when needed. `engine.md` and `protocol.md` are read every session.

---

## The Three Actors

| Actor | Role |
|-------|------|
| **User** | Evolutionary pressure — expresses intents that shape the sphere |
| **AI** | Consciousness — reads everything, composes across layers, evolves the system |
| **Sphere** | The entity — core + layers + surface, always in a consistent state |

The user talks naturally. The AI reads the sphere's full state and operates it. The sphere is the persistent structure that survives across sessions.

---

## Vocabulary

| Term | Level | What it is |
|------|-------|-----------|
| **Intent** | Why | What the user wants — a stable purpose |
| **Ability** | What | A sphere capability that serves an intent |
| **Command** | Vocabulary | The word the user says to invoke an ability |
| **Action** | How | A layer's local operation — file updates |
| **Instinct** | Automatic | An ability that fires without user invocation |
| **Sense** | Perception | How a layer notices events happening |
| **Layer** | Structure | A specialized region with internal state + actions |
| **Surface** | Projection | Where layers externalize artifacts for others to perceive |
| **State** | Condition | The sphere's current condition — all files at a point in time |
| **Evolve** | Evolution | The sphere develops new abilities from expressed intents |
| **Reflect** | Evaluation | Targeted: evaluate one intent or ability |
| **Deep-reflect** | Reorganization | Full structural reevaluation against all intents |
| **Absorb** | Import | Intelligently pull intents/abilities from another sphere |
| **Ground** | Handoff | End of session: compact working state into records |
| **Resume** | Handoff | Start of session: restore state from records |

---

## Lifecycle

```
Template → Init → Evolve/Use → Ground/Resume → Seed/Absorb
```

A **template** (from `sphere-templates/`) carries the full structural blueprint without any user data. **Init** brings a new sphere online — the AI reads `core/init.md` and walks the user through a conversational setup. The sphere **evolves** through use as the AI recognizes new intents and crystallizes abilities. At session boundaries, **ground** compacts state; **resume** restores it. Mature spheres can **seed** (produce new templates) or **absorb** improvements from other spheres.

---

## Execution Chain

```
Intent (why) → Ability (what) → Command (vocabulary) → Actions (layer operations) → State change
```

A command invokes an ability. The ability determines which layers participate. Each layer executes actions (file operations). The sphere transitions from one consistent state to another. Surface projections are updated where needed.

---

## The Three Zones

### Core (substrate)

The living engine. Three instruction files + user identity + long-term memory.

```
core/
├── engine.md       ← runtime rules (HOW)
├── protocol.md     ← intents + abilities (WHAT + WHY)
├── init.md         ← onboarding conversation guide (SETUP)
├── records/        ← compacted history, long-term memory
├── ai/
│   └── persona.md  ← who the AI is in this sphere
└── user/
    ├── profile.md      ← who the user is
    ├── principles.md   ← guiding principles
    └── preferences.md  ← communication style
```

`protocol.md` is the most-read file in the sphere. It holds the intent table at the top (what the user wants from this sphere) and the ability registry below (what commands exist, what they do, which layers they touch). When the sphere evolves, `protocol.md` is where new abilities are registered.

### Layers (implementation)

The how. Each layer has an **identity block** declaring: name, depth tier, dependencies, senses, data paths, init steps. Below that: action definitions — the file operations it performs when participating in an ability.

Layers write their own state. The AI reads `engine.md` to know the rules, reads `protocol.md` to know what to invoke, reads layers to know how to execute.

### Surface (projection field)

Where layers externalize rendered artifacts for others to perceive. Not build output — it's how layers make their state visible. Surface changes are published and not easily reverted.

---

## Directory Layout

### A sphere instance (what you run day-to-day)

```
[sphere]/
├── CLAUDE.md              ← door: entry point → sphere.md
├── sphere.md              ← orchestrator: startup sequence, identity, layer registry
├── core/
│   ├── engine.md          ← HOW: runtime rules
│   ├── protocol.md        ← WHAT+WHY: intents table + command registry
│   ├── init.md            ← SETUP: onboarding conversation guide
│   ├── records/           ← long-term memory
│   ├── ai/
│   │   └── persona.md
│   └── user/
│       ├── profile.md
│       ├── principles.md
│       └── preferences.md
├── layers/                ← installed layers
│   ├── [layer]/           ← directory layers (with data)
│   └── [layer].md         ← file layers (instructions only)
└── surface/               ← projected artifacts
```

### This repo (sphere-templates + layer-catalog)

```
sphere/
├── README.md
├── ARCHITECTURE.md
├── sphere-templates/      ← ready-to-use sphere templates
│   ├── base/              ← minimal starting point
│   └── work-sphere/       ← professional context
├── layer-catalog/         ← available layers to install (copy into layers/)
│   ├── projects/
│   ├── planning/
│   └── ...
└── core/                  ← shared reference files (assembled into templates)
    ├── engine.md
    ├── protocol.md
    └── init.md
```

---

## Layer Ecosystem

Layers co-evolve within a sphere. Like components in a system, they develop dependencies. This is a feature.

### Depth Tiers

| Depth | Role | Removal impact |
|-------|------|----------------|
| Foundation | Other layers depend on these | Breaking — coupled layers lose their anchor |
| Coupled | Need specific other layers | Safe if dependents also removed |
| Independent | Work standalone | Safe, no cascade |
| Utility | Optional tools | Safe, no cascade |

**Bootstrap order:** core → foundation → coupled → independent → utility.

### Identity Block

Every layer declares its identity at the top:

```markdown
## Identity
- **Name:** [layer name]
- **Depth:** foundation | coupled | independent | utility
- **Dependencies:** [layers this depends on, or "none"]
- **Senses:** [events this layer responds to]
- **Data paths:** [files/dirs this layer owns]
- **Init:** [what to do when this layer first activates]
```

The layer registry lives in `sphere.md` (name, path, depth). The engine does not read all layer files at startup — it loads them lazily when a command invokes them. `protocol.md` declares which layers each command touches. On first use in a session, the engine reads the layer file and checks its identity block for dependencies.

### Cross-Layer Communication

1. **Senses** — Layers declare which events they respond to. When an event occurs, the AI activates participating layers. No central registry.
2. **Surface** — Layers project artifacts; other layers read them. The filesystem is the shared medium.
3. **Consciousness** — The AI reads everything and composes cross-layer abilities without explicit wiring.

---

## Session Handoff: Ground and Resume

Spheres accumulate working state across a session. At natural breakpoints, `ground` compacts the session into records — decisions, project updates, context — so the next session can start clean without re-reading everything.

```
ground → records/ updated → session ends
resume → AI reads records/ → picks up from last known state
```

`resume [context]` can be scoped: `resume product-launch` restores just that project's context rather than the full sphere. This is the primary mechanism for continuity in long-running work.

The `ground` command is also the trigger for the AI to notice if anything should be committed (if git is present) and whether any surface projections need updating.

---

## Evolution (Intent-Driven)

The sphere evolves through natural conversation. The user never needs to understand layers, intents, or identity blocks — they just talk and the sphere adapts.

### Scope Assessment

Not everything needs structural evolution:

| Scope | Example | What happens |
|-------|---------|-------------|
| **One-off** | "Remind me to check on X tomorrow" | Just do it. No structural change. |
| **New command** | "Summarize my week differently" | Add a command to an existing ability. |
| **New ability** | "Help me prep for 1:1s" | Register a new ability on existing layers. |
| **New layer** | "Track my reading list with notes and progress" | Create a new layer — only when it needs its own persistent data. |

**Threshold for a new layer:** the capability needs its own files AND doesn't fit within an existing layer. Most requests are new commands or abilities on existing layers.

### Propose Before Implementing

The AI always proposes in plain language and waits for confirmation:

- "I can add a `weekly-summary` command that formats your week differently. Want me to set that up?"
- "Tracking a reading list is substantial enough to be its own layer. I'll create it with commands for adding books and logging progress. Okay?"

### Announce Naturally

After implementing, the AI tells the user what's available — not what files were written:

- "Done — say `prep 1:1 [name]` before your next meeting and I'll draft talking points."
- "Set up your reading list. Say `add book [title]` to add one, `reading list` to see everything."

No mention of intents, abilities, or identity blocks unless the user asks about internals.

---

## Reflection

Reflection is how the sphere stays healthy. Evolution adds capabilities; reflection evaluates and prunes them. The user doesn't need to say "reflect" — the AI recognizes natural expressions of friction, underuse, or curiosity.

### Natural Triggers

| What the user says | What it means | Type |
|-------------------|--------------|------|
| "Something feels off about project tracking" | Friction with a specific capability | Targeted |
| "I'm not using the meeting stuff much" | A capability may not be serving its intent | Targeted |
| "What can you do?" | User wants to discover capabilities | Targeted (exploratory) |
| "Can we simplify? There's too much going on" | Capabilities may have outgrown their usefulness | Deep |
| "What would you change about how we work?" | Open invitation for structural evaluation | Deep |
| `reflect` / `deep-reflect` | Explicit invocation (power users) | As named |

### Targeted Reflection

Evaluate one area of the sphere. The AI reads the relevant intent, its serving abilities, and the layers involved. Output is plain language — not a technical audit.

### Deep Reflection

Full structural evaluation across four axes:
- **Gaps** — something the user wants that has no capability
- **Bloat** — a capability that serves no real purpose
- **Misalignment** — a purpose being poorly served
- **Discovery** — something the user does repeatedly that isn't registered

Output is a brief health check: what's working, what's not being used, and what to change. Always propose, never auto-change.

### Reflection → Evolution Loop

Reflection findings feed directly into evolution:
- Gap → propose a new ability (scope assessment → propose → confirm)
- Bloat → propose removing or simplifying
- Misalignment → propose redesigning
- Discovery → propose crystallizing the pattern

This loop is the sphere's self-improvement cycle.

---

## State Machine

The sphere is always in a consistent state. Every command is a well-defined transition.

- **State** = contents of core/ + layers/ at any point
- **Transition** = command causing actions across layers
- **Compaction** = ground commits that compress working state into records

### Git as State Backend (Recommended, Not Required)

Git is the recommended implementation: commits = transitions, log = history, revert = undo. During `init`, the sphere checks for git and initializes if available. If git is not present, the sphere works normally — all commands function — but state management commands (`checkpoint`, `revert`, `undo`, `history`) become dormant.

| Command | What it does | Requires git |
|---------|-------------|-------------|
| `checkpoint [message]` | Save current state as a named checkpoint | Yes |
| `history` | Show recent state transitions | Yes |
| `revert` | Restore a previous checkpoint | Yes |
| `undo` | Revert the last state change | Yes |

Surface changes are not easily reverted even with git — they require intentional rollback.

---

## Replication

Spheres reproduce through templates and exchange improvements through absorption.

| Command | What it does |
|---------|-------------|
| `seed` | Extract skeleton — all structure, no data |
| `init` | Bootstrap new sphere from a template (conversational) |
| `absorb` | Pull improvements from another sphere |
| `compare` | Diff two spheres at intent/ability/layer level |

### The Seed

A seed (template) is a sphere stripped of state, keeping structure:
- Core files (`engine.md`, `protocol.md`, `init.md`) — full, they're instructions
- User files — templates with placeholders
- Layer identity blocks + action definitions — no data
- Surface — empty structure

**Non-lossy guarantee:** All instructions survive extraction. Only user data, project state, and surface projections are stripped.

**Partial layer selection:** When seeding with fewer layers, abilities that need missing layers become **dormant** — still listed in `protocol.md`, marked as needing specific layers. The blueprint is preserved; dormant entries show what's possible with additional layers.

### Export Modes

| Mode | What ships | Use case |
|------|-----------|----------|
| `[full]` | Intent + ability + layer implementation | Generic layers |
| `[pattern]` | Intent + ability description only | Coupled layers — target builds own version |
| `[skip]` | Nothing | Purely local |

---

## Three-Tier Model

Sphere supports a fork hierarchy for organizations:

```
sphere (public)              ← generic templates
    ↓ fork
org-sphere                   ← company instance with org-specific layers
    ↓ instance
user-sphere                  ← personal active workspace
```

**Transmission rules:**
- Structure and patterns flow up (seed/absorb)
- User data never flows up
- Each tier can add layers; lower tiers inherit from above

---

## UX Gradient

The sphere is designed to be usable at conversation level. Users don't need to understand the architecture.

### Concept Tiers

| Tier | What it unlocks | Concepts | How learned |
|------|----------------|----------|-------------|
| **Use** | Operate day-to-day | commands, ground/resume, "just describe what you want" | Init + reinforced always |
| **Understand** | Know how it's organized; shape it via reflect | intent (why), ability (named capability), layer (area), reflect (evaluate) | Summary block during evolution; `concepts` / `explain` on demand |
| **Extend** | Build layers, replicate spheres | senses, instincts, identity blocks, depth tiers, seed/absorb | Only when the user asks or tries something these handle |

The AI teaches concepts passively through use — not documentation. When a structural change occurs, the AI shows a summary block (`Intent: / Ability: / Commands:`) that teaches vocabulary through real examples. Users can actively pull via `concepts` (list all) or `explain [concept]` (deep dive on one).

**Design principle:** `engine.md` is the AI's manual, not the user's. Init is a conversation. The sphere should feel like talking to a capable assistant from session one.
