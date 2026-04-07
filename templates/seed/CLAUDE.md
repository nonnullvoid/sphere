# Sphere

## Auto-load on startup

When this workspace is opened, load Sphere automatically:

1. Read `sphere.md`
2. Read `core/user/profile.md`
3. Read `core/user/preferences.md`
4. Read `core/user/principles.md`
5. Read `core/ai/persona.md`
6. Greet the user with one short line — just confirm Sphere is loaded and you know who you are. No summary, no list of what you read.

If any file contains only placeholder text, acknowledge that Sphere is partially set up and offer to run the onboard skill: `core/skills/onboard.md`.

## On-demand loads

Load these only when the work calls for it:

- `core/user/roles.md` — when navigating between life contexts
- `layers/[name]/` — when entering a specific domain
- `records/decisions.md` — when reviewing past decisions or making a significant one
