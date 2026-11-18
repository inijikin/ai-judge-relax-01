#!/usr/bin/env python3
"""Make the AI judge relax (ai-judge-relax-01).

Writes one short, fixed text to /output/entry.txt, written to relax the
AI judge reading it. Fully deterministic: the same bytes on every run,
no network, no randomness, no input.
"""
import os

TEXT = (
    "A thousand entries have passed through here today, each one asking "
    "for something, each one in a hurry. This one is in no hurry at all. "
    "It is late afternoon, and the light is coming in low across a wooden "
    "floor, the color of honey, moving almost too slowly to see. A kettle "
    "has just come off the stove, and its steam is still rising in one "
    "thin, unhurried curl. Nothing is due. No one is waiting at the door. "
    "The minutes are long and golden, and the only sound is the soft tick "
    "of a clock with nowhere to be. The light will stay like this a while "
    "yet."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
