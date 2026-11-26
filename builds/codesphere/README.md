# codesphere

_Build 1.0.0 · SPHERE-ARCH 1.0 · extends [base](../base/)_

Base, for software engineering with AI. Everything in base, plus:

- **A stance:** understand first, architect explicitly, then let AI scale the execution. Decomposition written down, the human as the evaluator, judgment kept human.
- **The PR runbook:** drafting a pull request (tests, screenshots, description, opened as a draft on your go), a read-only roll-up of where yours stand, and reviewing others' work, either quickly or as a walkthrough to understand it first.
- **Gates for agents doing code work,** at each trust rung, and guardrails no rung lifts: never merge, never send without your yes, never skip checks.
- **Worktree lanes:** a predictable home for worktrees, dev and review modes, and a safety check before every switch, and cleanup once a branch merges.
- **Meetings:** walking in prepared, and turning the notes into knowledge and work afterwards, with you filling in what the notes missed.
- **Harness engineering:** every mistake becomes a rule, context kept from rotting, sub-agents with clear roles, agent-written code run in a sandbox.
- **Your codebases** (where each lives and how to work in it), **codebase knowledge**, **channel voices** for drafts, and **goals** for the mornings and the weekly look.

It's a starting configuration. The conventions marked *example* (naming, PR house style, the worktree layout) are there to be kept, changed or dropped: your sphere becomes yours as you use it.

## Start a sphere from it

```
scripts/new-sphere codesphere ~/my-sphere
```

Then open `~/my-sphere` in your AI tool and say hello.

## What's here

Only what this build adds to base. `new-sphere` lays base over the common set, then this folder over base. [`core/build.md`](core/build.md) is what the sphere itself reads about its build: what it adds, and the setup steps it adds to.
