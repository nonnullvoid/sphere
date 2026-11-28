---
projection: work-dashboard
title: My things
subtitle: Everything you're looking after, and where each one stands.
namespace: me
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

# My things

**What it's for:** everything the human has asked the sphere to help with, in one place, so nothing is forgotten: the parts of life they look after, what's on the go, what's on hold, and what's coming up.

## Panels

| Panel | Kind | From | Rule |
|---|---|---|---|
| **Looking after** | list | the parts of life they keep an eye on (work of kind *area*) | `list work where kind=area order title show title, summary empty "Nothing here yet. Say which parts of life you'd like help keeping an eye on."` |
| **On the go** | list | active things, most recently updated first | `list work where state=active and kind!=area order updated desc show title, summary empty "Nothing on the go."` |
| **On hold** | list | paused things, with what they're waiting on | `list work where state=paused show title, waiting_on empty "Nothing on hold."` |
| **Coming up** | list | planned things, at most five | `list work where state=planned limit 5 show title, summary empty "Nothing planned yet."` |
| **Done lately** | list | things finished in the last month | `list work+archived where state=done and updated>=30d show title empty "Nothing finished this month yet."` |

Each **Rule** is what `scripts/sphere render` follows; [Home](today.md) says how to write one. A row with no rule leaves the whole view to the AI.

## Leave out

Archived work, file paths, focus numbers, and plans' internals (link to a plan by its title only).

## Engine

`scripts/sphere render` rewrites `data.js` from the rules above and stamps `rendered` in `surface/projections/assets/registry.js`, at every ground or close that changes work.

## History

- Shipped with the `homesphere` build, over base's Work, as My things.
- Shipped with the `base` build.
