# Layer Catalog

_Reusable, self-contained extensions you can install into any sphere._

---

Each layer in this catalog is a standalone unit with:
- A clear identity block (name, depth, dependencies, senses)
- Its own data paths
- **Basic abilities** — the starting capabilities the layer ships with, before any inter-layer dependencies develop
- Install instructions

Layers co-evolve within a sphere. The abilities listed here are the initial set — your sphere will grow them over time.

---

## Available Layers

| Layer | Depth | What it does |
|-------|-------|-------------|
| [projects](projects/) | Foundation | Track active work across sessions with built-in handoff |
| [domain](domain/) | Independent | Professional domain — field, vocabulary, expertise |
| [philosophy](philosophy/) | Foundation | Examined worldview — beliefs, frameworks, open questions |
| [wellness](wellness/) | Independent | Physical and mental health context — energy, routines, patterns |

---

## Installing a layer

```bash
cp -r layer-catalog/[layer-name] your-sphere/layers/[layer-name]
```

Then register it in your `sphere.md` layers table and fill in the content file.

---

## Layer depth guide

| Depth | What it means |
|-------|--------------|
| **Foundation** | Other layers may depend on these — install first |
| **Coupled** | Needs specific other layers to function fully |
| **Independent** | Works standalone, no dependencies |
| **Utility** | Optional tools, no cascade if removed |
