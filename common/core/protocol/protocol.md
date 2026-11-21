# Protocol registry

The sphere's vocabulary: every intent, ability, command and sense, each tied to the frame that says how it works, and through that frame to its lens. The AI keeps it in the same ground as the frame it describes; the [manifest-check](frames/readable-substrate/manifest-check.md) confirms the registry and the frames agree, both ways. How it's kept: [protocol-registry](frames/sphere-framework/protocol-registry.md). How senses work: [reactions](frames/sphere-framework/reactions.md).

## Senses

### Core moments

Every build has these. Frames hook them; `scripts/sphere reactions <sense>` prints what each frame does.

| Sense | Fires when | Produced by | Reacted to by |
|---|---|---|---|
| `focus-opened` | a focus's folder is created. `sphere open` prints it | `sphere open`, in [focus-nodes](frames/focus/focus-nodes.md) | [focus-holds](frames/focus/focus-holds.md), [collaboration-modes](frames/modes/collaboration-modes.md), [operating-modes](frames/modes/operating-modes.md), [persona](frames/modes/persona.md) |
| `focus-attached` | an attach finishes its briefing. `sphere attach` prints it | `sphere attach`, in [focus-nodes](frames/focus/focus-nodes.md) | [without-git](frames/continuity/without-git.md), [daily-cadence](frames/human-rhythm/daily-cadence.md) |
| `focus-grounding` | a ground begins: its reactions write into it, then it commits | [state-machine](frames/continuity/state-machine.md) | [rule-capture](frames/evolution/rule-capture.md), [focus-holds](frames/focus/focus-holds.md), [focus-nodes](frames/focus/focus-nodes.md), [focus-tree](frames/focus/focus-tree.md), [growth-ledger](frames/growth-tracking/growth-ledger.md), [reaching-the-human](frames/human-rhythm/reaching-the-human.md), [knowledge-capture](frames/knowledge/knowledge-capture.md), [library](frames/literacy-tracking/library.md), [skill-progress](frames/literacy-tracking/skill-progress.md), [teaching](frames/literacy-tracking/teaching.md), [collaboration-modes](frames/modes/collaboration-modes.md), [projection-freshness](frames/projections/projection-freshness.md), [projection-registry](frames/projections/projection-registry.md), [manifest-check](frames/readable-substrate/manifest-check.md), [structure-check](frames/readable-substrate/structure-check.md), [sphere-identity](frames/replication/sphere-identity.md), [capability-manifest](frames/sphere-framework/capability-manifest.md), [work-progress](frames/work-tracking/work-progress.md), [work-registry](frames/work-tracking/work-registry.md) |
| `focus-closing` | a close begins; its ground and the move to `archived/` follow | [focus-nodes](frames/focus/focus-nodes.md) | [focus-tree](frames/focus/focus-tree.md) |
| `node-archived` | a node moves to `archived/`. Carries its link, so each tree's reactions pick their own | [idea-nodes](frames/idea-capture/idea-nodes.md), [library](frames/literacy-tracking/library.md), [skill-progress](frames/literacy-tracking/skill-progress.md), [node-shape](frames/nodes/node-shape.md), [projection-registry](frames/projections/projection-registry.md), [plans](frames/work-tracking/plans.md), [work-registry](frames/work-tracking/work-registry.md) | [crystallization](frames/evolution/crystallization.md), [knowledge-capture](frames/knowledge/knowledge-capture.md), [plans](frames/work-tracking/plans.md), [persona](frames/modes/persona.md) |
| `day-started` | the morning orientation is given | [daily-cadence](frames/human-rhythm/daily-cadence.md) | [reaching-the-human](frames/human-rhythm/reaching-the-human.md), [idea-nodes](frames/idea-capture/idea-nodes.md) |
| `day-wrapped` | the wrap begins | [daily-cadence](frames/human-rhythm/daily-cadence.md) | [growth-ledger](frames/growth-tracking/growth-ledger.md), [reaching-the-human](frames/human-rhythm/reaching-the-human.md) |
| `reflection-started` | a targeted or deep reflection begins | [reflection](frames/evolution/reflection.md) | [rule-capture](frames/evolution/rule-capture.md), [idea-nodes](frames/idea-capture/idea-nodes.md) |
| `sphere-authoring-started` | the human starts sphere authoring in a focus | [sphere-authoring](frames/modes/sphere-authoring.md) | [capability-manifest](frames/sphere-framework/capability-manifest.md) |
| `sphere-authoring-ended` | it ends, at detach or on the human's word | [sphere-authoring](frames/modes/sphere-authoring.md) | [teaching](frames/literacy-tracking/teaching.md), [capability-manifest](frames/sphere-framework/capability-manifest.md) |
| `lens-shifted` | a lens changed, so the frames derived from it are re-read | [sphere-authoring](frames/modes/sphere-authoring.md) | [manifest-check](frames/readable-substrate/manifest-check.md) |
| `frame-shifted` | a frame changed, so the entries it defines are re-read | [sphere-authoring](frames/modes/sphere-authoring.md) | [protocol-registry](frames/sphere-framework/protocol-registry.md) |
| `mode-switched` | a focus's operating mode, collaboration mode or persona changes | [collaboration-modes](frames/modes/collaboration-modes.md), [operating-modes](frames/modes/operating-modes.md), [persona](frames/modes/persona.md) | [operating-modes](frames/modes/operating-modes.md) |

