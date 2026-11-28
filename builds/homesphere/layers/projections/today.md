---
projection: today
title: Home
subtitle: What's waiting on you, what's on the go, and what you've done lately.
namespace: me
kind: refreshed
opens: static
lifespan: long-lived
freshness: stale after 1 day
sources: [layers/focus, layers/work/index.md, layers/witness]
writes: []
home: surface/projections/me/today/
sharing: private
template: dashboard
legacy: false
---

# Home

**What it's for:** the first thing the human sees, and the page they come back to. What needs them, what's on the go, and what they've done lately, so the good stuff is in view too.

## Panels

| Panel | Kind | From | Rule |
|---|---|---|---|
| **Waiting on you** | list | open foci whose latest entry says *waiting on you*, with what's next | `list foci where waiting=yes show intention, next empty "Nothing's waiting on you."` |
| **On the go** | list | active things, each with its summary; at most five, most recently updated first | `list work where state=active and kind!=area order updated desc limit 5 show title, summary empty "Nothing yet. Tell me what you'd like a hand with."` |
| **Done lately** | list | wins and finished things from the growth record, last two weeks, newest first | `list witness where updated>=14d order updated desc limit 5 show title empty "Nothing yet. What you finish shows up here."` |

Each **Rule** is what `scripts/sphere render` follows. Change a rule (or add a row with one) to change the view: `list <source> [where …] [order <key> [desc]] [limit N] show <key>, <key> [empty "…"]`, or `count <source> [where …] as <label>; …`. A source is `foci`, `witness` (the growth ledger: `updated`, `lane`, `title`), or a tree's name (`work`, `idea`; `work+archived` takes in the archive). Conditions: `key=a|b`, `key!=a`, `updated>=7d`, joined with `and`. A row with no rule leaves the whole view to the AI.

## Leave out

Focus numbers, file paths, closed foci, archived work, and anything about the sphere's own workings.

## Engine

`scripts/sphere render` rewrites `data.js` beside the page from the rules above and stamps `rendered` in `surface/projections/assets/registry.js`. `sphere ground` and `sphere close` run it whenever they change work or a focus, so the view is never behind.

## History

- Shipped with the `homesphere` build, over base's Today.
