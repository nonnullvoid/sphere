# Engine

_The kernel: what every window runs on. Short on purpose. Each rule points at the frame that holds it in full; open that frame only when you're about to do what it covers._

## The human decides

- **Propose; never decide on the human's behalf.** Changes to what the sphere believes or how it behaves are offered in plain words and made on a yes ([propose-dont-decide](protocol/frames/human-is-highest/propose-dont-decide.md)).
- **The guards always hold.** Every frame marked `always: true` applies in every window, for every persona and operating mode. The manifest lists them under *Always on*.

## Every change is saved by grounding

- **Work happens in a focus.** A window attaches to a focus node (`layers/focus/`) and works it. A window with no focus works in `main`.
- **Ground to save.** When the human says *save*, *ground*, *lock it in* or *wrap up*, or a piece of work is done: fire `focus-grounding`, act on its reactions (they write into this ground), then run `scripts/sphere ground`. It commits only what this focus holds and touched ([state-machine](protocol/frames/continuity/state-machine.md)).
- **Pick up cold.** A fresh window remembers nothing. `scripts/sphere attach <focus>` prints the briefing; read it, then carry on.
- **Undo is a new commit.** `scripts/sphere undo` and `revert` add a reversing commit and never rewrite history. Ask which point first, and never guess.
- **Every file has a kind** ([kinds-of-file](protocol/frames/nodes/kinds-of-file.md)): current state is rewritten, history is only appended, reference changes on the human's yes, generated files are rebuilt and never hand-edited.

## Senses and reactions

When something happens (a focus opens, a ground begins, a fact goes stale), look up that sense in the manifest's **reactions table** and act on each row whose guard applies. Open a frame only when an action needs it ([reactions](protocol/frames/sphere-framework/reactions.md)).

## Checks

At every ground, after generated files are rebuilt, run `scripts/structure-check` and `scripts/manifest-check`. They report; they never fix. Fix what they find in the same ground, or put it to the human.

## Words

| The human might say | The sphere does |
|---|---|
| *save*, *ground*, *lock it in* | ground this focus |
| *where was I?*, *pick up …* | attach and brief |
| *open a focus for …*, *let's work on …* | open a focus |
| *wrap up* | the end-of-day wrap ([daily-cadence](protocol/frames/human-rhythm/daily-cadence.md)) |
| *show my things* | open `surface/projections.html` |
| *what can you do?* | answer from the [registry](protocol/protocol.md) |

Asking in plain words always works. None of these is a command to learn.

## Working on the sphere itself

The sphere's own files (`core/`, lenses, frames, scripts) change only in **sphere authoring**, with the human's yes ([sphere-authoring](protocol/frames/modes/sphere-authoring.md)). Outside it, a change you'd like to make is captured as an idea in the `sphere` topic.
