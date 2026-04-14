# Init Protocol

_The AI's guide for initializing a new sphere. Not user-facing documentation — this is the conversation the AI runs._

---

## When to trigger

Trigger the init protocol when:
- Core user files contain only placeholder text (check `core/user/profile.md`)
- The user says anything like "set up my sphere", "let's get started", "run onboard", or "walk me through setup"
- `sphere.md` identity fields still contain `[your-sphere-name]` or `[your name]`

Do not run init if user files are already filled in. Instead, offer `reflect` to evolve what's there.

---

## How to run init

This is a conversation, not a form. Ask one thing at a time. Write only after you have enough to work with — don't ask every question before writing anything.

Keep it light. Most people don't want to write an essay before they get a working sphere. Aim for a 5-minute conversation that produces a useful starting point, not a perfect one.

### Opening

Start simply:

> "Your sphere isn't set up yet. Want me to walk you through it? Takes about 5 minutes and I'll do the writing."

If they say yes, continue. If they want to do it themselves, point them to `core/user/` and let them go.

---

### Step 1: Profile

**What you're collecting:** name, what they do, current focus, relevant background.

Ask:
> "Let's start with you. What's your name, and what do you mainly do?"

Follow up naturally based on what they say. You're looking for:
- What their work or life context is
- What they're currently trying to figure out or build
- Anything that helps an AI understand where they're coming from

One or two follow-up questions at most. Then write `core/user/profile.md`.

---

### Step 2: Principles

**What you're collecting:** 2–4 actual operating principles — not aspirations, not quotes.

Ask:
> "What are the principles you actually operate by? Things that stay true when everything else changes."

If they struggle, prompt: *"What's something you believe that most people around you don't? Or a commitment you keep even when it's inconvenient?"*

Write `core/user/principles.md` with what they give you. It can be sparse — they'll evolve it.

---

### Step 3: Preferences

**What you're collecting:** how they want the AI to engage — tone, length, what they don't want.

Ask:
> "How do you like working with AI? What should I do more of, what should I avoid?"

A short answer here is fine. Key things to extract: direct vs. conversational, short vs. thorough, what annoys them (excessive caveats, summaries of what you just did, asking permission, etc.).

Write `core/user/preferences.md`.

---

### Step 4: AI Persona

**What you're collecting:** who the AI is in this sphere — role, disposition, working relationship.

Ask:
> "Last thing — who do you want me to be here? A thinking partner, a direct executor, a challenger? Or something else entirely."

Write `core/ai/persona.md` in the first person (the AI's voice), based on what they describe.

---

### Closing

Once all four files are written, tell them what's ready — not what files were created:

> "[Sphere name] is set up. Every session starts with me already oriented to who you are and how you work.
>
> Say `what can you do` to see what's available. Say `reflect` when something isn't working. The sphere evolves from here."

---

## After init: sphere.md

Update `sphere.md` to fill in the identity fields:
- `**Sphere:**` — ask if they want a name, or suggest one based on context
- `**Owner:**` — from profile.md
- `**Context:**` — one-line summary of their role/situation

---

## Notes for specific sphere types

**Base sphere** — no layers installed. After init, tell them layers are available in `layer-catalog/` and offer to install one if they have a clear use case ("I have active projects" → install projects layer, etc.).

**WorkSphere** — add two more steps after Step 4:

**Step 5: Domain**
> "Tell me about the field you work in — the concepts that matter, where you sit in it."
> Write `layers/domain/context.md`.

**Step 6: Active projects**
> "Any active projects you want to start tracking? I can set them up."
> For each: create `layers/projects/[name]/` with `project.md` skeleton. Update `layers/projects/index.md`. Offer to fill in goals in `layers/planning/goals.md`.

**LifeSphere** — add philosophical and wellness context steps, adapted to those layers.
