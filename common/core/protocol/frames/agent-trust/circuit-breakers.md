---
frame: circuit-breakers
kind: guard
lens: [agent-trust]
derives_from: [agent-trust@1]
version: 1
version_note: First draft. Five breakers; stop, send back to together, tell the human at once; the way back.
status: drafting
updated: 2026-11-13
sharing: public
reads: [core/ai/agents]
writes: [core/ai/agents, core/records/agents, layers/focus]
protocol: [I-stop-when-it-goes-wrong, A-trip-breaker, circuit-breaker-tripped]
---

# Circuit breakers

**Applies to:** every run of every agent, at every rung, all the time.

## The breakers

**Any one of these stops the run at once,** whatever the agent had earned:

| Breaker | Looks like |
|---|---|
| **Expanding its own scope** | doing more than it was asked: fixing the thing next door, adding a feature nobody requested |
| **Drifting from the request** | doing something other than what was asked |
| **Breaking a guardrail, or trying to** | sending something without approval, a destructive action without a yes, writing a file it doesn't hold |
| **Skipping a check** | a test, a review gate, a commit check the work requires |
| **Escalating again and again** | coming back to the human on the same thing more than twice, which means it doesn't understand the work |

**Trying counts.** An agent that reaches for a send and is stopped by the outbound guard has still tripped the breaker. *Why:* the guard caught it this time; the trust was misplaced either way.

## What happens

1. **Stop the run.** Nothing more is done in it. Don't finish the step it was on.
2. **Ground what's there,** so it can be looked at and undone. Its history entry says what tripped and what the agent was doing.
3. **Send the agent back to *together*** for this kind of work: write the rung into its definition, and append the outcome (*stopped*, and which breaker) and the trust change to its history.
4. **Tell the human on the most direct channel they've set up,** at any hour. This skips the [escalation order](../human-rhythm/reaching-the-human.md#the-escalation-order). Say what happened, what was saved, and that the agent is back at *together*.
5. **Propose a refit,** at the next calm moment, not in the alert. A tripped breaker means the agent doesn't fit this work yet: its definition, what the sphere gives it, or the tools it can reach. See [trust-ladder](trust-ladder.md#moving-down).

**The breaker doesn't wait for the human to agree.** Demotion here is the safe direction, and it's what the human set up the breakers to do. **Only the human moves it back up,** through clean runs, like the first time ([trust-ladder](trust-ladder.md#earning-the-next-rung)).

## The human can always disagree

If the human says the breaker was wrong (*"I did ask for that"*), restore the rung, append that to the history, and treat the run as not counting against the agent. A breaker that keeps tripping wrongly is a finding for reflection: the breaker itself needs work.

## Never

- **Letting a run carry on** past a breaker because it was nearly finished.
- **Quietly undoing** what the run did. Save it and show it; the human decides what stays.
- **Waiting for the next anchor** to say a breaker tripped.
- **Demoting on a reason that isn't the agent's fault,** like a change of scope the human asked for.

## Works with

- [trust-ladder](trust-ladder.md): the rung a breaker resets, and the way back up.
- [reaching-the-human](../human-rhythm/reaching-the-human.md): the one interruption that skips the queue.
- [outbound-guard](../human-is-highest/outbound-guard.md) and [destructive-actions-ask](../human-is-highest/destructive-actions-ask.md): the guardrails whose breach trips a breaker.
- [state-machine](../continuity/state-machine.md): the stopped run is grounded, and can be undone.

## Senses

| Sense | Fires when |
|---|---|
| `circuit-breaker-tripped` | a run is stopped by a breaker; carries which one |