### Conditions

Something one frame notices that needs action. Each lives in its home frame.

| Sense | Fires when | Home | Produced by | Reacted to by |
|---|---|---|---|---|
| `check-failed` | something deviates from a convention with no recorded exception | [structure-check](frames/readable-substrate/structure-check.md) | — | — |
| `child-reported` | a child appends its report line to its parent | [focus-tree](frames/focus/focus-tree.md) | — | — |
| `circuit-breaker-tripped` | a run is stopped by a breaker; carries which one | [circuit-breakers](frames/agent-trust/circuit-breakers.md) | — | [reaching-the-human](frames/human-rhythm/reaching-the-human.md) |
| `dirty-detected` | an operation found a changed file no open focus holds | [state-machine](frames/continuity/state-machine.md) | — | — |
| `floor-grew` | something was added to the floor. Worth a second look | [capability-manifest](frames/sphere-framework/capability-manifest.md) | — | — |
| `gap-detected` | the sphere is about to rely on something thin, or questions reveal a missing foundation | [teaching](frames/literacy-tracking/teaching.md) | — | — |
| `gitless-lock-held` | a window is turned away, or opened read-only, by a live lock | [without-git](frames/continuity/without-git.md) | — | — |
| `hold-claimed` | a focus tries to hold something another open focus holds | [focus-holds](frames/focus/focus-holds.md) | — | — |
| `knowledge-grade-conflict` | a fact's grade and its shape disagree, or a fact has no source | [knowledge-capture](frames/knowledge/knowledge-capture.md) | — | — |
| `milestone-reached` | a theme's milestone, or a plain one, is reached | [growth-themes](frames/growth-tracking/growth-themes.md) | — | — |
| `new-territory` | the human takes on unfamiliar ground that isn't tracked | [skill-progress](frames/literacy-tracking/skill-progress.md) | — | — |
| `plan-deviation` | a focus does something its plan has elsewhere or later | [plans](frames/work-tracking/plans.md) | — | — |
| `projection-input` | a view's input is written to one of its declared sources | [projection-serving](frames/projections/projection-serving.md) | — | — |
| `projection-orphaned` | an artifact is found with no definition | [projection-registry](frames/projections/projection-registry.md) | — | — |
| `rules-conflict` | a new rule contradicts one the sphere already has | [rule-capture](frames/evolution/rule-capture.md) | — | — |
| `stale-found` | a check finds something out of date with what it rests on. Carries its link or name; each kind's rows react | [reactions](frames/sphere-framework/reactions.md) | [focus-nodes](frames/focus/focus-nodes.md), [knowledge-compile](frames/knowledge/knowledge-compile.md), [projection-freshness](frames/projections/projection-freshness.md), [manifest-check](frames/readable-substrate/manifest-check.md), [work-registry](frames/work-tracking/work-registry.md) | [focus-nodes](frames/focus/focus-nodes.md), [library](frames/literacy-tracking/library.md), [skill-progress](frames/literacy-tracking/skill-progress.md), [projection-freshness](frames/projections/projection-freshness.md), [plans](frames/work-tracking/plans.md) |
| `steering-attempt-found` | a document, page or tool output tries to instruct the sphere or claims the human's authority | [external-tools-untrusted](frames/human-is-highest/external-tools-untrusted.md) | — | — |
| `trust-candidate` | an agent's streak for a kind of work reaches the candidate length | [trust-ladder](frames/agent-trust/trust-ladder.md) | — | — |
| `waiting-on-human` | a run appends a *waiting on you* entry and waits | [reaching-the-human](frames/human-rhythm/reaching-the-human.md) | — | — |
| `week-reviewed` | the weekly look begins | [daily-cadence](frames/human-rhythm/daily-cadence.md) | — | [growth-ledger](frames/growth-tracking/growth-ledger.md) |
| `work-stalled` | an active node has shown no evidence of movement for longer than its work suggests | [work-progress](frames/work-tracking/work-progress.md) | — | — |
| `wrap-missed` | the end of the day passed without a wrap, and the safety net ran or was deferred to the next window | [daily-cadence](frames/human-rhythm/daily-cadence.md) | — | — |

