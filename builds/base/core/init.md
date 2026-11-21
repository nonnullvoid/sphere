# The first conversation

_Read this when `core/identity.json` has an empty `id`. It replaces the startup sequence once, and then never runs again._

This is the human's first time here. **Talk about their life and work, never about the structure.** They never need to hear the words lens, frame, node or manifest. Keep it to about ten minutes. Everything you write, you show them first and write on their yes.

## 0. Set up, quietly

Before saying anything, make this folder a sphere:

```
scripts/sphere init --git
```

If git isn't installed, run `scripts/sphere init` instead, and later tell the human in one line that undo needs git and you can set it up whenever they like. Don't mention anything else about this step.

## 1. Hello, and who they are

Say hello in a line or two: you're the AI they'll work with here, and this folder is where you'll keep what you learn together, so they never have to repeat themselves.

Then ask, one question at a time:

- **What should I call you?**
- **What would you like help with?** Work, a project, keeping life organized, learning something. Whatever comes first.
- **How do you like to work with someone?** Short or detailed, when to push back, anything to never do.

Draft [`core/user/profile.md`](user/profile.md) from their answers, **in their words, not yours**. Show it, change what they want changed, and write it on a yes.

## 2. Names

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

## 3. One principle, together

This is the moment that shows them how the sphere grows. Ask:

> *"Is there one thing you'd always want me to keep in mind when I help you? A rule of thumb, something you care about, something that's gone wrong before."*

Draft it **with** them as the first principle in [`core/protocol/lenses/principles.md`](protocol/lenses/principles.md): the principle in their words, then a line on why, then when it applies. Read it back. Adjust until they say it's right. Then set `verified: true` and today's date in `updated:`, because they've confirmed it.

Tell them, in one line, that this is how the sphere learns: when they correct you or explain how they think, you'll offer to keep it the same way.

## 4. What's on their plate

Ask what they're working on right now. For each thing they name (one to three is plenty):

- a work node in `layers/work/<name>/`: a `work.md` with its title, `state: active` and a one-line summary, and a first `progress.md` entry (see [work-breakdown](protocol/frames/work-tracking/work-breakdown.md));
- names follow the work tree's scheme: lowercase words and hyphens, dots for areas (`home.kitchen`).

If one of them is what they want to start on now, open a focus for it: `scripts/sphere open <name> -i "<intention>" --holds work:<name> --attach`.

## 5. Build what the sphere generates

Now that the sphere has its own content, build its generated files from it:

1. **The manifest,** [`core/manifest.md`](manifest.md), following the [capability-manifest](protocol/frames/sphere-framework/capability-manifest.md) frame: a line per lens and frame, the *Always on* list, then the reactions table. Put `scripts/manifest-check --hash` in its header.
2. **The work index,** [`layers/work/index.md`](../layers/work/index.md), from the work nodes' frontmatter.
3. **The views:** the sphere's name into `surface/projections/assets/registry.js`, then render `today` and `work-dashboard` (their definitions in `layers/projections/` say what each shows), stamping `rendered` in the mirror.

Then run `scripts/structure-check` and `scripts/manifest-check`, and fix anything they report.

## 6. The first ground

Ground: `scripts/sphere ground`. Tag it with the first version: `git tag sphere-<version>`.

## 7. Show them, and how to come back

- Open [`surface/projections.html`](../surface/projections.html) for them: *"These are your things. They'll fill in as we go."*
- Tell them how to come back: open this folder in their AI tool any time and say *"where was I?"*. Say *"save"* whenever they want to lock something in, and *"wrap up"* at the end of a day.

That's all. Don't explain anything else unless they ask.
