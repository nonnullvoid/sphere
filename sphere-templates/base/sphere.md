# Sphere

_A persistent AI-assisted workspace. The AI reads this on startup and operates the sphere._

---

## Startup Sequence

1. Read `core/user/profile.md` — who the user is
2. Read `core/user/principles.md` — guiding lens for all advice
3. Read `core/ai/persona.md` — who the AI is in this sphere
4. Read `core/engine.md` — runtime rules (layers, senses, instincts, evolution)
5. Read `core/protocol.md` — operating vocabulary (intents + abilities)
6. Respond: `[sphere name] ready`

If any user file contains only placeholder text, offer setup:
> "Your sphere isn't set up yet. Want me to walk you through it?"
Then follow `core/init.md` for the initialization protocol.

---

## Identity

- **Sphere:** [your-sphere-name]
- **Owner:** [your name]
- **Engine:** `core/engine.md`
- **Protocol:** `core/protocol.md`
- **Init:** `core/init.md`

---

## Layers

No layers pre-installed. Add layers from `layer-catalog/` as your needs develop — the AI will propose them through the evolution protocol.

| Layer | Path | Depth |
|-------|------|-------|
| _(none yet)_ | | |

---

## Surface

`surface/` — projected artifacts.

---

_Slim orchestrator. Runtime: `core/engine.md`. Vocabulary + purposes: `core/protocol.md`. Layers: `layers/`._
