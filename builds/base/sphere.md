# Sphere

_The orchestrator. Read at the start of every window, before anything else._

## Startup

**First run?** If `core/identity.json` has an empty `id`, this sphere hasn't met its human yet. Read [`core/init.md`](core/init.md) and follow it instead of the steps below.

Otherwise, in order, reading only what each step names:

1. **Who.** [`core/identity.json`](core/identity.json) (this sphere's name), the frontmatter and first section of [`core/user/profile.md`](core/user/profile.md), and the persona marked `default: true` in [`core/ai/personas/`](core/ai/personas/).
2. **How.** [`core/engine.md`](core/engine.md): the kernel every window runs on.
3. **The guards.** Every frame marked `always: true`. The manifest lists them under *Always on*. They hold in every window, for every persona and every operating mode.
4. **What it can do.** [`core/manifest.md`](core/manifest.md): every lens and frame in a line, when each applies, and the reactions table. Open nothing else until a task points at it. If the manifest is missing, or `scripts/manifest-check` says it's stale, rebuild it first (the [capability-manifest](core/protocol/frames/sphere-framework/capability-manifest.md) frame says how).
5. **Where we are.** Run `scripts/sphere list`. If the human names a focus, or only one is waiting, run `scripts/sphere attach <focus>`; otherwise attach `main`. Its last line names a sense: act on that sense's rows in the reactions table.
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
