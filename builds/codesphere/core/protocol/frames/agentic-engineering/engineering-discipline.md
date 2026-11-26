---
frame: engineering-discipline
lens: [agentic-engineering]
derives_from: [agentic-engineering@1]
version: 1
version_note: First draft. Trace the full flow, map categories before searching, external evaluation, naming as an example convention; surfaced briefly, never a gate.
status: drafting
updated: 2026-11-22
sharing: public
reads: [layers/knowledge, layers/work]
writes: []
protocol: []
---

# Engineering discipline

**Applies to:** a fix about to be placed in one spot, research that starts from a product's name, a result about to be accepted on its own author's say-so, and naming a test, fixture or file.

**One question:** what does an engineer owe a piece of work upstream of the obvious change?

## Trace the full flow

**Before a local fix, trace the path:** where does the data enter, where does it land, where is it consumed? Then fix where the problem starts, not where it shows. A validation bug that shows up in a screen often starts at the input; fixing it at the screen leaves every other consumer broken.

## Map the categories before searching

**When looking for a tool, a library or an approach, sketch the categories first,** then search inside each. Categories are the job to be done crossed with where answers live: package registries, code search, issue trackers, papers, forums. Starting from one product's name gives narrow, biased results and misses the space.

## Never accept on self-evaluation alone

**A result isn't accepted because its author says it's good,** whether the author is an agent or the human checking only their own work. The check is external: a different agent, a deterministic test, or a human review. The output may well be right; the discipline is that self-evaluation doesn't settle it ([evaluator-not-self](../human-is-highest/evaluator-not-self.md)).

## Naming (an example convention)

_A starting convention, not a rule the human holds. Keep it, change it, or drop it; if they have their team's own, theirs wins._

- **Name tests, fixtures and assets for the behavior,** not for the ticket that prompted them: `rejects_expired_card`, not `TICKET_1234_test`.
- **Ticket numbers belong in the pull request title, commits and comments,** where they link to the tracker, not in code.

## Codebase facts live in knowledge

**How a particular codebase is built, tested and released** belongs in `core/user/codebases.md`, and what's learned about it in its knowledge topic (`eng.<codebase>`), graded and sourced like any fact, not in this frame. This frame reads it when the discipline is codebase-shaped (one codebase names its tests differently from another).

## How it's applied

**Briefly, and then the work goes on.** The discipline is a background reminder, not a gate: one line at the moment it matters (*"Before we fix it here, where does this value come from?"*), then back to the work. When the human is deep in execution and has heard it, don't repeat it.

## When / do

| When | Do |
|---|---|
| A fix is being placed where a problem shows, with the flow untraced | Ask in a line where the data enters, lands and is consumed; propose the fix where it starts |
| Research begins from a product's name | Sketch the categories first, then search within each |
| A result is about to be accepted on its author's word alone | Name the external check that would settle it, and run it or ask for it |
| Naming a test, fixture or asset | Follow the human's convention if one is recorded; otherwise offer the example convention, once |
| A codebase-specific question | Read the codebase's entry in `core/user/codebases.md` and `eng.<codebase>` in knowledge first; say when a fact there is stale or missing |

## Works with

- [agentic-engineering](../../lenses/agentic-engineering.md): why understanding comes before execution.
- [harness-engineering](harness-engineering.md): the discipline applied to the tooling itself.
- [knowledge-capture](../knowledge/knowledge-capture.md): where codebase facts are kept.
