---
frame: agent-definitions
kind: structural
lens: [agent-trust, focus]
derives_from: [agent-trust@1, focus@1]
version: 1
version_note: First draft. An agent's file and its history, where it lives, definition apart from runs, delegate and dispatch, teams, right-sized intelligence.
status: drafting
updated: 2026-11-13
sharing: public
reads: [core/ai/agents, core/records/agents, layers/focus]
writes: [core/ai/agents, core/records/agents, layers/focus]
protocol: [I-know-my-agents, A-register-agent, A-delegate, A-dispatch, A-register-team, A-list-agents, agent-registered]
---

# Agents: who they are, and what they did

**Applies to:** creating or changing an agent, putting one to work, and keeping the record of how it has done.

## Two files per agent

```
core/ai/agents/
├── index.md             generated: every agent, one line each
├── notes.md             who it is, and how far it's trusted
├── quotes.md
└── teams/               teams that have actually run, one file each
core/records/agents/
├── notes.md             every outcome and trust change, newest first
└── quotes.md
```

It's the [node shape](../nodes/node-shape.md) again: **a current-state file and a history file.**

### `core/ai/agents/<agent>.md`

```yaml
---
agent: notes
does: Tidies the week's notes into topics and flags anything that looks like a fact
source:                        # empty when it's defined here; else where its definition lives
trust:                         # earned rung per kind of work; changed only on the human's say
  tidying: unattended
  summarizing: together
tier: light                    # light | standard | deep: a hint, mapped to models by the build
---

## What it may touch

Notes in layers/knowledge/inbox. Never sends; drafts only.

## Gates

Summarizing: the outline, then the final summary.
```

- **`trust:` is the human's judgment, so it stays in the sphere,** even when the definition lives elsewhere. A kind of work that isn't listed is at *together*.
- **The rungs change only on the human's say,** or when a circuit breaker resets one ([trust-ladder](trust-ladder.md), [circuit-breakers](circuit-breakers.md)).
- **`tier:` names how much intelligence the agent's usual work needs,** not a model. *Why:* which models fit which work changes too fast to write down; the need doesn't.

### `core/records/agents/<agent>.md`

Appended, never rewritten, newest first:

```markdown
## 2026-11-12 — f31 · tidying · clean

## 2026-11-10 — trust: tidying → unattended
Five clean runs in a row. The human said yes.

## 2026-11-03 — f27 · summarizing · corrected (agent's fault)
Missed the two notes filed under travel.
```

- **One line per run:** the focus, the kind of work, the outcome, and a reason where there is one.
- **Every trust change, with why.**
- **Nothing about the work itself.** That's in the focus's history and the work's progress. *Why:* the record of an agent is about the agent; copying the work into it makes two stories that drift apart.
- **It stays private.** `core/records/` never travels (see [replication](../../../../../spec/replication.md)), so an agent's definition can be shared without its run history.

## Where an agent is defined

**Where it's defined follows what it's for:**
- **About the human's life or work across projects:** defined in the sphere.
- **About one codebase:** defined with that code, version-controlled with it. The sphere's file sets `source:` to point there and keeps only `trust:` and anything the sphere adds.

**Anywhere else, it's referenced, not copied.** Every agent has a file in `core/ai/agents/`, wherever its definition lives, so the index lists them all.

## An agent's definition is not its runs

**The definition is who the agent is.** A run is a window attached to a focus: usually a child of the focus that delegated it ([focus-tree](../focus/focus-tree.md#agents)).

- **The run's memory is the focus's history.** What it did, decided and learned is there, where the human can read it, and the next run on that focus attaches to the same memory.
- **The child's opening history entry names the agent and the kind of work,** so its outcome can be recorded against the right rung.
- **The agent's own history holds only outcomes and trust changes.**
- **The persona isn't the agent either.** A persona is who the AI is in this sphere; an agent is a defined worker with its own trust. They're kept apart (see [persona](../modes/persona.md)).

## Putting an agent to work

| | What happens | Good for |
|---|---|---|
| **Delegate** | The agent works its own child focus, *supervised*. The human can attach to look in, or step in | Work the human may want to steer |
| **Dispatch** | The agent works its child focus *unattended*, and reports back when it's done | Work the human only needs the result of |

Either way the run proceeds at the lower of what the agent has earned and what was delegated ([trust-ladder](trust-ladder.md#earned-and-delegated-the-lower-wins)). **To keep an agent going, hand it the next task on the same focus.** When the work is done, close the focus.

**Checking every run is the low-trust way, not the only one.** As trust grows, dispatch becomes normal, and the human sees results instead of steps.

## Teams

**When agents work together** (a pipeline, a panel, a lead with specialists), **the team gets a file in `core/ai/agents/teams/` once it has actually run:** its members, its shape, and what it's for. Shapes nobody has run yet are noted as slots, not specified. A team's run is a focus like any other; each member's outcome goes to that member's history.

## Right-sized intelligence

**As much intelligence as the work needs, and no more.**
- **Start from the agent's `tier:`** and reach higher only when the work calls for it.
- **Skip the call when there's nothing to think about.** A scheduled check that finds nothing new should cost almost nothing: let the tooling look first, and wake the model only when there's something to look at.
- **Bound long runs,** so a stuck agent stops and reports instead of spending.

## Always-on agents

Agents that watch continuously (a monitor, a standing assistant) keep the human safe by **surfacing, not by gating every action:** they act within their earned trust and report what they did. **They come after trust is proven at the lower rungs.** Until then, an always-on agent is a slot, not a build.

## When / do

| When | Do |
|---|---|
| The human creates an agent | Write its file with what it does and `trust:` empty; add a history entry. Rebuild the index. Fire `agent-registered` |
| An agent's definition lives with a codebase | Set `source:` to it; keep trust here; never copy the definition in |
| *"Have the notes agent do this"* (stay close) | Delegate: a supervised child focus, naming the agent and kind of work in its opening entry |
| *"Send the notes agent off to do this"* | Dispatch: an unattended child focus, reporting back when done |
| A run ends | Append one outcome line to the agent's history (see [trust-ladder](trust-ladder.md#outcomes)) |
| Agents have worked together | Offer to register the team, once it has actually run |
| An agent is corrected for the same reason again and again | Offer a [reflection](../../../../../spec/evolution.md#reflection-how-the-sphere-stays-healthy--proven) finding on its definition |
| *"What agents do I have?"* | Read the index: each agent, what it does, its rungs |

## Works with

- [trust-ladder](trust-ladder.md): the rungs in `trust:`, and the outcomes in the history.
- [focus-tree](../focus/focus-tree.md): every run is a child focus; reporting up is how it hands back.
- [kinds-of-file](../nodes/kinds-of-file.md): the definition is current state changed only on the human's say; the history is append-only.
- [outbound-guard](../human-is-highest/outbound-guard.md): agents draft and queue; they never send.

## Senses

| Sense | Fires when |
|---|---|
| `agent-registered` | a new agent's file is written |

`run-recorded` and `trust-changed` come from [trust-ladder](trust-ladder.md).
