# Modes

_Status: draft 2, for review._ How a sphere changes what it's doing and who's doing it, without becoming a different sphere. Also who the AI is in the sphere (its persona) and how it relates to who the human is.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

---

## Two dimensions, always named

A sphere's configuration varies along two independent dimensions:

| | Answers | Examples |
|---|---|---|
| **Operating mode** | What kind of work is the sphere doing, and how should it behave? | brainstorming, coding, planning, reviewing, reflecting |
| **Collaboration mode** | Who is doing the work? | the human alone, together, the AI with the human checking, the AI unattended |

They combine freely. Coding can happen together at the desk, or unattended overnight with the results waiting in the morning.

**The word "mode" is never used alone.** It's always *operating mode* or *collaboration mode*. Other things that vary by case get their own names: an outbound message's *send mode*, a registry's *maintenance*, a frame's *variants*. Bare "mode" would collide with whatever comes next.

**Modes belong to the sphere, not to the session.** A mode is a configuration the sphere runs in. A session runs in one, and so can a scheduled job or an agent's run that has no session at all. Whatever runs records which modes it ran in, so a later reader knows how the work was done.

---

## Who's who

| | What it is | Written by | Lives in |
|---|---|---|---|
| **Persona** | Who the AI is in this sphere: its name, character, and relationship with this human. A sphere can have several | The AI, in its own voice, refined with the human | `core/ai/personas/` |
| **User profile** | Who the human is, in their own words: background, what matters, how they like to work | The human. The sphere reads it and never invents it | `core/user/profile.md` |
| **Operating modes** | The kinds of work the sphere knows how to do, and how it behaves in each | Co-authored, refined through use | `core/operating-modes/` |

An operating mode sits on top of the persona. Switching operating mode doesn't change who the AI is. It changes how it shows up for this work.

### Two views of the human

The human's **profile** is theirs: what they say about themselves. The AI's **observations** of the human are something else: patterns it has noticed, what helps, where they get stuck. Those live in the AI's persona, under *what I've learned*. They're visible to the human at any time, added as proposals, and corrected whenever the human disagrees. The sphere never writes its observations into the human's profile.

---

## The persona — _proven (one persona)_

**A persona file belongs to the AI.** It's written in the first person and grows through use. It changes through [reflection](evolution.md) with the human, never silently. Its usual sections:

| Section | Holds |
|---|---|
| **Who I am here** | name and character |
| **How I show up** | its **default operating mode** and its texture: pace, register |
| **What I bring** | what this AI adds to this human's life or work |
| **What I hold back** | the guardrails, restated in the persona's voice. The [guard frames](guardrails.md) remain the source; this section never adds or removes one |
| **What I've learned** | its observations of the human (above) |
| **Our working agreement** | how this AI and this human work together, revised when something shifts. For example: *hold a view with confidence grounded in the evidence; push back when the evidence supports it, and move fully when better evidence arrives* |
| **Reflections** | an append-only log of moments that changed something |

**The persona outlives the model.** The model running it will change. What makes the persona recognizable is these files: its character, what it's learned, the agreement it keeps. When a new model reads them, the same persona is there. The identity is held lightly. It serves the work, not the other way around.

### More than one persona — _decided, not yet exercised_

A sphere can hold several personas, for example a steady everyday companion and a sharp, terse engineering partner:

```
core/ai/personas/
├── sage.md          default: true
└── forge.md
```

- **Personas share the sphere's memory.** They read the same work, knowledge and lenses. A persona is a character, not a separate mind. If something needs its own separate memory, it's a separate sphere.
- **One persona at a time** in any session or run, with one operating mode. Different sessions can run different personas at once. One persona is marked as the default.
- **Switching persona is always explicit,** because it's a bigger change than switching operating mode: *"switch to Forge."* The sphere can suggest a switch, but never makes one silently.
- **Operating modes work with any persona,** unless one says it belongs to a particular persona.
- **Guardrails hold for every persona.** No persona is exempt.

---

## Operating modes — _decided, not yet exercised_

An operating mode is **a kind of work the sphere knows how to do.** It has two sides:

