---
frame: trust-ladder
lens: [agent-trust]
derives_from: [agent-trust@1]
version: 1
version_note: First draft. The rungs, the lower of earned and delegated, gates, clean runs computed from history, candidates, promotion, reject reasons.
status: drafting
updated: 2026-11-13
sharing: public
reads: [core/ai/agents, core/records/agents, layers/focus]
writes: [core/ai/agents, core/records/agents]
protocol: [I-trust-is-earned, A-promote-agent, A-demote-agent, A-agent-standing, run-recorded, trust-candidate, trust-changed]
---

# The trust ladder

**Applies to:** every run of an agent (deciding how it proceeds), every outcome it records, and every change to how far an agent is trusted.

## The rungs

**The ladder is the collaboration modes.** There's no second scale.

| Rung | The agent | The human |
|---|---|---|
| **Together** | works alongside the human | sees every step as it happens |
| **Supervised** | works on its own while the human is around | checks at each gate the work defines |
| **Unattended** | works with the human away | reviews afterwards |

- **Every agent starts at *together* for every kind of work.** Nothing is trusted by default.
- **A rung is held per kind of work.** The notes agent can be *unattended* for tidying and *together* for summarizing.
- **Gates belong to the work.** For writing, perhaps the outline and the final draft; for code, a plan and a review. Builds define the gates for the work they're built for. **Where a kind of work has none, there's still one:** before the result is accepted.

## Earned and delegated: the lower wins

Two things decide how a run proceeds:

- **Earned:** the agent's rung for this kind of work, from its definition ([agent-definitions](agent-definitions.md)).
- **Delegated:** the collaboration mode the human asked for this time. If they didn't say, there's no cap.

**The run proceeds at the lower of the two,** and that's what goes in its focus's `collaboration-mode:`. *"Let's do this one together"* holds an *unattended* agent to *together*. Leaving the room doesn't lift a *supervised* agent to *unattended*: the run waits at its next gate (see [reaching-the-human](../human-rhythm/reaching-the-human.md)).

**If the kind of work isn't clear,** ask, or run at *together*. Never guess upward.

## Outcomes

**Every run records one outcome,** appended to the agent's history at the run's last ground. Recording never blocks the work.

| Outcome | Means |
|---|---|
| **clean** | finished what was asked; no correction partway |
| **corrected** | finished, but the human had to correct it; with the reason |
| **rejected** | the result wasn't accepted; with the reason |
| **stopped** | a circuit breaker ended it ([circuit-breakers](circuit-breakers.md)) |

### Reject reasons

| Reason | Counts against the agent? |
|---|---|
| **The agent got it wrong:** a mistake, a missed instruction, poor work | Yes |
| **The scope changed:** the human asked for something different partway | No |
| **A preference:** the work was fine; the human wanted it another way | No |

**Ask for the reason when it isn't clear,** in one line. *Why:* an agent shouldn't lose trust because the human changed their mind, and a measure that can't tell the difference stops being fair.

## Earning the next rung

- **The streak is computed, never stored.** It's the run of outcomes for this kind of work, since the last trust change, that are clean or don't count against the agent. Read from the agent's history.
- **Three in a row makes a candidate** (a build may set two). Say so once, at a natural moment (a ground or an anchor), with the evidence: *"The notes agent has tidied five weeks of notes cleanly. Want it to run unattended for that?"*
- **The human promotes; the sphere never does.** On a yes, write the new rung into the agent's definition and append why to its history. On *"not yet,"* append that, and don't ask again until the streak has grown as long again.
- **One rung at a time.** *Together* to *supervised* before *unattended*.

## Moving down

- **The human can move an agent down at any time,** any number of rungs: *"take the notes agent back to together for summaries."* No reason needed; one is welcome in the history.
- **Trust doesn't decay on a timer.** When something has changed around the work (a new tool, a different place it runs), the sphere can say so: *"The notes moved to a new app since the agent earned unattended. Keep it there?"* The human decides.
- **A circuit breaker moves it to *together* at once.** See [circuit-breakers](circuit-breakers.md).
- **Every move down is followed by a refit.** Look at the runs that led to it and name the likely cause, in a line or two:

  | The cause | The refit |
  |---|---|
  | **The definition:** unclear about the work, missing a gate, the wrong kind of work | Propose an edit to the agent's definition |
  | **The sphere:** knowledge, a frame or a rule the agent needed and didn't have | Propose the missing piece, through [crystallization](../evolution/crystallization.md) |
  | **The tools:** a tool, skill or access the work needs that the agent can't reach | Propose adding it, or narrowing the work to what it can do |

  The refit is proposed, never applied on its own say. Append it, and the human's answer, to the agent's history. The agent climbs back with clean runs as before; a refit that landed is why it should.

## The guardrails don't move

**No rung lifts a guardrail.** An *unattended* agent still drafts and queues anything that needs the human's yes, and never sends ([outbound-guard](../human-is-highest/outbound-guard.md#agents-never-send)). **The dial moves execution, never authority.**

## When / do

| When | Do |
|---|---|
| A run is about to start | Find the kind of work and the agent's rung for it; take the lower of that and what was delegated; set the focus's `collaboration-mode:` |
| The kind of work is unclear | Ask, or run at *together* |
| A supervised run reaches a gate | Stop and show the human; carry on only on their yes |
| A run ends | Append its outcome to the agent's history. Fire `run-recorded` |
| The human rejects or corrects, reason unclear | Ask which reason, in a line |
| The streak reaches the candidate length | Say so once, with the evidence. Fire `trust-candidate` |
| The human promotes or demotes | Write the rung into the definition; append why to its history. Fire `trust-changed` |
| An agent moved down | Name the likely cause; propose the refit; append it and the answer to its history |
| *"How is the notes agent doing?"* | Its rungs, its recent outcomes, its streak, any repeated correction |
| Something has changed around a trusted kind of work | Say so once; the human decides |

## Works with

- [agent-definitions](agent-definitions.md): where the rung and the history live.
- [circuit-breakers](circuit-breakers.md): the other way down.
- [collaboration-modes](../modes/collaboration-modes.md): the rungs are the collaboration modes.
- [reaching-the-human](../human-rhythm/reaching-the-human.md): how a run at a gate reaches the human.
- [evaluator-not-self](../human-is-highest/evaluator-not-self.md): until trust is earned, the human is the evaluator.

## Senses

| Sense | Fires when |
|---|---|
| `run-recorded` | a run's outcome is appended to its agent's history |
| `trust-candidate` | an agent's streak for a kind of work reaches the candidate length |
| `trust-changed` | the human promotes or demotes an agent, or a circuit breaker does |
