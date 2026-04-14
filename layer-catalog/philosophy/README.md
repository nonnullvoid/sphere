# Layer: Philosophy

## Identity
- **Name:** philosophy
- **Depth:** foundation
- **Dependencies:** none
- **Senses:** `reflection`, `decision-point` (load when values or meaning are at stake)
- **Data paths:** `layers/philosophy/`
- **Init:** Fill in `context.md` with your current worldview — what you believe, the frameworks you actually use, the questions you're sitting with.

---

Your examined worldview — the beliefs, frameworks, and questions that shape how you see and act in the world.

This layer is for the thinking underneath the thinking. Not a task list or a goal tracker — a living record of your philosophical commitments and the questions you're still working out.

---

## Basic Abilities

_The starting capabilities this layer ships with._

| Command | What it does |
|---------|-------------|
| `philosophy context` | Load philosophical context for values-informed work |
| `examine [question]` | Think through a question using your philosophical framework |

---

## Install

```bash
cp -r layer-catalog/philosophy your-sphere/layers/philosophy
```

Register in `sphere.md`:

```markdown
| philosophy | `layers/philosophy/` | Foundation |
```

---

## What to keep here

- `context.md` — your current worldview: what you believe, how you think about meaning, what frameworks you actually use
- `questions.md` (optional) — the open questions you're sitting with
- `influences.md` (optional) — thinkers, traditions, or ideas that have shaped you

---

## When the AI loads this layer

Load `layers/philosophy/context.md` when:
- Working on questions of meaning, purpose, or identity
- Making major decisions that involve values
- Reviewing principles
- The user explicitly references philosophical context
