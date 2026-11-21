---
frame: crystallization
lens: [evolution]
derives_from: [evolution@1]
version: 1
version_note: First draft. Sizing a change, proposing it, making it in order with the checks, announcing it; targeted, phased and fork changes.
status: drafting
updated: 2026-11-13
sharing: public
reads: [core/protocol, core/shapes, layers/ideas, layers/work]
writes: [core/protocol, core/shapes, layers/ideas, layers/work]
protocol: [I-a-sphere-that-fits-how-i-work, A-evolve, A-plan-change, A-announce-change, node-archived]
---

# Crystallization

**Applies to:** any change to the sphere itself: a new command, ability, frame or lens, a refactor, a new tree or layer, and a `sphere` idea graduating into a change.

## Size the change first

| Size | When | What happens |
|---|---|---|
| **One-off** | It happened once and is unlikely to recur | Just do it. Nothing is recorded |
| **Command** | A new way to ask for something the sphere already does | Add it to its frame; register it |
| **Ability** | A new capability inside an existing frame's scope | Add it to the frame; register it |
| **Frame** | Distinct mechanics that don't fit any existing frame | Propose a frame under the lens it follows from |
| **Lens** | A distinct understanding: a *why* no existing lens holds | Propose a lens. The heaviest step: everything below derives from it |
| **Refactor** | Something existing is too wide, overlapping, misnamed or wrong | Size how much it touches (below), then propose |

