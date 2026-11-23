---
projection: life
title: Life
subtitle: The parts of life you keep an eye on, the habits you're building, and what's on the go.
namespace: me
kind: refreshed
opens: static
lifespan: long-lived
freshness: stale after 1 day
sources: [layers/work]
writes: []
home: surface/projections/me/life/
sharing: private
template: dashboard
legacy: false
---

# Life

**What it's for:** the whole of a life at a glance, not just the to-do list. The areas the human looks after, the habits they're building, and what's moving.

## Panels

| Panel | Kind | From | Rule |
|---|---|---|---|
| **Areas** | list | the life areas they've named (work items of kind *area*) | `list work where kind=area order title show title, summary empty "No areas yet. Say which parts of life you'd like to keep an eye on."` |
| **Habits** | list | ongoing work that's active, with how it's going (areas aside) | `list work where ongoing=true and kind!=area and state=active show title, progress, summary empty "No habits yet."` |
| **On the go** | list | active projects that aren't habits, most recently updated first | `list work where kind=project and ongoing!=true and state=active order updated desc limit 6 show title, summary empty "Nothing on the go."` |
| **Done this week** | list | anything finished in the last seven days | `list work+archived where state=done and updated>=7d show title empty "Nothing finished this week yet."` |

Each **Rule** is what `scripts/sphere render` follows; [today](today.md) says how to write one.

## Leave out

File paths, focus numbers, and anything about the sphere's own workings.

## Engine

`scripts/sphere render` rewrites `data.js` from the rules above and stamps `rendered` in `surface/projections/assets/registry.js`, at every ground or close that changes work.

## History

- Shipped with the `lifesphere` build.
