# Surface

_Every space in `surface/`: what it holds, who can see it, and whether it carries live state. Surface is flatspace: one always-latest copy that every window sees._

```yaml
- space: projections
  kind: projections
  sharing: private
  rendered-by: projection-freshness
  flatspace: true
  liveness: none
- space: state
  kind: state
  sharing: private
  rendered-by: focus-nodes
  flatspace: true
  liveness: side-layer        # heartbeats and indexes; never committed
- space: raw
  kind: raw
  sharing: private
  rendered-by: none           # files the human drops in, not yet processed
  flatspace: true
  liveness: none
- space: inbox
  kind: inbox
  sharing: private
  rendered-by: export-contract
  flatspace: true
  liveness: none
- space: outbox
  kind: outbox
  sharing: private
  rendered-by: export-contract
  flatspace: true
  liveness: none
```
