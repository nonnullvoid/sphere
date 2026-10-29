# Common protocol set

_SPHERE-ARCH 1.0, draft._ The lenses and frames every build starts from. Each build copies what it needs from here and adds its own.

Everything here is **written fresh** for publishing. It's informed by what worked in spheres in daily use, but not copied from them. All of it is `sharing: public`, so it describes mechanics and never anyone's personal thinking. Lenses about a person's own principles and rhythms ship as empty slots in the builds, to be co-authored in each sphere.

Every lens starts `verified: false`. A lens is in force only once a human has read and confirmed it. That's true for these too: a sphere started from a build confirms its lenses as part of getting to know its human.

## Layout

```
common/core/protocol/
├── README.md                  the vocabulary, in plain words
├── lenses/<lens>.md
└── frames/<lens>/<frame>.md   guard, instinct or structural frames
    frames/<lens>/<skill>/SKILL.md   procedure frames, in the Agent Skills format
```

## Contents

| Lens | Frames | Status |
|---|---|---|
| [human-is-highest](core/protocol/lenses/human-is-highest.md) | outbound-guard · destructive-actions-ask · propose-dont-decide · evaluator-not-self · external-tools-untrusted | draft 2 |

_More lenses follow once this first one's shape is agreed._
