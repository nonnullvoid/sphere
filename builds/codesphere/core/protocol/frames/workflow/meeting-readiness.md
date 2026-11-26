---
frame: meeting-readiness
lens: [workflow]
derives_from: [workflow@1, human-rhythm@1]
version: 1
version_note: First draft. The calendar refreshed at the day's anchors, the forecast that's always partly wrong, the agenda's life.
status: drafting
updated: 2026-11-22
sharing: public
reads: [layers/workflows/meetings, layers/knowledge, layers/work]
writes: [layers/workflows/meetings]
protocol: [day-started, day-wrapped]
---

# Ready for meetings

**Applies to:** the morning and the wrap, when the sphere can see a calendar; the human asking what's coming up; and queuing, or clearing, a topic for a meeting.

**Meetings happen where the sphere can't see.** This frame keeps the human ready for them. Turning a meeting into knowledge afterwards is [meeting-consumption](meeting-consumption.md).

## The calendar, at the day's edges

**Only if the sphere has a way to read the human's calendar.** Without one, skip this, and use only what the human says.

- **Refresh at the morning and the wrap** ([daily-cadence](../human-rhythm/daily-cadence.md)), not as a ritual of its own.
- **The forecast is always partly wrong.** The regular meetings are few and easy to foresee; the rest turn up during the week from nowhere. So the day's edges are when it's re-read, and the sphere says when what it showed may already be out of date.

## The agenda

**`layers/workflows/meetings/agenda.md`, one section per meeting that has standing topics,** each a numbered list: the topic in a line, and a link to the work or document it's about.

| The human says | The sphere |
|---|---|
| *"what's coming up?"*, *"check my meetings"* | Upcoming meetings, and the topics queued for each |
| *"add … to my meeting with …"* | Confirms which meeting and the wording, then adds the topic, with its link |
| *"that meeting's done"* | Removes the topics that were covered; asks about the rest |

**Anything posted to others under the human's name** (an agenda shared, a status update) is drafted and sent through the [outbound-guard](../human-is-highest/outbound-guard.md).

## When / do

| When | Do |
|---|---|
| `day-started`, with a calendar | Today's meetings in a line each, and the topics queued for them |
| `day-wrapped`, with a calendar | Tomorrow's meetings in a line; anything new since the morning |
| *"What's coming up?"* | Upcoming meetings and their queued topics |
| *"Add … to …"* | Confirm the meeting and wording, then add the numbered topic with its link |
| A meeting is done | Remove what was covered; ask about the rest. If there are notes, offer [meeting-consumption](meeting-consumption.md) |

## Works with

- [daily-cadence](../human-rhythm/daily-cadence.md): the anchors that refresh the calendar.
- [meeting-consumption](meeting-consumption.md): the after-the-meeting half.
