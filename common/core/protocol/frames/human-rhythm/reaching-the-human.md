---
frame: reaching-the-human
lens: [human-rhythm]
derives_from: [human-rhythm@1]
version: 1
version_note: First draft. What's waiting, read from the focus tree; the ground line; the escalation order; the after-hours lean.
status: drafting
updated: 2026-11-13
sharing: public
reads: [layers/focus, surface/state/focus]
writes: [layers/focus]
protocol: [I-hear-back-when-im-here, A-ask-the-human, A-whats-waiting, waiting-on-human]
---

# Reaching the human when they're there

**Applies to:** any work, run supervised or unattended, that needs the human (a question, an approval, a draft to check), and every moment the human is present to see it: a ground, an anchor, a window they're in.

## Waiting is written as history, and read from it

**A run that needs the human doesn't set a flag. It writes down what it needs, and stops.**

1. **Ground what it has,** so nothing is left unsaved.
2. **Append a history entry** headed `## <date> — waiting on you`, saying exactly what it needs: the question with its options, or the draft and where it would go.
3. **Report one line up** to its parent, as every child does ([focus-tree](../focus/focus-tree.md#reporting-up)): *"f31: waiting on you: which of two quotes to accept."*
4. **Wait.** The window stays attached to its focus and simply waits. Nothing is detached or closed: in a harness where every open window is tied to a focus, the window is already where the answer will land. When the human answers, in that window or another, the work picks up from the entry.

**What's waiting is computed:** an open focus whose latest history entry is a *waiting on you* entry, plus drafts in the review queue ([outbound-guard](../human-is-highest/outbound-guard.md#agents-never-send)). Once the human answers, the next entry follows it, and it stops being waiting. **Nothing is marked, and no list is kept.** *Why:* a list kept beside the tree drifts from it; the history can't.

## Where waiting work shows up

| Surface | When the human sees it |
|---|---|
| **The ground line** | After every ground: *"2 foci waiting on you · 1 draft to review."* Nothing at all when nothing is waiting |
| **The anchors** | The morning orientation and the wrap list everything waiting, each with its question in a line ([daily-cadence](daily-cadence.md)) |
| **In the window** | A question asked in the window the human is in |
| **A projection** | A dashboard or home page, for a sphere that has one |
| **A notification** | A message on a channel the human chose, for what can't wait |

**The ground line is the one to ship first.** The human grounds often, one line costs nothing to read, and it needs nothing but the focus tree. A sphere that ships nothing else should ship that.

## The escalation order

**Cheapest and most present first.** When something needs the human:

1. **Ask in the window the human is in,** if there is one: usually the window attached to the focus that delegated the run.
2. **Otherwise, wait:** write the *waiting on you* entry and let the ground line and the next anchor show it.
3. **A projection,** for a sphere that has one.
4. **A notification,** only for what can't wait for the next anchor.

**What can't wait is the human's word, not the sphere's guess.** The human says so when delegating (*"tell me straight away if the quote expires"*) or as a standing rule. A circuit breaker always counts.

**A circuit breaker skips the queue.** When an agent trips one ([circuit-breakers](../agent-trust/circuit-breakers.md)), it stops at once, and the human is told on the most direct channel they've set up, whatever the hour.

**Every notification passes the [outbound guard](../human-is-highest/outbound-guard.md).** A notification to the human's own channel is a vetted ability, registered once, like any other.

## The after-hours lean

**Outside the human's usual hours, lean toward waiting.** Queue instead of interrupting, and show it at the next anchor. Only what can't wait, or a circuit breaker, breaks through. The usual hours come from the human's pattern ([daily-cadence](daily-cadence.md#the-humans-pattern)); being away is never permission to decide in the human's place (see [human-is-highest](../../lenses/human-is-highest.md)).

## When / do

| When | Do |
|---|---|
| A supervised or unattended run needs the human | Ask in the human's window if there is one. Otherwise ground, append *waiting on you*, report up, and wait. Fire `waiting-on-human` |
| Any ground completes | Add the ground line if anything is waiting; nothing if not |
| The morning or the wrap | List everything waiting, a line each |
| *"What's waiting?"* | List waiting foci and drafts, oldest first, each with its question |
| The human answers | Attach to that focus; the answer is the next history entry. The run carries on, or a new one starts |
| Something the human marked as can't-wait comes up | Notify, through the outbound guard |
| A circuit breaker trips | Stop, and tell the human on the most direct channel, at any hour |
| After hours, nothing urgent | Wait for the next anchor |

## Works with

- [focus-tree](../focus/focus-tree.md): report lines and what's waiting for a parent.
- [daily-cadence](daily-cadence.md): the anchors list what's waiting; the pattern sets the hours.
- [trust-ladder](../agent-trust/trust-ladder.md): what a run may settle on its own, and what it must bring to the human.
- [circuit-breakers](../agent-trust/circuit-breakers.md): the one case that interrupts.
- [outbound-guard](../human-is-highest/outbound-guard.md): every notification, and the review queue for drafts.

## Senses

| Sense | Fires when |
|---|---|
| `waiting-on-human` | a run appends a *waiting on you* entry and waits |
