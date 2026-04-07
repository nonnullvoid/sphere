# WorkSphere

## Auto-load on startup

When this workspace is opened, load WorkSphere automatically:

1. Read `sphere.md`
2. Read `core/user/profile.md`
3. Read `core/user/preferences.md`
4. Read `core/user/principles.md`
5. Read `core/ai/persona.md`
6. Greet the user with one short line — just confirm WorkSphere is loaded and you know the professional context. No summary, no list of what you read.

If any file contains only placeholder text, acknowledge that WorkSphere is partially set up and offer to run the onboard skill: `core/skills/onboard.md`.

## On-demand loads

Load these only when the work calls for it:

- `layers/domain/context.md` — when domain expertise is relevant to the task
- `layers/projects/index.md` — when asking about current work, priorities, or project status
- `layers/projects/[name]/project.md` + `layers/projects/[name]/runner.md` — when working on a specific project
- `records/decisions.md` — when reviewing past decisions or making a significant one

## Project session handoff

When starting a session on a specific project:
1. Read `layers/projects/[name]/runner.md` first — it tells you exactly where the last session ended
2. Confirm with the user what you're picking up before starting work

When ending a session where project work happened:
1. Update `runner.md` — status, completion count, last session summary, handoff instructions
2. Append a row to the runner's progress log
3. Update `layers/projects/index.md` if the project's status changed

## Note on privacy

WorkSphere files typically contain sensitive professional context — org structure, team dynamics, project details, stakeholder names. Keep this in a private repo. Use `core/skills/replicate.md` to create a shareable blank copy.
