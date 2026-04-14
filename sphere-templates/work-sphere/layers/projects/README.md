# Layer: Projects

## Identity
- **Name:** projects
- **Depth:** foundation
- **Dependencies:** none
- **Senses:** `session-start` (read index, build startup table), `session-end` (update runner + progress log), `status-mentioned` (passive sync)
- **Data paths:** `layers/projects/`
- **Init:** Copy `_template/` to start a new project. Fill in `project.md`. AI maintains `runner.md`.

---

Active professional work — what's in flight, what's next, and where each project stands.

Each project lives in its own subdirectory with two files:
- `project.md` — stable definition: what it is, goal, human-readable task list
- `runner.md` — volatile session state: what was done last session, where to pick up, machine-readable progress

This split keeps the project definition stable while session handoffs happen in a separate file the AI maintains automatically.

---

## What lives here

```
layers/projects/
├── index.md              ← sphere-level status of all active projects
├── _template/            ← copy this to start a new project
│   ├── project.md
│   └── runner.md
└── [project-name]/
    ├── project.md
    └── runner.md
```

---

## Starting a new project

```bash
cp -r layers/projects/_template layers/projects/my-project
```

Fill in `project.md`. The AI maintains `runner.md` each session.

---

## When the AI loads this layer

- Load `index.md` at `session-start` → render the startup status table
- Load `[project]/project.md` + `[project]/runner.md` when working on a specific project
- Update `runner.md` at the end of any session where project work happened
- Update `index.md` when a project's status changes
- Fire passive sync when a status change is mentioned in conversation
