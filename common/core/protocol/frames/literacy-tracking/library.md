---
frame: library
lens: [literacy-tracking]
derives_from: [literacy-tracking@1]
version: 1
version_note: First draft. Artifacts worth keeping, their tags, drafts, staleness, browsing, and the perspective that decides what may be shared.
status: drafting
updated: 2026-11-13
sharing: public
reads: [layers/literacy, layers/knowledge]
writes: [layers/literacy]
protocol: [I-keep-what-i-learned, A-save-artifact, A-browse-library, A-share-artifact, artifact-added, artifact-stale]
---

# The library

**Applies to:** an explanation worth keeping, *"save this as a cheat sheet"*, browsing or searching what's been made, revising an artifact, and any request to share one.

## Teaching shouldn't evaporate

**An explanation worth coming back to becomes an artifact:** a walkthrough, a cheat sheet, a reference card. Together they're the human's **library**, their own growing shelf of what they've learned, made for them.

```
layers/literacy/library/
├── compound-interest-walkthrough.md
├── math.infinite-series/              a group of related artifacts
│   ├── convergence-tests-cheat-sheet.md
│   └── why-the-harmonic-series-diverges.md
├── rust-ownership-cheat-sheet.md
└── archived/                          retired artifacts
```

- **One file per artifact,** named by a short slug. Its frontmatter says what it is; its body is the explanation; its last section is a short list of revisions.
- **Related artifacts can share a folder,** named by namespace the way subjects are: `math.infinite-series/`. One level only, so the shelf stays easy to scan. Start a group when a few artifacts clearly belong together; a single artifact stays at the top. Moving one into or out of a group changes nothing about it but its place.
- **An artifact is a small node in one file,** like an idea: the explanation is current state, the revisions are history.
- **A rendered version** (a page with diagrams, say) is a [projection](../../../../../spec/projections.md) built from the file. The file is the truth.

## Frontmatter

```yaml
---
artifact: compound-interest-walkthrough
title: How compound interest works, and why the second account wins
type: walkthrough            # walkthrough | cheat-sheet | reference | map | …
subjects: [money.investing]  # tracked subjects it explains
perspective: personalized    # generic | personalized
made_for: choosing between two savings accounts
rests_on: [knowledge:money.savings]   # optional: facts it's built on
sharing: private             # private | protected | public; only generic may be opened up
created: 2026-10-14
updated: 2026-10-14
---
```

| Key | Holds |
|---|---|
| `artifact` | The name; matches the file. Unique across the library, groups and archive included |
| `title` | One line saying what it explains |
| `type` | What shape it is. The list grows as the human needs new shapes: a map of a system, a breakdown of a change |
| `subjects` | The subjects it explains, by name. Can be untracked subjects too |
| `perspective` | `generic` (true for anyone) or `personalized` (built on this human's situation) |
| `made_for` | The context it was made in, in a few words |
| `rests_on` | Knowledge it's built on. Optional; used to tell when it's stale |
| `sharing` | `private` until the human opens it up. Only a generic artifact can be |
| `created`, `updated` | When it was made, and last revised |

## Drafts

**An explanation made while working is a draft until it's tagged.** It lives in the library from the start, with its body and whatever tags are known; an artifact missing `type`, `subjects` or `perspective` is a draft. The index lists drafts apart, and the sphere offers once, at ground, to finish tagging them: *"Two drafts in the library. Tag them now?"*

*Why no separate drafts folder:* whether it's a draft is already visible in its fields. A second place would be a second thing to keep in step.

## Staleness

**An artifact goes stale when what it explains changes.**

- **A topic in `rests_on` updated after the artifact's `updated`** makes it suspected stale, computed by the index. Nobody marks it.
- **A subject it explains, marked stale for an outside change** (see [skill-progress](skill-progress.md#staleness-is-computed)), makes it stale too.
- **Stale artifacts are flagged, never silently served.** Opening one says so: *"This predates the rate change in September."* Offer to revise it. Fire `artifact-stale`.

**Revising** rewrites the body, sets `updated`, and adds a line to the revisions.

## Browsing

*"What's in my library?"* lists artifacts from the generated index, newest first, one line each: title, type, subjects, and whether it's stale or a draft. *"Anything on Rust?"* filters by subject, type or group. **Reading the index never opens bodies.**

The literacy index (`layers/literacy/index.md`) is generated from subject and artifact frontmatter. A browsable page of the library is a projection of that index.

## The perspective decides what may be shared

| Perspective | In the sphere | Outside it |
|---|---|---|
| **Generic** | Available to the human, always | **May** be shared, at a level the human chooses, through the [outbound guard](../human-is-highest/outbound-guard.md) |
| **Personalized** | Available to the human, always | **Never.** It carries the human's situation inside it |

- **Tag the perspective when it's made.** It's the line that makes sharing safe later; guessing it afterwards is how a personalized artifact leaks.
- **Opening an artifact up is an outbound act.** It's drafted, shown and approved like any message, and `sharing:` changes only on the human's yes.
- **An artifact that mixes both** is personalized. To share the general part, make a generic copy without the human's situation in it, and share that.
- **Facts about other people** never appear in an artifact that's shared.
- **Between spheres,** a generic artifact the human has opened up is what a trusted sphere may read. A personalized one never travels. See [replication](../../../../../spec/replication.md#trusted-spheres--decided-not-yet-exercised).

## Retiring

An artifact nobody needs any more, or one replaced by a better one, moves to `library/archived/` (keeping its group folder, if it had one) with a last revision line saying why. Links to it still resolve by name.

## When / do

| When | Do |
|---|---|
| An explanation is worth keeping | Write it to the library with every tag that's known. Fire `artifact-added` |
| *"Save this as a cheat sheet"* | Write it, `type: cheat-sheet`, tagged. Fire `artifact-added` |
| Ground, with drafts in the library | Offer once to tag them |
| What an artifact rests on has changed | Flag it when opened; offer to revise. Fire `artifact-stale` |
| *"What's in my library?"* | List from the index, one line each |
| The human wants to share an artifact | If generic: draft the share through the outbound guard. If personalized: say why not; offer a generic version |
| An artifact is retired | Last revision line; move to `archived/` |

## Works with

- [teaching](teaching.md): where artifacts come from.
- [skill-progress](skill-progress.md): the subjects artifacts explain, and stale marks.
- [outbound-guard](../human-is-highest/outbound-guard.md): sharing an artifact is sending it.
- [kinds-of-file](../nodes/kinds-of-file.md): an artifact is current state with its revisions as history; the index is generated.
- [node-shape](../nodes/node-shape.md): retiring an artifact is finishing it.

## Senses

| Sense | Fires when |
|---|---|
| `artifact-added` | an artifact is written to the library |
| `artifact-stale` | an artifact is found to predate a change in what it explains |
