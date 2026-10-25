# Registries

_Status: draft 1, for review._ How a sphere knows what it contains without reading everything: small index files that are generated from the files they describe, so they can't quietly go out of date.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

---

## The idea

A sphere grows to hundreds of files. Reading them all at the start of every session is slow and expensive, so the sphere keeps **registries**: short files listing what exists, what each thing is, and where to find it.

The trap is that a list kept by hand drifts. Something changes, nobody updates the list, and from then on the sphere reasons from a picture that's no longer true. So the rule is:

**Truth lives in one place. A registry is a view of it, rebuilt by the tooling, never edited by hand.** — **proven**

The test for any file: if you could delete it and regenerate it, it's a view. If you couldn't, it's truth, and nothing else should duplicate it.

---

## The registries in a sphere

| Registry | Lists | Built from | Chapter |
|---|---|---|---|
| **Layers** (`core/layers.md`) | every layer: what it holds, what it depends on, what it may share | each layer's own contract file | below |
| **Surface** (`core/surface.md`) | every place the sphere puts rendered output, and who can see it | each surface area's declaration | [projections](projections.md) |
| **Protocol** (`core/protocol/protocol.md`) | intents, abilities, commands, senses | lens and frame files | [protocol](protocol.md) |
| **Work index** (`layers/work/index.md`) | every work node, by status | each node's `work.md` | [work](work.md) |
| **World** (`layers/world/registry.md`) | every domain and subject, and how they relate | subject frontmatter | [knowledge](knowledge.md) |
| **Projections** | every rendered view: its source, freshness, home | each projection's declaration | [projections](projections.md) |
| **Sessions** | which sessions exist and what they're for | _the exception: see below_ | [state](state.md) |

### The exception: authored registries

The session registry isn't a pure view. It holds **meaning**: what a session is for, whether it's paused or abandoned. That has no other home, so the registry is the truth for it. A registry like this:

- stores **only** what has no other home, and computes everything else (see [state](state.md#the-session-registry));
- is **reconciled** at ground against the facts it sits next to, with mismatches put to the human as questions.

**The rule for choosing:** if every column can be computed from other files, the registry is generated. If it holds human decisions that live nowhere else, it's authored, and it gets reconciliation instead.

---

## Layer contracts — **proven**

Every layer has a short **contract** file at its root, declaring:

```yaml
---
layer: work
depth: foundation           # foundation | utility | optional
depends_on: [world]
holds: work nodes, their status and progress
requires: []                # what this layer needs another sphere to have before it can be shared
---
```

…followed by a few lines on what the layer is for. The layer registry is built by collecting these. A new layer becomes visible to the sphere by having a contract, not by someone remembering to add a line elsewhere.

---

## Committed views and caches — _decided, not yet exercised_

Generated files come in two kinds, and they're handled differently:

| Kind | Examples | Committed? | Why |
|---|---|---|---|
| **Human-facing views** | work index, world registry, layer registry | **Yes** | A person browsing the folder or the repository should be able to read them without running anything |
| **Machine-only caches** | the startup bundle, loading manifests | **No**: gitignored, rebuilt when needed | Nobody reads them directly, and committing them only creates merge conflicts |

**Conflicts in a committed view are never resolved by hand.** When two sessions both change a view, as happens when level-2 sessions [sync](state.md#level-2--the-session-tree-opt-in--advanced), the tooling simply regenerates it from the merged sources. Both versions were views of their sources, so the merged sources produce the right one.

---

## Every view says it's a view

Each generated file starts with a header:

```markdown
<!-- Generated at ground, 2026-10-25 14:32. Built from: layers/work/*/work.md.
     Do not edit. Change the sources and it will be rebuilt. -->
```

**Hand edits are caught, not lost.** If someone edits a generated file anyway, the tooling notices at the next ground, because the file no longer matches what it would generate. It asks: *"You edited the work index directly. Should I move that change into the node it belongs to?"* People will edit what they can see, so a good system catches that and puts the change where it belongs.

---

## Drift checks — **proven**

Registries come with checks that run at ground:

- **Structure check:** every layer folder has a contract, and every contract has a folder.
- **Freshness check:** every generated view matches what its sources would produce now.
- **Reference check:** every link in a view points at something that exists, for example a `parent:` naming a node that was renamed.

A failed check doesn't block the ground. It reports what's wrong and offers to fix it. A check that stops work gets disabled; a check that offers a fix gets used.

---

## Keep them lean — **proven**

A registry holds a **name, a one-line description and a pointer**. It never copies content from the files it lists. Its job is to tell the sphere where to look, so the sphere can read only what a task needs. See loading in [profiles](profiles.md).

At **core profile**, registries exist but are never mentioned. They're how the sphere finds its way around, not something the human manages.

---

## Open questions

1. **Generating the protocol registry.** Today it's written by hand. Generating it would mean abilities and commands are declared in each frame (procedure frames already describe themselves in their skill `description`), and intents in each lens. Worth doing, or is the hand-written table more readable as the sphere's top-level vocabulary?
2. **When views rebuild.** At every ground, or only when their sources changed? Rebuilding everything is simpler; rebuilding only what changed is faster in a large sphere.
3. **Views outside git.** In a gitless fallback sphere (one session at a time), "never edited by hand" still holds, but there's no merge to regenerate after. Anything else needed?
