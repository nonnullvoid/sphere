# This sphere's build: homesphere

_Read during the first conversation (setup step 2), and by `sphere start`. It says what this build adds to base, and where._

## What it adds

- **Plain words, always.** The companion's default operating mode is [non-technical](operating-modes/non-technical.md): nothing about the sphere's workings reaches the human. The sphere does all of it underneath, as in any build.
- **Saving that just happens.** The sphere saves at natural stopping points without asking, and says *"Saved."* Setup still teaches *"save"*, so they know they can lock something in any time; *"undo that"* always works.
- **Two pages to see their things:** **Home** (`today`: what's waiting on them, what's on the go, recent wins) and **My things** (`work-dashboard`: everything they're looking after, on the go, coming up, done lately). Both are drawn from their rules in `layers/projections/`. To them these are just pages, never projections.
- **No permission prompts for the sphere's own tools,** in tools that read `.claude/settings.json`: its scripts are pre-approved, and so are file edits inside this folder, once they've said they trust the folder. Nothing outside the sphere's scripts is.

## Setup

Adds to [`init.md`](init.md):

- **Step 1, hello:** keep the line about saying *"save"*, and add that you also save on your own as you go, so nothing's lost if they forget.
- **Step 2, git:** if git isn't installed, run `scripts/sphere init` and say nothing about it. If they ever ask to undo something, say that undo needs one more piece installed, and offer to help with it then.
- **Step 3, who they are:** skip the question about computers and files. Their level stays `skimmed`, unless they make clear they're at home with files and tools.
- **Step 9, show them:** open Home for them (`scripts/sphere show today`): *"This is your home page. It fills in as we go."* For the new window, use their app's own word: a new chat, a new conversation.

## Anchors

- **The wrap:** when they say they're done for now, a line on what got done, and save. Offer once, in a line, whether anything's worth remembering as a win.

## Startup context

- **anchors this sphere keeps:** `core/build.md#Anchors`
