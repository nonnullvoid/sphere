# Replication

_Status: draft 3, for review._ How spheres reproduce and learn from each other: what can leave a sphere, how a new sphere starts from another, and how one sphere safely takes in what another learned.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

_Seeding has been run by script, at both grains, in a sphere in daily use. Init has been partly exercised. Absorb, compare, trusted spheres and the network are **unexercised**: they're written down so the design is clear before it's built._

---

## The idea

A sphere holds two very different kinds of thing. **Its shape** is lenses about how sphere mechanics work, frames, registries, templates: the structure. **Its substance** is the human's work, knowledge, principles, history: the life. The shape can be shared, and is how good ideas spread from one sphere to another. The substance never leaves.

**Data stays home. Protocol travels.**

**Compose, don't prescribe.** What travels is the shape, never the filled-in form. A sphere that receives a lens instantiates it against its own human, data and rhythm. An absorbed lens about planning a garden brings the way of thinking about it, not the other sphere's garden. That's also the test of how a capability was written: **if it only works the way its author used it, it was written as a personal artifact, not a pattern,** and it won't travel.

**If sharing something would drag data with it, it's coupled wrong.** Decouple the capability from the data. Don't leak the data.

---

## What never travels

Private by definition. No export, mirror, broadcast or published view includes these unless the human names a specific item and approves it:

