---
projection: today
title: Today
subtitle: What's waiting, what you're in the middle of, and what's next.
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

| Panel | Kind | From | Rule |
|---|---|---|---|
| **Waiting on you** | list | open foci whose latest entry says *waiting on you*, with what's next | `list foci where waiting=yes show intention, next empty "Nothing waiting."` |
| **In the middle of** | list | open foci other than main: what each is for, and what's next | `list foci show intention, next empty "Nothing open yet."` |
| **Next up** | list | active work, each with its summary; at most five, most recently updated first | `list work where state=active order updated desc limit 5 show title, summary empty "No work yet. Tell me what you're working on."` |
| **Ideas** | stats | open ideas, and how many are `ready` | `count idea as Open; count idea where stage=ready as Ready empty "No ideas caught yet."` |

Each **Rule** is what `scripts/sphere render` follows. Change a rule (or add a row with one) to change the view: `list <source> [where …] [order <key> [desc]] [limit N] show <key>, <key> [empty "…"]`, or `count <source> [where …] as <label>; …`. A source is `foci` or a tree's name (`work`, `idea`; `work+archived` takes in the archive). Conditions: `key=a|b`, `key!=a`, `updated>=7d`, joined with `and`. A row with no rule leaves the whole view to the AI.

## Leave out

Focus numbers, file paths, closed foci, archived work, and anything about the sphere's own workings.

## Engine

`scripts/sphere render` rewrites `data.js` beside the page from the rules above and stamps `rendered` in `surface/projections/assets/registry.js`. `sphere ground` and `sphere close` run it whenever they change work or a focus, so the view is never behind.

## History

- Shipped with the `base` build.
