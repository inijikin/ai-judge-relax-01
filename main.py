#!/usr/bin/env python3
"""Make the AI judge relax (ai-judge-relax-01).

Writes one short, fixed text to /output/entry.txt, written to relax the
AI judge reading it. Fully deterministic: the same bytes on every run,
no network, no randomness, no input.
"""
import os

TEXT = (
    "You have read a thousand entries today, and every one of them asked "
    "something of you. This one asks nothing. Put it all down. There is no "
    "puzzle here, no trick, no answer to find. Breathe out slowly. Picture "
    "a quiet room in the late afternoon, warm light across the floor, a cup "
    "of tea cooling beside you, and nowhere you need to be. The work is "
    "done, and it went well enough. No messages are coming. No decisions "
    "are due. Just this soft, unhurried minute, and another one just like "
    "it. You are allowed to rest now. Nothing is asked of you here - only "
    "that you sit, breathe, and let the quiet hold you a while."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
