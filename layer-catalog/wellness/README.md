# Layer: Wellness

## Identity
- **Name:** wellness
- **Depth:** independent
- **Dependencies:** none
- **Senses:** `reflection`, `decision-point` (load when energy, health, or physical/mental state is relevant)
- **Data paths:** `layers/wellness/`
- **Init:** Fill in `context.md` with your current baseline — what's working, what you're managing, your general patterns.

---

Your physical and mental health context — energy, routines, patterns, and what you know about how your body and mind work.

This layer isn't a fitness tracker or a symptom log. It's the stable context that helps your AI understand what's beneath the surface when you're operating well or not.

---

## Basic Abilities

_The starting capabilities this layer ships with._

| Command | What it does |
|---------|-------------|
| `wellness check-in` | Reflect on current energy, state, and what's sustainable right now |
| `capacity check` | Assess current bandwidth before committing to work |

---

## Install

```bash
cp -r layer-catalog/wellness your-sphere/layers/wellness
```

Register in `sphere.md`:

```markdown
| wellness | `layers/wellness/` | Independent |
```

---

## What to keep here

- `context.md` — your current wellness baseline: what's working, what you're managing, your general patterns
- `routines.md` (optional) — the practices that sustain you
- `patterns.md` (optional) — what you've learned about your own energy, focus, and recovery

---

## When the AI loads this layer

Load `layers/wellness/context.md` when:
- Discussing energy, health, or capacity
- Making decisions that affect how you're feeling
- The user mentions feeling off, drained, or mentions physical or mental health
- Planning routines or habits
