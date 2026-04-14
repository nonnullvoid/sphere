# Runner — [Project Name]

> Machine-readable session state. The AI updates this at the end of every session where project work happened. Read this at the start of a session to resume without re-explaining.

---

## Status

**Current state:** `not-started` | `in-progress` | `blocked` | `ready-to-continue` | `done`

**Completion:** 0 / 0 tasks done

---

## Last session

**Date:** —

**What was done:**
*Summary of work completed in the last session.*

**Outcome:** *What changed as a result — code merged, doc sent, decision made.*

---

## Handoff

**Pick up here:**
*The exact next action. Specific enough that a cold-start agent knows what to do.*

**Context to reload:**
*Files, links, PRs, docs, or state needed to resume. List explicitly.*

**Open decisions:**
*Unresolved questions or choices that need to be made before proceeding.*

---

## Blockers

*What's in the way right now. Who or what needs to move.*

---

## Progress log

*Append-only. One line per session.*

| Date | What happened |
|------|--------------|
| — | Project created |

---

## Instructions for AI

At the **start** of a session working on this project:
1. Read this file and `project.md`
2. Tell the user where you're picking up from and confirm before starting

At the **end** of a session:
1. Update **Status**, **Completion**, **Last session**, and **Handoff** sections above
2. Append a row to the **Progress log**
3. Update `index.md` if status changed