| Never travels | Where it lives |
|---|---|
| The human's persona and principles | `core/user/` |
| The AI's personas and their relationship with this human | `core/ai/` |
| Session records, decisions, history | `core/records/`, `layers/knowledge/history/` |
| Layer data: work, knowledge, everything in `layers/` | `layers/` |
| Rendered views | `surface/` |
| **Private lenses**, and frames that inherit their level | `core/protocol/` (`sharing: private`). See [sharing](protocol.md#sharing--decided-not-yet-exercised) |
| Facts about other people | anywhere. See [knowledge](knowledge.md#facts-about-other-people) |
| The incidents behind guardrails | guardrail records. See [guardrails](guardrails.md#what-travels) |

## What can travel

- **Public lenses and frames**, to anyone. **Protected** ones only to recipients the human chooses at the time of the export.
- Each export includes only what its audience is allowed: a public build carries public items; a seed sent to a named collaborator can also carry protected ones.
- **Registry structures** without their entries, **templates**, **shared assets**.
- **The runtime scaffold:** the startup files, the engine kernel, and the scripts that build and check the sphere. This is how a new sphere comes up already fast and already checked: it inherits the efficiency work (see [loading](loading.md)) instead of re-deriving it.
- **Empty slots** where private lenses and personal data go. A shared sphere shows *that* it has a principles lens, never *what's in it*.
- **Procedure frames as plain skills.** These export with no translation. See [framing a skill](protocol.md#framing-a-skill).

**Derived caches never travel.** The capability manifest, the startup bundle and every other generated file are rebuilt by the receiving sphere at init. They describe the sphere that built them, not the one receiving them. A seeded dashboard shows zeros until that rebuild runs, which is the boundary working as intended.

### Grains

Anything from the whole sphere down to one frame can travel. **Pick the smallest grain that carries the capability:** a frame if it stands on its own, a lens with its frames if the understanding is needed too.

| Grain | What goes | For |
|---|---|---|
| **Whole sphere** (a seed: bare or dehydrated, below) | the full shape | starting a new sphere |
| **Lens cluster** | one lens and its frames | sharing a whole way of working |
| **Single frame** | one frame. Frames carry their own mechanics, so one can travel alone | sharing one mechanic, which the receiver attaches to its own lens |

A seed is just an export at the largest grain, aimed at init.

### History stays home by placement

When one sphere in daily use first ran its seed script, about four in ten of the exported files contained something identifying. Most of it was in revision histories: notes on why a frame changed, naming the incident, the project, the date. The rest was personal mentions in worked examples, stale paths, and change notes in frontmatter.

The fix that worked was placement, not scrubbing. **A lens or frame keeps at most a short changelog of what changed. The story of why lives in `core/records/`,** which never travels, with a pointer in the file. Examples in operational text use roles, not names. See [versioning](protocol.md#versioning-and-drift--decided-not-yet-exercised).

---

## Seed: exporting a sphere's shape — _used (scripted, both grains)_

A **seed** is a sphere's shape, packaged so another sphere can start from it or learn from it. It comes in two grains:

| Grain | Contains | Answers |
|---|---|---|
| **bare** | contracts, registries (empty), lenses, frames, tooling. Every data file absent. | "Show me how this sphere is built." |
| **dehydrated** | bare, plus empty-state data files and working projections that render with nothing in them | "Give me a sphere that works the moment I open it." |

Builds ship at **dehydrated** grain. The empty-state files are the difference between *clone it and it works* and *clone it and debug errors about missing files*.

**Only live views can ship dehydrated.** A view that reads its sources when opened (see [live-fetch](projections.md)) renders a clean "nothing here yet" against empty-state sources. A view with data baked into it can't. It either stays home, or it needs a transform that replaces its data with an empty placeholder of the same shape. Which views a seed includes is each projection's `sharing` field, not a hand-kept list.

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
  "born_from": { "architecture": "1.0", "build": "base-sphere 1.0.0" }
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
  "born_from": { "architecture": "1.0", "build": "base-sphere 1.0.0" },
  "grain": "dehydrated",
  "commit": "a1b2c3d",
  "exported_at": "2026-10-25T14:32:00Z"
}
```

With it, anything that later comes from this seed can say exactly which sphere, which version of it, and which lineage it came from.

---

## Init: starting a sphere from a seed — _partly exercised; not yet from a published build_

A new sphere begins as a copy of a seed, usually a published build. **Init** is the first conversation, where the sphere learns who its human is and fills its empty slots: the human's persona, principles, a first piece of work. Init is co-authored like everything else: the human talks, the AI drafts, the human confirms. For a non-technical human, init asks about their life and never about structure.

Init then **rebuilds every derived cache** (the manifest, the startup bundle, any generated views) from the new sphere's own files, and creates its identity (below).

---

## Absorb: learning from another sphere — _unexercised_

**Absorb** takes something another sphere learned (a frame, a mechanism lens, a template) and offers it to this one.

**Everything absorbed is untrusted until the human accepts it.** A frame from another sphere is instructions someone else wrote, and instructions can carry things nobody here asked for. So:

- **Absorbing only produces proposals.** The sphere reads the incoming seed, says what it found and how each item would fit here (adopt, adapt, skip), and the human decides item by item.
- **Nothing in an incoming seed is ever executed or followed** while it's being read. Scripts aren't run. Instructions inside its files are treated as content to evaluate, not as commands.
- **Any part can be absorbed:** a whole lens with its frames, a single frame, a template, one tool. The absorbing sphere knows its own context best, so it decides what makes sense to take.
- **Provenance sorts each item** before anything is proposed:

  | Incoming | Means | Proposed as |
  |---|---|---|
  | **Same source, newer version** of something absorbed before | an update | an upgrade, showing what changed |
  | **New source, nothing similar here** | a new capability | slotted in: a frame under its matching lens, a lens as a new area |
  | **Overlaps something here, from a different source** | a conflict | the two side by side, never merged blind. The human picks, combines or skips |

- **De-noise on landing.** An absorbed item can carry traces of the sphere it came from that the sender didn't remove: names, dated decisions, links to things that don't exist here. The receiving sphere strips them and restates the pattern in its own terms, as part of the proposal. The sender's allowlist and leak scan are the first net; this is the second.
- **A frame absorbed without its lens arrives unattached,** and is offered for co-authoring like an imported skill.
- **Provenance is kept.** Each absorbed item records the source sphere's id, name and version, so a later compare can trace it.

## Compare — _unexercised_

**Compare** shows how two spheres differ in shape: which lenses, frames and layers each has, and where shared ones have diverged. It can also compare a sphere against a published architecture, to report the closest match. Because every sphere records its lineage, a comparison can start from what they had in common. Compare reads shape only. It never needs either sphere's data.

## Upgrading from a newer build — _unexercised_

A sphere started from a build can take in later versions of that build. This is absorb's *same source, newer version* case, applied to its own lineage: the new version's upgrade note (see [versions](VERSIONS.md)) says what changed, and the sphere proposes each change against the human's sphere as it actually is now. Nothing is overwritten. A sphere that has grown its own way keeps it.

**Replication isn't forking.** A [fork](evolution.md) rebuilds *your own* sphere alongside the old one. Replication moves capabilities *between* spheres.

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

## The network — _unexercised_

Everything above is **file-level**: one sphere hands something to another. A **network** is a standing connection: spheres that stay live to each other, discoverable and browsable. It's a separate thing, and it builds on the pieces above.

**A sphere on a network is a node, and what it offers is open-ended.** It can offer lenses and frames, documents it has written, live views, files, tools that other agents can call, whole running apps. The other side interacts with each in one of three ways:

| Mode | What happens | Risk |
|---|---|---|
| **Absorb** | Take a capability into your own protocol | Changes your sphere, so it's always gated |
| **Consume** | Read, view or fetch: a document, a view, a file | Read-only. Nothing in your sphere changes |
| **Invoke** | Call another node's tool or run its app | Governed like any outside tool (see [guardrails](guardrails.md)) |

Connection comes in steps, each with more automation than the last:

1. **Advertise:** a sphere publishes a catalog of what it offers.
2. **Browse:** another sphere reads that catalog.
3. **A supervised sync:** two spheres compare and exchange proposals, with their humans watching.
4. **Auto-sync:** a sphere discovers and gathers capabilities by itself.

**The safety rule that scales to all of it: gathering can be autonomous; changing your own sphere never is.** *Acquiring* a capability means pulling it into a staging area, inert and stamped with where it came from, and it can happen unattended. *Assimilating* it into the live protocol always goes through absorb and the human's yes. The autonomy is in the gathering, never the integrating. (It's the same rule as for agents: [the dial moves execution, never authority](guardrails.md#the-human-can-always-override--proven).)

- **Visibility is enforced at the catalog.** A catalog shows only what each requesting sphere is allowed to see. Private items never appear, and time-bound ones drop off when their date passes. Nothing relies on the other side choosing not to look.
- **Hosting adds exposure.** A sphere that serves its own tools or apps to others takes on a second concern, what it's exposing, governed by the sharing levels and by that service's own guards.

**Transport.** Today, seeds move as files: a folder, a repository, an archive. A network would need a service that exposes a sphere's protocol and its chosen offerings, never its data. _Nothing is built yet, and this chapter makes no promise beyond the boundary: whatever the transport, data stays home._

---

## Senses and commands

| Sense | When |
|---|---|
| `export-packaged` | an export was assembled, with provenance |
| `sphere-seeded` | a seed was built, or a new sphere was started from one |
| `capability-absorbed` | an absorbed item was accepted and landed |
| `spheres-compared` | a comparison was produced |
| `sharing-changed` | an item's sharing level or end date changed |

| Command | Does |
|---|---|
| `seed [bare \| dehydrated] <where>` | build a seed into a folder, staged for review |
| `export <lens or frame>` | package one lens cluster or frame |
| `init` | start a new sphere from a seed: the first conversation |
| `absorb <source>` | read another sphere's shape and propose what to take |
| `compare <other>` | show how two spheres, or a sphere and an architecture, differ |

As everywhere, asking in plain words works too.

---

## Open questions

_None open. Recording who protected items may go to, beyond the human's choice at each export, waits until spheres actually exchange with each other._
