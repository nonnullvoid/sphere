# This sphere's build: lifesphere

_Read during the first conversation (setup step 2), and by `sphere start`. It says what this build adds to base, and where._

## What it adds

- **Life areas and habits.** The parts of life the human keeps an eye on are work items of `kind: area`; what they're doing sits under them (`parent:`). A habit is ongoing work (`ongoing: true`) under its area.
- **A Life page** (`life`): areas, habits, what's on the go, what finished this week. Drawn from its rules in `layers/projections/life.md`.
- **The human's thinking:** the [philosophy](protocol/lenses/philosophy.md) lens, two empty lens slots written with them over time ([values](protocol/lenses/values.md), [worldview](protocol/lenses/worldview.md)), and `layers/philosophy/realizations.md`, where what they come to see is kept in their words.
- **More anchors:** the morning and the weekly look, as well as the wrap.

## Setup

Adds to [`init.md`](init.md):

- **Step 5, the principle:** after it's written, say in a line that the sphere can also keep what matters most to them and how they see things, over time and only when they want. Don't start either now.
- **Step 6, what's on their plate:** first ask which parts of life they'd like to keep an eye on. Offer a few in plain words (*health, money, home, people, work, growing*); their own words win. For each one they pick, make a work item in `layers/work/<area>/` with `kind: area`, `state: active`, `ongoing: true` and a one-line summary in their words. Then put each thing they're working on under its area with `parent:`. Anything they describe as a habit (*"sleep before eleven"*, *"walk every day"*) is ongoing work under its area.
- **Step 9, show them:** open the Life page too: `scripts/sphere show life`.

## Anchors

- **The morning:** a short look at the day, when they say they're starting.
- **The wrap:** what got done, saved, at the end of a day.
- **The weekly look:** on the day they choose, how the week went across their areas and habits.

## Startup context

- **what matters to them (values):** `core/protocol/lenses/values.md#headings`
- **anchors this sphere keeps:** `core/build.md#Anchors`
