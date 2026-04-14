# Layer: Domain

## Identity
- **Name:** domain
- **Depth:** independent
- **Dependencies:** none
- **Senses:** `decision-point` (load when domain expertise is relevant to the current work)
- **Data paths:** `layers/domain/`
- **Init:** Fill in `context.md` with your field, key concepts, vocabulary, and where you sit in it. Add `stack.md` for technical roles.

---

Your professional domain — the field you work in, the concepts that matter, and the context that makes your AI a peer rather than a generalist.

This layer is loaded on-demand when the work requires domain depth. A well-filled domain layer means the AI can engage with your field at a real level rather than explaining basics you already know.

---

## Basic Abilities

_The starting capabilities this layer ships with._

| Command | What it does |
|---------|-------------|
| `domain context` | Load full domain layer for deep, context-aware work |

This layer primarily serves as loaded context rather than a command surface — its value is in making everything else domain-aware.

---

## Install

```bash
cp -r layer-catalog/domain your-sphere/layers/domain
```

Register in `sphere.md`:

```markdown
| domain | `layers/domain/` | Independent |
```

---

## What to keep here

- `context.md` — your domain: what the field is, how it works, where you sit in it, key concepts and vocabulary
- `stack.md` (optional, for technical roles) — architecture, conventions, tools you work with

---

## When the AI loads this layer

Load `layers/domain/context.md` when:
- Working on domain-specific problems
- Drafting external-facing content that requires domain accuracy
- Advising on domain questions
- The user invokes `domain context`
