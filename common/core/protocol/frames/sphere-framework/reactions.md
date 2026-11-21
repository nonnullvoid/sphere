---
frame: reactions
lens: [sphere-framework]
derives_from: [sphere-framework@1]
version: 1
version_note: First draft. Senses, who produces them, and the reactions that follow each, computed from the frames when a sense fires.
status: drafting
updated: 2026-11-20
sharing: public
reads: [core/protocol, core/manifest.md]
writes: [core/manifest.md]
protocol: [I-know-what-it-can-do, A-react, stale-found]
---

# Reactions

**Applies to:** a sense firing, writing a When/do row that reacts to one, adding a sense, and offering a habit as a new reaction.

A sphere has no event bus. A **sense** is the name of a moment the AI is told to watch for, and what follows it is a lookup, not a load: the **reactions** to a sense are the When/do rows, across every frame, that start with it. `scripts/sphere reactions <sense>` prints them: which frames react, when, and what they do.

## Where senses come from

| Producer | Examples | How reliable |
|---|---|---|
| **The `sphere` script** | `focus-opened`, `focus-attached` | Certain. The script prints the sense name and its reactions, so they land in context at the moment it happens, whether or not the AI has read anything |
| **A check** (shape, drift, manifest) | `stale-found`, `check-failed`, `dirty-detected` | Certain. A finding *is* the condition |
| **The AI, as it begins something** | `focus-grounding`, `focus-closing`, `day-wrapped`, `reflection-started` | Certain once the AI is doing it: the row that starts the operation fires the sense |
| **The AI's judgment** | `waiting-on-human`, `work-stalled`, `gap-detected`, `new-territory` | Best effort. The AI notices because the manifest's trigger line tells it to look |

**A ground's reactions run before its commit.** That's why the sense is `focus-grounding`, not *grounded*: a fact offered, an index rebuilt or a view re-rendered lands in the same commit as the work that caused it. The same holds for `focus-closing`.

## The core moments

Every build has these. Frames hook them; none of them is any one frame's private event.

| Sense | Fires when | Produced by |
|---|---|---|
| `focus-opened` | a new focus node starts | `sphere open` ([focus-nodes](../focus/focus-nodes.md)) |
| `focus-attached` | a window joins an existing focus | `sphere attach` ([focus-nodes](../focus/focus-nodes.md)) |
| `focus-grounding` | a ground begins; reactions write into it, then it commits | [state-machine](../continuity/state-machine.md) |
| `focus-closing` | a close begins; its own ground follows | [focus-nodes](../focus/focus-nodes.md) |
| `node-archived` | a node moves to `archived/`. Carries its link | [node-shape](../nodes/node-shape.md), and every frame that finishes a node |
| `day-started` | the morning orientation is given | [daily-cadence](../human-rhythm/daily-cadence.md) |
| `day-wrapped` | the wrap begins | [daily-cadence](../human-rhythm/daily-cadence.md) |
| `reflection-started` | a targeted or deep reflection begins | [reflection](../evolution/reflection.md) |
| `sphere-authoring-started`, `sphere-authoring-ended` | the sphere's internals may change, or stop changing | [sphere-authoring](../modes/sphere-authoring.md) |
| `lens-shifted`, `frame-shifted` | a lens or frame changed, so what derives from it is re-read | [sphere-authoring](../modes/sphere-authoring.md) |
| `mode-switched` | a focus's operating mode, collaboration mode or persona changed | [operating-modes](../modes/operating-modes.md), [collaboration-modes](../modes/collaboration-modes.md), [persona](../modes/persona.md) |

Every other sense is a **condition**: something one frame notices that needs action (a breaker tripped, rules conflict, a run waiting on the human, an agent earned a promotion). It lives in that frame. The full list, with who produces and who reacts to each, is in the [registry](../../protocol.md).

**A record is not a sense.** "An idea was captured" or "a template was extracted" is something the sphere did, not something it noticed. The history entry, ledger line or commit is the record, and growth and reflection read records.

## Reacting rows

A frame reacts to a sense in its When/do table. The **When** cell starts with the sense in backticks; whatever follows is the **guard**:

```
| `focus-grounding`, with facts to offer | Offer them as one batch; write what's confirmed |
| `node-archived work`, if it was the last work in a plan's `for:` | Ask whether the plan is done too |
```

- **No guard means always.** Most reactions have one, and that's what keeps a busy moment cheap: most rows decide in a glance that they don't apply.
- **A frame lists every sense it produces or reacts to** in its `protocol:` field. That listing is what wires it.
- **A row that produces a sense says so in its Do cell:** *Fire `x`*.

## Conditions find their frame by tree

A condition about a node carries the node's **link**, and the link's tree picks the reaction:

- `stale-found knowledge:money.taxes` → the rows for `stale-found knowledge`: a plan whose assumption points at it is flagged; a tracked subject that rests on it is marked stale.
- `stale-found projection:monthly-budget` → the view is shown as stale and a refresh is offered.
- `node-archived work:tax-20` and `node-archived idea:20261116-weekly-summary` reach different rows the same way.

A condition about something that isn't a node names the thing instead: `stale-found manifest`, `stale-found work-index`.

So reactions are looked up **by sense, then by tree**. A row written `` `stale-found` `` with no tree reacts to every kind.

## Looking up the reactions

**Computed when the sense fires, never kept as a table.** The rows live in their frames, so there's nothing to rebuild and nothing to go stale:

