# Sphere Architecture

_Deep reference for how Sphere works. For getting started, see [README.md](README.md)._

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

Sphere uses a consistent vocabulary across all operations.

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
| **State** | Condition | The sphere's current condition (all files) |
| **Evolve** | Evolution | The sphere develops new abilities from expressed intents |
| **Reflection** | Evaluation | Targeted: evaluate one intent or ability |
| **Deep-reflection** | Reorganization | Full structural reevaluation against all intents |
| **Absorb** | Import | Intelligently pull intents/abilities from another sphere |
| **Init** | Bootstrap | A new sphere coming online from a seed |
| **Ground** | Handoff | Persist session knowledge so any new session can pick up instantly |

---

## Lifecycle

```
Seed → Init → Evolve/Use → Seed/Absorb
```

A **seed** carries the full structural blueprint without any user data. **Init** brings a new sphere online — the AI reads the seed and walks the user through a conversational setup. The sphere **evolves** through use as the AI recognizes new intents and crystallizes abilities. Mature spheres can **seed** (produce new seeds) or **absorb** improvements from other spheres.

---

## Execution Chain

```
Intent (why) → Ability (what) → Command (vocabulary) → Actions (layer operations) → State change
```

A command invokes an ability. The ability determines which layers participate. Each layer executes actions (file operations). The sphere transitions from one consistent state to another. Surface projections are updated where needed.

---

## The Three Zones

### Core (substrate)

The living engine. Three instruction files + user identity + long-term memory:

- `engine.md` — runtime: layer discovery, senses dispatch, instincts, evolution protocol, state machine rules
- `intents.md` — why: user purposes, stable compass, reflection axis
- `abilities.md` — what: shared vocabulary + command registry. The most-read file — defines what the sphere can do and what each word means
- `ai/persona.md` — who the AI is in this sphere: identity, working style, learned behaviors
- `user/` — identity: profile, principles, preferences, voice/style (sphere-variant specific)
- `records/` — compacted history: cross-cutting decisions, long-term memory

### Layers (implementation)

The how. Each layer has an **identity block** declaring: name, depth tier, dependencies, senses, data paths, init steps. Below that: action definitions — the file operations it performs when participating in an ability.

Layers write their own state. The AI reads abilities.md to know what to invoke, reads layers to know how to execute.

### Surface (projection field)

Where layers externalize rendered artifacts for others to perceive. Not build output — it's how layers make their state visible. Surface changes are published and not easily reverted.

---

## Repository Layout

```
sphere/
├── README.md
├── ARCHITECTURE.md        ← this file
├── core/                  ← plug-and-play sphere mechanism (reference implementation)
│   ├── README.md
│   ├── engine.md          ← runtime rules
│   ├── intents.md         ← user purposes
│   ├── abilities.md       ← command vocabulary + registry
│   ├── ai/
│   │   └── persona.md
│   └── user/
│       ├── profile.md
│       ├── principles.md
│       ├── preferences.md
│       └── roles.md
├── layer-catalog/         ← reusable, self-contained layer extensions
│   ├── README.md
│   ├── projects/          ← track active work (foundation layer)
│   ├── domain/            ← professional domain context (independent)
│   ├── philosophy/        ← examined worldview (foundation)
│   └── wellness/          ← health and capacity context (independent)
└── sphere-templates/      ← pre-assembled spheres ready to use
    ├── base/              ← minimal sphere, no layers (start here)
    ├── work-sphere/       ← professional work (projects + domain + planning)
    └── life-sphere/       ← whole-life lens (projects + philosophy + wellness)
```

---

## Deployed Sphere Layout

When a sphere is actually deployed (user runs it), the directory looks like this:

