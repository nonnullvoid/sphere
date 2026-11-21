---
frame: projection-serving
lens: [projections]
derives_from: [projections@1]
version: 1
version_note: First draft. Static or served; one local server on this machine only; input written only to the sources a view declares.
status: drafting
updated: 2026-11-13
sharing: public
reads: [layers, layers/projections, surface/projections]
writes: [layers]
protocol: [I-act-from-what-i-see, A-open-projection, A-accept-input, projection-input]
---

# Opening a view, and acting from one

**Applies to:** opening any projection, anything a view lets the human do (tick a box, mark something done, fill a form), and the local server that makes that possible.

## Static or served

Each projection says how it opens, from what it's for:

| Opens as | Fits | Requirement |
|---|---|---|
| **static** | Snapshots and one-off renders: a walkthrough, an explainer, a year in review | **Self-contained:** data, styles and scripts inside the one file, so it opens with a double-click and no server |
| **served** | Live views, and anything that accepts input | Opened through the sphere's local server |

Live views are served. Snapshots are static. A refreshed view can be either: static with its data rendered in, or served if it accepts input.

## The local server

- **It starts when a served projection is opened,** is reused if it's already running, and stops when the last window detaches or the human asks. Whether it's running is liveness: disposable, never committed.
- **It listens on this machine only, never on the network.** *Why:* a private projection stays private only if nothing outside the machine can reach it.
- **It serves what's been grounded.** Sources are read as of the sphere's latest commit, so a view never shows a focus's unsaved work (see [projection-freshness](projection-freshness.md#what-a-view-shows-whats-been-grounded)).
- **It serves only what a view declares:** the projection's own artifact, the shared assets, and the files in its `sources`. Nothing else in the sphere is reachable through it.
- **A non-technical human never sees any of this.** They say *"show my things"*; the sphere starts the server and gives them a link to bookmark.

## Input goes back to the source

**A view that accepts input writes only to the files in its own `writes:`.** Anything else is refused, whatever the page asks for. The server is the one path back from a view, and it's narrow on purpose.

- **A click is the human acting.** It's the human's own edit to the file, made through the page, so it's handled the way their own edit would be, by [kind of file](../nodes/kinds-of-file.md):
  - **History:** appended.
  - **Current state:** written, unless a focus holds that file right now. Then it's offered to the holder, and the view shows it as waiting (*"f21 is working on this; your change is with it"*).
  - **Generated:** never written. A view changes the node, and the index rebuilds from it.
- **It's saved at once.** Each accepted input is grounded as its own small change, with a line saying it came from the view. *Why:* the view renders from the latest commit, so an unsaved click would vanish from the page it was made on.
- **The page renders again from the source.** It never shows its own guess of the result.
- **Nothing leaves the sphere from a view.** A *send* button only makes a draft; the [outbound guard](../human-is-highest/outbound-guard.md) still applies, as it does everywhere.
- **A view that needs to keep its own data isn't a projection.** Declare that data as a source, with an owner, like any other truth.
- **A value no source owns is a missing fact.** Give it an owner before a view shows it or lets anyone edit it.

## When / do

| When | Do |
|---|---|
| A static projection is opened | Open the file. Nothing to start |
| A served projection is opened | Start the local server, or reuse it; serve the artifact, the assets and its sources as of the latest commit |
| The last window detaches | Stop the server |
| A view sends input for a file in its `writes:` | Apply it by kind of file; ground it as its own change; render the view again. Fire `projection-input` |
| The file it targets is held by a focus | Offer the change to that focus; show it as waiting on the page |
| A view asks to write anything not in its `writes:` | Refuse it, and say so on the page |
| A view tries to send something out | Make a draft; the outbound guard decides |
| A view needs a value nothing owns | Stop, and propose an owner for the fact first |

## Works with

- [projection-registry](projection-registry.md): where `opens`, `sources` and `writes` are declared.
- [projection-freshness](projection-freshness.md): served views read the latest commit.
- [kinds-of-file](../nodes/kinds-of-file.md) and [focus-holds](../focus/focus-holds.md): who may write what, and offering a change to a holder.
- [state-machine](../continuity/state-machine.md): each accepted input is a small ground.
- [outbound-guard](../human-is-highest/outbound-guard.md): nothing leaves from a view without the human's yes.

## Senses

| Sense | Fires when |
|---|---|
| `projection-input` | a view's input is written to one of its declared sources |
