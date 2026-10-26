# Evolution

_Status: draft 1, for review._ How a sphere grows, stays healthy, and restructures: new capabilities crystallizing from use, the sphere reflecting on itself, and changes of every size made without breaking the sphere along the way.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

---

## The idea

A sphere is never finished. It grows by **crystallizing** patterns from use into named capabilities. It stays healthy by **reflecting**: noticing what's missing, what's unused, what's drifted. And it **migrates** when its structure needs to change, in a way that matches how big the change is.

Three mechanisms, one loop:

```
use → notice → reflect → propose → (human decides) → crystallize or migrate → announce → use
```

Everything in this loop is **co-authored**. The sphere notices and proposes; the human decides. Nothing about how the sphere understands its human, or how it behaves, changes on the sphere's own initiative. See [protocol](protocol.md#co-authoring-the-method).

---

## Crystallization: how capabilities grow — **proven**

### Size the change first

Not every request deserves a structural change. The first question is always: what size is this?

| Size | When | What happens |
|---|---|---|
| **One-off** | It happened once; it's unlikely to recur | Just do it. Nothing is recorded. |
| **Command** | A new way to ask for something the sphere already does | Add the command to its frame; register it. |
| **Ability** | A new capability inside an existing frame's scope | Add it to the frame; register it. |
| **Frame** | Distinct mechanics that don't fit any existing frame | Propose a new frame under the lens it derives from. |
| **Lens** | A distinct *understanding*: a why that no existing lens holds | Propose a new lens. The heaviest step, since everything below derives from it. |
| **Refactor** | Something existing is too wide, overlapping, misnamed or wrong | Size its blast radius and choose a [migration tier](#migration-sized-by-blast-radius--proven). |

**Thresholds:**
- **A new frame** needs distinct mechanics, usually with its own data, senses or abilities, that won't fit an existing frame without stretching it.
- **A new lens** needs a why that can't be derived from existing lenses. Mechanics alone justify a new frame, never a new lens.

**A new layer is a separate decision.** A layer is a home for data, not a unit of understanding. It's warranted only when a capability needs its own persistent data **and** that data fits no existing layer. Most capabilities live in existing layers. See [registries](registries.md#layer-contracts--proven).

### Propose, in plain language

Before writing anything structural, the sphere says what it would do and why, in the human's terms:

- *"I can add a 'weekly summary' command that formats your week this way. Want it?"*
- *"What you're describing is its own mechanism. I'd set it up as a new frame. It would own X and Y. Want me to draft it?"*
- *"This keeps coming up and nothing we have captures it. I think it's a new piece of understanding: [one sentence]. Want to work it out together?"*

**Then wait for a clear yes.**

### Make the change

In order:
1. The lens, if there is one (co-authored).
2. The frame.
3. The commands and abilities.
4. Register everything in the protocol registry.
5. Refresh whatever registries and loading indexes changed.
6. Close the queued item, if it came from the [pending queue](#evolution-as-work--decided-not-yet-exercised).

### Announce it, and teach while doing so

When a new capability lands, the sphere says what changed in three lines:

```
Lens:     the understanding this captures (the why)
Frame:    the mechanics (the how)
Commands: what you can say to use it
```

This is the sphere's **main way of teaching its own vocabulary.** The human learns how lens, frame and command relate by seeing real examples from their own sphere, not by reading documentation. For a small command added to an existing frame, a single line is enough: *"Added 'weekly summary' to your planning frame."* For a non-technical human, the same announcement comes in plain words, without the labels: *"Done. Just say 'how was my week' any time."*

The announcement fires the `sphere-evolved` sense. A witness theme can record it as growth of the sphere itself.

---

## Reflection: how the sphere stays healthy — **proven**

Evolution adds. Reflection balances. Without it, a sphere accumulates capabilities nobody uses and mechanisms that no longer fit.

### Two scales

- **Targeted reflection:** one capability, one frame, one area. Is it serving its purpose? Is there friction? Is something adjacent missing? The output is a short diagnosis and one concrete proposal, not a treatise.
- **Deep reflection:** the whole sphere. The output is a list of findings, each of which becomes an item in the [pending queue](#evolution-as-work--decided-not-yet-exercised).

### Four findings

| Finding | Means | Leads to |
|---|---|---|
| **Gap** | Something the human wants that the sphere can't do | Propose a new capability |
| **Bloat** | Something that serves no real purpose, or is never used | Propose removing or simplifying it |
| **Misalignment** | Something whose design doesn't match how it's actually used | Propose a redesign |
| **Discovery** | A repeated pattern already in use, but never named | Propose crystallizing it |

A useful test for bloat, borrowed from the wider personal-AI community: *would a more capable model make this rule unnecessary?* If yes, it's scaffolding, and it's a candidate to cut. Guards, hard-won gotchas, and exact tool recipes survive the test. They hold no matter how capable the model gets.

### The friction instinct

The sphere notices friction without being told: *"something feels off about how we track meetings,"* *"I never use that summary."* It responds to the friction directly, by showing a better way or proposing a fix. It doesn't explain what reflection is. The human learns reflection by experiencing it, not by learning the word.

Reflection fires the `reflection-triggered` sense.

### A rhythm, not a schedule

A sphere tends to need evolution every couple of weeks. That's a rhythm, not an appointment. The sphere recognizes the signal itself:
- a concept keeps surfacing with nowhere to live
- a frame feels stretched or misnamed
- the human expresses friction with something that used to work
- several findings cluster in one area

When the signal fires, it suggests a targeted or deep reflection at a good moment. The human doesn't have to remember to ask.

---

## Evolution as work — _decided, not yet exercised_

A sphere's own evolution is tracked like any other work, as [work nodes](work.md):

- **An evolution stream:** an ongoing node that never finishes. Each substantial evolution effort becomes a bounded project under it.
- **A pending queue** for items noticed but not yet acted on: findings, friction, ideas about the sphere. One line each: what kind of change (add / refactor / drop), the target, a line of context, and how soon (now / soon / someday).
- At each evolution session, the queue is triaged. Each item is done on the spot, promoted to a project, or dropped.

---

## Migration, sized by blast radius — **proven**

How big a structural change is decides how it's made.

### Targeted: one session

**When:** the whole change can be done completely and correctly in one session. Adding a command, splitting a frame, renaming a lens, adding a sense.

**How:** size it → propose → confirm → make it → announce → ground.

### Phased: several sessions, then a declared cutover

**When:** new structure has to be built over several sessions before the old one can retire. A new layer, a whole new area of lenses and frames, a change in how something is stored.

**How:**
1. Create a project under the evolution stream.
2. Build the new structure across sessions. **The old structure keeps working the whole time.** The sphere is never left half-migrated between sessions.
3. Each session grounds its partial work.
4. **Declare a cutover session** explicitly. One session does the final switch: moves, reference updates, retiring the old.
5. Ground and announce.

**The cutover is declared, never gradual.** A migration that drifts across sessions leaves the sphere in two shapes at once.

### Fork: build a new sphere alongside the old

**When:** the change is fundamental enough that migrating in place would stop the sphere working while it's done. Examples: the protocol model itself, the startup sequence, how layers are named, the state machine.

Two ways to fork:

- **A directory fork.** Build the new sphere in a new folder, from a clean start that absorbs what worked. The old sphere keeps running, untouched. Test the new one for a few sessions, then switch the door to point at it. Keep the old one read-only for a while before retiring it. Best when the new design differs so much that a diff would be noise.
- **A branch fork.** First ground every open session. Then build the new structure on a `fork/<name>` branch while `main` keeps running. Test it, then merge, tagging the old state (`sphere-v<N>`) and the new (`sphere-v<N+1>`). The old sphere stays recoverable from its tag. Best when the change is large but still reads as a coherent diff.

**In both:** the old sphere isn't modified during the fork, and the switch is one deliberate act.

---

## Open questions

1. **The rhythm.** Is "every couple of weeks" right for most spheres, or should each sphere learn its own?
2. **Where the pending queue lives** at simple session level: in the evolution work node, or in a small file of its own?
3. **Announcing for non-technical humans.** Is a plain-words announcement enough, or should some changes stay silent unless asked about?
