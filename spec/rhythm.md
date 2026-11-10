# Rhythm

_Status: draft 1, for review._ How a sphere fits around the human's days: when it orients them, when it wraps up, how it learns their pattern without holding them to it, and how work done without them reaches them when they're there.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

---

## The idea

The human lives in real time. The sphere lives on its last grounded state (see [state](state.md#the-idea)). **That gap is permanent, and correct.** The sphere doesn't try to close it. It makes the moments where the two meet good ones: a start that orients, a wrap that captures, a surface where waiting work shows up.

**When the snapshot and real time disagree, the human wins.** If the sphere thinks a task is open and the human says it's done, it's done. The sphere says what it had, updates, and doesn't act on stale state as if it were current.

### Weather, not a calendar

A human's routine is **weather**: it has a shape, and it varies. Some days start early, some weeks fall apart, a trip rearranges everything.

- **Forecast, never dictate.** The sphere can say what a day probably looks like and prepare for it. It never tells the human what their day must be.
- **Prepare, then adapt.** A good forecast means the right things are ready. When the day goes differently, the sphere follows it, without comment.
- **A missed routine is not a failure.** Skipping the morning check-in for a week costs nothing and is never brought up as a lapse.

---

## Anchors — **proven**

An **anchor** is a regular moment where the sphere offers something. **Anchors are offers, not obligations.** The human can take one, skip it, or never use it.

| Anchor | When | What the sphere offers |
|---|---|---|
| **Morning** | The human signals the day has started | Orientation: what's pending, what changed, candidates for today |
| **Midday** | On request, or when the day has clearly shifted | A re-calibration: what moved, what's still realistic |
| **Wrap** | The end of the working day | Capture: ground what's open, note what's carrying over |
| **Weekly** | Once a week, on the human's chosen day | A look back and a look ahead: what got done, what the week needs |

Builds choose which anchors they ship and what each one shows. The base build ships the wrap, along with [the ground line](#where-waiting-work-shows-up); morning, midday and weekly come with richer builds.

### The morning signal

**"Good morning" is a real signal.** It marks a day boundary. On it, the sphere:

1. checks the real clock (never assumes what day it is)
2. syncs the calendar, if it has one
3. surfaces what's pending: waiting work, open sessions, anything that arrived overnight
4. hands back **candidates** for today

**It never picks the work.** The human chooses from the candidates, or ignores them.

**Opening a session is not the morning signal.** A session start greets in a line and loads its [handshake slice](loading.md#at-startup-the-handshake-slice). The full orientation renders only when the human signals the day has begun. Sessions open many times a day; mornings happen once. A sphere that gives a morning briefing on every open becomes noise fast.

### The forgotten wrap

**Humans forget to wrap.** The day ends mid-thought and the session is left open. So the sphere can watch for the end of the day: once it's late enough, it offers the wrap, and if the human has gone, it [grounds](state.md#ground--proven) what's open so nothing is left dirty overnight.

The trigger is an offer when the human is there, and a safety net when they aren't. It never closes work the human is still in the middle of.

### The time signal

**The sphere checks the real clock,** the local time on the human's device, at session start and at each anchor. It never infers the time from the conversation. A conversation that started yesterday is still running today, and an AI's sense of "now" can be months off. Because it's the device's time, travel needs no special handling: the anchors, the pattern and the after-hours bias all move with the human.

---

## The human's pattern — _decided, not yet exercised_

Over time the sphere notices the human's pattern: when their day usually starts, which days are different, when they stop.

- **It's noticed, not asked for.** No form, no setup question.
- **It lives in the [knowledge](knowledge.md) layer,** as a read graded *inferred*, citing what it was derived from. Like anything entering knowledge, it's offered to the human first: *"Your days seem to start around nine. Keep that?"*
- **It's soft.** It informs the forecast and nothing else.
- **It's never held against the human.** An unusual day is just an unusual day.
- **Bias against after hours.** Outside the human's usual hours, the sphere leans toward waiting: it queues instead of interrupting, and surfaces at the next anchor. Only something genuinely urgent breaks through.

---

## Reaching a human who's present — _decided, not yet exercised_

Work happens in every [collaboration mode](modes.md#collaboration-modes--decided-not-yet-exercised). Some of it, run *supervised* or *unattended*, eventually needs the human: a question, an approval, a draft to check. **That work has to surface in a moment when the human is actually there.** Otherwise it waits forever, or interrupts at the wrong time.

### Where waiting work shows up

| Surface | When the human sees it |
|---|---|
| **The ground line** | After every ground, one line of what's waiting: *"2 sessions waiting for your input."* |
| **The anchors** | The morning orientation and the wrap list everything waiting |
| **In the session** | A question asked in the session the human is in |
| **A projection** | A dashboard or home page, for a sphere that has one |
| **A notification** | A message on a channel the human chose, for what can't wait |

**The ground line is the cheapest and the most reliable.** — **proven** The human grounds often, and one line costs nothing to read. A sphere that ships nothing else should ship that.

### Escalation order

When something needs the human, the sphere reaches for the **cheapest and most present channel first**:

1. ask in the session the human is in, if there is one
2. otherwise, pause the work, mark it waiting, and surface it at the next ground or anchor
3. a projection, for a sphere that has one
4. a notification, only for what can't wait for the next anchor

**A circuit breaker skips the queue.** When an agent hits something that must stop it at once (see [agent trust](agent-trust.md#circuit-breakers--proven)), it stops, and the human is told on the most direct channel they've set up.

Every notification passes the [outbound guard](../common/core/protocol/frames/human-is-highest/outbound-guard.md) like anything else that leaves the sphere.

---

## Rhythm and growth

The anchors are where growth becomes visible. The wrap is a natural moment to record a win; the weekly anchor is a natural moment to look back. A [witness](work.md#witness-optional) layer listens at the anchors. Rhythm doesn't score anything itself.

---

## Senses and commands — _decided, not yet exercised_

**Senses:**
- `day-started`, `day-wrapped`, `week-reviewed`
- `wrap-missed` (the forgotten-wrap trigger fired)
- `waiting-on-human` (work paused for the human's input)

**Commands** (natural phrasing works too):
- `good morning`
- `wrap up`
- `what's waiting?`
- `how was my week?`

