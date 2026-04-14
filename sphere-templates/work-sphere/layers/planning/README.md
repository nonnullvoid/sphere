# Layer: Planning

## Identity
- **Name:** planning
- **Depth:** coupled
- **Dependencies:** `projects`
- **Senses:** `session-start` (read goals + today's priorities), `day-planned` (update plan state), `day-wrapped` (write EOD notes), `project-grounded` (update daily log)
- **Data paths:** `layers/planning/`
- **Init:** Fill in `goals.md` with your current goals and near-term priorities. The AI will maintain `today.md` and `log/` from there.

---

Daily rhythm and planning context — goals, today's priorities, EOD notes, and the structured rituals that keep work oriented across days.

This layer powers the Day Planning ability. Without it, commands like `plan my day` and `wrap up my day` are dormant. With it, every session starts and ends with intention.

---

## Basic Abilities

_The starting capabilities this layer ships with._

| Command | What it does |
|---------|-------------|
| `plan my day` | Read goals + project index → draft today's priorities |
| `start my day` | Read goals + latest plan → what to work on now |
| `wrap up my day` | Ground all touched projects → write EOD notes |
| `what's on my plate?` | Summarize all active/blocked work and open tasks |
| `catch me up` | Full situational summary across all projects |
| `what should I work on?` | Recommend highest-leverage action right now |

---

## What lives here

```
layers/planning/
├── README.md        ← this file
├── goals.md         ← current goals and priorities (you maintain)
├── today.md         ← today's plan (AI maintains each day)
└── log/             ← EOD notes, one file per day (AI maintains)
    └── YYYY-MM-DD.md
```

---

## What to fill in

**`goals.md`** — your current goals and near-term priorities. Keep it honest and current. The AI uses this when planning your day and recommending what to work on.

Example structure:
```markdown
# Goals

## This quarter
- [goal one]
- [goal two]

## This week
- [what you're trying to accomplish this week]

## Current priorities
P1: [most important thing]
P2: [second most important]
P3: [everything else]
```

---

## When the AI loads this layer

- Load `goals.md` + `today.md` on `session-start` (after reading project index)
- Update `today.md` when `plan my day` or `start my day` is invoked
- Append to `log/YYYY-MM-DD.md` when `wrap up my day` is invoked
- Load `goals.md` when recommending what to work on
- Fire on `day-planned` and `day-wrapped` senses from projects layer

---

_This layer is a skeleton. As you use it, the AI will propose evolving the planning structure based on what patterns emerge from your actual workflow._
