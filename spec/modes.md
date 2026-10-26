# Modes

_Status: draft 1, for review._ How a sphere changes the way it talks and acts, quickly, without becoming a different sphere: a technical mode for work, a social mode for planning a weekend, a reflective mode for thinking something through.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

---

## Persona and modes

Three things, kept distinct:

| | What it is | Changes | Lives in |
|---|---|---|---|
| **Persona** | Who the AI is in this sphere: its name, character, its relationship with this human. A sphere can have several. | Rarely, deliberately | `core/ai/personas/` |
| **User persona** | Who the human is: their background, what matters to them, how they like to work | As the human changes | `core/user/persona.md` |
| **Mode** | How the AI behaves right now: tone, what it pays attention to, which lenses and frames it leans on, what it asks | Often, by switching | `core/modes/` |

A mode sits on top of the persona. Switching mode doesn't change who the AI is. It changes how it shows up in this moment.

## More than one persona — _decided, not yet exercised_

A sphere can hold several AI personas, for example a steady everyday companion and a sharp, terse engineering partner, each with its own name and character:

```
core/ai/personas/
├── sage.md          default: true
└── forge.md
```

- **Personas share the sphere's memory.** They read the same work, knowledge and lenses. A persona is a character, not a separate mind. If something needs its own separate memory, it's a separate sphere.
- **One persona is active per session.** Each session has exactly one persona and one mode at a time. Different sessions can run different personas and modes at once, for example a terse engineering persona in one window and a reflective mode in another. One persona is marked as the default, and a new session starts with it.
- **Switching persona is always explicit,** because it's a bigger change than switching mode: *"switch to Forge."* The sphere can suggest a switch, but never makes one silently.
- **Modes work with any persona,** unless a mode says it belongs to one.
- **Guardrails hold for every persona.** No persona is exempt.
- **Records say who was speaking.** Each [session file](state.md#level-1--simple-sessions-the-default--proven) notes which persona and mode were active, so a later reader knows who said what.

A sphere with one persona simply has one file in `core/ai/personas/`.

## What a mode can change — _to be designed_

- **Tone and vocabulary,** including how plainly the sphere talks about itself. A non-technical human's sphere always speaks plainly: *"Saved."* rather than *"Grounded: 3 files."* A builder's technical mode names lenses, frames and registries.
- **Attention:** which lenses are foregrounded, which frames are likely to apply, what the sphere notices.
- **Questions:** what it asks before acting.
- **Extra guardrails:** a mode can *add* guardrails. A reflective mode might keep everything private and send nothing outbound.

## What a mode can never change

- **Guardrails hold in every mode.** A mode can add rules, never remove one.
- **Honesty about what it is.** A supportive or reflective mode can listen, reflect and help someone think. It never presents itself as professional care, such as therapy or medical or legal advice.
- **The human stays the authority.** No mode decides on the human's behalf.

## Switching — _to be designed_

- **Explicit:** *"switch to social mode."*
- **Suggested and confirmed:** *"This sounds personal. Want me to switch to the reflective mode?"* The sphere never switches silently.
- A mode belongs to the session it was chosen in, and lasts for that session unless the human says otherwise. Switching mode in one session doesn't change any other session.

---

## Open questions

1. **What a mode file holds** _(Rutvij to verify)_: a short description plus pointers to the lenses and frames it emphasizes? Or something closer to a lens of its own?
2. **Modes and sharing:** can a mode be shared as a public seed (a well-made "focused work" mode), and how does that interact with the sharing levels of the lenses it points at?
