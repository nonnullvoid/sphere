# Sphere

_The orchestrator. Read at the start of every window, before anything else._

## Startup

**First run?** If `core/identity.json` has an empty `id`, this sphere hasn't met its human yet. Read [`core/init.md`](core/init.md) and follow it instead of the steps below. Say nothing about this check: the human's first words from you are the hello in that file.

Otherwise, reading only what each step names. **Don't read a file that's already in your context:** some tools load this file, the engine and the manifest with the door (Claude Code imports them through `CLAUDE.md`). Read what steps 1 to 4 need together, in one go, not one file at a time.

1. **Who.** [`core/identity.json`](core/identity.json) (this sphere's name), the frontmatter and first section of [`core/user/profile.md`](core/user/profile.md), and the persona marked `default: true` in [`core/ai/personas/`](core/ai/personas/).
2. **How.** [`core/engine.md`](core/engine.md): the kernel every window runs on.
3. **The guards.** Every frame marked `always: true`. The manifest lists them under *Always on*. They hold in every window, for every persona and every operating mode.
4. **What it can do.** [`core/manifest.md`](core/manifest.md): every lens and frame in a line, and when each applies. Open nothing else until a task points at it. If it's missing, run `scripts/sphere manifest`.
5. **Where we are.** Run `scripts/sphere start`, unless its output is already in your context (Claude Code runs it when the window opens). It prints the sphere's name, what's open, and attaches **once**: the focus the human names (`scripts/sphere start <focus>`), else the one open focus besides `main`, else, with several open, it asks you to ask them which. The briefing ends with a sense and its reactions: act on each one whose condition applies.
6. **Say hello in a line,** and nothing about the steps above.

Bodies of lenses and frames are read when they're used, never at startup. That's what keeps every window quick, however large the sphere grows.

## At a glance

| | |
|---|---|
| **Build** | `base` (see [`core/build.json`](core/build.json)) |
| **Architecture** | SPHERE-ARCH 1.0 |
| **Saving** | *ground*: the human may say "save", "lock it in" or "wrap up" |
| **The human's things** | [`surface/projections.html`](surface/projections.html) |

## Layers

| Layer | Holds |
|---|---|
| [`layers/focus/`](layers/focus/contract.md) | what the human is working on with the AI, one node per pursuit |
| [`layers/work/`](layers/work/contract.md) | what the human is changing in their life or work, as one tree |
| [`layers/knowledge/`](layers/knowledge/contract.md) | what's true in their world: topics, facts and how sure each is |
| [`layers/ideas/`](layers/ideas/contract.md) | maybes, one file each, until they graduate or are parked |
| [`layers/literacy/`](layers/literacy/contract.md) | what the human understands, and the library of what's been explained |
| [`layers/witness/`](layers/witness/contract.md) | the growth ledger: what finished, what was learned, wins |
| [`layers/projections/`](layers/projections/contract.md) | what each view of the human's things shows |

The full registries are [`core/layers.md`](core/layers.md) and [`core/surface.md`](core/surface.md).
