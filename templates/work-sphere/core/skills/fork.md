# Skill: Fork
*Copy this Sphere with all personal data — for personal clones and backups.*

---

## When to use this

Use fork when you want:
- A full copy of your Sphere to move to a new machine
- A backup snapshot before a major Sphere restructure
- A personal variant — a copy you'll evolve differently (e.g., a more experimental version)

Fork copies everything: structure, content, and all your personal data.

If you want to share your Sphere template without sharing your personal data, use `core/skills/replicate.md` instead.

---

## Run it

Tell your AI: **"Fork my Sphere to [destination path]"** or **"Make a full copy of this Sphere."**

---

## Instructions for AI

When this skill is invoked:

1. **Confirm** the destination path with the user
2. **Copy** the entire Sphere directory to the destination — all files, all content
3. **Update** `MODE.md` in the fork if the user wants to declare it a different variant
4. **Optionally** create a `records/decisions.md` entry in both the original and the fork noting the fork date and reason
5. **Confirm** the fork is complete and the destination is clean

### Notes

- This is a full copy — personal data travels with it. Confirm the user understands before copying to a shared or public location.
- If copying to a work machine or semi-public location, suggest `replicate` instead.