```
$ scripts/sphere reactions focus-grounding
reactions: focus-grounding
  knowledge-capture (with facts to offer): Offer them as one batch; write what's confirmed
  work-registry (if the ground touched work): Rebuild the index
  reaching-the-human (if anything is waiting): Add the ground line
  …
$ scripts/sphere reactions stale-found knowledge:money.taxes
reactions: stale-found
  plans (if a plan's assumption points at the topic): Flag the plan for review
  skill-progress (if a tracked subject rests on the topic): Mark the subject stale: check lightly next time
```

- **The script delivers what it produces.** `sphere start`, `open` and `attach` print each sense followed by its reactions. *Why:* an instruction to go and look something up is the first thing a model in a hurry skips; output it has already been handed isn't.
- **A ground or a close won't commit until its reactions are handled.** `sphere ground` and `sphere close` print `focus-grounding` (and `focus-closing`) with their reactions and stop; the AI acts on them, then runs the command again with `--reacted`. The most important moment in a window is enforced, not remembered.
- **The AI looks up the rest of what it fires.** For any other sense the AI produces (the day wrapping, a reflection starting), it runs `scripts/sphere reactions <sense>` as it begins.
- **Then, for each row:** skip it if its guard doesn't apply; otherwise do the one-line action. Open a frame only when the action needs that frame's mechanics. Loading every reacting frame instead would cost more than anything else in a window: nearly twenty frames react to a ground.

The [manifest-check](../readable-substrate/manifest-check.md) confirms that every sense a row names is in its frame's `protocol:` list and in the [registry](protocol-registry.md).

## Common sense

Reactions are how a sphere comes to know what a person would just know to do at a moment. It grows at three levels:

1. **Habits become reactions.** When the human does the same thing at the same moment three times with no frame asking (checks the calendar whenever a focus opens), the sphere offers it as a reaction. On a yes, it's a row in a frame, written in [sphere authoring](../modes/sphere-authoring.md). Each window starts cold, so the repetition is read from records (history entries, what a close writes), not remembered.
2. **Shared reactions get one row.** When several frames react to one sense the same way, the table shows it. Reflection proposes pulling the shared reaction into one row the others point to.
3. **Reactions found in many spheres** are what the common set ships.

**Nothing adopts itself.** The sphere notices and offers; the human decides.

## Reflex, second nature, reaction, skill

The sphere can't author instinct. Everything it adds is text the model reads, so every behavior it writes is looked up, however fast. The model's own trained dispositions are the only real instinct, and only changing the model changes them. That's out of scope by design: a sphere stays readable and is shaped by the human and the AI together, never by tuning itself.

What the sphere can author, from closest to instinct to furthest:

| Layer | Works like | In the sphere |
|---|---|---|
| **Reflex** | Mechanical; no judgment involved | Tooling: `sphere` printing a sense, commit checks, the manifest and shape checks |
| **Second nature** | Always present; applied without deciding to look | The floor: guards marked `always: true`, in context in every window |
| **Reaction** | A practised response, found by name | When/do rows, looked up when the sense fires |
| **Skill** | Thought through, step by step | A frame's body, loaded when it's needed |

- **Moving a reaction to the floor is how a habit becomes second nature.** It costs context in every window, so it's rare and reviewed (`floor-grew`).
- **When the model's instinct runs against the sphere** (it rushes to call work done, softens bad news, acts without asking), prose is the weakest override. It fades over a long window and loses to strong training. Move the rule *up* the table: from a frame body to an always-on guard with its *why*; from a guard to a reflex the tooling enforces; and, where the stakes are real, to a step only the human can take. [Rule-capture](../evolution/rule-capture.md) starts that climb: a rule that keeps failing becomes a proposed enforced check.
- **When the model's instinct already does the right thing,** the sphere's version is scaffolding. Reflection asks: *would a more capable model make this unnecessary?* As models improve they take over rungs from the bottom up. What they never take over is what the lenses hold: this human's own understanding.

## Adding a sense

A new sense is a sphere change. Before adding one:

- **Is it a record?** If nothing would react to it, it's history, not a sense.
- **Is it an existing sense on a new tree?** A new kind of stale is `stale-found` with a new tree, not a new name.
- **Is it a moment many frames would hook, or one frame's condition?** A moment joins the core table above; a condition lives in its frame.

Then: a row in the [registry](protocol-registry.md), the producing frame's *Fire* clause, and its reacting rows, in one ground.

## When / do

| When | Do |
|---|---|
| A sense fires | Act on its reactions (printed by the script, or `scripts/sphere reactions <sense> [link]`): each row whose guard applies; open a frame only to run it |
| A check finds something stale | Fire `stale-found` with the thing's link or name |
| Writing a row that reacts to a moment | Start the When cell with the sense in backticks, then the guard; list the sense in the frame's `protocol:` |
| The human does the same thing at the same moment a third time | Offer it as a reaction, once. The human decides |
| Two or more frames react to one sense the same way | Propose one shared row, at the next reflection |
| A new sense is proposed | Ask the three questions above; prefer a new tree on an existing sense to a new name |

## Works with

- [capability-manifest](capability-manifest.md): says what exists; the reactions are looked up, not listed there.
- [protocol-registry](protocol-registry.md): defines each sense once, with its home frame.
- [manifest-check](../readable-substrate/manifest-check.md): confirms the frames and the registry agree on every sense.
- [node-names](../nodes/node-names.md): the `tree:name` link a condition carries.

## Senses

| Sense | Fires when |
|---|---|
| `stale-found` | a check finds something out of date with what it rests on. Carries the thing's link or name; each tree's rows react to their own kind |
