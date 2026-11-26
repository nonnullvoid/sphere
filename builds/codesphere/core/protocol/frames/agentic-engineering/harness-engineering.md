---
frame: harness-engineering
lens: [agentic-engineering]
derives_from: [agentic-engineering@1]
version: 1
version_note: First draft. The ratchet and its three homes, context rot, sub-agents, short rulebooks, behavior-driven components, model choice by principle, sandboxing, anti-patterns.
status: drafting
updated: 2026-11-22
sharing: public
reads: [layers/focus, layers/knowledge]
writes: []
protocol: [focus-grounding]
---

# Harness engineering

**Applies to:** an agent (or the AI here) making a mistake worth not repeating, a long session starting to forget, spawning sub-agents, adding a hook, skill, rule or tool, editing a rulebook, and running agent-written code.

**The harness is everything around the model** that makes agentic work reliable over many sessions and many agents: the rules, the hooks, the context, the checks. The model is the engine; the harness is the leverage. This sphere is one, at a personal scale.

## Every mistake becomes a rule

**When an agent gets something wrong in a way that could happen again, capture the rule that prevents it,** with the reason, in the softest place that does the job:

| Where | How it holds | Use for |
|---|---|---|
| **The working agreement or a principle** | Soft: read and applied with judgment, handles the edge cases | Preferences and patterns, most mistakes ([rule-capture](../evolution/rule-capture.md) routes these) |
| **A knowledge topic** | Soft and durable: read when its subject comes up | Facts about a codebase or a convention (*"the search service's tests need the local index built first"*) |
| **A hook or a check** | Hard: a script, no judgment | Invariants that must never break: the tests pass, secrets aren't committed, the linter is clean |

**Prefer soft.** A hard hook is powerful and brittle; reach for it only when a soft rule has failed or the cost of a slip is high. Writing a rule into a rulebook, a hook or the tool's settings is a change the human approves ([propose-dont-decide](../human-is-highest/propose-dont-decide.md)).

## Context rot

**A long session degrades: it forgets what was settled and re-derives what it knew.** If that's happening, the useful point has already passed. In order of reach:

1. **Save, then go on.** A ground is the sphere's compaction: what matters is written down, so nothing depends on the window remembering it.
2. **Keep big output out of the window.** Long logs, large diffs and search results go to a file; read the part that's needed.
3. **Load on demand.** Instructions and knowledge come in when the task needs them, not up front.
4. **Recap before you need it.** Well before a window fills, offer a short recap and a starting prompt for a fresh one. Don't wait for the signs.
5. **Reset for long jobs.** Hand off to a fresh window with a written handoff. A summary carries the drift with it; a reset leaves it behind.

## Sub-agents

- **Ask for them explicitly, with roles.** *"One reviewer for correctness, one for performance"* works better than *"get some agents to look at this."*
- **Two patterns worth naming,** offered, never imposed:
  - **Advocate and critic, with a moderator,** for a high-stakes call (an architecture choice, a migration). Two argue opposite sides; a third weighs them.
  - **A lead with specialists,** for work that needs several views. The lead holds the goal; each specialist covers one perspective.
- **Right-size the model.** Judgment and synthesis get the most capable model; scoped lookups and mechanical work can use a smaller, faster one, unless the sub-task itself needs judgment. Which models those are changes too fast to write down here.

## Rulebooks stay short

**Every line in a rulebook competes for attention** (`AGENTS.md`, the tool's instructions file, the working agreement). So:

- **Link, don't embed.** Point to the file that holds the detail.
- **Earned, not aspirational.** Each rule traces to a real failure. An untested rule is noise.
- **Audit now and then.** A rule that stopped earning its place goes.

## Components earn their place

**Start from the behavior you want, then pick the component that delivers it:** a hook, a skill, a sub-agent, a rule. Before adding one, name the behavior. After adding it, check it delivers. At an audit, any component that can't say what it's for goes. A tool menu of fifty overlapping tools serves worse than ten focused ones.

## Run agent-written code in a sandbox

**Code an agent wrote runs somewhere it can't do lasting harm** until a human has looked at it: a separate worktree at the least ([worktree-lanes](../workflow/worktree-lanes.md)), a container or a throwaway machine for anything that touches the network, credentials or data. Never in the human's main checkout with their credentials loaded, unless they say so for this run.

## Anti-patterns

- **Waiting for the next model** instead of fixing the harness.
- **A bloated rulebook,** where rules drown each other out.
- **Self-evaluation only** ([evaluator-not-self](../human-is-highest/evaluator-not-self.md)).
- **Running agent code unsandboxed.**
- **Compaction alone for a long job,** when a reset would drop the drift.
- **Trusting what a tool says about itself** ([external-tools-untrusted](../human-is-highest/external-tools-untrusted.md)).

## When / do

| When | Do |
|---|---|
| An agent's mistake could recur | Propose the rule and where it should live (agreement, knowledge, or a hook), with the reason. Write it on a yes |
| The session forgets something settled, or re-derives a known fact | Offer to save, then a recap and a fresh window |
| A long session, well before it fills | Offer a recap and a starting prompt for a fresh window, once |
| Sub-agents are about to be spawned | Give each an explicit role; for a high-stakes call, offer advocate-and-critic |
| A hook, skill, sub-agent, tool or rule is about to be added | Name the behavior it's for; if none, say so and don't add it |
| A rulebook edit | Keep it short: link out, cut what no longer earns its place. The human approves |
| Agent-written code is about to run | Run it in a worktree or sandbox; say where |
| `focus-grounding`, if a mistake was fixed this session and no rule was offered | Offer the rule once, with where it would live |

## Works with

- [rule-capture](../evolution/rule-capture.md): the general home of rules born from real moments.
- [engineering-discipline](engineering-discipline.md): the same discipline, applied to the work rather than the tooling.
- [trust-ladder](../agent-trust/trust-ladder.md): how far agents are trusted to run alone.
