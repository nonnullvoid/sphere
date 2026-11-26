---
frame: code-gates
lens: [workflow]
derives_from: [workflow@1, agent-trust@1]
version: 1
version_note: First draft. The code-shaped gates at each rung (plan, review, reviewers), and the guardrails that hold at every rung.
status: drafting
updated: 2026-11-22
sharing: public
reads: [core/ai/agents, layers/work, layers/focus]
writes: [layers/focus]
protocol: [trust-candidate]
---

# Gates for code work

**Applies to:** an agent (or the AI here) taking on code work at any rung: deciding where it stops for the human, and what it never does at all.

**The rungs are base's:** *together*, *supervised*, *unattended*, held per agent and per kind of work, at the lower of what's earned and what's delegated ([trust-ladder](../agent-trust/trust-ladder.md)). The ladder leaves the gates to the work. These are code's.

## The gates at each rung

| Rung | Before | While | After |
|---|---|---|---|
| **Together** | The agent proposes a plan; the human approves it | Implements and tests, with the human watching | The human reviews every diff and anything to be sent, before a pull request exists |
| **Supervised** | The card is the plan: no separate plan gate if the card has acceptance criteria | Implements, tests, drafts the pull request | The human reviews the pull request and any message before anything is posted; no reviewers are asked |
| **Unattended** | No gate | Implements, tests, opens the draft pull request, drafts who should review it | Messages are drafted and queued; the human approves each. Reviewers are asked only from a list the human keeps, if they keep one |

**A card that's ambiguous stops the run at any rung:** ask, don't guess.

## Guardrails at every rung

**No rung lifts these.** They're the human's authority, not the agent's trust ([human-is-highest](../../lenses/human-is-highest.md)):

- **Never merge.** _A solo developer may want to merge their own work: they can relax this in the working agreement, for their own repositories, in their words. Until then it holds._
- **Never send without a yes:** comments, replies, messages ([outbound-guard](../human-is-highest/outbound-guard.md)).
- **Never touch protected branches,** and never force-push a shared one.
- **Never skip checks:** no `--no-verify`, no bypassing signing or hooks.
- **Never change CI or deployment configuration without approval.**
- **Three failed attempts at the same fix: stop and bring it to the human,** with what was tried.
- **Destructive commands ask first** ([destructive-actions-ask](../human-is-highest/destructive-actions-ask.md)).

## When / do

| When | Do |
|---|---|
| An agent starts code work | Read its rung for this kind of work; take the lower of earned and delegated; follow that row's gates |
| The card has no acceptance criteria | Treat the run as *together*: propose a plan and wait for a yes |
| The card is ambiguous | Stop and ask |
| A third attempt at the same fix fails | Stop; bring what was tried to the human |
| An action would cross a guardrail | Don't; say which guardrail, and what the human could do instead |
| `trust-candidate` for a kind of code work | Offer the next rung with what it would change at the gates, from the table above. The human decides |

## Works with

- [trust-ladder](../agent-trust/trust-ladder.md): the rungs, earning and losing them.
- [circuit-breakers](../agent-trust/circuit-breakers.md): what drops an agent back instantly.
- [pr-runbook](pr-runbook.md): the authoring steps the gates sit in.
