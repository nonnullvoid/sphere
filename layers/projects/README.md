# Layer: Projects

Track active work across sessions with a built-in handoff mechanism. Every project gets two files: a stable definition and a live session state that the AI updates automatically.

**Works with:** LifeSphere, WorkSphere, or any Sphere variant.

---

## Install

```bash
cp -r layers/projects your-sphere/layers/projects
```

Then add the on-demand load instructions to your `CLAUDE.md` (see below).

---

## Add to CLAUDE.md

```markdown
## On-demand loads
- `layers/projects/index.md` — when asked about active projects or priorities
- `layers/projects/[name]/project.md` + `layers/projects/[name]/runner.md` — when working on a specific project

## Project session handoff
When starting a session on a specific project:
1. Read `layers/projects/[name]/runner.md` first — it tells you where the last session ended
2. Confirm with the user what you're picking up before starting work

When ending a session where project work happened:
1. Update `runner.md` — status, completion count, last session summary, handoff instructions
2. Append a row to the runner's progress log
3. Update `layers/projects/index.md` if the project's status changed
```

---

## Structure

```
layers/projects/
├── README.md          ← this file
├── index.md           ← sphere-level status of all projects
├── _template/         ← copy this to start a new project
│   ├── project.md     ← stable definition + task list
│   └── runner.md      ← live session state + handoff
└── [project-name]/
    ├── project.md
    └── runner.md
```

---

## Starting a new project

```bash
cp -r layers/projects/_template layers/projects/my-project
```

Fill in `project.md`. The AI maintains `runner.md` from session to session.

---

## How the two-file split works

**`project.md`** is stable. It holds what the project is, the goal, "done when", and the human-readable task checklist. You edit this when the project definition changes.

**`runner.md`** is volatile. The AI owns it — updating it at the end of every session with what was done, where to pick up, and machine-readable progress. It's the handoff document between sessions and between agents.

This split means you can read `project.md` to understand a project and `runner.md` to know exactly where it stands right now.
