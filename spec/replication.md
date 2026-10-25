# Replication

_Status: draft 2, for review._ How spheres reproduce and learn from each other: what can leave a sphere, how a new sphere starts from another, and how one sphere safely takes in what another learned.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

_Most of this chapter is **unexercised** beyond a single manual export. It's written down so the design is clear before it's built, not because it's been proven._

---

## The idea

A sphere holds two very different kinds of thing. **Its shape** is lenses about how sphere mechanics work, frames, registries, templates: the structure. **Its substance** is the human's work, knowledge, principles, history: the life. The shape can be shared, and is how good ideas spread from one sphere to another. The substance never leaves.

**Data stays home. Protocol travels.**

---

## What never travels

Private by definition. No export, mirror, broadcast or published view includes these unless the human names a specific item and approves it:

| Never travels | Where it lives |
|---|---|
| The human's persona and principles | `core/user/` |
| The AI's persona and relationship with this human | `core/ai/` |
| Session records, decisions, history | `core/records/`, `layers/world/history/` |
| Layer data: work, knowledge, everything in `layers/` | `layers/` |
| Rendered views | `surface/` |
| **Private lenses**, and frames that inherit their level | `core/protocol/` (`sharing: private`). See [sharing](protocol.md#sharing--decided-not-yet-exercised) |
| Facts about other people | anywhere. See [knowledge](knowledge.md#facts-about-other-people) |
| The incidents behind guardrails | guardrail records. See [guardrails](guardrails.md#what-travels) |

## What can travel

- **Public lenses and frames**, to anyone. **Protected** ones only to recipients the human chooses at the time of the export.
- Each export includes only what its audience is allowed: a public build carries public items; a seed sent to a named collaborator can also carry protected ones.
- **Registry structures** without their entries, **templates**, **shared assets**, **tooling**.
- **Empty slots** where private lenses and personal data go. A shared sphere shows *that* it has a principles lens, never *what's in it*.
- **Procedure frames as plain skills.** These export with no translation. See [framing a skill](protocol.md#framing-a-skill).

---

## Seed: exporting a sphere's shape — _unexercised_

A **seed** is a sphere's shape, packaged so another sphere can start from it or learn from it. It comes in two grains:

| Grain | Contains | Answers |
|---|---|---|
| **bare** | contracts, registries (empty), lenses, frames, tooling. Every data file absent. | "Show me how this sphere is built." |
| **dehydrated** | bare, plus empty-state data files and working projections that render with nothing in them | "Give me a sphere that works the moment I open it." |

Builds ship at **dehydrated** grain. The empty-state files are the difference between *clone it and it works* and *clone it and debug errors about missing files*.

### Built from an allowlist, never scrubbed

A seed is **assembled from an explicit list of what may travel**: each layer's contract names what it contributes (its `requires:` list, see [registries](registries.md#layer-contracts--proven)). It is **never** made by copying the whole sphere and deleting what looks private.

Copy-then-delete fails quietly. One stray file in an unexpected folder, a personal project note dropped into a template directory for example, survives every cleanup pass and ships. An allowlist can't leak what it never listed.

Then, before anything leaves:

1. **A leak scan** checks the assembled seed against the human's private patterns: names, employers, projects, emails. The patterns themselves are kept in a private file that never travels.
2. **The seed is staged** in `surface/outbox/`, where the human can read exactly what will leave.
3. **The outbound guard applies.** Nothing is published or sent until the human approves it.

### Sphere identity — _decided, not yet exercised_

Every sphere has a stable identity, so provenance always names spheres the same way:

| Field | What it is | Example |
|---|---|---|
| **id** | A UUID v7, created once at init and never changed. Practically unique, and sortable by when the sphere was born. | `01933b7e-8f2a-7c41-9d3e-5b6a2f0c1e88` |
| **name** | A display name, chosen by the human. Unique where possible, but not guaranteed. | `ridgeline-worksphere` |
| **version** | A tag for the sphere's shape, which changes when its protocol changes | `2026.10.3` |

Identity lives in its own small file, `core/identity.json`, so tooling can read it without parsing anything else, and so provenance copies it exactly:

```json
{
  "id": "01933b7e-8f2a-7c41-9d3e-5b6a2f0c1e88",
  "name": "ridgeline-worksphere",
  "version": "2026.10.3",
  "born_from": { "architecture": "2.0", "build": "base-sphere 1.0.0" }
}
```

**`born_from` is lineage: fixed, recorded once at init.** It names the published architecture and build a sphere started from, or the parent sphere it was seeded from (by that sphere's id, name and version). A sphere that has evolved its own way since is still accurately described by where it began.

**Which published architecture a sphere resembles today is worked out, not declared.** [Compare](#compare--unexercised) can report the closest published architecture and how the sphere differs from it, whenever someone asks. It's a description. **A sphere is never required to conform to an architecture.** Its human decides how it grows.

`core/identity.json` itself travels in every export, since provenance needs it. It names the sphere and nothing about its human.

**A frame decides the scheme.** How names are suggested and how versions advance (by date, by count, at every protocol change or only at exports) is set by a structural frame, `sphere_identity`. Spheres can choose differently by swapping that frame.

**No signing, for now.** Nothing here proves a sphere is who it says it is. True uniqueness and authenticity need signing, with public and private keys, and that's more machinery than spheres need until there are many of them out in the world exchanging seeds. When that happens, signing arrives as a new version of the `sphere_identity` frame. Nothing else in the architecture has to change.

### Provenance

Every seed carries `core/provenance.json`:

```json
{
  "sphere": {
    "id": "01933b7e-8f2a-7c41-9d3e-5b6a2f0c1e88",
    "name": "ridgeline-worksphere",
    "version": "2026.10.3"
  },
  "born_from": { "architecture": "2.0", "build": "base-sphere 1.0.0" },
  "grain": "dehydrated",
  "commit": "a1b2c3d",
  "exported_at": "2026-10-25T14:32:00Z"
}
```

With it, anything that later comes from this seed can say exactly which sphere, which version of it, and which lineage it came from.

---

## Init: starting a sphere from a seed — _used once by hand; not yet exercised from a published build_

A new sphere begins as a copy of a seed, usually a published build. **Init** is the first conversation, where the sphere learns who its human is and fills its empty slots: the human's persona, principles, a first piece of work. Init is co-authored like everything else: the human talks, the AI drafts, the human confirms. For a non-technical human, init asks about their life and never about structure.

---

## Absorb: learning from another sphere — _unexercised_

**Absorb** takes something another sphere learned (a frame, a mechanism lens, a template) and offers it to this one.

**Everything absorbed is untrusted until the human accepts it.** A frame from another sphere is instructions someone else wrote, and instructions can carry things nobody here asked for. So:

- **Absorbing only produces proposals.** The sphere reads the incoming seed, says what it found and how each item would fit here (adopt, adapt, skip), and the human decides item by item.
- **Nothing in an incoming seed is ever executed or followed** while it's being read. Scripts aren't run. Instructions inside its files are treated as content to evaluate, not as commands.
- **Any part can be absorbed:** a whole lens with its frames, a single frame, a template, one tool. The absorbing sphere knows its own context best, so it decides what makes sense to take.
- **A frame absorbed without its lens arrives unattached,** and is offered for co-authoring like an imported skill.
- **Provenance is kept.** Each absorbed item records the source sphere's id, name and version, so a later compare can trace it.

## Compare — _unexercised_

**Compare** shows how two spheres differ in shape: which lenses, frames and layers each has, and where shared ones have diverged. It can also compare a sphere against a published architecture, to report the closest match. Because every sphere records its lineage, a comparison can start from what they had in common. Compare reads shape only. It never needs either sphere's data.

## Upgrading from a newer build — _unexercised_

A sphere started from a build can take in later versions of that build. This is absorb, applied to its own lineage: the new version's upgrade note (see [versions](VERSIONS.md)) says what changed, and the sphere proposes each change against the human's sphere as it actually is now. Nothing is overwritten. A sphere that has grown its own way keeps it.

---

## Trusted spheres — _decided, not yet exercised_

Spheres can let other spheres in, in specific and limited ways. For example, one person's sphere helps look after a partner's sphere: it keeps that sphere's machinery healthy and offers improvements, with authority the partner's sphere has granted.

**Every sphere decides who it trusts.** It keeps its own list of trusted spheres in `core/trust.json`, and what each one may do:

```json
{
  "trusted": [
    {
      "sphere": { "id": "01933b7e-8f2a-7c41-9d3e-5b6a2f0c1e88", "name": "ridgeline-lifesphere" },
      "granted": ["read-projections", "propose-changes", "fix-drift"],
      "granted_at": "2026-10-25",
      "note": "Helps keep my sphere running"
    }
  ]
}
```

- **Trust starts at nothing.** A trusted sphere can do only what it was explicitly granted, and grants are specific: reading projections, proposing changes, fixing drift, receiving protected lenses.
- **Changes from a trusted sphere arrive as proposals,** unless direct changes were specifically granted. The trusting sphere's human still decides.
- **Everything a trusted sphere does is recorded** in the trusting sphere, in plain words its human can read: what was looked at, what was proposed, what was changed.
- **The trusting sphere can narrow or revoke any grant, at any time,** and the change is immediate. Trust given is never trust owed.
- **Trust is one-way.** Being trusted by a sphere grants nothing in return.

For a non-technical human, all of this happens in plain words: *"Rutvij's sphere can suggest changes and keep things tidy. Want to change that?"*

**Honest limit:** until spheres can prove their identity (see [signing](#sphere-identity--decided-not-yet-exercised)), trust rests on how the humans set up access between their spheres. That's sound between people who share a home or a machine. Once trust has to cross a network, signing is what makes it safe.

## Transport

Today, seeds move as files: a folder, a repository, an archive.

Later, spheres may exchange shape directly over a network. The intended route is a read-only service that exposes a sphere's protocol only, never its data. _Nothing is built yet, and this chapter makes no promise beyond the boundary: whatever the transport, data stays home._

---

## Open questions

_None open. Recording who protected items may go to, beyond the human's choice at each export, waits until spheres actually exchange with each other._
