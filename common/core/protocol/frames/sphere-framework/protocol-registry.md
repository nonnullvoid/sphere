---
frame: protocol-registry
kind: structural
lens: [sphere-framework]
derives_from: [sphere-framework@1]
version: 1
version_note: First draft. One registry for the sphere's vocabulary, tied to frames.
status: drafting
updated: 2026-11-12
sharing: public
reads: [core/protocol]
writes: [core/protocol/protocol.md]
protocol: [I-know-what-it-can-do, A-register-protocol, frame-shifted]
---

# The protocol registry

**Applies to:** adding, changing or retiring any frame, framing a skill, and looking up what a word or a command does.

`core/protocol/protocol.md` is the one registry of the sphere's vocabulary: everything the human can want from it, everything it can do, the words that ask for it, and the events it notices. Every row names the frame it comes from, and through that frame, its lens.

## What it lists

| Entry | Is | Named |
|---|---|---|
| **Intent** | something the human wants, steadily over time | `I-…`, in the human's terms: `I-pick-up-where-i-left-off` |
| **Ability** | something the sphere can do for an intent | `A-…`, a verb: `A-ground` |
| **Command** | the words that ask for an ability | the human's own words: *"save"*, *"where was I?"* |
| **Sense** | an event the sphere notices | a bare event name: `focus-opened` |

An instinct is an ability that runs on a sense instead of being asked for; its row names the sense.

## Rules

- **Every row names its home frame:** the frame that says how it works. Other frames that serve or vary it list it too, and the row names them all. *Why:* that's what makes a change cascade: change a frame, and you know exactly which words to revisit.
- **The registry and the frames agree, both ways.** Every entry in a frame's `protocol:` field has a row here, and every row here is listed by a frame that exists. The [manifest-check](../readable-substrate/manifest-check.md) confirms it.
- **Each entry is defined once.** A row says what the entry is in a line and points at its frame. The how stays in the frame.
- **Commands are optional.** Asking naturally always works. A fixed command is added when the human keeps using the same words, or asks for one.
- **Prefer updating to adding.** Before registering a new ability, look for one that should grow instead. A new way of doing the same thing is a variant inside its frame, not a new row.
- **Protocol travels; data stays home.** The registry holds no paths and no personal content, so it can be shared as it is, frame by frame. Private frames show only as names.

## Keeping it current

- **The AI keeps it,** in the same ground as the frame it describes. A new frame isn't usable until its rows exist.
- **A retired frame takes its rows with it,** except entries another frame still lists.
- **Framing a skill registers it:** the skill comes in unchanged as a procedure frame, and its abilities (and commands, if the human uses any) get rows. The human is offered a lens for it, and can say no.
- **A build ships a small core of senses;** a sphere adds its own as it grows.

## When / do

| When | Do |
|---|---|
| A frame is added | Add a row for each entry in its `protocol:` field, naming it as home |
| A frame changes | Fire `frame-shifted`; re-read its rows and change only what no longer follows |
| A frame is retired | Remove its rows, unless another frame lists the entry; then move its home |
| The human keeps asking with the same words | Offer them as a command. The human decides |
| Importing a skill | Frame it: copy unchanged, register its abilities, offer a lens |
| Asked "what can you do?" or "what does that word mean?" | Answer from the registry, not by reading frames |
| About to register a new ability | Check whether an existing one should grow instead |

## Works with

- [capability-manifest](capability-manifest.md): the manifest's frame triggers are this registry's commands and senses.
- [manifest-check](../readable-substrate/manifest-check.md): confirms this registry and the frames agree.
- [propose-dont-decide](../human-is-highest/propose-dont-decide.md): a new command, or a lens for a framed skill, is proposed to the human.
- [protocol](../../../../../spec/protocol.md#the-registry--proven): the vocabulary, the cascade and framing a skill, in full.

## Senses

| Sense | Fires when |
|---|---|
| `frame-shifted` | a frame changed, so the entries it defines are re-read |
