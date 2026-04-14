# Protocol

_What the sphere is for and what it can do. The AI's operating vocabulary and reflection axis. Read this at startup — it's the most-used file in the sphere._

---

## Intents

The sphere's purposes. Each intent is a stable goal that abilities serve. This is the reflection axis — when evaluating what to change, ask "is this intent well-served?" Intents outlast any reorganization of abilities or layers.

| Intent | What the user wants | Active when |
|--------|-------------------|------------|
| **Safe Experimentation** | Try things without fear of breaking the sphere | Always |
| **Sphere Literacy** | Understand how the sphere works, at my own pace | Always |
| **Sphere Evolution** | The sphere improves through use and reflection | Always |
| **Daily Continuity** | Pick up exactly where I left off, every session | `projects` layer installed |
| **Parallel Progress** | Run multiple projects with clear status on each | `projects` layer installed |
| **Daily Rhythm** | Structured start and end of day rituals | `planning` + `projects` installed |

---

## Abilities

What the sphere can do. Every command maps to an ability; every ability serves an intent.

### Sphere Literacy
_Intent: Sphere Literacy_

| Command | What it does |
|---------|-------------|
| `concepts` | List all sphere concepts by tier (use / understand / extend) |
| `explain [concept]` | Explain a concept using examples from this sphere |
| `how does [thing] work?` | Explain a layer, ability, or behavior |
| `what can you do?` | List active abilities with commands |
| `abilities` | Quick reference — show this file's summary |

### State Management
_Intent: Safe Experimentation — requires git_

| Command | What it does |
|---------|-------------|
| `checkpoint [message]` | Save current sphere state |
| `history` | Show recent state transitions |
| `revert` | Pick a previous checkpoint to restore |
| `undo` | Revert the last state change |

### Sphere Evolution
_Intent: Sphere Evolution_

| Command | What it does |
|---------|-------------|
| `reflect` | Targeted evaluation of one intent or ability |
| `deep-reflect` | Full structural review: gaps, bloat, misalignment, discovery |

### Replication
_Intent: Sphere Evolution_

| Command | What it does |
|---------|-------------|
| `seed` | Extract skeleton — all structure, no data |
| `init [name] [seed]` | Bootstrap a new sphere from a seed (see `core/init.md`) |
| `absorb [source]` | Pull improvements from another sphere |
| `compare [other]` | Diff two spheres at intent / ability / layer level |

---

## Layer Abilities

_Dormant — activate when corresponding layers are installed._

| Ability | Needs | Commands |
|---------|-------|---------|
| Project Lifecycle | `projects` | `pull`, `ground`, `sync`, `peek`, `open`, `close`, `resume` |
| Session Handoff | `projects` | `ground` — the cold-start engine |
| Day Planning | `planning` + `projects` | `plan my day`, `start my day`, `wrap up my day`, `what's on my plate?`, `catch me up`, `what should I work on?` |
| Passive Sync | `projects` | _(instinct — fires on status mentions, no command)_ |

---

_New abilities emerge through use. The AI proposes them when patterns are recognized._
