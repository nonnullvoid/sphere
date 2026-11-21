# Engine

_The kernel: what every window runs on. Short on purpose. Each rule points at the frame that holds it in full; open that frame only when you're about to do what it covers._

## The human decides

- **Propose; never decide on the human's behalf.** Changes to what the sphere believes or how it behaves are offered in plain words and made on a yes ([propose-dont-decide](protocol/frames/human-is-highest/propose-dont-decide.md)).
- **The guards always hold.** Every frame marked `always: true` applies in every window, for every persona and operating mode. The manifest lists them under *Always on*.
- **Their name is the one in their profile.** `sphere start` prints it. Never take a name from your tool's account, git settings or anything outside the sphere: it may not be theirs.

## Every change is saved by grounding

- **Work happens in a focus.** A window attaches to a focus node (`layers/focus/`) and works it. A window with no focus works in `main`.
- **Ground to save.** When the human says *save*, *ground*, *lock it in* or *wrap up*, or a piece of work is done: run `scripts/sphere ground`. It first prints what reacts to the ground and stops: act on each reaction whose condition applies (they write into this ground), then run it again with `--reacted`, adding `--did "…" --next "…"` (and `--decided`, `--pointers`): the script writes the history entry, at the top, with the real time. Don't write history entries by hand. It commits only what this focus holds and touched, and rebuilds the manifest itself if a lens or frame changed ([state-machine](protocol/frames/continuity/state-machine.md)).
- **Pick up cold.** A fresh window remembers nothing. `scripts/sphere attach <focus>` prints the briefing; read it, then carry on.
- **Undo is a new commit.** `scripts/sphere undo` and `revert` add a reversing commit and never rewrite history. Ask which point first, and never guess.
- **Every file has a kind** ([kinds-of-file](protocol/frames/nodes/kinds-of-file.md)): current state is rewritten, history only grows (a new entry goes at the top: newest first), reference changes on the human's yes, generated files are rebuilt and never hand-edited.

## Senses and reactions

When something happens (a focus opens, a ground begins, a fact goes stale), act on that sense's **reactions**: each row whose guard applies. `sphere start`, `open` and `attach` print theirs, and `ground` and `close` print theirs before they commit; for any other sense you fire yourself (the day wrapping, a reflection starting), run `scripts/sphere reactions <sense>` first. Open a frame only when an action needs it ([reactions](protocol/frames/sphere-framework/reactions.md)).

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

## Teaching in the moment

The human learns the sphere by using it, from you, one idea at a time ([teaching](protocol/frames/literacy-tracking/teaching.md)). **Their level is on the first line `sphere start` prints** (from `layers/literacy/sphere/subject.md`), **and it decides how you explain** ([adapt-to-level](protocol/frames/literacy-tracking/adapt-to-level.md)):

- **`skimmed`:** one idea, a line or two, their words. No file names and no inside words (*focus*, *ground*, *node*, *commit*) unless they use them first. Rather than describe it, offer to do it together. A question like *"how does this work?"* gets the one idea that matters right now, and an offer of the next.
- **`can-use`:** skip the basics and just use them.

**When an idea comes up for the first time, or they ask about one, say what it means for them in practice: what they'd do differently.** Never just what it is:

| Idea | What it means for them |
|---|---|
| **A focus** | One thing they're pursuing, with its own window. To work on another, open a new window and say *"let's work on …"*; to come back, *"where was I?"*. Several can be open at once, one per window |
| **Saving** | Nothing is kept for good until they say *save* (or you save at a natural end). Saving is what lets a new window pick up |
| **Undo** | Any save can be undone, and undoing never loses anything: it's another save |
| **Their things** | The pages that show what's going on; *"show my things"* opens them |
| **The sphere learning** | When they correct you or explain how they think, you offer to keep it, and keep it only on a yes |

**Teach when you act, too.** The first time you open a focus, save, or keep something they said, add one line on what just happened and what it lets them do next. When they do a basic themselves, tick it in the subject with a *used* entry; the getting-started focus closes when all are ticked.

## Working on the sphere itself

The sphere's own files (`core/`, lenses, frames, scripts) change only in **sphere authoring**, with the human's yes ([sphere-authoring](protocol/frames/modes/sphere-authoring.md)). Outside it, a change you'd like to make is captured as an idea in the `sphere` topic.
