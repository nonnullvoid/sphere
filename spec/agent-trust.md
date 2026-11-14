# Agent trust

How an agent earns the right to do more of the work on its own, how that trust is measured and withdrawn, and how agents are put to work. This is about trust in agents. Trust between spheres is in [replication](replication.md#trusted-spheres--decided-not-yet-exercised).

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

---

## The idea

[Collaboration modes](modes.md#collaboration-modes--decided-not-yet-exercised) say who does a piece of work: the human only, together, supervised, or unattended. **Trust is what moves work along that line.** An agent that has done a kind of work well, many times, can be given more of it with less checking.

Three rules shape everything below:

1. **Trust is per agent and per kind of work.** Never global. An agent trusted to tidy notes unattended isn't thereby trusted to draft emails unattended. There's no list of kinds to choose from: what kind of work an agent does becomes clear when the human builds it.
2. **Trust is earned, and the human grants it.** Clean runs are the evidence; the human decides when the evidence is enough.
3. **Trust is revocable at any time,** by the human or by a circuit breaker.

**The guardrails don't move with trust.** However much an agent has earned, it still drafts and waits for anything that needs the human's yes. The dial moves execution, never authority (see [modes](modes.md#collaboration-modes--decided-not-yet-exercised) and [human-is-highest](../common/core/protocol/lenses/human-is-highest.md)).

---

## The trust ladder — **proven**

**The ladder is the collaboration modes.** There's no second scale.

| Rung | The agent | The human |
|---|---|---|
| **Together** | works alongside the human | sees every step as it happens |
| **Supervised** | works on its own while the human is around | checks at each gate the work defines |
| **Unattended** | works with the human away | reviews afterwards |

*Human only* isn't a rung: it's work the human keeps for themselves.

What a "gate" is depends on the kind of work. For writing, it might be the outline and the final draft. For code, a plan and a review. **Builds define the gates for the work they're built for;** the spec defines only the ladder.

### Two axes, and the lower wins

Two things decide how a particular run proceeds:

- **What the agent has earned** for this kind of work: its rung on the ladder.
- **What the human delegated** for this run: the collaboration mode they asked for.

**The run proceeds at the lower of the two.** An agent that has earned *unattended* still works *together* when the human says *"let's do this one together."* An agent that has only earned *supervised* doesn't go *unattended* just because the human has left.

---

## Earning trust — **proven**

- **Clean runs are the evidence.** A run is clean when it finished what was asked without the human having to correct it partway through. A few clean runs in a row (two or three is a reasonable start) make the agent a **candidate** for the next rung.
- **Promotion is explicit.** The sphere can say an agent is a candidate: *"The notes agent has tidied five weeks of notes cleanly. Want it to run unattended?"* **The human promotes; the sphere never does.**
- **One rung at a time.** Trust moves from *together* to *supervised* before it reaches *unattended*.
- **Trust doesn't decay on a timer.** Whether it still holds depends on the kind of work and what has changed around it: a new tech stack, a different environment. The architecture builds nothing for this. When something has changed, the human moves the agent back down.

### Reject reasons

When the human rejects or corrects a run, the reason matters:

| Reason | Counts against the agent? |
|---|---|
| **The agent got it wrong:** a mistake, a missed instruction, poor work | Yes |
| **The scope changed:** the human asked for something different partway | No |
| **A preference:** the work was fine, the human just wanted it another way | No |

Counting only the agent's own faults keeps the measure fair. An agent shouldn't lose trust because the human changed their mind.

### Circuit breakers — **proven**

Some things demote an agent **at once,** to *together*, whatever it had earned:

- **Expanding its own scope:** doing more than it was asked to
- **Drifting from the request:** doing something other than what was asked
- **Breaking a guardrail,** or trying to: sending something without approval, a destructive action without a yes
- **Skipping a check** the work requires
- **Escalating again and again** on the same thing, which means it doesn't understand the work

A circuit breaker stops the run and tells the human on the most direct channel they've set up (see [rhythm](rhythm.md#escalation-order)). Climbing back up takes clean runs, like the first time.

---

## Outcomes are a byproduct — **proven**

Every run records its outcome: clean, corrected (and why), rejected (and why), or stopped by a circuit breaker. **Recording never blocks the work.** It happens alongside, the way a focus node's history is written at ground.

Outcomes feed three things:
- **trust:** the evidence for promotion
- **a view:** how each agent is doing, for a sphere with projections
- **a signal:** an agent that keeps getting corrected for the same reason probably has a definition that needs work. That's a [reflection](evolution.md) finding, not the agent's fault.

---

## Putting an agent to work — _decided, not yet exercised_

There are two ways:

| | What happens | Good for |
|---|---|---|
| **Delegate** | The agent works its own child [focus node](focus.md), supervised. The human can attach to look in, or step in | Work the human may want to steer |
| **Dispatch** | The agent works its child focus unattended and reports back when it's done | Work the human only needs the result of |

**Checking every run is the low-trust way, not the only one.** As trust grows, dispatch becomes normal, and the human sees results instead of steps.

---

## Agents — _decided, not yet exercised_

- **Where an agent is defined follows what it's for:** an agent about the human's life is defined in their sphere; an agent about one codebase is defined with that code. **Anywhere else, it's referenced, not copied** (see [registries](registries.md)).
- **Every agent has a home in the sphere,** at least a reference, wherever its definition lives: its own file in `core/ai/agents/`, beside the personas. A generated `index.md` there lists them all (see [registries](registries.md#where-a-registry-lives--decided-not-yet-exercised)).
- **Its trust lives in that file:** the rung it has earned for each kind of work. Rungs change only on the human's say. Trust is the human's judgment of the agent, so it stays with the human even when the definition lives elsewhere.
- **Its history lives in `core/records/agents/<agent>.md`:** every run's outcome, and why each promotion or demotion happened, appended and never rewritten. It's the same pattern as a work node's `work.md` and `progress.md`: a current-state file plus a history file. Placement keeps the history private: `core/records/` never travels (see [replication](replication.md)), so an agent's file can be shared without its run history.
- **An agent's definition and its runs are different things.** The file in `core/ai/agents/` is *who* the agent is and how far it's trusted. Each run works a [focus node](focus.md), usually a child of the focus that delegated it, and its memory of that work is the node's history. The agent's own history records only outcomes and trust changes.
- **Teams are registered as they're used.** When agents work together (a pipeline, a panel, a lead with specialists), the team gets an entry once it has actually run. Shapes that haven't run yet are noted as slots, not specified in advance.

### Right-sized intelligence

**Use as much intelligence as the work needs, and no more.**
- Default to the cheaper, faster tier; reach for more when the work calls for it.
- **Skip the call entirely when there's nothing to think about.** A scheduled check that finds nothing new should cost almost nothing.
- Bound long runs, so a stuck agent stops instead of spending.

Which models fit which work changes too fast to write down here. The principle doesn't.

### Always-on agents — _planned_

Agents that watch continuously (a monitor, a standing assistant) keep the human safe by **surfacing, not by gating every action:** they act within their earned trust and report what they did. This needs trust to be proven at the lower rungs first.

---

## Senses and commands — _decided, not yet exercised_

**Senses:**
- `run-recorded`
- `trust-candidate` (an agent has enough clean runs for the next rung)
- `trust-changed` (promoted or demoted)
- `circuit-breaker-tripped`

**Commands** (natural phrasing works too):
- `let [agent] run [kind of work] unattended` / `supervised`
- `take [agent] back to together for [kind of work]`
- `how is [agent] doing?`