```
[sphere]/
├── CLAUDE.md              ← startup loader (minimal — just @sphere.md)
├── sphere.md              ← slim orchestrator: startup sequence, identity, layer registry
├── init.md                ← init guide for new users
├── core/
│   ├── engine.md          ← runtime rules
│   ├── intents.md         ← user purposes
│   ├── abilities.md       ← command vocabulary + registry
│   ├── ai/
│   │   └── persona.md     ← who the AI is in this sphere
│   └── user/
│       ├── profile.md     ← who the user is
│       ├── principles.md  ← guiding principles
│       └── preferences.md ← working style
├── layers/                ← installed layers
│   └── [layer]/
└── surface/               ← projected artifacts
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

The layer registry lives in `sphere.md` (name, path, depth). The engine loads layers lazily — only when a command invokes them. `abilities.md` declares which layers each command touches.

### Cross-Layer Communication

1. **Senses** — Layers declare which events they respond to. When an event occurs, the AI activates participating layers. No central registry.
2. **Surface** — Layers project artifacts; other layers read them. The filesystem is the shared medium.
3. **Consciousness** — The AI reads everything and composes cross-layer abilities without explicit wiring.

---

## Evolution (Intent-Driven)

The sphere evolves through natural conversation. The user never needs to understand layers, intents, or identity blocks — they just talk and the sphere adapts.

### Scope assessment

| Scope | Example | What happens |
|-------|---------|-------------|
| **One-off** | "Remind me to check on X tomorrow" | Just do it. No structural change. |
| **New command** | "Summarize my week differently" | Add a command to an existing ability. |
| **New ability** | "Help me prep for 1:1s" | Register a new ability on existing layers. |
| **New layer** | "Track my reading list with notes and progress" | Create a new layer — only when it needs its own persistent data. |

### Announce naturally

After implementing, the AI tells the user what's available — not what files were written. A summary block teaches vocabulary through real examples:

```
Intent: [purpose this serves]
Ability: [capability name]
Commands: [what the user can say]
```

---

## State Machine

The sphere is always in a consistent state. Every command is a well-defined transition.

- **State** = contents of core/ + layers/ at any point
- **Transition** = command causing actions across layers
- **Compaction** = `ground` = summary commit that compacts working state into records

### Git as state backend (recommended, not required)

Git is the recommended implementation: commits = transitions, log = history, revert = undo. During `init`, the sphere checks for git and initializes if available. If git is not present, the sphere works normally — all commands function — but state management commands (`checkpoint`, `revert`, `undo`, `history`) become dormant.

---

## Replication

Spheres reproduce through seeds and exchange improvements through absorption.

| Command | What it does |
|---------|-------------|
| `seed` | Extract skeleton — all structure, no data |
| `init [name] [seed]` | Bootstrap new sphere from a seed (conversational) |
| `absorb [source]` | Pull improvements from another sphere |
| `compare [other]` | Diff two spheres at intent/ability/layer level |

### The Seed

A seed is a sphere stripped of state, keeping structure:
- Core files (engine, intents, abilities) — full, they're instructions
- User files — templates with placeholders
- Layer identity blocks + action definitions — no data
- Surface — empty structure
- Init guide — conversational bootstrap

**Non-lossy guarantee:** All instructions survive extraction. Only user data, project state, and surface projections are stripped.

**Partial layer selection:** When seeding with fewer layers, abilities that need missing layers become **dormant** — still listed, marked as needing specific layers.

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

### Concept tiers

| Tier | What it unlocks | Concepts | How learned |
|------|----------------|----------|-------------|
| **Use** | Operate day-to-day | commands, ground, abilities.md, "just describe what you want" | Init + reinforced always |
| **Understand** | Know how it's organized; shape it via reflect | intent (why), ability (named capability), layer (area), reflect (evaluate) | Summary block during evolution; `concepts` / `explain` on demand |
| **Extend** | Build layers, replicate spheres | senses, instincts, identity blocks, depth tiers, seed/absorb | Only when the user asks or tries something these handle |

**Design principle:** The engine is the AI's manual, not the user's. Init is a conversation. The sphere should feel like talking to a capable assistant from session one.
