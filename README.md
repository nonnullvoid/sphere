# Sphere

**Give your AI a persistent home.**

A folder of plain files your AI reads when a conversation starts, so every conversation begins oriented, not blank. You can open, read and change every one of them.

---

## What it looks like

Open your sphere in a new window and ask *"where was I?"*:

```
Hi Kane. You're on the recipe app: the stack is still open, and you were
leaning towards Next.js with SQLite. Next: decide who it's for. The kitchen
renovation is waiting on the contractor's quote.
```

No re-explaining. It knows who you are, what you're working on, how you like to work, and what you decided last time, because all of that is in the folder.

---

## How it works

1. **Make a sphere** from a build: `scripts/new-sphere base ~/my-sphere`.
2. **Open it in your AI tool and say hello.** The first conversation sets it up with you: who you are, what you'd like help with, one principle in your own words, what's on your plate. About ten minutes.
3. **Work, and say *save*.** Each thing you're working on gets its own window. Saving keeps it, so any new window can pick up where you left off.

Everything is plain markdown and a few small scripts. No servers, no accounts. Git keeps every change, and any save can be undone.

---

## Get started

```bash
git clone https://github.com/nonnullvoid/sphere.git
sphere/scripts/new-sphere base ~/my-sphere
cd ~/my-sphere && claude      # or open the folder in any AI tool that reads AGENTS.md
```

Then say hello.

Or open the cloned `sphere/` folder with your AI and ask it to set one up for you.

**Keeping it current:** after a `git pull` here, `sphere/scripts/update-sphere ~/my-sphere` brings your sphere's tools up to date. It changes nothing you and your AI have written.

---

## Builds

| Build | What it is |
|---|---|
| [`base`](builds/base/) | Everything a sphere needs: focus, work, knowledge, ideas, literacy, a growth ledger, and two pages (Today and Work). Start here |
| [`lifesphere`](builds/lifesphere/) | Base, for a whole life: life areas and habits, a Life page, the morning and weekly anchors, and a place for what you come to see and value |

Each build is assembled from [`common/`](common/) (and a build can extend another: lifesphere extends base): the lenses and frames that say how a sphere works, shared templates and pages, and the tools in [`scripts/`](scripts/).

---

## Going deeper

[ARCHITECTURE.md](ARCHITECTURE.md) is the overview: what's in a sphere and how it runs. [`spec/`](spec/) has a chapter per concern: focus, nodes, state, work, knowledge, loading, the protocol of lenses and frames, and more. [BUILDING.md](BUILDING.md) is for making a build of your own.

---

## Requirements

- **An AI tool that can read files and run commands in a folder:** Claude Code, Codex, or similar
- **Python 3.9 or later**, for the sphere's scripts
- **git**, for undo and history (recommended)

---

## License

MIT
