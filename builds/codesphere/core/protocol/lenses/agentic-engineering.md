---
lens: agentic-engineering
version: 1
version_note: First draft. AI multiplies what's upstream; understand, architect, then scale execution; distinct from vibe coding by structure; decomposition, the two loops, judgment stays human.
derives_from: practice in an engineering sphere in daily use, made generic
status: drafting
updated: 2026-11-22
verified: false
sharing: public
frames: [engineering-discipline, harness-engineering]
---

# Agentic engineering

**AI is a multiplier, and the sign of the multiplier depends on what it multiplies.** Capable agents make code cheap to write, prototypes cheap to try, and recall almost free. Cheap execution amplifies whatever sits upstream of it, including a bad understanding, a weak decomposition or an unclear scope. This lens is how the sphere works on software so that what gets multiplied is worth it.

## Understand, architect, then scale

| Step | Whose | What it means |
|---|---|---|
| **Understanding** | the human's | Whether this makes sense, fits, and solves the actual problem. AI speeds up the *act* of understanding (questions, exploration, summaries, reading code); the judgment stays with the human |
| **Architecting** | human-led, AI-assisted | Decomposition, sequencing, the dependencies. The shape of the work is clear before AI runs it |
| **Execution** | where AI runs | Agents in parallel, drafting, recall, mechanical refactors. Cheap, and it scales |

**Distinct from vibe coding by structure, not by tone.** Vibe coding skips the understanding step: prompt, see what happens, iterate. That's fine, and faster, when the stakes are low and being wrong is cheap: a throwaway prototype, a quick script, learning an API by poking at it. Agentic engineering insists on the step when the stakes warrant it.

**It isn't anti-speed.** For non-trivial work, structure upstream is faster, because cheap execution turns an upstream mistake into a working prototype in ten minutes, and that can cost more than one that took three days to scaffold. Speed accelerates the wrong thing too.

**The step compresses with experience.** An engineer who knows the domain may understand in seconds what looks like skipping the step. Don't mistake speed for absence.

## How it shows up

- **Decomposition is the differentiator.** When execution is cheap, the core skill is breaking work into pieces an agent can carry out reliably: the end goal said plainly, a plan first, agent-ready cards with acceptance criteria. **Write the decomposition down** ([work-breakdown](../frames/work-tracking/work-breakdown.md), [plans](../frames/work-tracking/plans.md)): one held in a head isn't durable, and the next agent can't see it.
- **Two loops.** The inner loop is the human's: the cards, the scope, what done looks like. The outer loop is the agents': running the cards. The human reviews the output; they don't babysit the execution.
- **The human is the evaluator** until an agent has earned more, per kind of work ([trust-ladder](../frames/agent-trust/trust-ladder.md)). An agent's view of its own work skews positive ([evaluator-not-self](../frames/human-is-highest/evaluator-not-self.md)).
- **AI scales execution, not judgment.** *Should we do this? What's the second-order effect? Does this feel right?* Those aren't leverage; they're meaning, and they stay with the human ([human-is-highest](human-is-highest.md)).
- **Agentic isn't autonomous.** This lens is about how the work is structured. How far an agent is trusted to run it alone is [agent-trust](agent-trust.md)'s question.
- **Don't wait for the next model.** A failure is an engineering signal. The next model won't add a missing tool, write the rule nobody wrote, or fix a context that's been allowed to rot.

**The sphere is itself a harness:** a personal one, built from the same discipline it applies to the work.

## What follows from it

| Frame | In short |
|---|---|
| [engineering-discipline](../frames/agentic-engineering/engineering-discipline.md) | What an engineer owes a piece of work upstream of the obvious change: trace the full flow, map the categories before searching, name for behavior, and never accept a result on self-evaluation alone |
| [harness-engineering](../frames/agentic-engineering/harness-engineering.md) | How agentic work stays reliable over many sessions: every mistake becomes a rule, context rot, sub-agents, short rulebooks, components that earn their place, sandboxing |

## Revision history

- **v1:** First draft.
