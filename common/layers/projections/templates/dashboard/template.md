# Template: dashboard

**For:** a view that gathers the state of one area at a glance: work on the plate, where a project stands, what's waiting. Panels of numbers, lists and short text, refreshed from the sphere's files.

## Files

| File | Becomes | Holds |
|---|---|---|
| `index.html` | `surface/projections/<namespace>/<name>/index.html` | The page. Chrome, header, panels, footer. Changes only when the template does |
| `data.js` | `surface/projections/<namespace>/<name>/data.js` | The derived view data: what the panels show, rendered from the sources. A cache, rebuilt at every render |

The page reads `data.js` with a `<script>` tag, so it opens with a double-click and works offline. A render rewrites `data.js` only; the page stays as it is.

## Placeholders

| Placeholder | In | Filled with |
|---|---|---|
| `{{title}}` | `index.html` | The view's title, as in its definition |

Everything else comes from `data.js`:

```js
window.VIEW_DATA = {
  title: "…",                 // shown in the header
  subtitle: "…",              // one line under it; optional
  generated: "2026-11-17T09:30:00Z",   // when this render ran
  sources: ["layers/work/index.md"],   // what it was rendered from
  panels: [
    { title: "At a glance", kind: "stats", items: [{ label: "Active", value: 4 }] },
    { title: "Next up", kind: "list", items: [{ text: "…", meta: "…", href: "…" }] },
    { title: "Notes", kind: "markdown", text: "…", wide: true },
  ],
};
```

Panel kinds: `stats` (numbers with labels), `list` (lines with an optional right-hand note and link), `text`, `markdown`. `wide: true` spans the row. `empty` sets what an empty panel says.

## Craft notes

- **Lead with what needs the human.** The first panel answers "what should I look at?", not "how much is there?"
- **One line per item.** Detail lives in the node; the dashboard links to it.
- **Empty is a state, not an error.** Every panel says something kind when it has nothing: *"Nothing waiting."*
- **Matter, never machinery.** No focus numbers, file paths or frame names in what the human sees, unless the build is for people building spheres.
- **Derived data only.** `data.js` is computed from the sources at render time; nothing in it is typed in by hand.
