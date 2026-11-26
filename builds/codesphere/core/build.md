# This sphere's build: codesphere

_Read during the first conversation (setup step 2), and by `sphere start`. It says what this build adds to base, and where._

## What it adds

- **A stance for engineering with AI:** the [agentic-engineering](protocol/lenses/agentic-engineering.md) lens (understand first, architect explicitly, let AI scale the execution) and its two frames, engineering discipline and harness engineering.
- **Runbooks:** the [workflow](protocol/lenses/workflow.md) lens and its frames: the PR runbook (authoring and reviewing), the gates code work passes at each trust rung, worktree lanes, meetings before and after, and channel voices for drafts.
- **Codebase knowledge:** three starting domains in knowledge: `product` (what the product and the business are), `eng` (conventions, and what's learned about each codebase), `people` (the people and teams the human works with; private).
- **Goals:** `layers/work/goals.md`, read by the morning and weekly anchors.
- **Your codebases:** `core/user/codebases.md`, where each one lives on this machine and how to work in it (tests, build, worktrees, the team's pull request conventions). Work that's out for review carries `review:` (the link to the pull request).
- **Channel voices:** `core/user/channels.md`, a starting set for how drafts read on each channel. They're a starting point, to be made the human's own.
- **More anchors:** the morning and the weekly look, as well as the wrap.

**A starting configuration, not a finished one.** Conventions marked *example* in these files (naming rules, PR house style, the worktree layout) are there to be kept, changed or dropped by the human. Never present them as rules the human already holds.

## Setup

Adds to [`init.md`](init.md):

- **Step 3, who they are:** they're an engineer, so set the literacy level to `can-use` unless they say otherwise.
- **Step 6, what's on their plate:** first ask which codebases they work in. For each, add a section to `core/user/codebases.md` (replacing the example) with only what they give: what it is, where it lives, how to run the tests. Don't go reading the codebase now. Then ask what they're working on: tickets, features, reviews. Each is a work item; one already open as a pull request gets `review:` with its link.
- **Step 6, goals:** ask, lightly, whether there's a goal for this quarter or half they'd like the mornings to keep in view. On a yes, write it in `layers/work/goals.md`, in their words. On a no, leave it.

## Anchors

- **The morning:** a short look at the day, when they say they're starting: their work that's out for review, reviews waiting on them if the sphere can see the host, today's meetings if the sphere can see a calendar, and the goals in a line.
- **The wrap:** what got done, saved, at the end of a day.
- **The weekly look:** on the day they choose, what shipped, what's stuck in review, worktrees ready to clear, and how the week sat against the goals.

## Startup context

- **their goals:** `layers/work/goals.md#headings`
- **anchors this sphere keeps:** `core/build.md#Anchors`
