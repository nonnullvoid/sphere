---
frame: projection-templates
lens: [projections]
derives_from: [projections@1]
version: 1
version_note: First draft. Extract on the third repetition, instantiate, shared chrome and themes, navigation from the registry, the one-shot template, and what views are built with.
status: drafting
updated: 2026-11-13
sharing: public
reads: [layers/projections, surface/projections]
writes: [layers/projections, surface/projections/assets]
protocol: [I-reuse-what-works, A-save-as-template, A-new-from-template]
---

# Templates, and what views are built with

**Applies to:** *"save this as a template"*, *"new X from Y"*, the same kind of view being built again, the shared look of every view, and choosing what a new projection is built with.

## Two operations

```
extract:      a good projection   →  "save this as a template"     →  a template
instantiate:  a template + fills  →  "new <thing> from <template>"  →  a new projection
```

- **Extract** keeps what's reusable (the structure, the look, the engine) and leaves placeholders where instances differ: sources, title, scope, lifespan.
- **Instantiate** fills the placeholders. The new projection gets its own definition like any other, with `template:` naming where it came from, and its body says only what it fills in.

**Templates are authored sources,** kept in `layers/projections/templates/<template>/`: a short `template.md` saying what the template is for, its placeholders and its craft notes, beside the files it's made of. Only shared assets they link (stylesheets, scripts) are served from `surface/projections/assets/`.

## Extract on the third repetition, never before

**The first two views of a kind are written directly.** The third is the signal: when a pattern appears a third time without a template, suggest extracting one. *Why:* extracting earlier guesses at a pattern that doesn't exist yet, and a wrong template is worse than none.

**Bespoke views stay bespoke.** Not every projection should become a template, and a one-off isn't a failure.

## One look

- **Chrome is shared; content isn't.** Every view uses one stylesheet and a small set of components: a header, panels, a footer, a freshness badge, navigation. The design effort goes into each view's content. They live in `surface/projections/assets/`: `sphere-chrome.css` (the tokens and every component's look), `sphere-chrome.js` (the top bar, badge, panels and footer), `markdown.js` (the viewer) and `registry.js` (the registry's mirror, below). A static snapshot copies the stylesheet in, so it stays self-contained.
- **Themes vary; structure doesn't.** Colors, type and density come from design tokens, so a build or a sphere can re-theme every view without touching any view's structure.
- **Navigation comes from the [registry](projection-registry.md#the-registry-is-generated),** never written into pages. *Why:* when each page carries its own list of links, a new page stays unlinked from the others, and the lists quietly drift apart. One list built from the registry makes adding a view a single change.
- **Moving assets is checked.** When a projection or its assets move, the [structure check](../readable-substrate/structure-check.md) confirms its stylesheet and scripts still resolve. A view that renders unstyled is easy to miss for days.

## The one-shot template

**A snapshot isn't a mechanism of its own. It's the canonical one-shot template:**

1. **Read across the sphere:** the layers, sources and context that matter.
2. **Compose the artifact.** This is the one place AI judgment belongs in a projection.
3. **Stamp provenance:** what it was built from, and when.
4. **Write it once.**
5. **Freeze it.** It's never refreshed (see [projection-freshness](projection-freshness.md#snapshots-are-made-once)).

Its implementations share that shape and differ in what they read and how they compose it:

| Implementation | Is |
|---|---|
| **Walkthrough** | How something works, step by step: a system, a change, a decision |
| **Guide** | A how-to or a deep dive, prepared for the human to read |
| **Report** | Research or findings, surfaced for reading and feedback |
| **Documentation on request** | A point-in-time explanation, made when asked |

A build can ship each as a template with its own craft notes: *bottom line first*, *cite every source*, *self-contained, with no outside images*.

## What a view is built with

**A sphere has one default stack for projections,** so templates and shared chrome can rely on one base and nobody installs anything to see their own sphere. It escalates only when it has to:

| Step | Built with | When | Lives |
|---|---|---|---|
| **1. Default** | Plain HTML, CSS and JavaScript. **No build step.** Type hints, if wanted, go in comments editors read without compiling | Almost every view | `surface/projections/` |
| **2. With a library** | The default, plus a library saved into `surface/projections/assets/`. Still no build step | When the default can't draw a chart or an interaction well | `surface/projections/` |
| **3. An app** | Any stack the app needs | It needs a database, logins, background jobs, a build step or a phone | **Outside the sphere,** as its own project, registered as `kind: external` |

- **Libraries are saved locally, never loaded from the internet.** *Why:* a page that fetches code from someone else's server when it opens has stopped being private and stopped working offline.
- **Why plain web is the default:** a static file opens with a double-click, and a served one needs only the sphere's [local server](projection-serving.md). Models write it reliably. It's readable and diffable like the rest of the sphere. And it will still open in ten years.
- **An app isn't a projection.** It reads the sphere; the sphere doesn't host it. Its registry entry names its home and how it stays current.

## When / do

| When | Do |
|---|---|
| *"Save this as a template"* | Keep the structure, look and engine; mark the placeholders; write it to `templates/`. |
| *"New X from Y"* | Fill Y's placeholders; write X's definition with `template: Y`; render it. |
| The same kind of view is built a third time with no template | Suggest extracting one. The human decides |
| A snapshot is asked for (a walkthrough, a guide, a report) | Instantiate the one-shot template: read, compose, stamp, write once, freeze |
| A new view is being built | Start from the default stack and the shared chrome; reach for a library only when needed |
| A view needs a database, logins or a build step | Say it's an app, not a projection; build it outside the sphere and register it as `external` |
| The look should change everywhere | Change the theme tokens, never each view |

## Works with

- [projection-registry](projection-registry.md): an instantiated view gets its own definition; navigation is built from the registry.
- [projection-freshness](projection-freshness.md): a snapshot is frozen once the one-shot template has made it.
- [projection-serving](projection-serving.md): how a view built on the default stack opens.
- [readable-substrate](../../lenses/readable-substrate.md): plain web, kept local, readable and diffable.

