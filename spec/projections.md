# Projections

_Status: draft 2, for review._ How a sphere shows its state to people: rendered views of its files, such as dashboards, maps and pages, that are always honest about what they show and how fresh it is.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

---

## The idea

A sphere's files are its truth, but files aren't how most people want to see their life or their work. A **projection** is a view rendered from those files: a dashboard of work in motion, a map of growth over time, a home page that links everything.

One rule underneath all of it: **a projection is never the source of truth.** It's a picture of the files. If the picture and the files disagree, the files win, and the picture is fixed by re-rendering it, never by editing it. — **proven**

For a non-technical human, projections are the whole interface. They see their things, never the sphere's machinery. See [Matter, not machinery](#matter-not-machinery).

---

## Four parts, kept separate — **proven**

| Part | What it holds | Where |
|---|---|---|
| **Frame** | The mechanics: when a projection is rendered, refreshed, published | `core/protocol/frames/projections/` |
| **Render rules** | What this projection shows and how: sources, layout, what to leave out | `layers/projections/<name>.md` |
| **Registry entry** | Its kind, freshness, source, home, who can see it, template | `layers/projections/registry.md` |
| **Artifact** | The rendered thing itself | `surface/projections/<name>/` |

Kept apart, each can change without breaking the others. A new look is a template change. A new data source is a render-rule change. A new audience is a registry change.

---

## Freshness — **proven**

Every projection declares which of three kinds it is:

| Kind | How it stays current | Example |
|---|---|---|
| **live** | Reads its source files when someone opens it. Nothing to sync. | A work dashboard that reads the work index each time it loads |
| **manually synced** | Someone or something runs a sync to update it | A portfolio view built from exported account data |
| **snapshot** | Rendered once, at a moment, and never updated | A year-in-review page |

**Staleness must be visible on the projection itself.** Every artifact shows when it was last rendered and from what. A manually synced view that's past its freshness window says so plainly, on the page, where the reader is looking. A stale view that looks current is the worst failure a projection can have, because people make decisions from it. — _decided, not yet exercised_

_The lesson behind this rule:_ a dashboard showing stale financial numbers, silently, because the sync step hadn't run. Nothing on the page said so.

## How it opens — _decided, not yet exercised_

Separately from freshness, each projection declares how it opens. That depends on what the projection is for, not on a rule for all of them:

| Opens as | Fits | Requirement |
|---|---|---|
| **static** | Snapshots and one-off renders: a walkthrough of a code change, a technical explainer, a year-in-review | **Self-contained:** data, styles and scripts inside the one file, so it opens with a double-click and no server |
| **served** | Live views and anything interactive: work tracking, a checklist, a "mark done" button | Opened through a local server that the sphere starts |

Live projections are served. Snapshots are static. A manually synced projection can be either: static with its data baked in at sync time, or served if it's interactive.

### Serving

Serving is its own frame (`projection_serving`, under the projections lens), so every projection doesn't reinvent it. The sphere:

