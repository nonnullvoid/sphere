---
projection: work-dashboard
title: Work
subtitle: Everything you're changing, by state.
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

| Panel | Kind | From | Rule |
|---|---|---|---|
| **At a glance** | stats | counts of active, paused and planned work, and work done in the last seven days | `count work where state=active as Active; count work where state=paused as Paused; count work where state=planned as Planned; count work+archived where state=done and updated>=7d as Done this week empty "No work yet."` |
| **Paused** | list | paused work, each with why and what it's waiting on | `list work where state=paused show title, paused, waiting_on empty "Nothing stuck."` |
| **Active** | list | active work with its summary, most recently updated first | `list work where state=active order updated desc show title, summary empty "Nothing active yet."` |
| **Planned** | list | planned work, at most five | `list work where state=planned limit 5 show title, summary empty "Nothing planned yet."` |

Each **Rule** is what `scripts/sphere render` follows; [today](today.md) says how to write one. A row with no rule leaves the whole view to the AI.

## Leave out

Archived work, file paths, focus numbers, and plans' internals (link to a plan by its title only).

## Engine

`scripts/sphere render` rewrites `data.js` from the rules above and stamps `rendered` in `surface/projections/assets/registry.js`, at every ground or close that changes work.

## History

- Shipped with the `base` build.
