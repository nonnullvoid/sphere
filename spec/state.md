# State

_Status: stub._ The sphere as a state machine: sessions, ground, resume.

_Status tags: **proven** (exercised in real daily use) · **advanced** (opt-in, proven but with sharp edges) · **unexercised** (designed, not yet used in practice)._

## Will cover

- Level 1, simple sessions (the default): one branch, a flat log, ground = commit with a summary, resume = read the work's journal. No tree vocabulary; git optional and invisible at core profile. **proven**
- Level 2, session tree (opt-in): ground commits state, sync merges up into the parent without finishing, close finishes. Ships with its sharp edges documented. **advanced**
- Nested features stay hidden until needed. The sphere proposes them; the human confirms.
- No migration between levels: a level-1 log entry is a depth-1 tree node.
- Session registry: facts from git, meaning in the registry (human-confirmed), runtime state in a disposable gitignored file; reconciled at ground.
- Compaction commits with staged-files discipline. **proven** Flatspace surface. **advanced**
