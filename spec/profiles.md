# Profiles

_Status: draft 1, for review._ One architecture, three depths. How the same sphere can serve someone who will never read a file and someone who builds on its internals daily, without being two different systems.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

---

## The idea

People come to a sphere wanting very different things. Some want it to remember their life and show it back to them, and should never meet the words *lens*, *frame* or *git*. Others want to shape every mechanism themselves. A sphere serves both with **profiles**: the same architecture and the same files, at different depths of what's switched on and what's shown.

**A profile changes presentation and features, never the data model.** Every profile stores work, knowledge, sessions and protocol the same way. So moving between profiles is turning things on or off, never a migration. It's the same rule as [session levels](state.md#no-migration-between-levels) and [work depth](work.md#depth-is-a-dial--proven). — _decided, not yet exercised_

---

## The three profiles

| | **core** | **standard** | **full** |
|---|---|---|---|
| **For** | People who will never open the files | Technical daily users | Heavy use, many sessions in parallel, several spheres |
| **Sessions** | Level 1. Git present, invisible. | Level 1 by default; level 2 available | Level 2 |
| **Protocol** | Lenses and frames exist but are never shown or named | Lens and frame split visible and editable | Same, plus tiered loading |
| **Registries** | Present, never mentioned | Visible; drift checks reported at ground | Same |
| **Work** | A flat list, in the human's own words ("my things") | Nodes, nesting when wanted | Deep trees, mirrors to outside tools |
| **Projections** | **The interface:** home, my things, witness | Work and other dashboards; machinery views optional | Same |
| **Loading** | A small startup | A generated startup bundle (a cache) | A tiered manifest: identity eager, everything else on demand |
| **Replication** | Not offered | Seeds, absorb, compare | Same, plus network exchange _(unexercised)_ |

---

## What the human hears

The clearest difference between profiles is vocabulary. What a sphere says out loud:

| The sphere does… | At core it says… | At standard and full it says… |
|---|---|---|
| Grounds a session | *"Saved."* or nothing at all | *"Grounded: 3 files, work index rebuilt."* |
| Proposes a new lens | *"You seem to always want to see things before they're sent. Should I remember that?"* | *"Proposing a lens, outbound-comms, sharing: private."* |
| Records a guardrail | *"Got it. I won't do that again."* | *"New guardrail under comms-guard: …"* |
| Reports drift | Nothing; it fixes what it can, quietly | *"Drift check: world registry stale, rebuilt."* |
| Offers level-2 sessions | Never | *"You're running two pieces of work in parallel. Want separate sessions for them?"* |

At core profile, **evolution still works fully.** The sphere proposes, the human confirms, and the sphere adapts. It just never uses the structural words. A non-technical human co-authors their sphere in plain conversation.

---

## Moving between profiles

- **Up:** the sphere proposes it when it sees a need: the human starts editing files directly, asks how something works, or runs parallel work. The human decides. Nothing is rewritten; features switch on.
- **Down:** features switch off and vocabulary simplifies. Nothing is deleted. A sphere that later moves back up finds everything where it was.
- **Partial is normal.** A standard sphere that never uses level-2 sessions is still standard. Profiles describe what's *available*, not what must be used.

---

## Declaring a profile

A sphere declares its architecture version and profile alongside its [identity](replication.md#sphere-identity--decided-not-yet-exercised):

```json
{
  "id": "01933b7e-8f2a-7c41-9d3e-5b6a2f0c1e88",
  "name": "ridgeline-worksphere",
  "version": "2026.10.3",
  "architecture": "2.0",
  "profile": "standard"
}
```

Builds declare the same in their provenance, so anyone starting from a build knows what they're getting.

## Conformance — _decided, not yet exercised_

A sphere can claim a profile only if it has what that profile requires:

| Profile | Must have |
|---|---|
| **core** | `core/identity.json`; a protocol registry; ground and resume (level 1); a work layer; a world layer; at least a home projection; the four [shipped guardrails](guardrails.md#guardrails-every-sphere-ships-with--proven) |
| **standard** | core, plus: lens and frame folders; layer contracts and a layer registry; drift checks; a startup bundle; export at bare and dehydrated grain |
| **full** | standard, plus: level-2 session tooling; a tiered loading manifest |

The drift checks can verify conformance, so a sphere's claimed profile stays true as it changes.

---

## The builds

| Build | Profile | Notes |
|---|---|---|
| **base** | standard | The week-one starter. Level-1 sessions. |
| **lifesphere** | standard | Life-shaped layers and projections |
| **codesphere** | standard, level 2 available | Grows naturally into full |
| **non-technical build** | **core** | Projections are the whole interface |

---

## Open questions

1. **A caretaker.** A core-profile sphere is often set up and looked after by someone else: a partner, a family member. Should a second person be able to see the machinery that the sphere's own human never sees, and what can they change without the human's say?
2. **Detecting readiness to move up.** Which signals are strong enough for the sphere to offer a higher profile, and which would just be noise?
3. **Loading at core.** Is a small startup enough as a core sphere grows over years, or does core need the startup bundle too, invisibly?
