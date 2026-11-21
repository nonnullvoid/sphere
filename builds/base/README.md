# base

_Build 1.0.0 · SPHERE-ARCH 1.0_

The week-one starter, and the build every other one derives from. It ships the whole common protocol set (17 lenses with their frames), an empty slot for the human's principles, one persona (*Companion*), two operating modes (*everyday*, *planning*), seven layers (focus, work, knowledge, ideas, literacy, witness, projections) and two views (*Today* and *Work*).

## Start a sphere from it

```
scripts/new-sphere base ~/my-sphere
```

Then open `~/my-sphere` in your AI tool and say hello. The first conversation ([`core/init.md`](core/init.md)) gets to know you, writes your first principle with you, puts what you're working on into the sphere, and shows you your things. It takes about ten minutes.

## What's here

This folder holds only what the build adds. `new-sphere` lays it over the common set (`common/`) and copies in the tools (`scripts/`), so the lenses and frames are written once and every build stays in step with them. Its [`core/build.json`](core/build.json) says what it includes. This README stays in the repository.
