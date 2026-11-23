# Builds

A build is a ready-to-assemble sphere: a folder of only what it adds, laid over the common set by `scripts/new-sphere <build> <folder>`.

| Build | What it is |
|---|---|
| [base](base/) | Everything a sphere needs: focus, work, knowledge, ideas, literacy, a growth ledger, and the Today and Work pages. Every other build extends it |
| [lifesphere](lifesphere/) | Base, for a whole life: life areas and habits, a Life page, the morning and weekly anchors, and a place for what you come to see and value |

## How a build is put together

`new-sphere` assembles, in order: the common lenses and frames (`common/core/protocol` → `core/protocol`), the shared pages and templates (`common/surface`, `common/layers`), the build's own files, which win where both have one, and the tools (`scripts/`). It then builds the capability manifest from what it copied.

- **`core/build.json`** says what the build is: its name and version, the architecture it was built for, the lenses it ships (`"all"` or a list), its layers, views and anchors, and its word for saving.
- **`"extends": "<parent>"`** lays the build over another: the parent's files first, then its own. `lifesphere` extends `base`, so it holds only what it adds or changes.
- **`core/build.md`** is what the sphere itself reads about its build. *What it adds*; *Setup*, the steps of base's first conversation it adds to (read during setup); *Anchors*; and *Startup context*, extra lines `sphere start` prints in every window. A build without one is base as it is.
- **A view** is a definition in `layers/projections/` whose Panels rows carry **rules**, plus its page under `surface/projections/`, and an entry in the projection registry and its mirror. `sphere render` draws it; nothing about it is in code.
- **The build's `README.md`** stays here, in the repository.

`scripts/tests/test_build.py` assembles every build, inits it, and checks it comes out clean.
