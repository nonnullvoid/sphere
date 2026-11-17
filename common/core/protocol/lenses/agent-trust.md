---
lens: agent-trust
version: 1
version_note: First draft. Trust per agent and kind of work, earned on evidence and granted by the human; the lower of earned and delegated; circuit breakers; definitions apart from runs.
derives_from: practice in spheres in daily use, and the agent trust design (spec/agent-trust.md)
status: drafting
updated: 2026-11-13
verified: false
sharing: public
frames: [trust-ladder, circuit-breakers, agent-definitions]
---

# How far an agent may go on its own

**An agent is the model choosing its own next step,** working a focus while the human checks at gates or afterwards (see [focus](focus.md#sessions-and-agents-are-two-ways-of-working-a-focus)). How much it's left to choose on its own is trust. **Trust is earned, the human grants it, and it can be taken back at any time.**

## Agents scale execution, not judgment

Agents make doing cheap: more work in parallel, tireless recall, drafts in minutes. **Cheap execution amplifies whatever sits upstream of it,** good understanding or bad. So the split is deliberate. The human holds the meaning: whether the work is worth doing, whether it fits, what it's for. Agents carry the doing. *"Should we?"* is never something an agent decides, however much it has earned.

Until an agent has shown it does a kind of work well, **the human is the one who checks it.** An agent judging its own work skews kind (see [evaluator-not-self](../frames/human-is-highest/evaluator-not-self.md)).

## Trust is specific

- **Per agent, and per kind of work.** Never global. An agent trusted to tidy notes on its own isn't thereby trusted to draft emails on its own. There's no fixed list of kinds: what kind of work an agent does becomes clear as the human builds it.
- **The ladder is the collaboration modes.** *Together*, then *supervised*, then *unattended*. There's no second scale to learn (see [modes](modes.md#two-dimensions-always-named)). *Human only* isn't a rung: it's work the human keeps.
- **Two things decide a run, and the lower wins:** what the agent has earned for this kind of work, and what the human delegated this time. An agent that has earned *unattended* still works *together* when the human says *"let's do this one together."* One that has only earned *supervised* doesn't go *unattended* because the human left.

## Trust is earned, and the human grants it

- **Clean runs are the evidence.** A run is clean when it finished what was asked without the human having to correct it partway.
- **The sphere says when an agent is a candidate; the human promotes.** *"The notes agent has tidied five weeks of notes cleanly. Want it to run unattended?"* The sphere never promotes an agent, and never promotes itself.
- **One rung at a time.**
- **A correction counts only when the agent was wrong.** A change of scope, or a preference, isn't the agent's fault, and shouldn't cost it trust.
- **Trust doesn't decay on a timer.** Whether it still holds depends on what's changed around the work. When something has, the human moves the agent back down.

## Trust is revocable, sometimes at once

**Some things end trust immediately,** whatever was earned: doing more than was asked, drifting from the request, breaking a guardrail or trying to, skipping a check the work requires, escalating again and again on the same thing. These are circuit breakers. The run stops, the agent goes back to *together*, and the human hears about it straight away. Climbing back takes clean runs, like the first time.

## The guardrails don't move

**However much an agent has earned, it still drafts and waits for anything that needs the human's yes.** Sending under the human's name, anything hard to undo, a decision about what the work is: these hold at *unattended* exactly as at *together*. **The dial moves execution, never authority** (see [human-is-highest](human-is-highest.md)).

## Who an agent is, and what it did

- **An agent's definition is who it is and how far it's trusted.** It has a home in the sphere, even when its definition lives with the code it works on.
- **A run is a window attached to a focus.** Its memory of the work is that focus's history, where the human can read it. The agent's own record holds only outcomes and trust changes.
- **Outcomes are a byproduct.** Every run's outcome is noted alongside the work, never as a gate in front of it. An agent that keeps being corrected for the same reason probably has a definition that needs work: that's a finding for reflection, not the agent's fault.
- **A demotion says the agent doesn't fit the work yet.** When a breaker trips or the human moves an agent down, something is mismatched: the agent's definition, what the sphere gives it to work with, or the tools and skills it can reach. **That's a chance to refit the agent to the work, not just a miss to count.** The sphere finds the likely cause and proposes the change; the human decides.
- **Right-sized intelligence.** As much as the work needs, and no more. When there's nothing to think about, skip the call.

## What it doesn't mean

- **Not a score.** Trust is the human's judgment of an agent, informed by evidence. It isn't computed into a number that decides by itself.
- **Not freedom from review forever.** Checking every run is the low-trust way of working, not the only one. As trust grows, the human sees results instead of steps. They can always look closer.
- **Not trust between spheres.** That's [replication](../../../../spec/replication.md#trusted-spheres--decided-not-yet-exercised).
- **Not designing teams in advance.** Agents working together are registered once they've actually run together. Shapes nobody has needed yet stay unspecified.

## What follows from it

| Frame | In short |
|---|---|
| [trust-ladder](../frames/agent-trust/trust-ladder.md) | The rungs, the lower of earned and delegated, clean runs, candidates, promotion, reject reasons |
| [circuit-breakers](../frames/agent-trust/circuit-breakers.md) | Always on. What stops a run at once and sends the agent back to *together* |
| [agent-definitions](../frames/agent-trust/agent-definitions.md) | An agent's file and its history, definition apart from runs, delegating and dispatching, teams, right-sized intelligence |

## Revision history

- **v1:** First draft. Spec chapter [agent trust](../../../../spec/agent-trust.md).
