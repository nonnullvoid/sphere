# Template: one-shot

**For:** every snapshot: a walkthrough, a guide, a report, documentation on request. It's read once, composed with judgment, stamped and frozen. See [projection-templates](../../../../core/protocol/frames/projections/projection-templates.md#the-one-shot-template).

## The five steps

1. **Read across the sphere:** the layers, sources and context that matter.
2. **Compose** the body. This is the one place AI judgment belongs in a projection.
3. **Stamp provenance:** fill the sources and the time.
4. **Write it once,** to `surface/projections/<namespace>/<name>/index.html`, or to `surface/projections/_scratch/` if it isn't being kept.
5. **Freeze it.** It's never refreshed. A newer picture is a new snapshot.

## Files

| File | Becomes |
|---|---|
| `page.html` | The snapshot, **self-contained**: styles inline, no outside files, so it opens with a double-click anywhere and survives being moved or sent |

## Placeholders

| Placeholder | Filled with |
|---|---|
| `{{chrome}}` | The full text of `surface/projections/assets/sphere-chrome.css`, copied in at write time |
| `{{title}}` | The title |
| `{{subtitle}}` | One line: what this is and who it's for |
| `{{generated}}` | When it was made, as the human reads dates (`17 Nov 2026`) |
| `{{generated_iso}}` | The same moment as ISO time, for tooling |
| `{{body}}` | The composed HTML: headings, paragraphs, lists, tables, inside `.sphere-prose` |
| `{{sources}}` | One `<li>` per source it was built from |

## Implementations

| Kind | Craft notes |
|---|---|
| **Walkthrough** | How something works, in the order a person meets it. One idea per section. Show, then explain |
| **Guide** | A how-to or a deep dive. Start with what the reader will be able to do. Steps are numbered and each one is checkable |
| **Report** | Research or findings. **Bottom line first**, then the evidence. **Cite every source.** Say what's uncertain and how sure |
| **Documentation on request** | A point-in-time explanation. Say what moment it describes; it will go out of date and should say so |

**For all of them:**
- **Self-contained:** no outside images, fonts or scripts.
- **Matter, never machinery,** unless the reader asked about the machinery.
- **Plain words** at the reader's level (see [adapt-to-level](../../../../core/protocol/frames/literacy-tracking/adapt-to-level.md)).
