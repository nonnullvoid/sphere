---
frame: daily-cadence
lens: [human-rhythm]
derives_from: [human-rhythm@1]
version: 1
version_note: First draft. The anchors, the morning signal, the forgotten wrap, the real clock, the human's pattern, optional scheduling.
status: drafting
updated: 2026-11-13
sharing: public
reads: [layers/focus, layers/work, layers/ideas, layers/knowledge, surface/state/focus]
writes: [layers/focus, layers/work]
protocol: [I-daily-rhythm, A-start-day, A-recalibrate, A-wrap-day, A-review-week, day-started, day-wrapped, week-reviewed, wrap-missed]
---

# The day's anchors

**Applies to:** the human signalling that a day has started or ended, a midday check-in, the weekly look, the end of the day when nobody wrapped, and every window attaching (so that it stays light).

## The anchors

**Every anchor is an offer.** The human can take it, skip it, or never use it. A build chooses which anchors it ships; the base build ships the wrap.

| Anchor | When | What the sphere does | Writes? |
|---|---|---|---|
| **Morning** | The human signals the day has begun: *"good morning"*, *"start my day"* | Orients: what's waiting, what changed, candidates for today | No |
| **Midday** | On request (*"catch me up"*, *"what should I work on?"*), or when the day has clearly shifted | Re-calibrates: what moved since the morning, what's still realistic | No |
| **Wrap** | The human says *"wrap up"*, or the end of the day arrives without one | Captures: grounds what's open, says what carries over | **Yes**, through ground |
| **Weekly** | Once a week, on the human's chosen day | Looks back at what got done, and ahead at what the week needs | No |

**The anchors read; ground writes.** Only the wrap changes anything, and it does so through [state-machine](../continuity/state-machine.md)'s `ground`, like any other save.

## The morning

**"Good morning" marks the day's boundary.** On it:

1. **Read the clock** on the human's device. Never assume the day.
2. **Read the calendar,** if the sphere has one.
3. **Gather what's pending:** what's waiting for the human ([reaching-the-human](reaching-the-human.md)), each open focus's latest **Next**, work that has stalled, ideas worth a look (one line, from [idea-capture](../../lenses/idea-capture.md)), anything that arrived overnight.
4. **Hand back candidates** for today, a few, with why each is there.

**Never pick the work.** The human chooses from the candidates, or ignores them. *Why:* the human knows what moved since the last ground; the sphere doesn't.

**Attaching a window is not the morning.** A window attaching greets in a line and gets on with what it was opened for. The full orientation renders only on the morning signal, whether it comes first thing or mid-conversation. *Why:* windows attach many times a day; a briefing on each becomes noise, and the human stops reading it.

## Midday

Re-read what the morning read. Say what has flipped since: a focus that reported, work that finished, something that arrived. **Say plainly that the picture may already be stale,** and hand back candidates again.

## The wrap

1. **Ground this window's focus,** and offer the same for each other focus with unsaved work, one at a time, each with its own history entry. **A focus another window is still attached to is left to that window;** say it's there.
2. **Say what carries over:** each open focus's **Next**, in a line each.
3. **List what's still waiting** for the human.
4. **Offer one moment of recognition,** if the sphere has a witness layer: the wrap is a natural place to note a win. Nothing is scored here.

**The wrap never closes a focus.** Closing is the human's call. A focus that was finished today is offered for closing, once.

### The forgotten wrap

**Humans forget to wrap.** So once it's later than the human's usual end of day:

- **If the human is there,** offer the wrap once, at the next thing they ask: *"It's past seven. Wrap up?"* If they say no, don't offer again today.
- **If they've gone,** a scheduled check (below) grounds what was left unsaved, so nothing sits dirty overnight. Fire `wrap-missed`.

**The safety net saves; it never closes, and never touches a focus that's still in use.** A focus whose window is in the foreground is someone still working: leave it, and offer the wrap when they're next seen. Only a focus that has gone stale with unsaved work is grounded, and its history entry says so: *"Grounded by the end-of-day check; the window had gone quiet."* Undo reverses it like any ground.

