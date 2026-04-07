# WorkSphere

> A context-aware identity layer for AI — scoped to your professional world.

WorkSphere gives your AI persistent knowledge of your domain, org, working style, and active projects. Every work session starts with your AI already oriented — no re-explaining what you do, who your team is, or what you're building.

---

## What lives here

```
core/           ← professional identity and machinery
  user/         ← who you are professionally
  ai/           ← your AI persona for this Sphere
  skills/       ← onboard, reflect, fork, replicate
layers/
  domain/       ← the field you work in, your expertise
  projects/     ← active work and current focus
surface/        ← work artifacts and outputs
records/        ← work decisions log
```

## When to use WorkSphere

- You're doing actual work — writing, building, designing, analyzing
- You need the AI to understand your domain, org, or stack
- You're planning or reviewing projects
- You want contextual suggestions based on your professional situation

For big-picture career questions, transitions, or work-life questions, switch to LifeSphere.

## Growing your WorkSphere

The domain and projects layers are pre-installed. Others to consider:

- `layers/stack/` — technical architecture and conventions (if you do technical work)
- `layers/org/` — team structure, stakeholders, decision-making patterns

Install layers by creating a directory under `layers/` with a `README.md` and `context.md`.

## Privacy

WorkSphere files are meant to be kept private. The `replicate` skill strips your personal content and gives you a shareable blank copy of the structure.

## Skills

| Skill | What it does |
|-------|-------------|
| `core/skills/onboard.md` | Guided setup |
| `core/skills/reflect.md` | Sphere evolution |
| `core/skills/fork.md` | Copy with all data |
| `core/skills/replicate.md` | Copy structure only |
