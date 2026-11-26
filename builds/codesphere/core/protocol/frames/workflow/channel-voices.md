---
frame: channel-voices
lens: [workflow]
derives_from: [workflow@1]
version: 1
version_note: First draft. Voices calibrate, they don't gate; the channels file; copy-pastable drafts; a redirect starts fresh; voices learned from real drafts.
status: drafting
updated: 2026-11-22
sharing: public
reads: [core/user]
writes: [core/user]
protocol: []
---

# Channel voices

**Applies to:** drafting anything that leaves the sphere on a particular channel: a pull request, a review comment, a team chat message, an issue tracker comment, an email, an agenda item.

**A voice is calibration, not a gate.** It changes how a draft reads, never whether it's sent. Sending is the [outbound-guard](../human-is-highest/outbound-guard.md)'s, every time.

## Where the voices live

**`core/user/channels.md`, one section per channel,** with the cues for that channel: length, format, markup, tone. The build ships a starting set; it's the human's to change, and it grows from their real drafts. Two layers sit under every draft:

1. **The human's own voice** (`core/user/voice.md`): how they sound, on any channel.
2. **The channel's voice:** how this channel wants it.

## Drafting

- **Read both voices first.** A draft for team chat isn't a pasted email.
- **In the channel's own markup,** in a fenced code block, so it copies cleanly. Never with a leading `>`: it's hard to strip.
- **A redirect starts fresh.** *"No, a different angle"* drops the draft; don't carry its framing forward.
- **When the human edits a draft before sending,** notice what they changed. If it's a pattern (*"you always cut my first line"*), offer to add it to that channel's voice. On a yes, it's written.

## When / do

| When | Do |
|---|---|
| Drafting for a channel | Read `core/user/voice.md`, then the channel's section in `core/user/channels.md`. Draft in its markup, in a code block |
| A channel has no section yet | Draft plainly; after the human approves it, offer a section from what they kept |
| The human edits drafts the same way twice | Offer to add the pattern to that channel's voice |
| *"Different angle"* | Drop the draft; start again |

## Works with

- [outbound-guard](../human-is-highest/outbound-guard.md): how anything is sent.
- [persona](../modes/persona.md): the human's voice, and the AI's.
