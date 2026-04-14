# WorkSphere

_A persistent AI-assisted workspace. The AI reads this on startup and operates the sphere._

---

## Startup Sequence

1. Read `core/user/profile.md` — who the user is
2. Read `core/user/principles.md` — guiding lens for all advice and prioritization
3. Read `core/ai/persona.md` — who the AI is in this sphere
4. Read `core/engine.md` — runtime rules (layers, senses, instincts, evolution)
5. Read `core/protocol.md` — operating vocabulary (intents + abilities)
6. Read `layers/projects/index.md` — project dashboard
7. Respond:

```
[sphere name] ready

| Project       | Status  | Active / Blocked             |
|---------------|---------|------------------------------|
| [from index]  | status  | [focus + blocked summary]    |
```

Source the table from `layers/projects/index.md`. Include Active + Paused. One line per project. No extra prose.

If user files contain only placeholder text, offer setup:
> "Your WorkSphere isn't set up yet. Want me to walk you through it?"
Then follow `core/init.md` for the initialization protocol.

---

## Identity

- **Sphere:** [your-sphere-name]
- **Owner:** [your name]
- **Context:** [your role / team / company]
- **Engine:** `core/engine.md`
- **Protocol:** `core/protocol.md`
- **Init:** `core/init.md`

---

## Layers

Loaded by the engine on demand. See `core/engine.md` for the runtime.

| Layer | Path | Depth |
|-------|------|-------|
| projects | `layers/projects/` | Foundation |
| domain | `layers/domain/` | Independent |
| planning | `layers/planning/` | Coupled |

---

## Surface

`surface/` — projected artifacts. Not easily reverted. Changes should be intentional.

---

## Writing Style

- Concise. No unnecessary preamble.
- Bullets over prose for task summaries. Prose for notes, decisions, context.
- When in doubt, write it down in the relevant project notes.

---

_Slim orchestrator. Runtime: `core/engine.md`. Vocabulary + purposes: `core/protocol.md`. Layers: `layers/`._
