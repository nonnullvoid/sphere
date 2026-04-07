# Sphere

> A context-aware identity layer for AI.

Sphere gives your AI a persistent home — a place it returns to every session, already knowing who you are, how you think, and what you're working toward. No re-explaining. No blank slates.

---

## What lives here

```
core/           ← identity and machinery (think twice before editing structure)
  user/         ← who you are
  ai/           ← who your AI persona is
  skills/       ← what Sphere can do
layers/         ← optional domain extensions you install
surface/        ← artifacts and outputs from your work
records/        ← decisions and history
```

## How it works

1. `CLAUDE.md` tells the AI to read Sphere on startup
2. `core/user/` gives the AI a model of you — your profile, how you like to work, what you believe
3. `core/ai/persona.md` gives the AI its own identity in your world
4. `layers/` are optional domains you install — philosophy, wellness, finance, projects, whatever fits your life
5. `surface/` is where things you create together land

## Growing your Sphere

Start minimal. Fill in `core/user/` first — that's the foundation. Add layers when you feel a domain needs dedicated structure. Run `core/skills/reflect.md` periodically to let Sphere evolve with you.

### Skills

| Skill | What it does |
|-------|-------------|
| `core/skills/onboard.md` | Guided setup — fills in core/user/ and starts persona.md |
| `core/skills/reflect.md` | Sphere evolution — review, refine, let it grow |
| `core/skills/fork.md` | Copy this Sphere with all your data (personal clone) |
| `core/skills/replicate.md` | Copy structure only, no personal data (for sharing or new contexts) |

## Future growth paths

As Sphere evolves, `core/` will grow to include:
- `core/agents/` — specialized AI agents for recurring tasks
- `core/scripts/` — automation scripts that interact with your Sphere

These are not included in Seed but the structure is reserved.

---

## What Sphere is not

Sphere is not a task manager, a note-taking app, or a second brain. It's an identity layer — the persistent foundation that makes every AI session continuous rather than fresh. Build your workflows on top of it.
