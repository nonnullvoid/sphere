---
projection: work-dashboard
title: Work
namespace: work
kind: refreshed
opens: static
lifespan: long-lived
freshness: stale after 1 day
sources: [layers/work/index.md, layers/work]
writes: []
home: surface/projections/work/work-dashboard/
sharing: private
template: dashboard
legacy: false
---

# Work

**What it's for:** everything the human is changing, by state, with what needs them first.

## Panels

| Panel | Kind | From |
|---|---|---|
| **At a glance** | stats | counts of active, paused and planned work, and work done in the last seven days |
| **Paused** | list | paused nodes, each with what it's waiting on. Empty: *"Nothing stuck."* |
| **Active** | list | active nodes with their summary, grouped under their top-level area where there is one |
| **Planned** | list | planned nodes, at most five |

## Leave out

Archived work, file paths, focus numbers, and plans' internals (link to a plan by its title only).

## Engine

Rendered at ground when the work index changed: rewrite `data.js` beside the page (see the [dashboard template](templates/dashboard/template.md)), then stamp `rendered` in `surface/projections/assets/registry.js`.

## History

- Shipped with the `base` build.