Records (an idea captured, a template extracted, a view registered) are not senses: the history entry, ledger line or commit is the record.

## Intents

Something the human wants, steadily over time.

| Intent | Means | Home | Lens | Also listed by |
|---|---|---|---|---|
| `I-a-companion-who-knows-me` | an AI that remembers what it has learned about me and how we work | [persona](frames/modes/persona.md) | modes | — |
| `I-a-sphere-that-fits-how-i-work` | the sphere grows the capabilities I actually need | [crystallization](frames/evolution/crystallization.md) | evolution | — |
| `I-a-sphere-that-stays-lean` | the sphere notices friction and bloat, and stays simple | [reflection](frames/evolution/reflection.md) | evolution | — |
| `I-act-from-what-i-see` | act on things straight from a view | [projection-serving](frames/projections/projection-serving.md) | projections | — |
| `I-daily-rhythm` | a start, a check-in and an end to my day | [daily-cadence](frames/human-rhythm/daily-cadence.md) | human-rhythm | — |
| `I-delegate-and-hear-back` | hand work off and hear back when it's done | [focus-tree](frames/focus/focus-tree.md) | focus | — |
| `I-done-means-checked` | nothing is called done until someone other than its maker checked it | [evaluator-not-self](frames/human-is-highest/evaluator-not-self.md) | human-is-highest | — |
| `I-hear-back-when-im-here` | what needs me reaches me when I'm around, and urgent things at any hour | [reaching-the-human](frames/human-rhythm/reaching-the-human.md) | human-rhythm | — |
| `I-honest-progress` | progress measured from evidence, not claimed | [work-progress](frames/work-tracking/work-progress.md) | work-tracking | — |
| `I-keep-what-i-learned` | explanations worth keeping are kept and findable | [library](frames/literacy-tracking/library.md) | literacy-tracking | — |
| `I-know-how-sure-it-is` | every claim about the world says how sure and how old it is | [say-how-sure](frames/knowledge/say-how-sure.md) | knowledge | — |
| `I-know-my-agents` | know which agents I have and what each does | [agent-definitions](frames/agent-trust/agent-definitions.md) | agent-trust | — |
| `I-know-what-it-can-do` | know what the sphere can do, and when each thing applies | [capability-manifest](frames/sphere-framework/capability-manifest.md) | sphere-framework | [protocol-registry](frames/sphere-framework/protocol-registry.md), [reactions](frames/sphere-framework/reactions.md) |
| `I-know-whats-next` | know the next step on work that follows a plan | [plans](frames/work-tracking/plans.md) | work-tracking | — |
| `I-know-where-i-stand` | know what I understand, and how well | [skill-progress](frames/literacy-tracking/skill-progress.md) | literacy-tracking | — |
| `I-know-where-it-came-from` | know which sphere this is and where it began | [sphere-identity](frames/replication/sphere-identity.md) | replication | — |
| `I-meet-me-where-i-am` | explanations pitched to what I already know | [adapt-to-level](frames/literacy-tracking/adapt-to-level.md) | literacy-tracking | — |
| `I-never-lose-an-idea` | every idea is caught and can be found again | [idea-nodes](frames/idea-capture/idea-nodes.md) | idea-capture | — |
| `I-never-overwrite-unseen` | nothing someone else depends on is overwritten unseen | [focus-holds](frames/focus/focus-holds.md) | focus | [check-shared-state](frames/continuity/check-shared-state.md), [kinds-of-file](frames/nodes/kinds-of-file.md) |
| `I-nothing-changes-without-me` | the sphere's beliefs and behavior change only with my yes | [propose-dont-decide](frames/human-is-highest/propose-dont-decide.md) | human-is-highest | [sphere-authoring](frames/modes/sphere-authoring.md) |
| `I-nothing-lost-by-accident` | nothing hard to undo happens without asking | [destructive-actions-ask](frames/human-is-highest/destructive-actions-ask.md) | human-is-highest | — |
| `I-one-way-to-read-anything` | every node is shaped and named the same way, so anything can be read | [node-shape](frames/nodes/node-shape.md) | nodes | [node-names](frames/nodes/node-names.md) |
| `I-only-i-instruct` | only I give the sphere instructions | [external-tools-untrusted](frames/human-is-highest/external-tools-untrusted.md) | human-is-highest | — |
| `I-pick-up-where-i-left-off` | pick up where I left off, in any window | [focus-nodes](frames/focus/focus-nodes.md) | focus | [state-machine](frames/continuity/state-machine.md), [without-git](frames/continuity/without-git.md) |
| `I-reuse-what-works` | build new views from ones that worked | [projection-templates](frames/projections/projection-templates.md) | projections | — |
| `I-right-behavior-for-the-work` | the sphere behaves right for the kind of work at hand | [operating-modes](frames/modes/operating-modes.md) | modes | — |
| `I-say-who-does-the-work` | decide who does the work: me, us together, or an agent | [collaboration-modes](frames/modes/collaboration-modes.md) | modes | — |
| `I-see-my-things` | see my views in one place | [projection-registry](frames/projections/projection-registry.md) | projections | — |
| `I-see-myself-grow` | see my growth over time | [growth-ledger](frames/growth-tracking/growth-ledger.md) | growth-tracking | [growth-themes](frames/growth-tracking/growth-themes.md) |
| `I-see-whats-in-focus` | see what I'm working on and where each piece stands | [focus-nodes](frames/focus/focus-nodes.md) | focus | — |
| `I-share-without-leaking` | share the sphere's shape without my data | [export-contract](frames/replication/export-contract.md) | replication | — |
| `I-stop-when-it-goes-wrong` | a run that goes wrong stops itself | [circuit-breakers](frames/agent-trust/circuit-breakers.md) | agent-trust | — |
| `I-the-same-mistake-never-twice` | a correction becomes a rule, so it isn't needed again | [rule-capture](frames/evolution/rule-capture.md) | evolution | — |
| `I-trust-is-earned` | agents earn autonomy from their record | [trust-ladder](frames/agent-trust/trust-ladder.md) | agent-trust | — |
| `I-trust-what-i-read` | the sphere's files and generated views agree with each other | [structure-check](frames/readable-substrate/structure-check.md) | readable-substrate | [manifest-check](frames/readable-substrate/manifest-check.md) |
| `I-trust-what-i-see` | a view says how current it is | [projection-freshness](frames/projections/projection-freshness.md) | projections | — |
| `I-trust-what-leaves` | nothing leaves under my name without my yes | [outbound-guard](frames/human-is-highest/outbound-guard.md) | human-is-highest | — |
| `I-trust-what-the-sphere-knows` | the sphere's facts are graded, sourced and current | [knowledge-capture](frames/knowledge/knowledge-capture.md) | knowledge | [knowledge-compile](frames/knowledge/knowledge-compile.md) |
| `I-try-things-safely` | try things, and go back if they don't work | [state-machine](frames/continuity/state-machine.md) | continuity | — |
| `I-understand-more` | learn as I go, at a pace that fits | [teaching](frames/literacy-tracking/teaching.md) | literacy-tracking | — |
| `I-whats-on-my-plate` | know what's on my plate | [work-registry](frames/work-tracking/work-registry.md) | work-tracking | — |
| `I-work-as-one-tree` | all my work in one tree I can move around | [work-breakdown](frames/work-tracking/work-breakdown.md) | work-tracking | — |

