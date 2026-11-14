---
frame: focus-holds
kind: structural
lens: [focus, continuity]
derives_from: [focus@1, continuity@1]
version: 1
version_note: First draft. Holds, soft claims, writing by kind.
status: drafting
updated: 2026-11-11
sharing: public
reads: [layers/focus]
writes: [layers/focus]
protocol: [I-never-overwrite-unseen, A-hold, A-offer-change, hold-claimed]
---

# What a focus holds

**Applies to:** every write a focus makes, and every focus that tries to hold something.

## Holds

- **`holds:` is the focus's scope: the nodes it's pursuing, never a list of files.** A held node covers everything in its folder. Name the most specific node that covers the work: `work:home.kitchen.plumbing`, not each file inside it, and not all of `work:home`. For something outside any node, name its folder.
- **Git can't tell which window changed a file,** so ground goes by holds. It commits what this focus holds and lists other changed files no focus holds (left for main); it never stops on them. **Ask "hold it too?" only about files this window edited:** *"I also changed the budget sheet. Hold budget work in f21 too?"*
- **The most specific hold wins.** If f20 holds `work:home` and its child f21 holds `work:home.kitchen.plumbing`, plumbing's files are f21's. A child rarely needs to edit its parent's holds.
- **Say "in focus", not "held".** To the human, something is *in focus* when an open focus holds it. "Hold" is the mechanism's word.

**Holds do three jobs:**
1. **Loadout.** What a focus holds, plus the lenses it works through, decides what's warmed when a window attaches.
2. **Writing.** A focus writes directly only to what it holds, plus its own `focus.md` and `history.md`.
3. **Seeing overlap early,** when it's claimed, not later as a merge conflict.

## Claims are soft

When a focus tries to hold something another open focus already holds:
- **Ask, through the parent:** *"Plumbing is already in focus in f20-kitchen-renovation. Ask it, or just read?"*
- **Never refuse.** The human can say "both." Then the overlap is handled like any content conflict: proposed, never silent.
- **Reading is never claimed.** Any focus can read anything.

## Writing by kind

Every file is one of [four kinds](../nodes/kinds-of-file.md): current state, history, reference, generated. **Write only to what you hold; anything else is appended, offered, proposed or rebuilt.** For a focus:

- **Its holds and its own two files are the current state it may rewrite.**
- **Reference proposals stay in its own folder** until confirmed, so two foci proposing facts about one topic never touch the same file.
- **Two proposals about the same fact** are a real disagreement, not a file conflict. Show them as one question: *"f31 says 2 of 4 payments are made; f32 says 3 of 4. Which is right?"*
- **A compile holds its topic while it runs.** *"Compile what we know about the house from the inspection report"* is a large batch for one topic, so a second compile into it gets the claim question before it starts.

## When / do

| When | Do |
|---|---|
| About to write a file | Is it current state this focus holds, its own record, history to append, reference to propose, or generated? Act by kind |
| About to write current state another focus holds | Don't. Offer the change to the holder, as an entry in your own history |
| Opening a focus whose holds overlap an open one | Ask through the parent; never refuse. Fire `hold-claimed` |
| Ground finds other changed files no focus holds | List them in one line, left for main. Don't stop |
| This window edited a file outside the holds | Ask once whether to hold it too |
| Two proposals disagree about one fact | Show them as one question |

## Works with

- [kinds-of-file](../nodes/kinds-of-file.md): the four kinds, and how each is written.
- [focus-tree](focus-tree.md): a child takes part of its parent's hold by carving it.
- [check-shared-state](../continuity/check-shared-state.md): applies to everything that isn't held, especially reference files and anything outside the sphere.
- [propose-dont-decide](../human-is-highest/propose-dont-decide.md): why reference files are proposed, never written.

## Senses

| Sense | Fires when |
|---|---|
| `hold-claimed` | a focus tries to hold something another open focus holds |
