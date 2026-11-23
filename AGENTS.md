# Sphere repository

You are inside the **sphere** repository: not a running sphere, but the workshop spheres are built from.

**What's here:**
- `builds/`: ready-to-assemble spheres. `base` is the one to start from.
- `common/`: the lenses, frames, templates and shared pages every build starts from.
- `scripts/`: the tools. `scripts/new-sphere` assembles a sphere from a build, and `scripts/update-sphere <folder>` brings an existing sphere's tools up to date; the rest ship inside every sphere.
- `spec/`: the architecture, a chapter per concern. `ARCHITECTURE.md` is the overview.

**What the person probably wants:** a sphere of their own. Help them make one:

1. Ask where it should live (a new or empty folder), then run `scripts/new-sphere base <folder>`.
2. Tell them to open that folder in their AI tool and say hello. The sphere's first conversation sets it up with them; you don't need to.

If they want to understand sphere first, point them to `README.md`; for the internals, `ARCHITECTURE.md` and `spec/`.

**This repo is a workshop, not a workspace.** It has no profile, no state and no layers of its own. Don't run it as a sphere.