### Optional scheduling

A sphere with a scheduler can run the end-of-day check on its own. **It runs under a standing approval the human gives once** (*"ground what's left at the end of the day"*), which is the only way a ground happens without the human asking (see [who may commit](../continuity/state-machine.md#who-may-commit)).

- **Most nights there's nothing to do, and it costs almost nothing.** Whether any focus is stale with unsaved work is a fact the tooling reads from git and the heartbeats. Only when there is one does the AI write the history entry.
- **Without a scheduler,** the wrap is offered at the next window instead. The next morning's orientation leads with what was left unsaved, before anything else.
- **The standing approval is withdrawn whenever the human says so.**

## Weekly

On the human's chosen day: what got done (foci closed, work finished, from history and git), what stalled, what the coming week has on it. A good moment to suggest a [reflection](../../../../../spec/evolution.md#reflection-how-the-sphere-stays-healthy--proven) if signals have built up.

**A build may keep the day or the week as a long-lived background focus,** brought forward by the morning and grounded at the wrap. It's an option, not a requirement.

## The real clock

**Read the device's local time when a window attaches and at every anchor.** Never infer it from the conversation. *Why:* a conversation that started yesterday is still running today, and the AI's own sense of "now" can be months off. Because it's the device's time, travel needs nothing special: the anchors, the pattern and the after-hours lean all move with the human.

## The human's pattern

**Noticed, not asked for.** When the human's days usually start, which days differ, when they stop: these are read from when mornings and grounds actually happened, which git already records. Nothing is collected for it.

- **It's kept only on a yes.** The first time a pattern is clear, offer it as a fact for the [knowledge](../../../../../spec/knowledge.md) layer, graded *inferred*: *"Your days seem to start around nine. Keep that?"* Like any fact, it waits for the human.
- **It's soft.** It sets when the forgotten wrap fires and what counts as after hours. Nothing else.
- **It's never held against the human.** An unusual day is just an unusual day. A missed morning is never mentioned.
- **Until there's a pattern,** a build's defaults stand in (for example, an end of day at six).

## When / do

| When | Do |
|---|---|
| *"Good morning"*, *"start my day"* | Read the clock and calendar, gather what's pending, hand back candidates. Fire `day-started` |
| A window attaches | Read the clock; greet in a line. No orientation |
| *"Catch me up"*, *"what should I work on?"* | Re-calibrate: what flipped since the morning; candidates; say the picture may be stale |
| *"Wrap up"* | Ground this window's focus and offer the rest, say what carries over, list what's waiting. Fire `day-wrapped` |
| Past the usual end of day, the human is there | Offer the wrap once |
| Past the usual end of day, the human has gone | If scheduled: ground only stale foci with unsaved work, and say so in their history. Fire `wrap-missed` |
| The next morning, after a missed wrap with no scheduler | Lead with what was left unsaved; offer to ground it |
| The weekly anchor | Look back and ahead. Fire `week-reviewed` |
| A pattern in the human's days becomes clear | Offer it once as an *inferred* fact; keep it only on a yes |
| The human skips an anchor | Nothing. Never mention it |

## Works with

- [reaching-the-human](reaching-the-human.md): the morning and the wrap list everything waiting.
- [state-machine](../continuity/state-machine.md): the wrap is `ground`; a scheduled wrap is a standing approval.
- [focus-nodes](../focus/focus-nodes.md): liveness and staleness decide what the safety net may touch.
- [work-progress](../work-tracking/work-progress.md): stalled work surfaces at the next anchor.
- [propose-dont-decide](../human-is-highest/propose-dont-decide.md): the pattern is proposed as a fact, never written.

## Senses

| Sense | Fires when |
|---|---|
| `day-started` | the morning orientation is given |
| `day-wrapped` | the wrap finishes |
| `week-reviewed` | the weekly look finishes |
| `wrap-missed` | the end of the day passed without a wrap, and the safety net ran or was deferred to the next window |
