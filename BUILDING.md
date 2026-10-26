# Building a sphere

_A practical guide to growing a sphere well. The [architecture](ARCHITECTURE.md) says what a sphere is; this says how to tend one. It's drawn from two spheres in daily use, including the mistakes._

---

## 1. Start small

You don't need the whole architecture on day one. A sphere that holds a few things well beats one that holds everything badly. A good first week:

- **Who you are, and how you like to work:** a short user persona and a few principles.
- **Your work,** one node per thing you're doing, each with a next action.
- **Facts worth keeping,** with where they came from.
- **Ground at the end of each session,** and resume at the start of the next.
- **The outbound guard:** nothing leaves under your name without you seeing it.

Everything else (session trees, mirrors, modes, sharing) can wait until you feel the need. Add things when something's missing, not because the architecture has a chapter on it.

---

## 2. Co-author your lenses and frames

The most valuable thing in a sphere is understanding only you could have supplied. It gets in through conversation:

1. **Start from a real moment.** *"I almost sent that reply before re-reading the thread. I never want that again."* A concrete case gives the AI something true to work from. An abstract wish ("be more careful") gives it nothing.
2. **Let the AI draft.** Ask it to say where it's guessing.
3. **Read it as if it were about you, because it is.** What's wrong? What's missing? What doesn't sound like you?
4. **Iterate until it's true.** Some lenses take one pass. Mechanics that touch tools can take many rounds of trial and error, and that's normal.
5. **Capture it only when you say so.** The AI may notice a pattern and ask. It never writes a lens on its own.

**When not to bother:** a one-off procedure you'll never revisit doesn't need a lens. A lens earns its place when the same understanding drives several behaviors, or keeps changing.

**Already have skills?** Say *"learn this skill"* and the sphere frames it: copies it in, registers it, and offers to attach a lens. See [framing a skill](spec/protocol.md#framing-a-skill).

---

## 3. Keep truth in one place

Every fact, decision and status should live in exactly one file. Everything else that shows it is a **view**.

**The test:** could you delete this file and rebuild it from others? If yes, it's a view, and it must never be edited directly. If no, it's truth, and nothing else should duplicate it.

_What goes wrong otherwise:_ a project index maintained by hand looked fine for weeks, while the projects it listed had moved on. Nobody edits two places reliably.

## 4. Update before you add

Before creating a new lens, frame, command or layer, ask whether an existing one should grow instead. A sphere that adds freely becomes hard to read and starts contradicting itself. Adding a lens is the heaviest step of all, because everything else derives from it. See [governance](spec/protocol.md#governance--proven).

---

## 5. Habits lapse, so check

Some registries are rebuilt by a script and some by the AI. Either way, **give every registry a check that runs in tooling.**

_What goes wrong otherwise:_ a registry whose instructions said "rebuild at every ground" went five months without being rebuilt. Nothing was broken, so nothing noticed. A one-line freshness check would have caught it the first day.

The same applies to anything a sphere promises to do every time: if it matters, put it in tooling, and let the AI rely on the check. See [registries](spec/registries.md).

## 6. Mechanics in tooling, meaning in prose

When a frame's value is in getting operations exactly right (git, file moves, servers), write a script. When its value is understanding, write the lens or frame text.

_What goes wrong otherwise:_ a session system described entirely in prose took many iterations to make git behave, and every session re-derived the same commands. The understanding was settled early. The mechanics kept breaking, because prose isn't a program.

---

## 7. Load lazily

At startup, load only what tells the sphere **who** and **where**: the personas, the rules, and the registries that point at everything else. Load the rest when a task needs it.

Count what your startup reads. If it keeps growing, move something behind a registry pointer. A sphere that reads everything at the start of every session gets slower and more expensive as it gets better.

## 8. Ground for a stranger

The test of a good ground: **could a new session, with no memory of this one, continue the work?** Write `progress.md` entries for that reader. Say what happened, what was decided and why, and the single next step.

- Stage only what this session touched. Other changes belong to other sessions, or to you.
- Propose facts; don't write them. You decide what becomes knowledge.
- Ground often enough that a lost session costs little.

---

## 9. Make projections honest

- **Declare freshness up front:** live, manually synced, or snapshot.
- **Show staleness on the page.** A view that looks current but isn't is worse than no view.
- **Start plain:** HTML, CSS and JavaScript with no build step. Reach for an app only when you need a database, logins or a phone. At that point, it's an app that reads your sphere, and it must declare how it stays in sync.
- **Extract a template on the third repetition,** never sooner.

See [projections](spec/projections.md).

## 10. Write guardrails with their reasons

Every near-miss is a chance to prevent the next one. Capture the rule, **why** it exists, and **when** it applies. A rule without its reason can't be applied sensibly to a case nobody anticipated, or retired when the reason goes away.

Record what worked, too. When the AI makes a good non-obvious call and you say "yes, exactly," that's worth keeping. A sphere that only records corrections slowly becomes timid. See [guardrails](spec/guardrails.md).

---

## 11. Export from an allowlist

When sharing your sphere's shape (publishing a build, or seeding a friend's sphere), **assemble the export from a list of what may go.** Never copy your sphere and delete what looks private.

_What goes wrong otherwise:_ a personal project note, dropped into a template folder during a busy session, survived every cleanup and sat in a public repository's working copy until someone happened to look. An allowlist can't leak a file it never listed.

Then scan for your own private terms before anything leaves, and read what's staged before you approve it. Mark each lens's sharing level when you create it, and when unsure, private. See [replication](spec/replication.md).

## 12. Be honest about what's proven

Mark what you've exercised for real versus what you've only designed. Ideas look finished on paper long before they survive real use. A sphere, or an architecture, that says "this part isn't proven yet" is one people can trust about the parts that are.

---

## Quick reference: common mistakes

| Mistake | Instead |
|---|---|
| Editing an index or registry by hand | Edit the source; let the view rebuild |
| A rule with no reason | Rule, why, and when it applies |
| The AI writing facts on its own | Facts proposed at ground; you decide |
| Promising the sphere is always up to date | Promise the boundaries: true at session start and end |
| A startup that reads everything | Who and where at startup; the rest on demand |
| Private files in something you share | Build exports from an allowlist |
| Prose instructions for exact operations | A script, plus a short frame saying when to run it |
| A view that hides how old it is | Freshness on the page |
| Forcing a sphere to match an architecture | Record where it came from; compare when useful |
