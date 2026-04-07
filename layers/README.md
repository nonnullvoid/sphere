# Layers

Layers are optional domain extensions you install into your Sphere. Each layer adds a focused context that the AI loads on-demand — only when the work requires it.

A layer is a directory with a `README.md` (what it's for, when to load it) and one or more content files. That's it.

---

## Available layers

### Official

| Layer | What it holds | Best for |
|-------|--------------|---------|
| [`projects/`](projects/) | Active projects with session handoff — `project.md` + `runner.md` per project | Tracking work across sessions and agents |

### Community / build your own

| Layer | What it holds | Best for |
|-------|--------------|---------|
| `philosophy/` | Your worldview, beliefs, and open questions | Meaning, values, big decisions |
| `wellness/` | Health, energy, routines, what you know about your body and mind | Health, capacity, routines |
| `financial/` | Financial picture, goals, and constraints | Financial decisions, tradeoffs |
| `domain/` | Professional domain expertise and vocabulary | Work contexts |
| `stack/` | Technical architecture and conventions | Engineering and technical work |
| `org/` | Team structure, stakeholders, decision patterns | Management, org navigation |
| `family/` | Family context, caregiving, relationships | Personal life decisions |
| `style/` | Communication and aesthetic preferences | Writing, creative work |

---

## Installing a layer

```bash
# Copy an official layer into your sphere
cp -r layers/projects your-sphere/layers/projects
```

Then follow the layer's `README.md` for any `CLAUDE.md` additions needed.

---

## Building a layer from scratch

A layer is just a directory with structured context. The most important file is the `README.md` — it tells the AI what the layer is for and *when to load it*. A layer loaded at the wrong time is noise; a layer loaded at the right moment is leverage.

Contribute back: if you build a layer that works well, open a PR.

---

*Layers are yours to invent. If your life has a domain that doesn't fit any of the above, make one.*
