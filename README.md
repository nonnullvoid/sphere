# Sphere

**A context-aware identity layer for AI.**

Sphere gives your AI a persistent home — a place it comes back to at the start of every session, already knowing who you are, how you think, and what you're working toward. No re-explaining. No blank slates.

Built for Claude Code. The file architecture works with any AI.

---

## The idea

Every AI session starts cold. You re-explain your context, your goals, your working style. The AI forgets everything when you close the window.

Sphere fixes that. It's a folder of markdown files that your AI reads at startup — a persistent identity layer that makes every session continuous rather than fresh. Your profile. Your principles. Your AI's persona in your world.

---

## How it works

1. **Clone a template** — blank or pre-structured for life or work
2. **Fill in `core/user/`** — who you are, how you work, what you believe
3. **Every session starts oriented** — your AI reads Sphere on startup via `CLAUDE.md`

Everything is plain text files you own. No servers, no accounts, no sync. It lives wherever you put it.

---

## Templates

| Template | What it is | Best for |
|----------|-----------|---------|
| [`templates/seed/`](templates/seed/) | Blank Sphere — minimal, no pre-filled content | Starting from scratch |
| [`templates/life-sphere/`](templates/life-sphere/) | LifeSphere — philosophy + wellness layers pre-installed | Whole-life context |
| [`templates/work-sphere/`](templates/work-sphere/) | WorkSphere — domain + projects layers pre-installed | Professional work |

---

## Get started

```bash
# Clone the repo
git clone https://github.com/nonnullvoid/sphere.git

# Copy the template you want
cp -r sphere/templates/seed ~/my-sphere
# or: cp -r sphere/templates/life-sphere ~/my-sphere
# or: cp -r sphere/templates/work-sphere ~/my-work-sphere

# Open in Claude Code — sphere loads automatically
cd ~/my-sphere && claude

# Tell Claude: "Run the onboard skill"
```

---

## Structure

```
[your-sphere]/
├── CLAUDE.md          ← tells the AI to load Sphere on startup
├── sphere.md          ← what this Sphere is and how it works
├── MODE.md            ← declares the Sphere type
├── core/
│   ├── user/
│   │   ├── profile.md       ← who you are
│   │   ├── preferences.md   ← how you like to work with AI
│   │   ├── principles.md    ← what you believe and how you operate
│   │   └── roles.md         ← the contexts you inhabit
│   ├── ai/
│   │   └── persona.md       ← who the AI is in your world
│   └── skills/
│       ├── onboard.md       ← guided setup
│       ├── reflect.md       ← review and evolve
│       ├── fork.md          ← copy with all data
│       └── replicate.md     ← copy structure only
├── layers/            ← optional domain extensions
├── surface/           ← artifacts and outputs
└── records/
    └── decisions.md   ← append-only decisions log
```

---

## Layers

Layers are optional domain extensions that load on-demand. The AI reads a layer only when the work calls for it.

Pre-installed layers by template:
- **LifeSphere** → `philosophy/`, `wellness/`
- **WorkSphere** → `domain/`, `projects/`

Browse the [full layers catalogue](layers/README.md) or build your own.

---

## Skills

Every Sphere comes with four built-in skills:

- **Onboard** — guided setup through conversation
- **Reflect** — periodic review and evolution
- **Fork** — full copy with personal data (for cloning or backup)
- **Replicate** — structure copy, no personal data (for sharing or new contexts)

Run a skill by telling your AI: *"Run the onboard skill"* or *"Let's do a Sphere reflect."*

---

## Requirements

- **Claude Code** — or any AI assistant that reads files at session start
- **A text editor**
- **A folder**

---

## License

MIT
