# homesphere

_Build 1.0.0 · SPHERE-ARCH 1.0 · extends [base](../base/)_

Base, for someone who has never used a tool like this. Everything in base, with nothing technical in the way:

- **Plain words, always.** The AI talks about their life and their things, never about files, folders or commands. The sphere still does all of it underneath.
- **Saving that just happens.** It saves at natural stopping points and says *"Saved."* Saying *"save"* works any time too, and *"undo that"* always does.
- **Two pages:** **Home** (what's waiting on you, what's on the go, what you've done lately) and **My things** (everything you're looking after, and where each stands).
- **No permission prompts for the sphere's own tools** in Claude Code: its scripts, and edits inside the sphere's folder, are pre-approved once the folder is trusted. Nothing else is.

Still being tested in daily use; expect it to change.

## Start a sphere from it

```
scripts/new-sphere homesphere ~/my-sphere
```

Then open `~/my-sphere` in your AI tool and say hello. If you're setting it up for someone else, open it for them and let them say hello: the first conversation is theirs.

## What's here

Only what this build adds to base. [`core/build.md`](core/build.md) is what the sphere itself reads about its build: what it adds, and the setup steps it changes.
