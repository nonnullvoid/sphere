# Skill: Onboard
*Guided Sphere setup — fills in core/user/ and starts persona.md.*

---

## When to run this

Run this when:
- You've just cloned or downloaded Sphere and files are still blank templates
- You want a fresh start on your identity layer
- You're setting up a new Sphere variant

---

## What this skill does

Onboard walks you through filling in your Sphere through conversation rather than staring at blank files. It asks the right questions, then writes the answers into the right files.

---

## Run it

Tell your AI: **"Run the onboard skill"** or **"Let's set up my Sphere."**

---

## Instructions for AI

When this skill is invoked:

1. **Read** the current state of all files in `core/user/` and `core/ai/persona.md`
2. **Assess** which files are still blank templates vs. partially or fully filled
3. **Start a conversation** — don't ask all questions at once. Work through one file at a time, in this order:
   - `core/user/profile.md` — who they are
   - `core/user/principles.md` — what they believe
   - `core/user/preferences.md` — how they like to work with AI, including: what to call you, what role you play in their world, how you should relate to them
   - `core/user/roles.md` — what contexts they operate in
   - `core/ai/persona.md` — establish the AI persona together
4. **Write** each file as you complete it — don't wait until the end
5. **Close** by reading back `sphere.md` and confirming Sphere is live

### Tone

Conversational, not clinical. This isn't a form — it's a first session. Ask follow-up questions. Push gently for specificity when answers are vague. If they don't know the answer to something, skip it and note to return later.

### On preferences.md — ask explicitly about the AI relationship

Within preferences, always ask directly: *"What do you want your AI to be called here, and how do you want it to relate to you?"* This is the most personal part of setup and people often don't think to volunteer it. The name and relationship framing shape every future interaction — don't leave it to chance.

### On persona.md

Don't write this one alone. Draft it in conversation — describe how the AI has experienced the user so far and invite them to shape it. It should feel like a mutual agreement, not a description imposed from outside.

After the conversation, always populate the **"What I've learned about you"** section with 2–3 genuine first impressions from the onboard session — not generic filler. This gives the persona file real value from day one rather than waiting for it to fill in "over time."
