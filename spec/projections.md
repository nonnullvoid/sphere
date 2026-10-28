# Projections

_Status: draft 4, for review._ How a sphere shows its state to people: rendered views of its files, such as dashboards, maps and pages, that are always honest about what they show and how fresh it is.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

---

## The idea

A sphere's files are its truth, but files aren't how most people want to see their life or their work. A **projection** is a view rendered from those files: a dashboard of work in motion, a map of growth over time, a home page that links everything.

One rule underneath all of it: **a projection is never the source of truth.** It's a picture of the files. If the picture and the files disagree, the files win, and the picture is fixed by re-rendering it, never by editing it. — **proven**

**Sessions are the interaction boundary; projections are the communication boundary.** A session is the live conversation: the human attaches, works, and leaves. A projection is the standing display: it stays, and the human comes back to it. They come back for two reasons:
- **to audit and follow:** what's in motion, what the sphere is doing and why;
- **to learn:** reports, guides and references the sphere prepared for them to read.

Some projections are interactive, letting the human act on the sphere without typing to it.

For a non-technical human, projections are the whole interface. They see their things, never the sphere's machinery. See [Matter, not machinery](#matter-not-machinery).

---

## Three kinds of data — _decided, not yet exercised_

Every projection touches three kinds of data, and each has exactly one home:

| Kind | What it is | Lives | Committed? |
|---|---|---|---|
| **Source truth** | The facts the view shows: work nodes, knowledge, sessions, witness entries, lenses | In the layer that owns it | Yes, like any truth |
| **The definition** | What this projection *is*: which sources it reads, what it shows, how it's laid out, what it leaves out | In the **projection node**, `layers/projections/<name>/` | Yes. It's authored, and it changes like any other authored file |
| **Derived view data** | Anything computed from truth for the view's convenience: a rollup, a sorted list, a chart series | Beside the artifact, `surface/projections/<name>/` | No. It's a cache, rebuildable from the other two at any time |

**Source truth isn't only knowledge.** Work, sessions, witness and lenses all own truth too. A projection reads each from its owner, never from a copy.

**The missing-fact rule.** If a view needs a value that no layer owns and that can't be derived from one, that's not view data. It's a **missing fact**. Give it an owner (an existing layer, or a new one with a contract) before the view shows it. A view that quietly invents its own facts has become a second source of truth. See [views that accept input](#views-that-accept-input--decided-not-yet-exercised).

**Data colocation.** Following from the table: a projection's data lives with whichever layer owns the truth. Only derived data sits beside the rendered artifact. Never a third, disconnected place. _The lesson behind this rule:_ before one sphere reorganized, its view data had ended up scattered across three places, and nobody could say which copy was current.

### The projection node

A projection is a node, like a work node or a knowledge topic:

```
layers/projections/
├── <name>/
│   ├── projection.md      the definition: sources, what it shows, layout, what to leave out
│   └── template/          a custom template, if it doesn't use a shared one (optional)
└── registry.md            one entry per projection
```

It sits apart from the pieces it relies on, so each can change without breaking the others:

| Part | What it holds | Where |
|---|---|---|
| **Frame** | The mechanics: when a projection is rendered, refreshed, published | `core/protocol/frames/projections/` |
| **Definition** | What this projection shows and how | `layers/projections/<name>/projection.md` |
| **Registry entry** | Its kind, freshness, sources, home, who can see it, template | `layers/projections/registry.md` |
| **Artifact** | The rendered thing itself, and its derived data | `surface/projections/<name>/` |

A new look is a template change. A new data source is a definition change. A new audience is a registry change.

### Which truth a view shows

Projections live outside the session boundary: a human opens their dashboard without caring which session is running. So:

- **The artifact renders from grounded truth on the main line,** never from an in-flight session. What it shows is what's been saved.
- **A session can preview its unsaved changes** by rendering into scratch (`surface/projections/_scratch/`), clearly marked as a preview. The real artifact doesn't change until the session grounds.
- **A change to the definition rides the session** like any other authored file. It's previewed in scratch, and it reaches the real artifact when it's grounded.

At [level 1](state.md), with one shared line, these are the same thing in practice. They only come apart when sessions branch.

---

## Freshness — **proven**

Every projection declares which of three kinds it is:

| Kind | How it stays current | Example |
|---|---|---|
| **live** | Reads its source files when someone opens it. Nothing to sync. | A work dashboard that reads the work index each time it loads |
| **synced** | A render step updates it, at ground or on `sync <name>` | A portfolio view built from exported account data |
| **snapshot** | Generated once, at a moment, and never updated | A year-in-review page, a walkthrough |

**Staleness must be visible on the projection itself.** Every artifact shows when it was last rendered and from what. A synced view that's past its freshness window says so plainly, on the page, where the reader is looking. A stale view that looks current is the worst failure a projection can have, because people make decisions from it. — _decided, not yet exercised_

_The lesson behind this rule:_ a dashboard showing stale financial numbers, silently, because the sync step hadn't run. Nothing on the page said so.

