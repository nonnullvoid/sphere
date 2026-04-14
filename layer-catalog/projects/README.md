# Layer: Projects

## Identity
- **Name:** projects
- **Depth:** foundation
- **Dependencies:** none
- **Senses:** `session-start` (check for in-progress runners), `session-end` (update runner + progress log), `status-mentioned` (passive sync)
- **Data paths:** `layers/projects/`
- **Init:** Copy `_template/` to start a new project. Fill in `project.md`. AI maintains `runner.md`.

---

Track active work across sessions with a built-in handoff mechanism. Every project gets two files: a stable definition (`project.md`) and a live session state (`runner.md`) that the AI updates automatically.

**Works with:** any sphere variant.

---

## Basic Abilities

_The starting capabilities this layer ships with._

| Command | What it does |
|---------|-------------|
| `pull [project]` | Fetch updates from external sources → update tasks, status |
| `ground [project]` | Persist session knowledge to project files (the cold-start engine) |
| `sync [project]` | `pull` then `ground` in sequence |
| `peek [project]` | Quick status card — no full context load |
| `open [project]` | Full context load. Set as active project. |
| `close [project]` | Auto-ground + mark inactive for session |
| `resume [project]` | `open` + orientation briefing from latest session log |
| `new project [name]` | Create a new project from `_template/` |
| `project status` | Summary of all active projects |

---

## Install

```bash
cp -r layer-catalog/projects your-sphere/layers/projects
```

Register in `sphere.md`:

```markdown
| projects | `layers/projects/` | Foundation |
```

---

## Structure

```
layers/projects/
├── index.md              ← sphere-level status of all active projects
├── _template/            ← copy this to start a new project
│   ├── project.md        ← stable definition + task list
│   └── runner.md         ← live session state + handoff
└── [project-name]/
    ├── project.md
    └── runner.md
```

---

## How the two-file split works

**`project.md`** is stable. It holds what the project is, the goal, "done when", and the human-readable task checklist. You edit this when the project definition changes.

**`runner.md`** is volatile. The AI owns it — updating it at the end of every session with what was done, where to pick up, and machine-readable progress. It's the handoff document between sessions.

---

## When the AI loads this layer

- Load `index.md` on `session-start` and when asked about current work or priorities
- Load `[project]/project.md` + `[project]/runner.md` when working on a specific project
- Update `runner.md` at the end of any session where project work happened
- Update `index.md` when a project's status changes
