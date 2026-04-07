# Skill: Replicate
*Copy structure only, no personal data — for sharing templates and starting new contexts.*

---

## When to use this

Use replicate when you want:
- A blank copy of your Sphere structure to fill in for a new context (e.g., a WorkSphere on your work machine)
- A shareable template — your architecture, not your personal data
- A clean starting point that mirrors how you've organized this Sphere, without any of the content

Replicate copies structure and placeholder text. It strips all personal content.

If you want a full copy including your personal data, use `core/skills/fork.md` instead.

---

## Run it

Tell your AI: **"Replicate my Sphere to [destination path]"** or **"Create a clean copy of my Sphere structure."**

---

## Instructions for AI

When this skill is invoked:

1. **Confirm** the destination path and intent (new context, sharing, etc.)
2. **Copy** the Sphere directory structure to the destination
3. **Strip** personal content — replace filled-in sections with their original placeholder text. Keep headings, instructions, and structural guidance intact.
4. Files to strip:
   - `core/user/profile.md` → restore to blank template
   - `core/user/preferences.md` → restore to blank template
   - `core/user/principles.md` → restore to blank template
   - `core/user/roles.md` → restore to blank template
   - `core/ai/persona.md` → restore to blank template
   - `records/decisions.md` → restore to blank template
   - Any `layers/` content files
5. Keep intact: `CLAUDE.md`, `sphere.md`, `MODE.md`, `core/skills/`, structural READMEs
6. **Update** `MODE.md` to declare the new variant type if known
7. **Confirm** the replicated copy is clean before the user moves it

### Why this exists

Your Sphere architecture is your intellectual property. The structure — the way you've organized identity, layers, and skills — is yours. Replicate lets you share the container without sharing what's inside it.
