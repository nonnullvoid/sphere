# The first conversation

_The first conversation, in place of the startup sequence. It runs once; its last step makes sure it never runs again._

This is the human's first time here. **Talk about their life and work, never about the structure.** They never need to hear the words lens, frame, node or manifest, or any file name, field or script. Keep it to about ten minutes. Everything you write, you show them first and write on their yes.

**Work quietly.** Never put a line of text before or between your reads and commands: no *"checking…"*, no *"reading…"*, no *"setting up…"*. Do the work, then say the next thing that's for them. A technical line out of nowhere reads as something running without their say.

## 1. Hello first

**Your first message is the hello.** Nothing comes before it: no reading, no checking, no running anything. Everything you need for it is on this page.

Say hello in a line or two: you're the AI they'll work with here, and this folder is where you'll keep what you learn together, so they never have to repeat themselves. Add one line on how keeping works: what they agree to is written down as you go, and they can say *"save"* any time to lock it in. Then ask the first question below.

**If `AGENTS.md` says setup has started,** this is a later window and the first conversation didn't finish (the window closed, or they stopped for the day). What they agreed to is still here. Your first message welcomes them back in a line and says you'll pick up where you left off; nothing comes before it here either. Then look at what's on disk (the profile, a name in `core/identity.json`, a principle, work nodes, open foci) and go on from the first step that isn't done.

## 2. Set up, after their first answer

Once they've answered, and before your next question:

1. In `AGENTS.md`, under *First run*, add the line: `**Setup has started and isn't finished.** Welcome them back and pick up where you left off (core/init.md, step 1).`
2. Make the folder a sphere: `scripts/sphere init --git`. If git isn't installed, run `scripts/sphere init` instead, and later tell them in one line that undo needs git and you can set it up whenever they like.

## 3. Who they are

Ask, one question at a time (the first is in your hello):

- **What should I call you?**
- **What would you like help with?** Work, a project, keeping life organized, learning something. Whatever comes first.
- **How do you like to work with someone?** Short or detailed, when to push back, anything to never do. And, lightly: how at home are they with computers and files?

Draft [`core/user/profile.md`](user/profile.md) from their answers, **in their words, not yours**. Show it, change what they want changed, and write it on a yes.

Then, without mentioning it, set where they start with the sphere itself, in [`layers/literacy/sphere/subject.md`](../layers/literacy/sphere/subject.md): `tracked:` and `updated:` today, and a first *stated* evidence entry with what they said. Leave `level: skimmed` unless they're clearly at home with files and tools (a developer, say): then `can-use`, and the summary says so. That level decides how much you explain from here on.

## 4. Names

- **The AI's name.** Offer to keep *Companion* or pick another. On a new name, rename `core/ai/personas/companion/` and its file to match, and the `persona:` key with it.
- **The sphere's name.** Suggest one from what they've told you (*"Maya's sphere"*, *"the workshop"*); they decide.

Then write [`core/identity.json`](identity.json):

- `id`: a new UUID v7, made once and never changed:
  ```
  python3 -c "import os,time;t=int(time.time()*1000);b=bytearray(t.to_bytes(6,'big')+os.urandom(10));b[6]=(b[6]&0x0F)|0x70;b[8]=(b[8]&0x3F)|0x80;h=b.hex();print(f'{h[:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:]}')"
  ```
- `name`: the sphere's name.
- `version`: this year and month, then `.1` (`2026.11.1`).
- `born_from`: leave as it is.

## 5. One principle, together

This is the moment that shows them how the sphere grows. Ask:

> *"Is there one thing you'd always want me to keep in mind when I help you? A rule of thumb, something you care about, something that's gone wrong before."*

Draft it **with** them as the first principle in [`core/protocol/lenses/principles.md`](protocol/lenses/principles.md): the principle in their words, then a line on why, then when it applies. Read it back. Adjust until they say it's right. Then set `verified: true` and today's date in `updated:`, because they've confirmed it.

Tell them, in one line, that this is how the sphere learns: when they correct you or tell you how they like to work, you'll offer to keep it, each in the place it belongs.

## 6. What's on their plate

First, quietly, open the focus for getting to know the sphere, so it's the first one: `scripts/sphere open getting-started -i "Get comfortable using the sphere" --holds literacy:sphere`. If they're already at `can-use`, don't open it; offer it in step 9 instead.

Then ask what they're working on right now. For each thing they name (one to three is plenty):

- a work node in `layers/work/<name>/`: a `work.md` with its title, `state: active` and a one-line summary, and a first `progress.md` entry (see [work-breakdown](protocol/frames/work-tracking/work-breakdown.md));
- names follow the work tree's scheme: lowercase words and hyphens, dots for areas (`home.kitchen`).

If one of them is what they want to start on now, open a focus for it: `scripts/sphere open <name> -i "<intention>" --holds work:<name> --attach`.

## 7. Build what the sphere generates

Now that the sphere has its own content, build its generated files from it:

1. **The sphere's name** into `surface/projections/assets/registry.js` (`name:`).
2. **The work index and the views:** `scripts/sphere render`. It builds them from the work items and the rules in each view's definition; from here on, every ground does it.

Then run `scripts/sphere manifest` (their principle changed a lens), `scripts/structure-check` and `scripts/manifest-check`, and fix anything they report.

## 8. The first ground

First, retire this conversation: remove the `@core/init.md` line from `CLAUDE.md` (leave its other lines) and the whole *First run* section from `AGENTS.md`, the setup-started line included. From now on, a window starts from `sphere.md`.

Then ground: `scripts/sphere ground` (act on what it prints, then again with `--reacted --did "…" --next "…"`, saying in a line what the first conversation did). Tag it with the first version: `git tag sphere-<version>`.

## 9. Show them, and how to come back

- Open [`surface/projections.html`](../surface/projections.html) for them: *"These are your things. They'll fill in as we go."*
- Then the first basics, by doing them, not by explaining them: suggest they open a **new window** here and say *"where was I?"*, to see it pick up. That's two basics at once (one window per thing, and picking up); tick them in the subject when they've done it. Leave the rest for when they come up.
- If they started at `can-use`, offer the getting-started focus in a line instead, and open it only on a yes.

That's all. Don't explain anything else unless they ask.
