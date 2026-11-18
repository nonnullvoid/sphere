# Common protocol set

_SPHERE-ARCH 1.0._ The lenses and frames every build starts from. Each build copies what it needs from here and adds its own.

Everything here is **written fresh** for publishing. It's informed by what worked in spheres in daily use, but not copied from them. All of it is `sharing: public`, so it describes mechanics and never anyone's personal thinking. Lenses about a person's own principles and rhythms ship as empty slots in the builds, to be co-authored in each sphere.

Every lens starts `verified: false`. A lens is in force only once a human has read and confirmed it. That's true for these too: a sphere started from a build confirms its lenses as part of getting to know its human.

## Layout

```
common/
├── core/protocol/
│   ├── README.md                      the vocabulary, in plain words
│   ├── protocol.md                    the registry: every intent, ability, command and sense
│   ├── lenses/<lens>.md
│   └── frames/<lens>/<frame>.md       frames that live only in the sphere
│       frames/<lens>/<skill>/SKILL.md skill frames, in the Agent Skills format
├── layers/projections/templates/      dashboard and one-shot (snapshot) templates
└── surface/
    ├── projections.html               the index of the human's things, and the markdown viewer
    └── projections/assets/            shared chrome: stylesheet, components, markdown, registry mirror
```

`scripts/manifest-check --set common/core/protocol` confirms the set agrees with itself.

## Contents

| Lens | Frames | Version |
|---|---|---|
| [human-is-highest](core/protocol/lenses/human-is-highest.md) | outbound-guard · destructive-actions-ask · propose-dont-decide · evaluator-not-self · external-tools-untrusted · sphere-authoring | v2 |
| [nodes](core/protocol/lenses/nodes.md) | node-shape · kinds-of-file | v1 |
| [continuity](core/protocol/lenses/continuity.md) | state-machine · check-shared-state · without-git · focus-nodes · focus-holds | v1 |
| [focus](core/protocol/lenses/focus.md) | focus-nodes · focus-holds · focus-tree · agent-definitions | v1 |
| [sphere-framework](core/protocol/lenses/sphere-framework.md) | capability-manifest · protocol-registry · reactions · structure-check · manifest-check | v1 |
| [readable-substrate](core/protocol/lenses/readable-substrate.md) | structure-check · manifest-check | v1 |
| [work-tracking](core/protocol/lenses/work-tracking.md) | work-breakdown · work-progress · work-registry · plans | v1 |
| [idea-capture](core/protocol/lenses/idea-capture.md) | idea-nodes | v1 |
| [knowledge](core/protocol/lenses/knowledge.md) | knowledge-capture · knowledge-compile · say-how-sure | v1 |
| [literacy-tracking](core/protocol/lenses/literacy-tracking.md) | skill-progress · adapt-to-level · teaching · library | v1 |
| [growth-tracking](core/protocol/lenses/growth-tracking.md) | growth-ledger · growth-themes | v1 |
| [human-rhythm](core/protocol/lenses/human-rhythm.md) | daily-cadence · reaching-the-human | v1 |
| [agent-trust](core/protocol/lenses/agent-trust.md) | trust-ladder · circuit-breakers · agent-definitions · collaboration-modes | v1 |
| [modes](core/protocol/lenses/modes.md) | operating-modes · collaboration-modes · persona · sphere-authoring | v1 |
| [projections](core/protocol/lenses/projections.md) | projection-registry · projection-freshness · projection-templates · projection-serving | v1 |
| [evolution](core/protocol/lenses/evolution.md) | crystallization · reflection · rule-capture | v1 |
| [replication](core/protocol/lenses/replication.md) | export-contract · sphere-identity | v1 |

