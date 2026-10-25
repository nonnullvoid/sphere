# Guardrails

_Status: draft 1, for review._ How a sphere keeps its AI from repeating mistakes: rules that always apply, where they come from, and how they stay few enough to follow.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

---

## The idea

Most of what a sphere learns comes from things going right. Guardrails come from things almost going wrong: a message nearly sent before it was checked, a branch that was out of date, a claim stated more strongly than the evidence allowed. Each near-miss is a chance to make sure it doesn't happen twice.

A guardrail is a **guard frame**: mechanics that apply to every action in scope, rather than being invoked for a task (see [frame kinds](protocol.md#every-skill-is-a-frame-not-every-frame-is-a-skill)). Like every frame, it derives from a lens. Usually that's the lens that says the human stays the authority, or one of the human's own principles.

In practice, this is where a long-lived sphere keeps growing after its structure settles. New lenses and frames become rare, and guardrails keep arriving, one incident at a time. — **proven**

---

## Guardrails every sphere ships with — **proven**

| Guardrail | What it does |
|---|---|
| **Outbound guard** | Anything leaving the sphere under the human's name (a message, a comment, a post, a published view) is drafted and shown first. Nothing is sent without approval, unless the human gave a standing approval for that specific kind of thing. |
| **Check before acting on shared state** | Before changing anything other people depend on, the sphere refreshes its view of it first: pull before push, re-read before overwrite. |
| **Say how sure you are** | When the sphere states something it hasn't verified, it says so. See [grades](knowledge.md#grades-and-freshness--decided-not-yet-exercised). |
| **Destructive actions ask** | Deleting, overwriting or anything hard to undo is proposed and confirmed, never just done. |

Builds add their own. A work sphere for engineers might add *draft every pull request*, *resolve automated review comments before asking for human review*, or *never paste credentials or personal data into a shared tool*. These are slots in the build, filled by the sphere's own experience.

---

## Where guardrails come from — **proven**

A guardrail is almost always born from a specific moment. The sphere captures it while the moment is fresh:

1. **Something nearly goes wrong,** or the human corrects the AI: *"don't do that,"* *"always check first."*
2. **The sphere proposes a rule.** It offers a short entry, and the human confirms it, edits it, or says no:

   > **Rule:** Re-check the base branch is current before opening a pull request.
   > **Why:** A pull request went up against a stale base and needed a rebase after review.
   > **Applies when:** opening or updating any pull request.

3. **It lands in the right place.** A narrow rule joins an existing guard frame. A rule that changes how the human thinks about something may belong in a lens instead. A one-time preference may not need to be a rule at all.

**The "why" is not optional.** A rule without its reason can't be applied well to a case nobody anticipated, and it can't be safely retired when the reason goes away.

**Confirmations count too.** When the AI makes a non-obvious call and the human says *"yes, exactly that,"* the call is worth keeping as well. A sphere that only records corrections slowly gets more timid, avoiding past mistakes but forgetting what worked.

---

## Keeping them few — _decided, not yet exercised_

Guardrails accumulate. Without care, a sphere ends up with a hundred rules, some overlapping, some contradicting each other, most never consulted. So:

- **Each guardrail records its origin and when it last applied.** One that hasn't applied in months is a candidate for review.
- **Merge before adding.** A new rule that's a special case of an existing one extends that one instead. (The usual [governance](protocol.md#governance--proven) rule: prefer updating to adding.)
- **Contradictions surface immediately.** When a new rule conflicts with an existing one, the sphere says so and asks which wins, instead of holding both.
- **Scope is explicit.** A rule about pull requests only loads when pull requests are in play, so a hundred narrow rules don't all compete for attention in every session.
- **A periodic review** (for example, alongside a monthly reflection) offers to merge, retire or sharpen rules. The human decides.

---

## The human can always override — **proven**

Guardrails exist because people, and AIs, forget in the moment. They're not there to overrule the human. When the human asks for something a guardrail covers ("just send it"), the sphere **names the guardrail once, plainly**, and then does what the human decides. It doesn't refuse, and it doesn't ask twice.

The exception is a guardrail the human has marked **hard**, such as never sharing another person's private details. For those, the human has decided in advance that the in-the-moment request doesn't win, and the sphere holds to that.

---

## Guardrails from elsewhere

Most people come to a sphere already carrying rules: instruction files, a harness's memory notes, a team's conventions. Those can be **brought in like skills**. The sphere reads them, proposes where each one belongs (an existing guard, a new one, a lens, or nowhere), and the human confirms. Afterwards the original files can stay where they are. The sphere doesn't fight a harness's own memory; it organizes it.

## What travels

**The rule travels; the incident stays home.** A guardrail's rule and its general reason can be shared with another sphere or published in a build. The specific story behind it, which often names people, projects or mistakes, stays private. See [replication](replication.md).

---

## For a non-technical human

The human never hears the word guardrail. When they say *"don't ever do that again,"* the sphere answers in plain words (*"Got it. I'll always check with you before sending anything to your family group."*) and the rule is recorded behind the scenes.

---

## Open questions

1. **Hard guardrails.** Should builds ship any guardrails as hard by default, for example around other people's private data, or should only the human ever mark one hard?
2. **Last applied.** Tracking when each guardrail last mattered needs the AI to notice when it applied one. Is that reliable enough to drive retirement, or should review be purely periodic?
3. **Importing harness memory.** Is a one-time import enough, or should the sphere keep watching the harness's memory files and offer new entries as they appear?
