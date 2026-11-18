---
frame: projection-registry
lens: [projections]
derives_from: [projections@1]
version: 1
version_note: First draft. The projection node, the generated registry, namespaces, retiring, orphans and legacy views.
status: drafting
updated: 2026-11-13
sharing: public
reads: [layers/projections, surface/projections]
writes: [layers/projections, surface/projections]
protocol: [I-see-my-things, A-show-my-things, A-list-projections, A-register-projection, A-retire-projection, node-archived, projection-orphaned, focus-grounding]
---

# What projections exist

**Applies to:** making a new projection, *"show my things"*, *"list projections"*, retiring a view, and a page turning up that nobody registered.

## A projection is a node

Each projection is a node in `layers/projections/`: one file, or a folder when it needs more than one. The rendered page lives on the surface, apart from its definition:

```
layers/projections/
├── work-dashboard.md        the definition: current shape on top, history below
├── year-in-review-2026/     a projection that needs more than one file
│   ├── year-in-review-2026.md   the main file: frontmatter and recipe, as always
│   └── chapters.md          whatever else it needs to define itself
├── templates/               shared templates (projection-templates); not nodes
├── archived/
│   └── launch-tracker.md    a retired projection's definition
└── registry.md              generated from the definitions; never edited

surface/
├── projections.html         the index: every live view, built from the registry
└── projections/
    ├── assets/              shared stylesheet, components, theme, navigation
    ├── _scratch/            one-time renders and focus previews; never registered
    └── work/                a namespace
        ├── work-dashboard/  the artifact and its derived data
        └── _legacy/
            └── launch-tracker/  a retired artifact, kept as reference
```