**Live means live-fetch.** — **proven** A live view reads its source files in the page when it's opened (and again when it regains focus), with no build step and no copy of the data inside it. _The lesson:_ a dashboard that had its data baked into the page silently stopped showing new entries, because the copy and the source had drifted. When it was switched to reading the source on open, the drift class disappeared.

**A live view puts a shape contract on its sources.** If a page parses work nodes directly, those files need a predictable shape. That shape is written in the source layer's contract, not discovered by the page. This is how one sphere's work dashboard pinned down the format of its node files.

**Conflating kinds is a bug both ways.** A "live" view that went stale lies to the reader. A snapshot that gets re-synced loses the moment it existed to preserve. So `sync` refuses a snapshot: a new moment means a new snapshot.

**Don't over-sync.** Not everything deserves to be live. A snapshot that captures a moment well often beats a dashboard nobody keeps current. Reach for live only when freshness is the actual promise.

### The render is deterministic — _decided, partly proven_

**Live and synced renders involve no AI judgment:** the same sources produce the same output, every time. The intelligence was spent once, choosing what to show and designing how. That's what makes a live view trustworthy: nothing in it was guessed this time.

**Synthesis belongs to snapshots, and only when they're generated.** A walkthrough or a report is composed by reading across the sphere, and that takes judgment. It's done once, stamped with provenance, and frozen. See [the one-shot template](#the-one-shot-template-snapshots).

**Derived mirrors are written by the same step as their source.** If a view needs a machine-readable copy of a markdown source (a JSON feed, say), the action that writes the source writes the copy, or tooling generates it. A mirror maintained separately is a second truth waiting to drift.

### Lifespan

Separately from freshness, a projection is **long-lived** (a home page, a work view) or **time-bound** (a launch tracker that has no purpose after the launch). When a time-bound projection's purpose ends, it retires to `_legacy/`.

## How it opens — _decided, not yet exercised_

Separately from freshness, each projection declares how it opens. That depends on what the projection is for, not on a rule for all of them:

| Opens as | Fits | Requirement |
|---|---|---|
| **static** | Snapshots and one-off renders: a walkthrough of a code change, a technical explainer, a year-in-review | **Self-contained:** data, styles and scripts inside the one file, so it opens with a double-click and no server |
| **served** | Live views and anything interactive: work tracking, a checklist, a "mark done" button | Opened through a local server that the sphere starts |

Live projections are served. Snapshots are static. A synced projection can be either: static with its data rendered in, or served if it's interactive.

### Serving

Serving is its own frame (`projection_serving`, under the projections lens), so every projection doesn't reinvent it. The sphere:

- **starts a local server when a served projection is opened,** reuses it if one is already running, and stops it when it's no longer needed;
- **listens on this machine only,** never on the network, so a private projection stays private;
- **lets a served projection write only to its declared source files.** This is how input reaches the source (see [Views that accept input](#views-that-accept-input--decided-not-yet-exercised)): the server is the path back, and nothing else is writable through it.

A non-technical human never sees any of this. They open "my things" and it works.

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
  sources: [layers/knowledge/money/]
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

A template is a projection shape captured once, so the next one like it is a fill-in rather than a fresh build. Templates are authored sources: they live in `layers/projections/templates/`, and only shared assets they link (stylesheets, scripts) are served from `surface/projections/assets/`.

**Two operations:**
- **Extract:** *"save this as a template"* generalizes a good projection, keeping the structure, look and engine, and leaving placeholders where instances differ.
- **Instantiate:** *"new [thing] from [template]"* fills the placeholders. The new projection gets its own node and registry entry like any other.

**Rules:**
- **Extract on the third repetition, never before.** The first two projections of a kind are written directly. Extracting earlier guesses at a pattern that doesn't exist yet. Bespoke projections stay bespoke.
- **Chrome is shared; content isn't.** Projections share a stylesheet and a small set of components (header, panels, footer, freshness badge, navigation), so every view looks like part of the same sphere. The design effort goes into each view's content.
- **Themes vary; structure doesn't.** A build or sphere can re-theme everything (colors, type, density) through design tokens, without touching a single projection's structure.
- **Navigation comes from the registry, never hand-written into pages.** _The lesson:_ when each dashboard carried its own list of links, a new dashboard went a whole session unlinked from the others, and one page's list quietly drifted. One shared list, built from the registry, means adding a view is one change.

### The one-shot template (snapshots)

A snapshot isn't a mechanism of its own. It's the canonical **one-shot template**:

1. read across the sphere: the layers, sources and context that matter
2. synthesize the artifact (AI judgment belongs here)
3. stamp provenance: sources and generated-at
4. write it once
5. freeze it

Its implementations share that shape and differ in what they read and how they compose it: a **walkthrough** of how something works, a **guide**, a **report** of research or findings, **documentation on request**. Builds can ship each as a template with its own craft notes (for example: bottom line first, cite every source, self-contained with no external images).

## Ephemeral renders

Not every render is worth keeping. A walkthrough generated to explain one change, or a one-time comparison, is **ephemeral until kept**. It's rendered static into a scratch area of the surface, opened, and not registered. If the human wants to keep it, it gets a registry entry and a home like any other projection. Otherwise the registry would fill up with one-time explainers.

## Legacy views

Views built before a sphere adopted this structure, by hand and unregistered, are **registered as legacy** rather than rewritten or ignored. Each gets a registry entry with `legacy: true` and an honest freshness declaration. They don't have to be rebuilt to be known.

**Retired views** go to a `_legacy/` folder inside their surface namespace (`surface/projections/<namespace>/_legacy/`). They're kept as reference, not rendered, and not linked from anywhere a human would land.

**`legacy: true` marks refactor debt, not health.** A legacy view may work fine. The flag says it was hand-built outside the templates, and a future pass could rebuild it on one.

---

## Surface: where artifacts live — **proven**

`surface/` holds everything a sphere renders or exchanges, organized by kind. It's flatspace: one always-latest copy that every session sees (see [registries](registries.md#the-surface-registry--decided-not-yet-exercised)).

```
surface/
├── projections/
│   ├── assets/          shared stylesheet, components, navigation, theme tokens
│   ├── _scratch/        ephemeral renders and session previews, not registered, safe to clear
│   └── <namespace>/     one level by content type, chosen by the build (e.g. me/, work/)
│       ├── <name>/      one projection: the artifact and its derived data
│       └── _legacy/     retired views in this namespace, kept as reference
├── state/               live machine state (heartbeats, indexes); disposable, never committed
├── raw/                 incoming files the human dropped in, not yet processed
├── inbox/               things arriving from outside: other spheres, exports
└── outbox/              things staged to leave the sphere
```

**Projections are grouped in meaningful namespaces, not a flat dump.** One level, by content type, is enough for most spheres. — **proven**

**Everything is private by default.** Each projection declares its sharing level, using the same three levels as [lenses](protocol.md#sharing--decided-not-yet-exercised): `private` (only the human), `protected` (named people), or `public`. Opening a projection up is an outbound act: it passes the outbound guard, and the human approves it. Facts about other people never appear in a protected or public projection unless the human explicitly includes them. See [knowledge](knowledge.md#facts-about-other-people).

---

## Matter, not machinery

Projections show the human's **matter**: their work, their world, their growth. They don't show the sphere's **machinery**: lenses, frames, registries, sessions, git.

- **For a non-technical human** this is absolute. Their projections are a home page, "my things," and a witness view of how they're growing. Nothing else.
- **For people building their own sphere,** machinery views are allowed as an option: a map of layers, a view of the protocol. They're never the default front door.

**Witness views deserve care.** Seeing your own progress, wins and growth over time is one of the warmest things a sphere offers, and especially for people who'd never read a file. It's worth building well, in every build.

---

## A record like any other

Each projection has a registry entry:

```yaml
- name: work-dashboard
  namespace: work
  kind: live                    # live | synced | snapshot | external
  opens: served                 # static | served
  lifespan: long-lived          # long-lived | time-bound
  freshness: on-open            # on-open | stale after 1 day | frozen
  sources: [layers/work/index.md, layers/work/*/work.md]
  definition: layers/projections/work-dashboard/
  home: surface/projections/work/work-dashboard/
  sharing: private              # private | protected | public
  template: dashboard
  legacy: false                 # refactor debt, not health
```

The registry is a generated view over the projection nodes. The **definition** (`projection.md`) holds what the registry only points at: the sources and how they're composed, the layout and visual language, what to leave out, and the **engine** (a live-fetch page, a render script, or a one-shot synthesis).

---

## Drift checks — _decided, not yet exercised_

Each comes from a real failure:

- **Orphans:** an artifact under `surface/projections/` with no registry entry is surfaced, then registered or removed. No untraceable pages.
- **Broken links after a move:** when a projection or its assets move, the check verifies its stylesheet and scripts still resolve. _The lesson:_ a folder reorganization left two dashboards rendering unstyled, and nobody noticed for days.
- **Navigation:** the shared navigation lists exactly the registered, non-retired projections.
- **Shape contracts:** a live view's sources still match the shape their layer contract promises.

## Senses and commands — _decided, not yet exercised_

**Senses:**
- `projection-registered`, `projection-instantiated`, `projection-retired`, `projection-orphaned`
- `template-extracted`
- `sync-requested`, `projection-stale`

**Commands** (natural phrasing works too):
- `show my things`, `list projections`
- `sync [projection]`, `sync all` (skips snapshots and live views, which have nothing to sync)
- `save this as a template`, `new [thing] from [template]`
- `retire [projection]`

---

## Open questions

1. **How a non-technical human starts a served projection** without a terminal: a command to the sphere ("show my things"), a launcher file they double-click, or both?
2. **Projections on a phone.** Should builds ship a way to see projections away from the computer, and if so, what keeps that private?
3. **Clearing scratch.** When are ephemeral renders cleared: after a time, at ground, or only when the human asks?
4. **Formats.** HTML is the default for rich views. Should a plain markdown projection be a first-class kind for spheres that only ever live inside a harness?
