---
frame: collaboration-modes
kind: structural
lens: [modes, agent-trust]
derives_from: [modes@1, agent-trust@1]
version: 1
version_note: First draft. The four collaboration modes, setting and recording one, changing it without changing the focus, the guardrails that don't move.
status: drafting
updated: 2026-11-13
sharing: public
reads: [layers/focus, core/ai/agents]
writes: [layers/focus]
protocol: [I-say-who-does-the-work, A-set-collaboration-mode, collaboration-mode-changed]
---

# Collaboration modes

**Applies to:** every focus (it's always in some collaboration mode), every change of who is doing the work, and every run of an agent.

## The four

| Collaboration mode | Who works | Who checks | Who chooses each step |
|---|---|---|---|
| **Human only** | the human, without the AI | | the human |
| **Together** | the human and the AI at the same time | the human, as it happens | the human, turn by turn |
| **Supervised** | the AI, while the human is around | the human, at each gate | the AI |
| **Unattended** | the AI, with the human away | the human, afterwards | the AI |

**The last column is what separates a session from an agent** (see [focus](../../lenses/focus.md#sessions-and-agents-are-two-ways-of-working-a-focus)). *Together* is a session. *Supervised* and *unattended* are an agent.

**Human only is still a collaboration mode.** Work the human keeps for themselves can still have a focus: the sphere holds its intention and its memory, and the human brings back what happened.

## Setting it

- **Each focus records its collaboration mode** in `collaboration-mode:` ([focus-nodes](../focus/focus-nodes.md#focusmd)): `human-only`, `together`, `supervised` or `unattended`. A window that opens a focus and works it with the human sets `together`.
- **For an agent's run, it's the lower of earned and delegated** ([trust-ladder](../agent-trust/trust-ladder.md#earned-and-delegated-the-lower-wins)). The human asks; the agent's trust caps it.
- **Moving work toward *unattended* is trust.** The sphere can suggest it when an agent has earned it. The human decides.

## Changing it doesn't change the focus

**Work moving from *together* to *unattended* is one focus changing its collaboration mode.** Whether a new window attaches for the unattended part doesn't matter: the memory is the focus's. The change is written into `collaboration-mode:` at the next ground and noted in that ground's history entry, so a later reader knows how each stretch of the work was done.

- **Changing collaboration mode doesn't change the operating mode,** and the other way round. They combine freely.
- **Moving toward the human is always allowed,** at once: *"let me take over"*, *"let's do this one together."* The run drops to the lower collaboration mode and carries on.
- **Moving away from the human needs the trust for it.** If the agent hasn't earned *unattended* for this kind of work, say so, and offer *supervised*.

## The guardrails don't move

**However far work moves, the guardrails stay where they are.** Unattended work still drafts, queues and waits for anything that needs the human's yes. Being away isn't permission ([human-is-highest](../../lenses/human-is-highest.md)). **The dial moves execution, never authority.**

- **Sphere authoring is never unattended** ([sphere-authoring](sphere-authoring.md)).
- **Some operating modes may add limits of their own,** such as a reflecting operating mode that never runs unattended. They can tighten; they never loosen.

## When / do

| When | Do |
|---|---|
| A focus opens with the human in the window | `collaboration-mode: together` |
| A focus delegates to an agent | Set the lower of what was asked and what the agent has earned |
| *"Let me take over"*, *"let's do this together"* | Drop to that collaboration mode at once. Fire `collaboration-mode-changed` |
| *"Run this one unattended"* | If the agent has earned it for this kind of work, set it; otherwise say so and offer *supervised*. Fire `collaboration-mode-changed` |
| The human is doing this part alone | `human-only`; when they come back, capture what happened in the next ground |
| Grounding after a change | Write the new value and note the change in the history entry |

## Works with

- [trust-ladder](../agent-trust/trust-ladder.md): the rungs are these collaboration modes.
- [operating-modes](operating-modes.md): the other dimension.
- [reaching-the-human](../human-rhythm/reaching-the-human.md): how supervised and unattended work brings what it needs back to the human.
- [focus-nodes](../focus/focus-nodes.md): where the collaboration mode is recorded.

## Senses

| Sense | Fires when |
|---|---|
| `collaboration-mode-changed` | a focus's collaboration mode changes |