- **starts a local server when a served projection is opened,** reuses it if one is already running, and stops it when it's no longer needed;
- **listens on this machine only,** never on the network, so a private projection stays private;
- **lets a served projection write only to its declared source files.** This is how input reaches the source (see [Views that accept input](#views-that-accept-input--decided-not-yet-exercised)): the server is the path back, and nothing else is writable through it.

At core profile, the human never sees any of this. They open "my things" and it works.

## Stack — _decided, not yet exercised_

A sphere defines a default stack for projections, so templates and shared styling can rely on one base, and nobody needs to install anything to see their own sphere. It escalates in steps when the default isn't enough:

| Tier | Stack | When | Lives |
|---|---|---|---|
| **1. Default** | Plain HTML, CSS and JavaScript. **No build step.** Type hints, if wanted, go in comments that editors read without compiling. | Almost every projection | `surface/projections/` |
| **2. With a library** | Tier 1, plus a library saved into `surface/projections/assets/` (for example, a charting library). Still no build step. | When the default can't render a chart or an interaction well | `surface/projections/` |
| **3. An app that reads the sphere** | Any web or mobile stack. **TypeScript** is the default language at this tier. | When it needs a database, logins, background jobs, a build step, or a phone app | **Outside the sphere**, as its own project |

**Why plain web is the default:** static files open with a double-click, and served ones need only the local server from the [serving](#serving) frame. Models generate it reliably. It's readable and diffable like the rest of the sphere. And it will still open in ten years.

**Libraries are saved locally, not loaded from the internet.** A projection that fetches code from a third-party server when it opens has stopped being private and stopped working offline.

**Once it needs an app, it's no longer a projection.** At tier 3 the thing is an application that *reads* the sphere. The sphere doesn't host it. Its registry entry says `kind: external`, names the app's home, and declares how the app stays in sync with the sphere's files. That last part is not optional. An outside app with no declared sync is exactly how a view ends up silently stale.

```yaml
- name: portfolio
  kind: external
  home: ~/projects/portfolio-app    # outside the sphere
  sources: [layers/world/subjects/finance/]
  sync: on-ground                    # on-ground | on-open | manual (shown as stale after 1 day)
  sharing: private
```

## Provenance — **proven**

Each artifact carries a pointer to its sources and the time it was rendered, inside the artifact, not just in the registry. A projection that has been copied, shared or screenshotted can still say where it came from and how old it is.

---

## Views that accept input — _decided, not yet exercised_

Some projections invite interaction: a checklist, a form, a "mark done" button. Input on a projection **goes back to the source files**, through the sphere, and the projection re-renders from them. A view that stores its own state has quietly become a second source of truth, and the two will drift.

If a view genuinely needs to hold its own data, it isn't a projection any more. Declare it as a source, with a layer contract like any other, so the sphere knows it's truth. See [registries](registries.md).

---

## Templates — **proven**

- **Shared chrome:** projections share a stylesheet and a small set of components (top bar, cards, tables, freshness badge), so every view looks like part of the same sphere.
- **Themes vary; structure doesn't.** A build or sphere can re-theme everything (colors, type, density) through design tokens, without touching a single projection's structure.
- **Extract a template on the third repetition, never before.** The first two projections of a kind are written directly. When a third is needed, the shared shape is clear enough to extract. Extracting earlier guesses at a pattern that doesn't exist yet.

## Ephemeral renders

Not every render is worth keeping. A walkthrough generated to explain one change, or a one-time comparison, is **ephemeral until kept**. It's rendered static into a scratch area of the surface, opened, and not registered. If the human wants to keep it, it gets a registry entry and a home like any other projection. Otherwise the registry would fill up with one-time explainers.

## Legacy views

Views built before a sphere adopted this structure, by hand and unregistered, are **registered as legacy** rather than rewritten or ignored. Each gets a registry entry with `legacy: true` and an honest freshness declaration. They don't have to be rebuilt to be known.

---

## Surface: where artifacts live — **proven**

`surface/` holds everything a sphere renders or exchanges, organized by kind:

```
surface/
├── projections/
│   ├── assets/          shared stylesheet, components, theme tokens
│   ├── _scratch/        ephemeral renders, not registered, safe to clear
│   └── <name>/          one folder per projection
├── state/               live machine state (heartbeats, indexes); disposable, never committed
├── raw/                 incoming files the human dropped in, not yet processed
├── inbox/               things arriving from outside: other spheres, exports
└── outbox/              things staged to leave the sphere
```

**Everything is private by default.** Each projection declares its sharing: `private` (only the human), `shared` (named people), or `public`. Making something shared or public is an outbound act: it passes the outbound guard, and the human approves it. Facts about other people never appear in a shared or public projection unless the human explicitly includes them. See [knowledge](knowledge.md#facts-about-other-people).

---

## Matter, not machinery

Projections show the human's **matter**: their work, their world, their growth. They don't show the sphere's **machinery**: lenses, frames, registries, sessions, git.

- At **core profile** this is absolute. A non-technical human's projections are a home page, "my things," and a witness view of how they're growing. Nothing else.
- At **standard and full profile**, machinery views are allowed as an option for people building their sphere: a map of layers, a view of the protocol. They're never the default front door.

**Witness views deserve care.** Seeing your own progress, wins and growth over time is one of the warmest things a sphere offers, and especially for people who'd never read a file. It's worth building well, in every build.

---

## A record like any other

Each projection has a registry entry:

```yaml
- name: work-dashboard
  kind: live                    # live | manually-synced | snapshot | external
  opens: served                 # static | served
  freshness: on-open            # on-open | sync within 1 day | frozen
  sources: [layers/work/index.md, layers/work/*/work.md]
  home: surface/projections/work-dashboard/
  sharing: private              # private | shared | public
  template: dashboard
  legacy: false
```

---

## Open questions

1. **How a non-technical human starts a served projection** without a terminal: a command to the sphere ("show my things"), a launcher file they double-click, or both?
2. **Projections on a phone.** Should builds ship a way to see projections away from the computer, and if so, what keeps that private?
3. **Clearing scratch.** When are ephemeral renders cleared: after a time, at ground, or only when the human asks?
4. **Formats.** HTML is the default for rich views. Should a plain markdown projection be a first-class kind for spheres that only ever live inside a harness?
