---
projection: today
title: Today
namespace: me
kind: refreshed
opens: static
lifespan: long-lived
freshness: stale after 1 day
sources: [layers/focus, layers/work/index.md, layers/ideas]
writes: []
home: surface/projections/me/today/
sharing: private
template: dashboard
legacy: false
---

# Today

**What it's for:** the first thing the human sees. What's waiting on them, what they're in the middle of, and what's next, at a glance.

## Panels

| Panel | Kind | From |
|---|---|---|
| **Waiting on you** | list | foci whose history ends with *waiting on you*, and offers with no answer; oldest first. Empty: *"Nothing waiting."* |
| **In the middle of** | list | open foci other than main: name, and the first line of their *Now* as the note |
| **Next up** | list | active work nodes, each with its summary; at most five, most recently updated first |
| **Ideas** | stats | open ideas, and how many are `ready` |

## Leave out

Focus numbers, file paths, closed foci, archived work, and anything about the sphere's own workings.

## Engine

Rendered at ground when any source changed: rewrite `data.js` beside the page (see the [dashboard template](templates/dashboard/template.md)), then stamp `rendered` in `surface/projections/assets/registry.js`.

## History

- Shipped with the `base` build.
