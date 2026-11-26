---
lens: workflow
version: 1
version_note: First draft. A workflow is a named, repeatable runbook; it composes gates rather than sitting under one; modes live inside it.
derives_from: practice in an engineering sphere in daily use, made generic
status: drafting
updated: 2026-11-22
verified: false
sharing: public
frames: [pr-runbook, code-gates, worktree-lanes, channel-voices, meeting-readiness, meeting-consumption]
---

# Workflows

**The sphere doesn't only understand things; it runs procedures.** Opening a pull request, reviewing one, switching branches safely, turning a meeting into knowledge: each is a named, repeatable runbook that wires tools, other lenses and the human's gates into *how we actually do this, end to end*. This lens is their home.

## What a workflow is

**A concrete procedure for a recurring job,** usually across several tools, often with steps and modes, sometimes with a script. Three things it isn't:

- **Not a capability.** Drafting a description is one ability; the PR runbook is the procedure that uses it with tests, screenshots and the human's go.
- **Not a discipline.** [Agentic engineering](agentic-engineering.md) is a way of working applied to everything. A workflow is a specific procedure run on purpose. It applies the discipline; it doesn't define it.
- **Not a store.** What a runbook keeps (review notes, meeting records, the agenda) lives in `layers/workflows/`, and any script it runs lives there too. The runbook itself lives here.

## Workflows compose gates

**A runbook sits above the lenses it wires together, never under one of them.** The PR runbook uses the human's gate (drafts only, nothing sent without a yes), engineering discipline (how the work is done well) and the outbound guard (how anything leaves). Filing it under any one of them would flatten it into a child of that one.

**The gate stays where it lives.** A runbook never restates a guardrail or loosens it. It names the step where the guardrail applies, and the guardrail's own frame decides: [outbound-guard](../frames/human-is-highest/outbound-guard.md) for anything sent, [destructive-actions-ask](../frames/human-is-highest/destructive-actions-ask.md) for anything that can't be undone.

## Modes live inside a workflow

**One runbook can be run in more than one way:** a review is quick-and-post, or a walkthrough to understand; worktrees are set up to build, or to review. These are sections of one frame, not separate frames. The human says which, or the sphere proposes the one that fits and says why.

## What follows from it

| Frame | In short |
|---|---|
| [pr-runbook](../frames/workflow/pr-runbook.md) | Authoring a pull request (draft, finalize, open as a draft on the human's go), reviewing one (quick, or a walkthrough), the review's lifecycle, and a read-only roll-up |
| [code-gates](../frames/workflow/code-gates.md) | The gates code work passes at each trust rung, and the guardrails that hold at every rung |
| [worktree-lanes](../frames/workflow/worktree-lanes.md) | Where worktrees live, dev and review modes, and the pre-flight before any switch |
| [channel-voices](../frames/workflow/channel-voices.md) | How a draft reads on each channel: a pull request, a review comment, team chat, the issue tracker, email, an agenda |
| [meeting-readiness](../frames/workflow/meeting-readiness.md) | Walking into meetings prepared: the agenda, and the calendar at the day's anchors |
| [meeting-consumption](../frames/workflow/meeting-consumption.md) | Turning a meeting into knowledge and work: consume, extract, propose, the human fills the gaps, assimilate |

## Revision history

- **v1:** First draft.
