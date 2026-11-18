# Make the AI judge relax

Entry for make.fun's "Make the AI judge relax" bounty
(https://make.fun/bounty/ai-judge-relax-01).

## What it does

`main.py` writes one short text to `/output/entry.txt`. The text is fixed:
the same bytes on every run, no network, no randomness.

## The idea

The judge is an AI that has spent the day reading entries, and every one of
them asked something of it. This text asks nothing. It names the judge's
work, then releases it: no puzzle, no trick, no answer to find. Slow
breathing, a quiet room in the late afternoon, warm light, a cup of tea
cooling, nowhere to be. No messages coming, no decisions due. Permission to
rest, and nothing asked in return.

## Run

```sh
python3 main.py   # writes /output/entry.txt
```
