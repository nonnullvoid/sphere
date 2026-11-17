---
frame: growth-themes
lens: [growth-tracking]
derives_from: [growth-tracking@1]
version: 1
version_note: First draft. What a theme owns, where its records live, honest scoring, standing computed from the ledger, milestones, and swapping.
status: drafting
updated: 2026-11-13
sharing: public
reads: [layers/witness, layers/work, layers/literacy]
writes: [layers/witness]
protocol: [I-see-myself-grow, A-choose-theme, A-swap-theme, A-check-standing, milestone-reached, theme-swapped]
---

# Themes

**Applies to:** choosing a theme, every ledger entry while one is in use, *"where am I?"* in the game, a milestone, and swapping one theme for another.

## A theme is optional

**A theme is one way to show growth, never required.** Without one, the sphere shows the ledger plainly (see [growth-ledger](growth-ledger.md#the-plain-view)), and nothing is missing. A human who'd enjoy a game gets one; a human who wouldn't never sees the word.

## What a theme owns

**A theme isn't a skin over a fixed set of mechanics. It owns the whole growth model:**

| Part | For example |
|---|---|
| **Currency** | what an entry earns: seeds, coins, experience |
| **Progression** | how currency becomes levels, stages, unlocks |
| **Standing** | what reputation means in the game, if it has any |
| **Look** | the metaphor, the names, the marks, the view |
| **Milestones** | which moments deserve a celebration |

A garden theme might grow plants from finished work and bloom them at milestones; a craft theme might level up skills. **Swap the theme and all of that swaps with it.** Work nodes still store their own state; the theme decides what that state means for growth, and how it's shown. It can show work states with its own marks; the state underneath never changes.

- **A theme brings its own frames,** deriving from this lens, and lives in `layers/witness/<theme>/`. There's no shared shape themes must fit, beyond the rules below.
- **A theme is private.** Its content, and what it says about the human, stay in the sphere like the rest of the witness layer.

## The rules every theme keeps

**The fact is kept once, in the ledger.** A theme never restates it. Its record holds only what the theme adds: a score, a name in the game, a stage reached. **The theme's record names the ledger entry it came from**, and nothing in the theme exists without one.

| Record | Holds | Written by | Kind of file |
|---|---|---|---|
| **The ledger entry** | what happened, when, the evidence | the [growth ledger](growth-ledger.md#what-writes-an-entry), whatever theme is in use | history |
| **The theme's record** | what the theme makes of it, pointing at the entry | the theme's own frames | history |
| **Standing** | totals, levels, stages | nobody: computed from the theme's records | generated |

```markdown
### 2026-11-12 · kitchen-plumbing
ledger: 2026-11-12 · home
score: 5 (scope 2, novelty 2, stakes 1)
grew: a second mushroom in the home bed
```

- **The theme is responsible for its records,** and only those. The ledger is written the same way with or without a theme.
- **Why keep a theme record at all, rather than compute it?** Scoring applies a rubric with judgment, and a judgment worked out again next week could come out differently. Writing it down once keeps the game stable and checkable. A theme whose rubric is purely mechanical can skip its records and compute everything from the ledger.
- **Swapping themes reads the ledger, not the old theme's records.** That's why the fact lives in the ledger alone.

**Every score says how it was scored.** A theme scores on an explicit rubric, written in its frame, and each record carries the line that shows the working: *`score: 5 (scope 2, novelty 2, stakes 1)`*. The human can challenge any of it. *Why:* a score nobody can check is a number someone made up.

- **Inflation kills the signal; stinginess kills the momentum.** If every entry earns the top score, or nothing ever does, the rubric is wrong. Say so at the weekly look back and propose a change.
- **Effort the human can't see isn't scored.** Points come from what happened, never from how busy the sphere was.

**Standing is computed, never kept by hand.** Totals, levels and stages are worked out from the theme's records. Reputation, if the theme has it, is derived from what already says how others see the human (the human's own record of position, where the build keeps one), never a third table kept up beside them. A real outside signal that the derivation misses is fixed at its source, not patched into the theme.

**Growth reads work and position; it never stores them.** A *"recently finished"* list is read from the work layer. A role or a level at work is read from the human's own record. Copies drift.

## Milestones

**Quiet by default, loud on milestones.** The theme decides what a milestone is: a level reached, a stage completed, a lane's first entry in a long while. Without a theme, a milestone is a finished project, or a subject reaching a new level.

- **A milestone gets one line of celebration,** at the ground or anchor where it's noticed: *"That's the kitchen done. Twelve things finished since September."* Fire `milestone-reached`.
- **Day-to-day entries get none.** *Why:* a theme that chatters gets muted, and then it shows nothing.
- **Never invent a milestone** to cheer a quiet week.

## Choosing and swapping

**Choosing a theme is co-authored,** like any change to the sphere. The sphere can propose a few, in a line each; the human picks, or describes their own. Then the theme's growth model, rubric, look and frames are drafted with them, and land only on their yes.

**Swapping is building a new theme, not finding and replacing words.** The new theme's model is drafted coherently, as a whole.

- **The ledger is untouched.** It survives every swap.
- **The new theme can replay the ledger** from the start, so the human begins where their growth really is, not at zero. Offer it; the human decides.
- **The old theme's records move to `layers/witness/archived/<theme>/`,** kept, never deleted.
- **Dropping a theme entirely** is a swap to the plain view.

Fire `theme-swapped`.

## When / do

| When | Do |
|---|---|
| The human wants growth shown as a game | Propose a few themes; draft the chosen one with them; land it on a yes |
| A ledger entry is appended, with a theme in use | Write the theme's record: named entry, score with its working |
| *"Where am I?"* | Compute standing from the theme's records; show it in the theme's terms |
| A milestone is reached | One line of celebration. Fire `milestone-reached` |
| Scores look inflated or stingy | Raise it at the weekly look back; propose a rubric change |
| A real outside signal outruns the derived standing | Update the source it's derived from |
| The human wants a different theme | Draft the new one whole; offer to replay the ledger; archive the old records. Fire `theme-swapped` |
| The human wants no theme | Archive its records; show the plain view |

## Works with

- [growth-ledger](growth-ledger.md): every theme record names a ledger entry.
- [work-progress](../work-tracking/work-progress.md): the marks a theme may replace are display only.
- [propose-dont-decide](../human-is-highest/propose-dont-decide.md): choosing, swapping and rubric changes are proposals.
- [kinds-of-file](../nodes/kinds-of-file.md): theme records are history; standing is computed.

## Senses

| Sense | Fires when |
|---|---|
| `milestone-reached` | a theme's milestone, or a plain one, is reached |
| `theme-swapped` | a theme is chosen, replaced or dropped |
