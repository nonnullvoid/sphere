# Core

_The plug-and-play sphere mechanism. Take this, add layers, and you have a sphere._

---

Three files run the sphere:

- `engine.md` — how the sphere works: layer loading, senses, instincts, evolution, state machine
- `intents.md` — why the sphere exists: the stable purposes abilities serve
- `abilities.md` — what the sphere can do: the command vocabulary

Two identity directories:

- `user/` — who you are: profile, principles, preferences, roles
- `ai/` — who the AI is in this sphere: persona, working style, learned behaviors

---

## How to use this

**Starting from scratch:** Clone this `core/` directory into your sphere root, fill in `user/` files, and you have a working sphere. Add layers from `layer-catalog/` as your needs develop.

**Starting from a template:** The `sphere-templates/` directory has pre-assembled spheres with layers already chosen. Use those for a faster start.

---

## What belongs here vs. in layers

`core/` holds sphere-level identity and the runtime mechanism — things that apply to every session regardless of what you're working on. Layer files hold domain-specific data and actions. The split is: if it's about who you are and how the sphere runs, it's in `core/`. If it's about a specific area of work, it's in a layer.
