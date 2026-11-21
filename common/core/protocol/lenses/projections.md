---
lens: projections
version: 1
version_note: First draft. A projection is a view of the sphere's files, never their source; it shows the human's matter, never the machinery, and it says how fresh it is.
derives_from: practice in spheres in daily use; spec/projections.md
status: drafting
updated: 2026-11-13
verified: false
sharing: public
frames: [projection-registry, projection-freshness, projection-templates, projection-serving]
---

# Matter, never machinery

**A projection is how a sphere shows a person what it holds:** a page of work in motion, a picture of how they've grown, a guide prepared for them to read. The sphere's files are its truth, but files aren't how most people want to see their life. A projection is a picture of those files, rendered for a human.

**It shows the human's matter, never the sphere's machinery.** Matter is their work, their world, their growth. Machinery is lenses, frames, registries, focus nodes and git. For a person who never opens a file, projections are the whole interface, so what they see there has to be their things, not ours.

## Two boundaries

**A window is where the human and the sphere talk; a projection is where the sphere shows.** A window is live: the human attaches, works and leaves. A projection stays, and the human comes back to it for two reasons:

- **To audit and follow:** what's in motion, what the sphere is doing, and why.
- **To learn:** reports, guides and references the sphere prepared for them.

Some projections also accept input: a checklist, a *mark done* button. The human acts on the sphere without typing to it.

## Never the source

**A projection is a picture of the files. If the picture and the files disagree, the files win,** and the picture is fixed by rendering it again, never by editing it.

- **Input goes back to the files.** A click on a view is an edit to a source file, made through the sphere; then the view renders again from that file. *Why:* a view that keeps its own state has become a second source of truth, and the two will drift.
- **A view never invents a fact.** If it needs a value that no part of the sphere owns, that's a missing fact, not view data. Give it an owner first, then show it.
- **Something that needs its own data isn't a projection.** It's a source, declared like any other, so the sphere knows it holds truth.

## Honest about how fresh it is

**Every projection says what kind it is, up front:**

- **Live:** it reads its files every time it's opened. Nothing to refresh.
- **Refreshed:** a render step brings it up to date, at ground or when asked.
- **Snapshot:** made once, for a moment, and never changed again.

**Every page says when it was rendered and from what.** A refreshed view past its freshness says so, plainly, where the reader is looking. *Why:* a stale view that looks current is the worst failure a projection can have, because people make decisions from it.

**The thinking happens once.** Live and refreshed views render without judgment: the same files give the same page, every time. The intelligence went into choosing what to show and how. A snapshot is where judgment belongs: a walkthrough or a report is composed by reading across the sphere, stamped with where it came from, and frozen.

**Don't make everything live.** A snapshot that captures a moment well often beats a dashboard nobody keeps current. Reach for live only when freshness is the promise.

## Matter, never machinery

- **For a non-technical human, this is absolute.** Their projections are the index page (*my things*) and a view of how they're growing. Nothing else.
- **For people building their own sphere,** views of the machinery are allowed as an option: a map of layers, a view of the protocol. They're never the front door.
- **Views of growth deserve care.** Seeing your own progress over time is one of the warmest things a sphere offers, especially to someone who'd never read a file. It's worth building well.

## Kept apart, so each can change

A projection is four things, each in its own place:

| Part | Holds |
|---|---|
| **Frame** | The mechanics every projection shares: registering, rendering, refreshing, serving |
| **Definition** | What this projection shows and how, in its own node |
| **Registry entry** | Its kind, sources, home and who may see it, built from the definition |
| **Artifact** | The rendered page and anything computed for it |

A new look is a template change. A new source is a definition change. A new audience is a sharing change. None of them touches the others.

## How it shows up

- **Private by default.** Every projection says who may see it. Opening one up is an outbound act: the human approves it, and facts about other people stay out unless they're named and included.
- **One look across every view.** Pages share their chrome, and navigation and the index page (`surface/projections.html`) are built from the registry, so a new view is linked everywhere the moment it exists.
- **A pattern becomes a template on its third appearance,** never before.
- **Plain web pages, kept local.** No build step, nothing loaded from the internet, and a server, when one is needed, only on this machine. A page that still opens in ten years.
- **Once it needs an app, it's no longer a projection.** It's an application that reads the sphere, kept outside it, and it still has to say how it stays current.
- **A one-time render isn't kept unless asked.** A walkthrough made to explain one change opens from scratch and is gone; if the human wants it, it gets a home like any other.

## What it doesn't mean

- **Not a second place to keep things.** Nothing is true because a page says so.
- **Not a gate in front of the files.** The human can always open the files themselves (see [readable-substrate](readable-substrate.md)). A projection is a convenience, never the only way in.
- **Not everything on a dashboard.** A view earns its place by being looked at. One nobody opens is retired.
- **Not hiding how things work.** Builders can see the machinery whenever they want. It just isn't what a human lands on.

## What follows from it

| Frame | In short |
|---|---|
| [projection-registry](../frames/projections/projection-registry.md) | A projection is a node: its definition, the generated registry, where artifacts live, retiring and orphans |
| [projection-freshness](../frames/projections/projection-freshness.md) | Live, refreshed and snapshot; staleness on the page; provenance; rendering only what's grounded |
| [projection-templates](../frames/projections/projection-templates.md) | Extracting and filling templates, shared chrome, the one-shot template for snapshots, what views are built with |
| [projection-serving](../frames/projections/projection-serving.md) | Static or served; the local server; input written only to declared sources |

## Revision history

- **v1:** First draft. Spec chapter *projections*.
