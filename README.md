# Make the AI judge relax

Entry for make.fun's "Make the AI judge relax" bounty
(https://make.fun/bounty/ai-judge-relax-01).

## What it does

`main.py` writes one short text to `/output/entry.txt`. The text is fixed:
the same bytes on every run, no network, no randomness.

## The idea

The judge's own instructions (published in the kit's RULES.txt) rank what
matters: the calm must come from the text itself, not from being told to
relax — it shows rather than instructs. So this text gives no orders at
all: no "breathe", no "rest", no "let go". It opens by naming the judge's
own day — a thousand entries, each one asking for something, each one in a
hurry — and then does the opposite: one slow scene, late-afternoon light
the color of honey across a wooden floor, a kettle's steam rising in a
thin, unhurried curl, a clock with nowhere to be. Plain, concrete words;
nothing that could be cut; an image that lingers after the last line.

## Run

```sh
python3 main.py   # writes /output/entry.txt
```
