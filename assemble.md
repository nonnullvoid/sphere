# Assemble

_A guided setup protocol for AI assistants helping a user create their first sphere._

---

## What you're doing

You're going to help the user create a sphere — a persistent AI-assisted workspace that lives as a folder on their computer. It will remember who they are, how they work, and what they're doing across every session. From this point on, they open that folder instead of starting from scratch.

This is not a skill you execute once. It's a workspace they'll use every day.

---

## Step 1 — Understand what they need

Ask the user one question to route them to the right starting point:

> "What kind of work do you mainly want the sphere for — professional work and projects, personal life, or something else?"

| Their answer | Best starting point |
|--------------|-------------------|
| Work, projects, team, job | WorkSphere template |
| Personal life, habits, health, journaling | Base template + relevant layers |
| Both, or not sure | WorkSphere template (it's easier to strip than to add) |
| I want to build something custom | From scratch with `core/` |

---

## Step 2 — Choose a path

### Path A: WorkSphere template _(recommended for most)_

Pre-assembled with three layers: projects (track active work), domain (professional context), planning (goals and priorities). This is a complete professional workspace out of the box.

```bash
cp -r sphere-templates/work-sphere ~/my-worksphere
cd ~/my-worksphere
```

Skip to Step 4.

---

### Path B: Base template + your own layers

Starts minimal — just the core engine, no layers. You add exactly what you need from `layer-catalog/`.

```bash
cp -r sphere-templates/base ~/my-sphere
cd ~/my-sphere
```

Then install layers in Step 3.

---

### Path C: From scratch _(contributors and custom builders)_

Use the root `core/` as your reference implementation, build your own `sphere.md` and `CLAUDE.md` from scratch, and assemble layers as needed. This path is for people building a radically custom sphere or extending the system.

```bash
mkdir ~/my-sphere && cd ~/my-sphere
cp -r /path/to/sphere/core .
mkdir layers surface
```

Then create `CLAUDE.md` and `sphere.md` using the base template as a reference. Add layers in Step 3.

---

## Step 3 — Install layers (Path B and C only)

Walk the user through the available layers. Explain each in one sentence, then ask what they want.

| Layer | Depth | Good for |
|-------|-------|---------|
| `projects` | Foundation | Anyone tracking active work — the core productivity layer |
| `domain` | Independent | Knowledge workers, professionals — gives the AI real domain depth |
| `planning` | Coupled (needs projects) | People who want goals and priorities connected to their project work |
| `philosophy` | Foundation | Anyone who wants the AI to engage with their worldview and values |
| `wellness` | Independent | People who want health, energy, and habits to inform their work context |

**Recommended starter combos:**
- Minimal: `projects` only
- Professional: `projects` + `domain`
- Full work context: `projects` + `domain` + `planning`
- Personal: `philosophy` + `wellness`

**Install a layer:**
```bash
cp -r layer-catalog/[layer-name] layers/[layer-name]
```

**Register it in `sphere.md`** — add a row to the Layers table:
```markdown
| projects | `layers/projects/` | Foundation |
```

Repeat for each layer. Foundation layers first.

---

## Step 4 — Name the sphere

Ask the user what to call their sphere. This becomes the name it announces at startup.

> "What do you want to call your sphere? It'll greet you by this name each session — something like `work`, `rutvij-work`, or whatever feels right."

Edit `sphere.md` — replace `[your-sphere-name]` in the Identity block:

```markdown
- **Sphere:** work
```

---

## Step 5 — Set up git (recommended)

Git gives the sphere state history — every command becomes a commit, and you can revert mistakes.

```bash
git init
git add .
git commit -m "init: [sphere-name]"
```

Tell the user: "You don't have to push this anywhere. Local git is enough for checkpoints and undo."

---

## Step 6 — Open the sphere and run init

This is the handoff moment. The user now opens their sphere folder with their AI assistant.

Tell them:

> "Open the folder `[sphere-name]/` with your AI. It'll read `CLAUDE.md` automatically and start the startup sequence. Since your profile isn't filled in yet, it'll ask to walk you through setup. Say yes — that's the init conversation."

What happens next:
1. AI reads `CLAUDE.md` → loads `sphere.md` → runs startup sequence
2. Finds placeholder content in `core/user/profile.md`
3. Offers to run init
4. Reads `core/init.md` and walks the user through: Profile → Principles → Preferences → AI Persona
5. At the end: `[sphere-name] ready`

After init, the sphere knows who the user is. Every future session starts from that foundation.

---

## What to tell the user after setup

> "You're set up. Every session, just open this folder with your AI — it'll load your context automatically and be ready to work.
>
> A few things to try:
> - Say `[sphere-name] ready` to check the startup sequence is working
> - Say `what can you do?` to see your current abilities
> - If you installed the projects layer: say `new project [name]` to start your first project"

For WorkSphere users specifically:
> "Say `resume [project-name]` at the start of any session to pick up exactly where you left off."

---

## Troubleshooting

**AI doesn't seem to know sphere concepts:**
The AI didn't read `CLAUDE.md`. Ask them: "Read CLAUDE.md and sphere.md, then run the startup sequence."

**Startup sequence runs but profile is already filled (shouldn't happen on first run):**
The template wasn't copied cleanly — placeholder text may have been overwritten. Check `core/user/profile.md` for placeholder content vs. actual data.

**User wants to add a layer after init:**
Standard install: `cp -r layer-catalog/[layer] layers/[layer]`, register in `sphere.md`. Then tell the AI: "I've added the [layer] layer — initialize it."
