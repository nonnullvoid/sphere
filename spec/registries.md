# Registries

_Status: draft 2, for review._ How a sphere knows what it contains without reading everything: small index files that are generated from the files they describe, so they can't quietly go out of date.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

---

## The idea

A sphere grows to hundreds of files. Reading them all at the start of every session is slow and expensive, so the sphere keeps **registries**: short files listing what exists, what each thing is, and where to find it.

The trap is that a list kept by hand drifts. Something changes, nobody updates the list, and from then on the sphere reasons from a picture that's no longer true. So the rule is:

**Truth lives in one place.** A registry either points at that truth or is itself the only home for it. Never both. — **proven**

The test for any file: if you could delete it and rebuild it from other files, it's a view. If you couldn't, it's truth, and nothing else should duplicate it.

**How each registry is kept up to date is its own decision,** made by the registry's [frame](protocol.md#frame--proven): the structural frame that knows what the registry is for. What every registry shares is that **the tooling checks it**, whatever its mode.

---

## Three ways a registry is maintained

| Mode | Who maintains it | When it fits |
|---|---|---|
| **generated** | the tooling, by script | Every column can be computed from other files |
| **AI-maintained** | the AI, following the registry's frame | Some columns need judgment: a description, a relationship, a summary |
| **authored** | the human, with the AI drafting | It holds human decisions that live nowhere else |

**AI-maintained doesn't mean unchecked.** An instruction in a frame to "rebuild this at every ground" is a habit, and habits lapse. A registry that says it's rebuilt every ground can go months without being rebuilt, with nothing noticing. So every registry, whatever its mode, has a [drift check](#drift-checks--proven) that runs in the tooling.

**Authored registries are reconciled.** A registry that is the truth for some human decision (the session registry: what a session is for, whether it's abandoned) stores only those decisions. It computes everything else, and at ground it's checked against the facts it sits next to, with mismatches put to the human as questions. See [state](state.md#the-session-registry).

## The registries in a sphere

| Registry | Lists | Likely mode | Built or checked against | Chapter |
|---|---|---|---|---|
| **Layers** (`core/layers.md`) | every layer: what it holds, depends on, may share | generated | each layer's contract file | below |
| **Surface** (`core/surface.md`) | every place rendered output goes, and who can see it | generated | each surface area's declaration | [projections](projections.md) |
| **Protocol** (`core/protocol/protocol.md`) | intents, abilities, commands, senses | AI-maintained | lens and frame files: every command maps to a frame that exists, every layer it names exists | [protocol](protocol.md) |
| **Work index** (`layers/work/index.md`) | every work node, by status | generated | each node's `work.md` | [work](work.md) |
| **World** (`layers/world/registry.md`) | every domain and subject, and how they relate | generated, or AI-maintained if relationships need judgment | subject frontmatter | [knowledge](knowledge.md) |
| **Projections** | every rendered view: source, freshness, home | generated | each projection's declaration | [projections](projections.md) |
| **Sessions** | which sessions exist and what they're for | authored | git, for the facts | [state](state.md) |

"Likely mode" is the default a build ships with. A sphere's own frame for a registry can choose differently.

Every registry declares its mode where it can be seen:

```yaml
---
registry: work-index
maintained: generated        # generated | ai | authored
frame: work_registry
sources: layers/work/*/work.md
---
```

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

Files the sphere rebuilds (generated or AI-maintained) come in two kinds, and they're handled differently:

| Kind | Examples | Committed? | Why |
|---|---|---|---|
| **Human-facing views** | work index, world registry, layer registry | **Yes** | A person browsing the folder or the repository should be able to read them without running anything |
| **Machine-only caches** | the startup bundle, loading manifests | **No**: gitignored, rebuilt when needed | Nobody reads them directly, and committing them only creates merge conflicts |

**Conflicts in a committed view are never resolved by hand.** When two sessions both change a view, as happens when level-2 sessions [sync](state.md#level-2--the-session-tree-opt-in--advanced), it's rebuilt from the merged sources: by the tooling for a generated view, or by the AI for an AI-maintained one. Both versions were views of their sources, so the merged sources produce the right one.

---

## Every view says it's a view

Each generated or AI-maintained file starts with a header:

```markdown
<!-- Generated at ground, 2026-10-25 14:32. Built from: layers/work/*/work.md.
     Do not edit. Change the sources and it will be rebuilt. -->
```

**Hand edits are caught, not lost.** If someone edits a generated file anyway, the tooling notices at the next ground, because the file no longer matches what it would generate. It asks: *"You edited the work index directly. Should I move that change into the node it belongs to?"* People will edit what they can see, so a good system catches that and puts the change where it belongs.

---

## Drift checks — **proven**

Registries come with checks that run at ground:

- **Structure check:** every layer folder has a contract, and every contract has a folder.
- **Freshness check:** a view was rebuilt after its sources last changed. For a generated view, it also matches what its sources would produce now.
- **Reference check:** every link in a registry points at something that exists. Examples: a `parent:` naming a node that was renamed, or a command whose frame or layer no longer exists.

A failed check doesn't block the ground. It reports what's wrong and offers to fix it. A check that stops work gets disabled; a check that offers a fix gets used.

---

## Keep them lean — **proven**

A registry holds a **name, a one-line description and a pointer**. It never copies content from the files it lists. Its job is to tell the sphere where to look, so the sphere can read only what a task needs.

For a **non-technical human**, registries exist but are never mentioned. They're how the sphere finds its way around, not something the human manages.

---

## Open questions

1. **When views rebuild.** At every ground, or only when their sources changed? Rebuilding everything is simpler; rebuilding only what changed is faster in a large sphere.
2. **Views outside git.** In a gitless fallback sphere (one session at a time), "never edited by hand" still holds, but there's no merge to regenerate after. Anything else needed?
