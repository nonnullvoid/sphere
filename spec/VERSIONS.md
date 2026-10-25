# Versions

_Status: draft 1, for review._ How the architecture, the builds and each sphere are versioned, and how a sphere takes in what a newer version offers without being forced to.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

---

## Three kinds of version

| What's versioned | Scheme | Who sets it | Example |
|---|---|---|---|
| **The architecture**: this spec | `SPHERE-ARCH major.minor` | the published repository | `SPHERE-ARCH 2.0` |
| **A build**: a ready-to-use sphere in the repository | semantic versioning, per build | the published repository | `base-sphere 1.0.0` |
| **A sphere**: one person's living sphere | its own tag, by its own scheme | the sphere, through its `sphere_identity` frame | `2026.10.3` |

They move independently. A build can get a bug-fix release without the architecture changing. A sphere's own version moves whenever its protocol changes, whatever happens upstream.

---

## Architecture versions — _decided, not yet exercised_

A published architecture version is a **reference point**: something a sphere can say it was born from, and something [compare](replication.md#compare--unexercised) can measure a sphere against. **It is never a contract.** A sphere that has grown away from its architecture isn't out of compliance; it's simply further from that reference point, and compare can say how.

- **Major** (`2.0` → `3.0`): a structural change, where something an older sphere relies on works differently. Examples: files move, a core concept is redefined, a layout changes.
- **Minor** (`2.0` → `2.1`): additive. New chapters, new optional mechanics, new frames. Nothing an existing sphere relies on changes meaning.
- **Status tags move without a version change.** When something marked *unexercised* gets proven in real use, its tag is updated. That's a correction to the description, not a change to the architecture.
- **Deprecation is announced a version ahead.** Anything that will change in the next major version is marked deprecated in the current one, with what replaces it.

## Build versions — _decided, not yet exercised_

Each build in the repository is versioned on its own, with semantic versioning:

- **Patch:** fixes. A template renders correctly; a frame's wording is clarified.
- **Minor:** additions. A new projection, a new frame, a new optional layer.
- **Major:** a change that a sphere started from the previous version would need to absorb carefully. A layout change, or a frame that now behaves differently.

Every build records the architecture version it was built from. Builds also say plainly what they include, for example which session level they start at and which layers ship, so nobody has to infer it.

## A sphere's own version — _decided, not yet exercised_

A sphere versions its own shape. How is up to its [`sphere_identity`](replication.md#sphere-identity--decided-not-yet-exercised) frame: by date, by counting protocol changes, or only at exports. The version appears in `core/identity.json` and in every seed's provenance, so anything that came from the sphere can say which version of it.

---

## Upgrade notes

Every release of the architecture or a build ships an **upgrade note**. A living sphere reads it to decide what to take in:

```markdown
## base-sphere 1.1.0 — built from SPHERE-ARCH 2.0

### What changed
- Work dashboard shows `waiting_on` for paused nodes.

### Why
- Paused work was drifting into forgotten work.

### How a sphere can take this in
- Adopt the updated dashboard template. Your existing nodes need no changes.

### Breaking
- None.
```

**A sphere is never upgraded by overwriting.** Taking in a new version is [absorb](replication.md#absorb-learning-from-another-sphere--unexercised) applied to the sphere's own lineage. The sphere reads the upgrade note, proposes each change against how it actually is now, and the human decides item by item. A sphere that has grown its own way keeps it.

---

## SPHERE-ARCH 2.0 — what's new since v0.1

The first public release (v0.1, April 2026) described a sphere with a single protocol file, layer registries kept by hand inside the orchestrator, and an untyped output folder. Version 2.0 is mostly a backport of what two spheres in daily use worked out since:

- **Protocol:** lenses and frames. Every skill is a frame; frames come in four kinds; skills can be framed into a sphere. ([protocol](protocol.md))
- **State:** two session levels, simple by default and the session tree opt-in. A session registry with three homes for three kinds of truth. ([state](state.md))
- **Work:** nodes as `work.md` + `progress.md`, depth as a dial, a generated index, archiving. ([work](work.md))
- **Knowledge:** domain → subject → item, graded and dated facts, facts proposed at ground, care for facts about other people. ([knowledge](knowledge.md))
- **Registries:** maintained per registry, checked by tooling, whatever the mode. ([registries](registries.md))
- **Projections:** never the source of truth, visible staleness, static vs served, a default stack that escalates. ([projections](projections.md))
- **Guardrails:** incident-born rules with reasons, kept few, overridable except when marked hard. ([guardrails](guardrails.md))
- **Replication:** sharing levels, allowlist-built seeds, untrusted absorb, sphere identity and lineage, trusted spheres. ([replication](replication.md))
- **Modes:** switchable behavior on top of a persona. _Stub._ ([modes](modes.md))

---

## Open questions

1. **Why "2.0" and not "1.0".** The public repository's first release was v0.1, and the earlier private generation of spheres was informally called v1. Calling this 2.0 matches how the project has talked about it. Calling it 1.0 would match what the public has seen. Which reads better to someone arriving fresh?
2. **How long deprecated things live.** One major version ahead, or a fixed time?