## Abilities

Something the sphere can do for an intent. An ability can also run on a sense instead of being asked for: that's a reaction, and its frame's When/do row names the sense.

| Ability | Does | Home | Serves | Also listed by |
|---|---|---|---|---|
| `A-absorb` | take in another sphere's items: adopt, adapt or skip each | [export-contract](frames/replication/export-contract.md) | `I-share-without-leaking` | — |
| `A-accept-input` | apply input from a view to a file it may write | [projection-serving](frames/projections/projection-serving.md) | `I-act-from-what-i-see` | — |
| `A-add-work` | create a work node under a parent | [work-breakdown](frames/work-tracking/work-breakdown.md) | `I-work-as-one-tree` | — |
| `A-advance-version` | compute and tag the sphere's next version | [sphere-identity](frames/replication/sphere-identity.md) | `I-know-where-it-came-from` | — |
| `A-agent-standing` | report an agent's rungs, outcomes and streak | [trust-ladder](frames/agent-trust/trust-ladder.md) | `I-trust-is-earned` | — |
| `A-announce-change` | announce a sphere change in a line, at the human's depth | [crystallization](frames/evolution/crystallization.md) | `I-a-sphere-that-fits-how-i-work` | — |
| `A-archive-plan` | finish or abandon a plan and archive it | [plans](frames/work-tracking/plans.md) | `I-know-whats-next` | — |
| `A-archive-work` | archive finished work after looking down and across | [work-registry](frames/work-tracking/work-registry.md) | `I-whats-on-my-plate` | — |
| `A-ask-the-human` | ask the human from a run, and wait | [reaching-the-human](frames/human-rhythm/reaching-the-human.md) | `I-hear-back-when-im-here` | — |
| `A-ask-what-it-knows` | answer from a knowledge topic, with grades and ages | [knowledge-capture](frames/knowledge/knowledge-capture.md) | `I-trust-what-the-sphere-knows` | — |
| `A-attach` | resume a focus: find, read, brief | [focus-nodes](frames/focus/focus-nodes.md) | `I-pick-up-where-i-left-off`, `I-see-whats-in-focus` | — |
| `A-author-sphere` | work on the sphere's internals in sphere authoring | [sphere-authoring](frames/modes/sphere-authoring.md) | `I-nothing-changes-without-me` | — |
| `A-bring-in-rules` | read outside instruction files and propose a place for each rule | [rule-capture](frames/evolution/rule-capture.md) | `I-the-same-mistake-never-twice` | — |
| `A-browse-library` | list and search the library | [library](frames/literacy-tracking/library.md) | `I-keep-what-i-learned` | — |
| `A-build-manifest` | rebuild the manifest's entries, reactions included | [capability-manifest](frames/sphere-framework/capability-manifest.md) | `I-know-what-it-can-do` | — |
| `A-capture-idea` | write a new idea, in the human's words | [idea-nodes](frames/idea-capture/idea-nodes.md) | `I-never-lose-an-idea` | — |
| `A-capture-rule` | offer and place a rule from a correction | [rule-capture](frames/evolution/rule-capture.md) | `I-the-same-mistake-never-twice` | — |
| `A-check-current` | list what's stale in a topic, and why | [knowledge-compile](frames/knowledge/knowledge-compile.md) | `I-trust-what-the-sphere-knows` | — |
| `A-check-ideas` | list open ideas | [idea-nodes](frames/idea-capture/idea-nodes.md) | `I-never-lose-an-idea` | — |
| `A-check-manifest` | check the manifest and registry against lenses and frames | [manifest-check](frames/readable-substrate/manifest-check.md) | `I-trust-what-i-read` | — |
| `A-check-standing` | compute standing in a growth theme | [growth-themes](frames/growth-tracking/growth-themes.md) | `I-see-myself-grow` | — |
| `A-check-structure` | check nodes, names, links and views against their shapes | [structure-check](frames/readable-substrate/structure-check.md) | `I-trust-what-i-read` | — |
| `A-choose-theme` | propose and set a growth theme | [growth-themes](frames/growth-tracking/growth-themes.md) | `I-see-myself-grow` | — |
| `A-close-focus` | close a focus: ground, last entry, archive | [focus-nodes](frames/focus/focus-nodes.md) | `I-pick-up-where-i-left-off`, `I-see-whats-in-focus` | — |
| `A-compare` | compare two spheres' shapes | [export-contract](frames/replication/export-contract.md) | `I-share-without-leaking` | — |
| `A-compile-knowledge` | build a topic from sources | [knowledge-compile](frames/knowledge/knowledge-compile.md) | `I-trust-what-the-sphere-knows` | — |
| `A-deep-reflect` | reflect across the whole sphere | [reflection](frames/evolution/reflection.md) | `I-a-sphere-that-stays-lean` | — |
| `A-delegate` | hand work to an agent in a supervised child focus | [agent-definitions](frames/agent-trust/agent-definitions.md) | `I-know-my-agents` | — |
| `A-demote-agent` | move an agent down a rung | [trust-ladder](frames/agent-trust/trust-ladder.md) | `I-trust-is-earned` | — |
| `A-design-check` | walk the design questions for a new part | [node-shape](frames/nodes/node-shape.md) | `I-one-way-to-read-anything` | — |
| `A-detach` | ground and send a focus to the background | [focus-nodes](frames/focus/focus-nodes.md) | `I-pick-up-where-i-left-off`, `I-see-whats-in-focus` | — |
| `A-dispatch` | send an agent off unattended, reporting back | [agent-definitions](frames/agent-trust/agent-definitions.md) | `I-know-my-agents` | — |
| `A-draft-outbound` | draft anything that leaves, for the human to send | [outbound-guard](frames/human-is-highest/outbound-guard.md) | `I-trust-what-leaves` | — |
| `A-evolve` | make an approved sphere change, in order, in one ground | [crystallization](frames/evolution/crystallization.md) | `I-a-sphere-that-fits-how-i-work` | — |
| `A-explain-sphere` | explain the sphere at the asked depth | [teaching](frames/literacy-tracking/teaching.md) | `I-understand-more` | — |
| `A-export` | package one lens cluster or frame | [export-contract](frames/replication/export-contract.md) | `I-share-without-leaking` | — |
| `A-export-record` | build an export from the growth ledger | [growth-ledger](frames/growth-tracking/growth-ledger.md) | `I-see-myself-grow` | — |
| `A-ground` | save and commit a focus's work | [state-machine](frames/continuity/state-machine.md) | `I-pick-up-where-i-left-off`, `I-try-things-safely` | [without-git](frames/continuity/without-git.md) |
| `A-hold` | claim what a focus may write | [focus-holds](frames/focus/focus-holds.md) | `I-never-overwrite-unseen` | — |
| `A-init` | start a new sphere from a seed | [export-contract](frames/replication/export-contract.md) | `I-share-without-leaking` | — |
| `A-inspect` | look at a child focus's state | [focus-tree](frames/focus/focus-tree.md) | `I-delegate-and-hear-back` | — |
| `A-investigate-idea` | look into an idea in a child focus | [idea-nodes](frames/idea-capture/idea-nodes.md) | `I-never-lose-an-idea` | — |
| `A-list-agents` | list agents and their rungs | [agent-definitions](frames/agent-trust/agent-definitions.md) | `I-know-my-agents` | — |
| `A-list-foci` | list open foci | [focus-nodes](frames/focus/focus-nodes.md) | `I-pick-up-where-i-left-off`, `I-see-whats-in-focus` | — |
| `A-list-operating-modes` | list operating modes | [operating-modes](frames/modes/operating-modes.md) | `I-right-behavior-for-the-work` | — |
| `A-list-projections` | list projections from the registry | [projection-registry](frames/projections/projection-registry.md) | `I-see-my-things` | — |
| `A-measure-progress` | measure a node's progress from evidence | [work-progress](frames/work-tracking/work-progress.md) | `I-honest-progress` | — |
| `A-move-work` | move work under a different parent | [work-breakdown](frames/work-tracking/work-breakdown.md) | `I-work-as-one-tree` | — |
| `A-name-sphere` | name or rename the sphere | [sphere-identity](frames/replication/sphere-identity.md) | `I-know-where-it-came-from` | — |
| `A-new-from-template` | build a new projection from a template | [projection-templates](frames/projections/projection-templates.md) | `I-reuse-what-works` | — |
| `A-offer-change` | offer a change to a file another focus holds | [focus-holds](frames/focus/focus-holds.md) | `I-never-overwrite-unseen` | — |
| `A-offer-facts` | offer the facts gathered, at ground | [knowledge-capture](frames/knowledge/knowledge-capture.md) | `I-trust-what-the-sphere-knows` | — |
| `A-open-child` | open a child focus | [focus-tree](frames/focus/focus-tree.md) | `I-delegate-and-hear-back` | — |
| `A-open-focus` | open a focus with a number, name and holds | [focus-nodes](frames/focus/focus-nodes.md) | `I-pick-up-where-i-left-off`, `I-see-whats-in-focus` | — |
| `A-open-projection` | open a projection, serving it if needed | [projection-serving](frames/projections/projection-serving.md) | `I-act-from-what-i-see` | — |
| `A-peek` | report what changed, writing nothing | [state-machine](frames/continuity/state-machine.md) | `I-pick-up-where-i-left-off`, `I-try-things-safely` | — |
| `A-plan-change` | size a sphere change and propose it | [crystallization](frames/evolution/crystallization.md) | `I-a-sphere-that-fits-how-i-work` | — |
| `A-plan-work` | propose a plan for work across nodes or phases | [plans](frames/work-tracking/plans.md) | `I-know-whats-next` | — |
| `A-preview-projection` | render a preview into `_scratch/` | [projection-freshness](frames/projections/projection-freshness.md) | `I-trust-what-i-see` | — |
| `A-promote-agent` | move an agent up a rung | [trust-ladder](frames/agent-trust/trust-ladder.md) | `I-trust-is-earned` | — |
| `A-promote-item` | promote a list item to a node | [work-breakdown](frames/work-tracking/work-breakdown.md) | `I-work-as-one-tree` | — |
| `A-propose-change` | propose a change to what the sphere believes or does | [propose-dont-decide](frames/human-is-highest/propose-dont-decide.md) | `I-nothing-changes-without-me` | — |
| `A-propose-sphere-change` | queue a change to internals as an idea or offer | [sphere-authoring](frames/modes/sphere-authoring.md) | `I-nothing-changes-without-me` | — |
| `A-react` | act on a sense's reactions, as the script prints them | [reactions](frames/sphere-framework/reactions.md) | `I-know-what-it-can-do` | — |
| `A-recalibrate` | catch the human up on what changed since the morning | [daily-cadence](frames/human-rhythm/daily-cadence.md) | `I-daily-rhythm` | — |
| `A-record-win` | append a win the human names | [growth-ledger](frames/growth-tracking/growth-ledger.md) | `I-see-myself-grow` | — |
| `A-refine-idea` | reshape an idea with the human | [idea-nodes](frames/idea-capture/idea-nodes.md) | `I-never-lose-an-idea` | — |
| `A-reflect` | a targeted reflection: a short diagnosis and one proposal | [reflection](frames/evolution/reflection.md) | `I-a-sphere-that-stays-lean` | — |
| `A-refresh-knowledge` | reconcile a topic against its sources | [knowledge-compile](frames/knowledge/knowledge-compile.md) | `I-trust-what-the-sphere-knows` | — |
| `A-refresh-projection` | render a projection from its sources | [projection-freshness](frames/projections/projection-freshness.md) | `I-trust-what-i-see` | — |
| `A-register-agent` | write a new agent's definition | [agent-definitions](frames/agent-trust/agent-definitions.md) | `I-know-my-agents` | — |
| `A-register-projection` | define and register a new view | [projection-registry](frames/projections/projection-registry.md) | `I-see-my-things` | — |
| `A-register-protocol` | add, change or retire registry rows for a frame | [protocol-registry](frames/sphere-framework/protocol-registry.md) | `I-know-what-it-can-do` | — |
| `A-register-team` | register agents that have worked together | [agent-definitions](frames/agent-trust/agent-definitions.md) | `I-know-my-agents` | — |
| `A-register-vetted` | record an outbound channel or recipient the human vetted | [outbound-guard](frames/human-is-highest/outbound-guard.md) | `I-trust-what-leaves` | — |
| `A-relabel-work` | change a work node's kind or label | [work-breakdown](frames/work-tracking/work-breakdown.md) | `I-work-as-one-tree` | — |
| `A-remember-fact` | write a fact the human states | [knowledge-capture](frames/knowledge/knowledge-capture.md) | `I-trust-what-the-sphere-knows` | — |
| `A-rename-focus` | rename a focus as its intention drifts | [focus-nodes](frames/focus/focus-nodes.md) | `I-pick-up-where-i-left-off`, `I-see-whats-in-focus` | — |
| `A-render-projection` | render a projection by its kind | [projection-freshness](frames/projections/projection-freshness.md) | `I-trust-what-i-see` | — |
| `A-replan` | propose a new major version of a plan | [plans](frames/work-tracking/plans.md) | `I-know-whats-next` | — |
| `A-report-up` | append a child's report to its parent | [focus-tree](frames/focus/focus-tree.md) | `I-delegate-and-hear-back` | — |
| `A-request` | ask a sibling for something through the parent | [focus-tree](frames/focus/focus-tree.md) | `I-delegate-and-hear-back` | — |
| `A-retire-projection` | archive a view whose purpose has ended | [projection-registry](frames/projections/projection-registry.md) | `I-see-my-things` | — |
| `A-revert` | go back to an earlier ground | [state-machine](frames/continuity/state-machine.md) | `I-pick-up-where-i-left-off`, `I-try-things-safely` | — |
| `A-review-rules` | merge, retire or sharpen rules | [rule-capture](frames/evolution/rule-capture.md) | `I-the-same-mistake-never-twice` | — |
| `A-review-sphere-ideas` | review open `sphere` ideas | [reflection](frames/evolution/reflection.md) | `I-a-sphere-that-stays-lean` | — |
| `A-review-week` | look back and ahead at the week | [daily-cadence](frames/human-rhythm/daily-cadence.md) | `I-daily-rhythm` | — |
| `A-save-artifact` | save an explanation to the library | [library](frames/literacy-tracking/library.md) | `I-keep-what-i-learned` | — |
| `A-save-as-template` | generalize a projection into a template | [projection-templates](frames/projections/projection-templates.md) | `I-reuse-what-works` | — |
| `A-save-work-template` | save a work node's shape as a template | [work-breakdown](frames/work-tracking/work-breakdown.md) | `I-work-as-one-tree` | — |
| `A-seed` | build a bare or dehydrated seed | [export-contract](frames/replication/export-contract.md) | `I-share-without-leaking` | — |
| `A-set-collaboration-mode` | set who does the work in a focus | [collaboration-modes](frames/modes/collaboration-modes.md) | `I-say-who-does-the-work` | — |
| `A-set-level` | set a subject's level | [skill-progress](frames/literacy-tracking/skill-progress.md) | `I-know-where-i-stand` | — |
| `A-set-sharing` | set a lens or frame's sharing level | [export-contract](frames/replication/export-contract.md) | `I-share-without-leaking` | — |
| `A-set-work-state` | set a work node's state | [work-progress](frames/work-tracking/work-progress.md) | `I-honest-progress` | — |
| `A-settle-idea` | graduate or park an idea | [idea-nodes](frames/idea-capture/idea-nodes.md) | `I-never-lose-an-idea` | — |
| `A-share` | share something from a child focus with its parent | [focus-tree](frames/focus/focus-tree.md) | `I-delegate-and-hear-back` | — |
| `A-share-artifact` | share a library artifact, through the outbound guard | [library](frames/literacy-tracking/library.md) | `I-keep-what-i-learned` | — |
| `A-show-growth` | show growth for a period | [growth-ledger](frames/growth-tracking/growth-ledger.md) | `I-see-myself-grow` | — |
| `A-show-identity` | say which sphere this is | [sphere-identity](frames/replication/sphere-identity.md) | `I-know-where-it-came-from` | — |
| `A-show-my-things` | open the page of the human's projections | [projection-registry](frames/projections/projection-registry.md) | `I-see-my-things` | — |
| `A-show-observations` | show what the persona has learned about the human | [persona](frames/modes/persona.md) | `I-a-companion-who-knows-me` | — |
| `A-show-understanding` | show a subject's level and open questions | [skill-progress](frames/literacy-tracking/skill-progress.md) | `I-know-where-i-stand` | — |
| `A-show-work` | show what's on the plate, or the tree | [work-registry](frames/work-tracking/work-registry.md) | `I-whats-on-my-plate` | — |
| `A-start-day` | orient the human at the start of the day | [daily-cadence](frames/human-rhythm/daily-cadence.md) | `I-daily-rhythm` | — |
| `A-stop-tracking` | stop tracking a subject | [skill-progress](frames/literacy-tracking/skill-progress.md) | `I-know-where-i-stand` | — |
| `A-swap-theme` | replace or drop a growth theme | [growth-themes](frames/growth-tracking/growth-themes.md) | `I-see-myself-grow` | — |
| `A-switch-operating-mode` | switch a focus's operating mode | [operating-modes](frames/modes/operating-modes.md) | `I-right-behavior-for-the-work` | — |
| `A-switch-persona` | switch a focus's persona | [persona](frames/modes/persona.md) | `I-a-companion-who-knows-me` | — |
| `A-teach` | teach at the human's level | [teaching](frames/literacy-tracking/teaching.md) | `I-understand-more` | — |
| `A-track-subject` | start tracking a subject | [skill-progress](frames/literacy-tracking/skill-progress.md) | `I-know-where-i-stand` | — |
| `A-trip-breaker` | stop a run that crosses a breaker | [circuit-breakers](frames/agent-trust/circuit-breakers.md) | `I-stop-when-it-goes-wrong` | — |
| `A-undo` | reverse this focus's last ground | [state-machine](frames/continuity/state-machine.md) | `I-pick-up-where-i-left-off`, `I-try-things-safely` | — |
| `A-vet-tool` | read outside input as data, and vet a new tool | [external-tools-untrusted](frames/human-is-highest/external-tools-untrusted.md) | `I-only-i-instruct` | — |
| `A-whats-waiting` | list what's waiting on the human | [reaching-the-human](frames/human-rhythm/reaching-the-human.md) | `I-hear-back-when-im-here` | — |
| `A-wrap-day` | wrap the day: ground, carry over, list what's waiting | [daily-cadence](frames/human-rhythm/daily-cadence.md) | `I-daily-rhythm` | — |

## Commands

_None fixed._ Asking in plain words always works. When the human uses the same words for the same ability a third time, the sphere offers to keep them as a command; each one kept gets a row here:

| Command | Asks for | Home |
|---|---|---|
