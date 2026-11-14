---
frame: structure-check
kind: instinct
lens: [readable-substrate, sphere-framework]
derives_from: [readable-substrate@1, sphere-framework@1]
version: 1
version_note: First draft. Anatomy, shape, links and views, checked at ground.
status: drafting
updated: 2026-11-12
sharing: public
reads: [core, layers, surface]
writes: []
protocol: [I-trust-what-i-read, A-check-structure, convention-violated]
---

# The structure check

**Applies to:** every ground, and any time the human asks *"is everything in order?"*

A sphere is only as trustworthy as the picture it reads of itself. This check confirms that picture against the files: what the registries say exists does, every node has its shape, links lead somewhere, and views match what they're built from. It runs in the tooling (in the reference build, `scripts/structure-check`), not from the AI's memory of what should be there.

## What it checks

| Check | Confirms |
|---|---|
| **Anatomy** | Every layer folder has a contract, and every contract has a folder. Every surface space is declared, and every declared space exists |
| **Shape** | Every node has its parts: a name, a place in its tree, frontmatter in its tree's declared shape, current state, and history. No declared key missing, no undeclared key, no fixed-value key holding a value its tree doesn't allow |
| **Links** | Every `parent:` and every `tree:name` link points at a node that exists, live or archived |
| **Views** | Every generated file says it's generated and what from, was rebuilt after its sources last changed, and matches what its sources would produce now |
| **Finished things** | A node in a final state has moved to `archived/`; nothing live sits in `archived/` |

**Shapes are declared, never hard-coded.** Each tree's frontmatter shape (its keys, and the values fixed keys may take) is written down once, in plain text beside the tree, and the check reads it. *Why:* a check that hard-codes the shape breaks the day the shape improves, and then it gets switched off.

## Rules

- **It stays cheap.** It runs at every ground, so it reads only what it must: frontmatter and folder listings, never whole bodies, and never the archive unless asked. A check that slows every ground gets skipped. *Why:* a check is only worth what it costs to run every time.
- **It evolves with the sphere.** When the sphere grows a new tree, layer or kind of file, or changes a shape, the check and its declarations (`core/shapes`, the registries) change in the same evolution step. A check that lags the sphere reports noise, and noise gets ignored.
- **It reports; it never fixes.** Each finding comes with a fix to offer: *"`plumbing` names a parent `kitchen-reno` that was renamed to `kitchen`. Update the link?"* What's fixed is decided like any other change.
- **It never blocks the ground, and nothing it finds is silenced.** Each finding is fixed, or kept as an exception the human names. *Why:* a check that stops work gets switched off; one that offers a fix gets used.
- **An exception is explicit.** A deviation the human keeps is recorded where the check reads it (the tree's shape declaration, or the registry), with one line saying why. It isn't reported again.
- **Change a shape with its nodes.** Changing a tree's frontmatter means changing its declared shape in the same ground. Otherwise every node in that tree is reported.
- **A hand edit to a view is caught, not lost.** The view no longer matches its sources, so the check finds it and asks where the change belongs: *"The work index was edited directly. Move that change into the node it's about?"*
- **Plain words for the human.** A non-technical human hears what's wrong and what to do, never the name of a check.

## When / do

| When | Do |
|---|---|
| Ground, after generated files are rebuilt | Run the check; report findings in one line each, with a fix to offer |
| A layer or surface space is added, removed or restructured | Fire `structure-changed` so its registry is rebuilt this ground; then check |
| A node is missing a part or has an undeclared key | Fire `convention-violated`; offer to add the part, or to record an exception |
| A link points at nothing | Look for a rename or an archive first; offer the corrected link |
| A view doesn't match its sources | Rebuild it; if it was edited by hand, ask where the edit belongs first |
| A tree's frontmatter changes | Update its declared shape in the same ground |
| The human keeps a deviation | Record it as an exception, with its reason, where the check reads it |

## Works with

- [node-shape](../nodes/node-shape.md): the parts every node has, which the shape check confirms.
- [manifest-check](manifest-check.md): the same idea for the sphere's capabilities.
- [state-machine](../continuity/state-machine.md): ground is when this check runs.
- [registries](../../../../../spec/registries.md#drift-checks--proven) and [nodes](../../../../../spec/nodes.md#the-shape-check--decided-not-yet-exercised): the drift checks and the shape check, in the spec.

## Senses

| Sense | Fires when |
|---|---|
| `convention-violated` | something deviates from a convention with no recorded exception |
