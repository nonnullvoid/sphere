# Replication

_Status: draft 1, for review._ How spheres reproduce and learn from each other: what can leave a sphere, how a new sphere starts from another, and how one sphere safely takes in what another learned.

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
| The human's identity, profile, principles | `core/user/` |
| The AI's persona and relationship with this human | `core/ai/` |
| Session records, decisions, history | `core/records/`, `layers/world/history/` |
| Layer data: work, knowledge, everything in `layers/` | `layers/` |
| Rendered views | `surface/` |
| **Self-lenses**: lenses about this person's own thinking | `core/protocol/lenses/` (marked as self-lenses) |
| Facts about other people | anywhere. See [knowledge](knowledge.md#facts-about-other-people) |
| The incidents behind guardrails | guardrail records. See [guardrails](guardrails.md#what-travels) |

## What can travel

- **Mechanism lenses:** understanding of how sphere mechanics work, such as how projections should behave or why grounding matters.
- **Frames**, with any self-specific examples removed.
- **Registry structures** without their entries, **templates**, **shared assets**, **tooling**.
- **Empty slots** where self-lenses and personal data go. A shared sphere shows *that* it has a principles lens, never *what's in it*.
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

### Provenance

Every seed carries `core/provenance.json`:

```json
{
  "source": "my-worksphere",
  "grain": "dehydrated",
  "architecture": "2.0",
  "profile": "standard",
  "commit": "a1b2c3d",
  "exported_at": "2026-10-25T14:32:00Z"
}
```

With it, anything that later comes from this seed can say exactly which sphere, which commit and which architecture version it came from.

---

## Init: starting a sphere from a seed — _used once by hand; not yet exercised from a published build_

A new sphere begins as a copy of a seed, usually a published build. **Init** is the first conversation, where the sphere learns who its human is and fills its empty slots: profile, principles, a first piece of work. Init is co-authored like everything else: the human talks, the AI drafts, the human confirms. See [profiles](profiles.md) for how init differs at core profile.

---

## Absorb: learning from another sphere — _unexercised_

**Absorb** takes something another sphere learned (a frame, a mechanism lens, a template) and offers it to this one.

**Everything absorbed is untrusted until the human accepts it.** A frame from another sphere is instructions someone else wrote, and instructions can carry things nobody here asked for. So:

- **Absorbing only produces proposals.** The sphere reads the incoming seed, says what it found and how each item would fit here (adopt, adapt, skip), and the human decides item by item.
- **Nothing in an incoming seed is ever executed or followed** while it's being read. Scripts aren't run. Instructions inside its files are treated as content to evaluate, not as commands.
- **Accepted items arrive unattached.** A frame starts without a lens here, and is offered for co-authoring like an imported skill.
- **Provenance is kept.** Each absorbed item records where it came from, so a later compare can trace it.

## Compare — _unexercised_

**Compare** shows how two spheres differ in shape: which lenses, frames and layers each has, and where shared ones have diverged. Because every sphere declares its architecture version, the comparison is measured against a common anchor rather than guessed at. Compare reads shape only. It never needs either sphere's data.

## Upgrading from a newer build — _unexercised_

A sphere started from a build can take in later versions of that build. This is absorb, applied to its own lineage: the new version's upgrade note (see [versions](VERSIONS.md)) says what changed, and the sphere proposes each change against the human's sphere as it actually is now. Nothing is overwritten. A sphere that has grown its own way keeps it.

---

## Transport

Today, seeds move as files: a folder, a repository, an archive.

Later, spheres may exchange shape directly over a network. The intended route is a read-only service that exposes a sphere's protocol only, never its data. _Nothing is built yet, and this chapter makes no promise beyond the boundary: whatever the transport, data stays home._

---

## Open questions

1. **Marking self-lenses.** How does a lens declare that it's about the human (never travels) versus about mechanics (can travel)? A frontmatter field, or a separate folder?
2. **Partial absorb.** Can one sphere absorb a single frame without its lens, or must a frame always arrive with the mechanism lens it derives from?
3. **Signing seeds.** Should published seeds be signed, so a sphere can tell a build really came from its claimed source?