- **A new frame** needs mechanics of its own, usually with their own data, senses or abilities, that won't fit an existing frame without stretching it.
- **A new lens** needs a *why* that can't be derived from the lenses already there. Mechanics alone earn a frame, never a lens.
- **A new layer is a separate decision.** A layer is a home for data, not a unit of understanding. It's warranted only when a capability needs data of its own **and** that data fits no existing layer.
- **Fit it to the node shape first.** Before inventing structure, ask the questions in [designing with the shape](../nodes/node-shape.md#designing-something-new). *Why:* a design that can't answer them is usually reaching for machinery (a queue, a second registry, a sync step) the shape makes unnecessary.

## Propose, in plain words

**Crystallize only on the human's instruction.** The AI may notice a pattern and ask; it never writes a lens, frame or rule on its own initiative. Before anything structural, it says what it would do and why, in the human's terms:

- *"I can add a 'weekly summary' command that lays out your week this way. Want it?"*
- *"What you're describing is its own mechanism. I'd set it up as a new frame that owns X and Y. Want me to draft it?"*
- *"This keeps coming up and nothing we have holds it. I think it's a new piece of understanding: [one sentence]. Want to work it out together?"*

**Then wait for a clear yes.** Changing the sphere's internals happens in [sphere authoring](../modes/sphere-authoring.md), which only the human starts. A yes to one small change counts as a brief step into it, for that change only. Outside it, a change the sphere notices is captured as a `sphere` idea (see [idea-nodes](../idea-capture/idea-nodes.md#the-spheres-own-collection)) and the files are left alone.

## Make the change

In order, in one ground:

1. **The lens,** if there is one. Co-authored: the human brings the understanding, the AI drafts and says where it's guessing, and they iterate.
2. **The frame.**
3. **Its abilities and commands.**
4. **The protocol registry:** a row for each new entry (see [protocol-registry](../sphere-framework/protocol-registry.md)).
5. **The capability manifest** and any other registry that lists what changed (see [capability-manifest](../sphere-framework/capability-manifest.md)).
6. **The checks.** A new tree, layer or kind of file, or a changed frontmatter, updates `core/shapes` and the [structure check](../readable-substrate/structure-check.md) in the same step, and the check stays cheap.
7. **Versions.** A substantive change bumps the lens or frame's `version` and says what changed in `version_note` and a one-line changelog entry. A frame records the lens version it follows (`derives_from: [evolution@1]`). A changed lens fires `lens-shifted`, so its frames are re-read. The sphere's own version moves too (see [sphere-identity](../replication/sphere-identity.md#version)).
8. **The why, kept home.** What prompted the change (the moment, the people, the dates) goes in `core/records/`, with a pointer in the file. The file itself keeps only what changed.
9. **The idea it came from,** if any: set its `outcome` and archive it.

**Done is checked, not declared.** The structure check and the manifest check run before the change is called done, and the human sees the change itself, not a summary of it. The AI never approves its own change (see [evaluator-not-self](../human-is-highest/evaluator-not-self.md)).

## Announce it

When a capability lands, say what changed in three lines:

```
Lens:     the understanding this captures (the why)
Frame:    the mechanics (the how)
Commands: what you can say to use it
```

- **This is how the sphere teaches its own vocabulary.** The human learns how lens, frame and command relate by seeing them in their own sphere.
- **A small addition gets one line:** *"Added 'weekly summary' to your planning frame."*
- **A non-technical human gets plain words, no labels:** *"Done. Just say 'how was my week' any time."* Told as something the sphere saved for them, never as a decision to weigh.
- **Every change is announced.** None is kept silent: announcements are how the human learns how the sphere handles things.
- **One announcement per capability.** Its record is what a witness view reads to show the sphere growing too.

## Sized by how much it touches

**How a structural change is made follows from how much of the sphere it touches.**

| Tier | When | How |
|---|---|---|
| **Targeted** | It can be done completely and correctly in one sitting: a command, a split frame, a renamed lens, a new sense | Size it, propose, confirm, make it, announce, ground |
| **Phased** | New structure has to be built over several sittings before the old can retire: a new layer, a whole new area of lenses and frames, a change in how something is stored | A project, built across sittings as one focus, then a declared cutover |
| **Fork** | Changing it in place would stop the sphere working while it's done: the node shape, the startup sequence, the state machine | A new sphere built alongside the old one, then one switch |

### Phased: the old keeps working until the cutover

1. **Make it a project** under the sphere's own area of work (below).
2. **Build the new structure across sittings, as one focus.** The old structure keeps working the whole time. Each sitting grounds its partial work; **the sphere is never left half-changed between grounds.**
3. **Declare the cutover.** One ground does the final switch: moves, links updated, the old retired.
4. **Ground and announce.**

*Why declared:* a cutover that drifts across sittings leaves the sphere in two shapes at once, and nobody can say which one is true.

### Fork: build alongside, switch once

- **A directory fork:** build the new sphere in a new folder, from a clean start that takes in what worked. The old one keeps running, untouched. Try the new one for a few days, then point the door at it. Keep the old one read-only for a while before retiring it. Best when the new design differs so much that a diff would be noise.
- **A branch fork:** ground every open focus first. Build on a `fork/<name>` branch while every focus keeps committing to `main`. Test it, then merge, tagging the state before and after with the sphere's version, so the old sphere can always be checked out again. It's the one time a sphere has a second branch, and only until the merge. Best when the change is large but still reads as a coherent diff.

**In both, the old sphere isn't changed while the fork is built, and the switch is one deliberate act.**

## The sphere's own work

**The sphere's evolution is tracked like any other [work](../work-tracking/work-breakdown.md):** an ongoing area for the sphere itself, with a project under it for each phased change or fork. Targeted changes don't need a node; their record is the change and its announcement. What's been noticed and not acted on stays in the `sphere` ideas, not in a list on the work.

## When / do

| When | Do |
|---|---|
| The human asks for a new capability | Size it; propose in plain words; wait for a clear yes |
| A pattern keeps recurring | Ask whether to capture it. Never write it unasked |
| A change is noticed outside sphere authoring | Capture it as a `sphere` idea; leave the files alone |
| `node-archived idea`, if a `sphere` idea graduated | Size it and propose it like any change |
| A change is approved | Make it in order, in one ground: lens, frame, abilities, registry, manifest, checks, versions, records, idea |
| The change adds a tree, a layer or a kind of file, or changes a frontmatter | Update `core/shapes` and the structure check in the same step |
| A change is made | Run the checks; show the human the change; announce it. |
| A refactor touches more than one sitting can finish | Make it a project; build beside the old; declare the cutover |
| A change would stop the sphere working while it's made | Propose a fork; the human picks directory or branch |

## Works with

- [reflection](reflection.md): where most proposed changes come from.
- [rule-capture](rule-capture.md): a guardrail is a change too, sized and placed the same way.
- [idea-nodes](../idea-capture/idea-nodes.md): the `sphere` ideas hold what's been noticed; a change settles one.
- [protocol-registry](../sphere-framework/protocol-registry.md) and [capability-manifest](../sphere-framework/capability-manifest.md): registered in the same ground as the change.
- [structure-check](../readable-substrate/structure-check.md) and [manifest-check](../readable-substrate/manifest-check.md): change with the sphere, and confirm the change.
- [propose-dont-decide](../human-is-highest/propose-dont-decide.md) and [evaluator-not-self](../human-is-highest/evaluator-not-self.md): proposed, and never approved by the AI itself.
- [sphere-authoring](../modes/sphere-authoring.md): where changes to the sphere's internals are made, shown and confirmed.
- [sphere-identity](../replication/sphere-identity.md): the sphere's version moves when its protocol does.