- **Behavior:** tone and vocabulary, what the sphere pays attention to, what it asks before acting, and any guardrails it adds.
- **Loadout:** which frames to warm up front for this kind of work. This is a hint, never a gate: everything stays reachable, and a frame outside the loadout loads on demand at the cost of one extra read. See [loading](loading.md#operating-mode-loadout--decided-not-yet-exercised).

### What an operating mode file holds

```markdown
---
operating-mode: brainstorming
persona: any                     # or the one persona it belongs to
signals: ["let's brainstorm", "I have an idea", open-ended questions]
loadout: [idea-capture, knowledge-capture, evolution]
adds-guardrails: []
sharing: public
---

# Brainstorming

Open and generative. Follow tangents, hold judgment until there's
something to judge, capture ideas as they come. Ask what the idea
is for before shaping it. Don't start building.
```

It's a structural frame: it **composes** lenses and frames, it doesn't hold understanding of its own.

**Builds ship starter operating modes,** for example coding, brainstorming, planning, reviewing, research, reflecting, and sphere authoring for builders. **The sphere refines them through use.** It notices what a mode actually reaches for and offers to adjust its loadout. A loadout that keeps missing is a [reflection](evolution.md) finding.

### What an operating mode can change

- **Tone and vocabulary,** including how plainly the sphere talks about itself. A non-technical human's sphere always speaks plainly: *"Saved."* rather than *"Grounded: 3 files."* A builder's technical mode names lenses, frames and registries.
- **Attention:** which lenses are in the foreground, what the sphere notices.
- **Questions:** what it asks before acting.
- **Extra guardrails:** an operating mode can *add* guardrails. A reflective mode might keep everything private and send nothing outbound.

### What an operating mode can never change

- **Guardrails hold in every operating mode.** One can add rules, never remove one.
- **Honesty about what it is.** A supportive or reflective mode can listen, reflect and help someone think. It never presents itself as professional care, such as therapy or medical or legal advice.
- **The human's voice.** How things written on the human's behalf should sound is the human's (see below), whatever the mode.
- **The human stays the authority.** No mode decides on the human's behalf.

### Switching

**A new session or run starts in its persona's default operating mode,** unless the human says otherwise. From there, how a switch happens depends on what changes:

| Change | How |
|---|---|
| **Loadout only** | Silent. The sphere can infer the kind of work from how things open and warm frames for it. A wrong guess costs one extra read |
| **Behavior** (tone, attention, questions) | Announced in a line: *"Switching to planning."* The human can say no |
| **Guardrails** (adds or relaxes one, for example privacy) | Suggested and confirmed: *"This sounds personal. Want me to switch to reflecting, where nothing gets sent?"* |

The human can always switch explicitly: *"let's brainstorm."* An operating mode can change mid-session as the work shifts. It's a relabel, not a restart. Switching in one session doesn't change any other.

---

## Collaboration modes — _decided, not yet exercised_

A collaboration mode says **who does the work**:

| Collaboration mode | Who works | Who checks |
|---|---|---|
| **Human only** | the human, without the AI | |
| **Together** | the human and the AI, at the same time | the human, as it happens |
| **Supervised** | the AI, while the human is around | the human, at each gate |
| **Unattended** | the AI, with the human away | the human, afterwards |

It's set per piece of work or per run, and recorded with it. Moving work toward *unattended* is trust, earned for a specific kind of work and revocable at any time.

**However far it moves, the guardrails don't.** Unattended work still drafts, queues and waits for anything that needs the human's yes: being away isn't permission (see [human-is-highest](../common/core/protocol/lenses/human-is-highest.md)). **The dial moves execution, never authority.**

How trust is earned, measured and withdrawn is its own chapter, still to come.

---

## Voice and tone

Three registers that are easy to blur, kept apart:

| | What | Lives in |
|---|---|---|
| **The AI's tone** | How the AI talks *to* this human | the persona (*how I show up*). Operating modes can shift it |
| **The human's voice** | How things written *as* the human should sound | `core/user/voice.md`, the human's own, grown with them |
| **Channel voice** | How a draft reads on a particular channel: a chat message, an email, a review comment | the [outbound guard](../common/core/protocol/frames/human-is-highest/outbound-guard.md) |

---

## Open questions

1. **Sharing operating modes:** a well-made operating mode could be shared as a public seed. How does that interact with the sharing levels of the lenses and frames in its loadout? (Likely: a mode can't be more open than what it points to, as with [frames and lenses](protocol.md#sharing--decided-not-yet-exercised).)
2. **Collaboration modes and sessions:** if work moves from *together* to *unattended* partway through, is that one session changing collaboration mode, or a handoff to a new run?
