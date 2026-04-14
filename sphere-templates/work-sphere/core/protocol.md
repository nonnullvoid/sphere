# Protocol

_What the sphere is for and what it can do. The AI's operating vocabulary and reflection axis. Read this at startup — it's the most-used file in the sphere._

---

## Intents

The sphere's purposes. Each intent is a stable goal that abilities serve. This is the reflection axis — when evaluating what to change, ask "is this intent well-served?" Intents outlast any reorganization of abilities or layers.

| Intent | What the user wants |
|--------|-------------------|
| **Daily Continuity** | Pick up exactly where I left off, every session |
| **Parallel Progress** | Run multiple projects with clear status on each |
| **Daily Rhythm** | Structured start and end of day rituals |
| **Safe Experimentation** | Try things without fear of breaking the sphere |
| **Sphere Literacy** | Understand how the sphere works, at my own pace |
| **Sphere Evolution** | The sphere improves through use and reflection |

---

## Abilities

What the sphere can do. Every command maps to an ability; every ability serves an intent.

### Project Lifecycle
_Intent: Daily Continuity, Parallel Progress_

| Command | What it does | Layers |
|---------|-------------|--------|
| `pull [project]` | Fetch updates from external sources → update tasks, status | projects |
| `ground [project]` | Persist session knowledge to project files | projects |
| `sync [project]` | `pull` then `ground` in sequence | projects |
| `peek [project]` | Quick status card — no full context load | projects |
| `open [project]` | Full context load, set as active project | projects |
| `close [project]` | Auto-ground + mark inactive for session | projects |
| `resume [project]` | `open` + orientation briefing from latest session log | projects |

`ground` is the cold-start engine. It persists session knowledge so any new session picks up instantly.

### Day Planning
_Intent: Daily Rhythm_

| Command | What it does | Layers |
|---------|-------------|--------|
| `plan my day` | Read goals + project index → draft today's priorities | planning, projects |
| `start my day` | Read goals + latest plan → what to work on now | planning, projects |
| `wrap up my day` | Ground all touched projects → write EOD notes | planning, projects |
| `what's on my plate?` | Summarize all active/blocked work and open tasks | planning, projects |
| `catch me up` | Full situational summary across everything | planning, projects |
| `what should I work on?` | Recommend highest-leverage action right now | planning, projects |

### Passive Sync
_Intent: Parallel Progress — instinct, not a command_

Fires automatically when the user mentions a status change (PR merged, task done, blocker resolved). Updates project files in the same response without being asked.

### Domain Context
_Intent: Deep Work_

| Command | What it does | Layers |
|---------|-------------|--------|
| `domain context` | Load domain layer for deep, context-aware work | domain |

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

_New abilities emerge through use. The AI proposes them when patterns are recognized._
