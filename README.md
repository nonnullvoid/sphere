# Sphere

**Give your AI a persistent home.**

A folder of markdown files your AI reads at startup — so every session begins oriented, not blank.

---

## What it looks like

Open your WorkSphere in Claude and this is what greets you — no prompting, no re-explaining:

```
my-worksphere ready

| Project        | Status      | Next action          |
|----------------|-------------|----------------------|
| product-launch | in-progress | Draft release notes  |
| team-hiring    | blocked     | Waiting on recruiter |
| q2-retro       | on hold     | —                    |
```

Say `resume product-launch` and the AI picks up from your last session — what was done, what's next, open decisions. Say `ground` when you're done and the next session starts just as clean.

---

## How it works

1. **Clone a template** — base, WorkSphere, or LifeSphere
2. **Fill in `core/user/`** — your profile, principles, how you work. The AI walks you through it in conversation when you first open the sphere.
3. **Every session starts oriented** — your AI reads the sphere at startup via `CLAUDE.md`. No plugins, no config, just files.

Everything is plain markdown you own. No servers, no accounts, no sync.

---

## Get started

```bash
# Clone
git clone https://github.com/nonnullvoid/sphere.git

# Pick a template and copy it to where you work
cp -r sphere/sphere-templates/base ~/my-sphere
# or: cp -r sphere/sphere-templates/work-sphere ~/my-worksphere

# Open in Claude Code — sphere loads automatically
cd ~/my-worksphere && claude

# The AI will offer to walk you through setup on first open
```

**Want a guided setup?** Open the cloned `sphere/` folder with your AI. It reads `CLAUDE.md` automatically, understands what sphere is, and walks you through picking a template, installing layers, and running init — conversationally. See [`assemble.md`](assemble.md) for what it covers.

---

## Templates

| Template | What it is | Best for |
|----------|-----------|---------|
| [`sphere-templates/base/`](sphere-templates/base/) | Minimal — structure only, no layers | Starting from scratch |
| [`sphere-templates/work-sphere/`](sphere-templates/work-sphere/) | Projects + domain + planning layers pre-installed | Professional work |
| [`sphere-templates/life-sphere/`](sphere-templates/life-sphere/) | Philosophy + wellness layers pre-installed | Whole-life context |

---

## What's inside a sphere

```
[your-sphere]/
├── CLAUDE.md          ← tells the AI to load the sphere on startup
├── sphere.md          ← orchestrator: startup sequence, identity, layer registry
├── core/
│   ├── engine.md      ← runtime rules: layers, senses, instincts, evolution
│   ├── protocol.md    ← operating vocabulary: what the sphere can do and why
│   ├── init.md        ← initialization protocol: how the AI sets up a new sphere
│   ├── records/       ← compacted history and long-term memory
│   ├── ai/
│   │   └── persona.md ← who the AI is in this sphere
│   └── user/
│       ├── profile.md    ← who you are
│       ├── principles.md ← what you believe and how you operate
│       └── preferences.md ← how you like to work with AI
├── layers/            ← installed domain extensions
└── surface/           ← projected artifacts and outputs
```

The AI reads `core/` at every startup. Layers load on-demand when a command needs them. Surface is for outputs — what the sphere produces, kept separate from what it is.

---

## Layer catalog

The [`layer-catalog/`](layer-catalog/) contains reusable extensions you can install into any sphere:

| Layer | What it adds |
|-------|-------------|
| `projects/` | Track active work across sessions with built-in session handoff |
| `domain/` | Professional field context — makes the AI a peer, not a generalist |
| `philosophy/` | Examined worldview — beliefs, frameworks, open questions |
| `wellness/` | Physical and mental health baseline — energy, routines, patterns |

Each layer is self-contained: install by copying into your sphere's `layers/` directory and registering in `sphere.md`.

---

## Going deeper

The [Architecture doc](ARCHITECTURE.md) covers the full model: the three actors (user, AI, sphere), the execution chain (intent → ability → command → action → state), layer depth tiers, the evolution protocol, and the three-tier org model.

[`assemble.md`](assemble.md) is a guided setup protocol for AI assistants — open the repo with your AI and it will use this to walk you through template selection, layer installation, and first-run init.

---

## Requirements

- **Claude Code** — or any AI that reads files at session start
- **A text editor**
- **A folder**

---

## License

MIT
