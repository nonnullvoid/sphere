---
frame: node-names
lens: [nodes]
derives_from: [nodes@1]
version: 1
version_note: First draft. Named naming schemes and when each fits; names never reused; links and lists of links.
status: drafting
updated: 2026-11-16
sharing: public
reads: []
writes: []
protocol: [I-one-way-to-read-anything]
---

# Node names

**Applies to:** naming any node, choosing how a new tree names its nodes, adding a naming scheme, writing a link, and renaming.

## The characters

Every name is **lowercase letters, digits and hyphens, with dots between namespace levels.** Every scheme below stays inside that.

## Naming schemes

A tree names its nodes by one scheme. Each scheme has a name, so a tree can say which one it uses and a new tree can pick one on purpose.

| Scheme | Shape | Example | Fits | Trade-off | Used by |
|---|---|---|---|---|---|
| **`plain`** | a few words | `outbound-guard`, `sage` | Things with no place in a hierarchy and no order: definitions that are looked up by name | Says nothing about where it sits; the words are the whole identity | lenses, frames, agents, personas, operating modes, projections, plans |
| **`namespace`** | words, dot, words | `money.taxes.2025-return` | Things arranged by how the world is, which rarely move. The name *is* the place in the tree | Moving the node means renaming it | knowledge topics, literacy subjects, library groups, work areas |
| **`prefix-number`** | a prefix, then a running number | `tax-20`, `dubai-trip-21` | Work that recurs, or may move around the tree | Says less about what it is; never changes when it moves | work |
| **`number-name`** | a number, then a few words | `f21-kitchen-renovation` | Things that shift over time: the number is the identity, the words can be renamed as the thing changes | Two parts to remember, though people use either | focus |
| **`dated`** | the date, then a few words | `20261116-weekly-summary` | Things whose order of arrival matters and that are captured in quick succession | The date is fixed even when the thing matures | ideas |

**Choosing for a new tree:**

1. **Is its place in a hierarchy the thing itself, and does it rarely move?** → `namespace`.
2. **Will it shift or be renamed while staying the same thing?** → `number-name`.
3. **Does it recur, or move around a tree?** → `prefix-number`.
4. **Does the order of capture matter?** → `dated`.
5. **Otherwise** → `plain`.

A tree's pattern is written once, in its `name` line in `core/shapes`. Most trees use the characters above; `dated` adds its own pattern (`^\d{8}-…`).

## Adding a scheme

A new scheme is a sphere change, made in [sphere authoring](../modes/sphere-authoring.md) like any other. It's added **here**, as a row in the table: its name, its shape, an example, when it fits, its trade-off and the trees that use it. Then its pattern goes into the `name` line of each tree that uses it, in the same commit. A scheme that exists only in one tree's shape, without a row here, is drift: the next evolution session can't tell why it exists or whether to reuse it.

## Rules

- **Unique across the tree, archive included.** A finished node keeps its name, and links resolve by name, so a name is never given to anything else. Group folders don't make a second namespace: a library artifact's name is unique across all its groups. _The one exception:_ a focus number freed by a revert can be used again (see [focus](../../../../../spec/focus.md#names-a-number-and-a-memorable-name)).
- **Says what it is.** Short, plain words a person would search for.
- **Renaming is a refactor.** The tooling fixes links inside the sphere in the same commit. References written outside the sphere won't follow, so a stable name is worth choosing once. `number-name` exists for things that need renaming.

## Links

- **A link is `tree:name`** (`work:tax-20`). Within the same tree, the bare name is enough.
- **A list of links** (`related:`) uses the same two forms, mixed freely: `[money.investing, work:tax-20]`. The shape check checks every item.
- **A list of descriptions isn't links.** Fields the AI reads rather than follows, such as an operating mode's `signals` or a library artifact's `type`, stay free text and aren't checked.

## Checking

The [shape check](../readable-substrate/structure-check.md) checks every name against its tree's pattern and reports a name used twice in one tree, the archive included. Listing the archive reads folder names only, so it stays cheap.

## When / do

| When | Do |
|---|---|
| Making a node | Name it by its tree's scheme, unique in the tree, archive included |
| A name is taken by an archived node | Choose another; never reuse it |
| Designing a new tree | Pick a scheme with the questions above; write its pattern in `core/shapes` |
| No scheme fits | Add one here first, with its row, then use it |
| Renaming | Rename, and fix every link inside the sphere in the same commit |
| Writing a link to another tree | `tree:name` |

## Works with

- [node-shape](node-shape.md): a node's parts, and where its tree lives.
- [structure-check](../readable-substrate/structure-check.md): checks names and their uniqueness.

## Revision history

- **v1:** First draft.
