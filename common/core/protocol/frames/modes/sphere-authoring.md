---
frame: sphere-authoring
kind: guard
lens: [modes, human-is-highest]
derives_from: [modes@1, human-is-highest@2]
version: 1
version_note: First draft. Internals change only here; human-started, each edit shown and confirmed, recorded with its reason, never unattended.
status: drafting
updated: 2026-11-13
sharing: public
reads: [core/protocol, core/operating-modes, core/ai/personas, layers/ideas]
writes: [core/protocol, core/operating-modes, core/ai/personas, layers/ideas, layers/focus]
protocol: [I-nothing-changes-without-me, A-author-sphere, A-propose-sphere-change, sphere-authoring-started, sphere-authoring-ended]
---

# Sphere authoring

**Applies to:** every change to the sphere's internals:
- its lenses, frames and guardrails
- its operating-mode files
- its personas
- the shape of its registries: which keys a node has, which values a key may take

**Doesn't apply to** the sphere's notes and records (work, foci, history, generated views). The sphere keeps those current without asking, as always. Facts entering knowledge have their own rule ([propose-dont-decide](../human-is-highest/propose-dont-decide.md)).

**Sphere authoring widens what can change. It never widens who decides.**

## Outside sphere authoring, internals are read-only

The sphere can still notice that a lens is off, a frame is awkward, a guardrail should change. **It writes that down as an idea in the [`sphere` collection](../idea-capture/idea-nodes.md#the-spheres-own-collection),** with what it noticed and why, and leaves the file alone. The next reflection, or the next time the human starts sphere authoring, picks it up.

**Capturing a rule in the moment doesn't need a switch.** When something nearly goes wrong and the human says yes to a proposed rule ([where guardrails come from](../../../../../spec/guardrails.md#where-guardrails-come-from--proven)), that yes counts as a brief step into sphere authoring, for that one change only.

## Starting and ending

- **Only the human starts it:** *"let's work on the sphere"*, *"I want to change how ideas work."* **The sphere never infers it and never suggests switching into it.** *Why:* the one operating mode that can rewrite the rules must never be one the AI talks its way into.
- **It's recorded like any operating mode,** in the focus's `operating-mode:`, and the history entry that starts it names the operating mode it came from.
- **It ends when the window detaches,** or when the human says so. The ground on the way out sets `operating-mode:` back to the one it came from. **It never carries over:** a new window attaching to the same focus starts outside it.

## Every change is shown and confirmed

1. **Re-read the file.** Internals are reference files: someone may have changed them since.
2. **Show the change:** what's there, what it would become, and why. One change at a time.
3. **Wait for a yes.** A yes to one change is not a yes to the next.
4. **Apply exactly what was approved.** If anything changes after the yes, show it again.
5. **Record it.** A substantive change to a lens or frame bumps its `version`, says what changed in `version_note`, and adds a line to its revision history. A changed lens fires `lens-shifted`, so the frames derived from it are re-read; a changed frame fires `frame-shifted` (see [protocol](../../../../../spec/protocol.md#cascade--proven)). The ground's history entry lists each change and its reason.

**The AI never approves its own change** (see [evaluator-not-self](../human-is-highest/evaluator-not-self.md)). Drafting a whole new frame is fine; accepting it is the human's.

## Never unattended

**Sphere authoring runs only *together* or *supervised*.**
- **Supervised:** the AI prepares changes on its own and brings each to the human at a gate, before it's applied.
- **Unattended work never applies a change to internals,** whatever its trust. It can queue one: an idea in the `sphere` collection, or an offer in its own history (see [focus-tree](../focus/focus-tree.md#reporting-up)), the same way agents queue drafts and never send.

## Nothing is suspended

**While sphere authoring runs, every guardrail still holds.** It isn't a way to switch a rule off for a moment: that's never possible. It's where the human deliberately rewrites a rule, which is always their right.

- **A rule the human marked firm** can be changed here, by the human, as a change to the rule. It's never relaxed in passing.
- **An operating mode still can't remove a guardrail.** Changing a guardrail is an edit to the guardrail, made here, not a property of an operating mode.

## Never

- Entering sphere authoring on the sphere's own initiative, or suggesting it.
- Applying several changes under one yes.
- Editing a lens, frame, guardrail, operating-mode file or persona outside it, beyond the one-entry rule capture above.
- Carrying it into the next window.
- Applying a change to internals from unattended work.

## When / do

| When | Do |
|---|---|
| The human says they want to work on the sphere itself | Switch to sphere authoring; note the operating mode it came from. Fire `sphere-authoring-started` |
| Outside it, something in the internals looks wrong | Capture an idea in the `sphere` collection; leave the file alone |
| A correction yields a rule, and the human says yes | Apply that one entry; nothing else |
| Inside it, a change is ready | Re-read, show what's there and what it would become, wait for a yes, apply, record |
| A lens changed | Bump it, note it, fire `lens-shifted` |
| A frame changed | Bump it, note it, fire `frame-shifted` |
| An unattended run wants a change to internals | Queue it as an idea or an offer; never apply it |
| The window detaches, or the human says they're done | Ground, set the operating mode back, end it. Fire `sphere-authoring-ended` |

## Works with

- [propose-dont-decide](../human-is-highest/propose-dont-decide.md): changes to what the sphere believes are proposals; this frame is where the approved ones are applied.
- [operating-modes](operating-modes.md): sphere authoring is one of them, and the only one never inferred.
- [kinds-of-file](../nodes/kinds-of-file.md): internals are reference files, changed one confirmed edit at a time.
- [idea-nodes](../idea-capture/idea-nodes.md): where noticed changes wait.

## Senses

| Sense | Fires when |
|---|---|
| `sphere-authoring-started` | the human starts sphere authoring in a focus |
| `sphere-authoring-ended` | it ends, at detach or on the human's word |

`lens-shifted` and `frame-shifted` come from the protocol itself.
