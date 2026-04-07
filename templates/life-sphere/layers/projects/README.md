# Layer: Projects

Active projects — the work you're driving across all life contexts.

Each project lives in its own subdirectory with two files:
- `project.md` — stable definition: what it is, goal, human-readable task list
- `runner.md` — volatile session state: what was done last session, where to pick up, machine-readable progress

This two-file split means the project definition stays clean while session handoffs happen in a separate file the AI updates automatically.

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

Then fill in `project.md`. The AI will maintain `runner.md` from session to session.

---

## When the AI loads this layer

- Load `index.md` when asked about current projects or priorities
- Load `[project]/project.md` + `[project]/runner.md` when working on a specific project
- Update `runner.md` at the end of any session where project work happened
- Update `index.md` when a project's status changes