- **The name is the file's name,** short and hyphenated, and it never changes.
- **Namespaces are one level, by what the view is about** (`me/`, `work/`, `home/`), chosen by the build. Not a flat pile, and never deeper than one.
- **One file is usually enough.** A definition is small and its history stays short, so both live in the one file, like an [idea](../idea-capture/idea-nodes.md#one-file-per-idea). A view with a template of its own keeps it in `templates/` like any other.
- **A projection that needs more than one file gets a folder** named for it, with a **main file of the same name**: `layers/projections/year-in-review-2026/year-in-review-2026.md`. The main file holds the frontmatter and the recipe, exactly as a single-file projection does; the other files are whatever the definition needs (a list of chapters, a mapping of sources, a bespoke query). Everything that reads definitions reads the main file only. Start with one file, and move to a folder when the definition outgrows it.

## The definition

Frontmatter is enough to show the projection in one line, and it's everything the registry needs:

```yaml
---
projection: work-dashboard
title: What's in motion
namespace: work
kind: live                    # live | refreshed | snapshot | external
opens: served                 # static | served | markdown
lifespan: long-lived          # long-lived | time-bound
freshness: on-open            # on-open | stale after <time> | frozen
sources: [layers/work/index.md, layers/work/*/work.md]
writes: []                    # the only files input may change (projection-serving)
home: surface/projections/work/work-dashboard/
sharing: private              # private | protected | public
template: dashboard
legacy: false
---
```

| Key | Holds |
|---|---|
| `kind`, `freshness` | Its place on the freshness scale. See [projection-freshness](projection-freshness.md) |
| `opens` | Whether it opens as a file or through the local server. See [projection-serving](projection-serving.md) |
| `lifespan` | `time-bound` when its purpose ends (a tracker for one launch); `long-lived` otherwise |
| `sources` | Every file it reads, from the part of the sphere that owns it. Never a copy |
| `writes` | The sources input from the view may change. Empty for almost every view |
| `home` | Where the artifact lives. An `external` projection names the app's own home, outside the sphere |
| `sharing` | Who may see it. Same levels as lenses |
| `until` | Optional, right after `sharing`, only when it's `protected` or `public`: the date it goes back to private (a page shared with family for the holidays) |
| `template` | The template it was built from, or empty if it's bespoke |
| `legacy` | `true` for a view built by hand outside the templates |

A retired projection adds `retired:`, the date and why on one line (`retired: 2026-11-16 replaced by money-dashboard`), and only then.

**The body is the recipe:** what it shows and how its sources are composed, its layout and look, what it leaves out, and its engine (a page that reads its sources when opened, a render script, or a one-time synthesis). Below that, a `## History` section: dated entries, newest first, saying what changed and why.

## The registry is generated

`layers/projections/registry.md` is **built from the definitions' frontmatter alone,** one line per projection, grouped by namespace, and rebuilt at ground. It says it's generated. If it disagrees with the definitions, the definitions win.

- **Navigation is built from the registry,** never written into pages. One list for every view means adding a view is one change. See [projection-templates](projection-templates.md#one-look).
- **Which views a seed carries is read from `sharing`,** not from a list kept by hand. See [export-contract](../replication/export-contract.md).

## The index page

**Every sphere with projections has an index page, `surface/projections.html`.** It's the front door to the surface: every projection the human may see that isn't retired, grouped by namespace, one line each with its title and how fresh it is.

- **It's built from the registry,** at the same time as navigation, and rebuilt at ground when a definition changed. Never edited by hand.
- **It comes with the build.** A sphere doesn't have to make it; the first projection it registers already has somewhere to be found.
- **It's the registry's own view,** not a projection with a definition of its own, so it's never registered and never an orphan.
- **It shows matter, not machinery.** Time-bound views appear while they're live; retired ones and `_scratch/` never do.
- **It shows markdown too.** A projection with `opens: markdown` opens in the default markdown viewer that ships beside the index page.

## Show my things

**"Show my things" opens the index page.** For a non-technical human, that's the whole answer, and it never includes a view of machinery.

**"List projections"** answers from the registry: name, kind, how fresh, where it lives. One line each.

## Making one

Making a projection the human asked for is ordinary work, not a proposal. In one step:

1. Write its definition, with a first history entry.
2. **Propose a sharing level** as a best guess and confirm it. If nobody answers, it's `private`.
3. Render it into its home (see [projection-freshness](projection-freshness.md)).
4. The registry, navigation and index page rebuild at ground.

**A new kind of projection that needs a new tree or a new key** is an evolution step: its shape goes into `core/shapes` with it (see [crystallization](../evolution/crystallization.md#make-the-change)).

## Retiring

**A time-bound projection retires when its purpose ends.** The sphere can suggest it; the human decides. The same goes for a view the human says they no longer look at.

- **Definition:** add `retired:` and a last history entry, then move the file (or its folder) to `layers/projections/archived/`.
- **Artifact:** move it to `_legacy/` in its namespace. It's kept as reference, not rendered, and not linked from anywhere a human lands.
- **Navigation and the index page drop it** at the next rebuild. Fire `node-archived`.

This is [finishing a node](../nodes/node-shape.md#finishing-a-node) for projections.

## Orphans and legacy views

- **An artifact under `surface/projections/` with no definition is an orphan.** Fire `projection-orphaned`, and offer to register it or remove it. Removing it asks first, like anything hard to undo. No untraceable pages.
- **A view built by hand before the templates is registered as legacy,** not rewritten or ignored: `legacy: true`, with an honest `kind` and `freshness`. *Why:* it doesn't have to be rebuilt to be known. `legacy` marks refactor debt, not health; a legacy view can work perfectly well.
- **One-time renders aren't orphans.** Anything in `_scratch/` is never registered, and it's cleared only when the human asks. If the human wants to keep one, it gets a definition and a home.

## When / do

| When | Do |
|---|---|
| *"Show my things"* | Open `surface/projections.html`: the human's live projections, never machinery |
| *"List projections"* | One line each from the registry: name, kind, freshness, home |
| The human asks for a new view | Write the definition, confirm a sharing level, render it. |
| A view is opened up to more people | Outbound: the human approves it, through the outbound guard |
| `focus-grounding`, if it touched a definition | Rebuild the registry, navigation and index page from the definitions |
| A time-bound view's purpose has ended | Suggest retiring it; on yes, archive the definition, move the artifact to `_legacy/`. Fire `node-archived` |
| A page has no definition | Fire `projection-orphaned`; offer to register it (as legacy if hand-built) or remove it |
| The human wants to keep a one-time render | Give it a definition and a home; it leaves `_scratch/` |

## Works with

- [projection-freshness](projection-freshness.md): what `kind` and `freshness` promise, and how the artifact is rendered.
- [projection-serving](projection-serving.md): what `opens` and `writes` mean.
- [projection-templates](projection-templates.md): `template`, and the navigation built from this registry.
- [node-shape](../nodes/node-shape.md): a projection is a node; retiring is finishing it.
- [kinds-of-file](../nodes/kinds-of-file.md): the definition is current state and history; the registry is generated.
- [outbound-guard](../human-is-highest/outbound-guard.md): opening a view to more people is outbound.
- [structure-check](../readable-substrate/structure-check.md): finds orphans, and definitions out of shape.

## Senses

| Sense | Fires when |
|---|---|
| `node-archived` | for a projection: its definition is archived and its artifact moved to `_legacy/` |
| `projection-orphaned` | an artifact is found with no definition |
