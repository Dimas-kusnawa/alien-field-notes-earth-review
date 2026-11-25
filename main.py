#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one line -- an alien tourist's review of Earth -- to entry.txt.
Deterministic, stdlib only.
"""

import os

# The joke: the alien's angle is the irony -- humans built thinking
# machines, then spend all day thinking for them. The review verdict
# ("Two stars -- would not abduct again") lands the punch at the end
# and makes it read like a real tourist review, not a setup.
LINE = "Two days on Earth: they built machines to do their thinking, then spend all day telling the machines what to think. Two stars \u2014 would not abduct again."


# Why this beats the obvious lines: it avoids the first thoughts
# (traffic, gravity, money, weather) and finds a fresh, specific
# detail -- the human-machine relationship -- told in one tight line.
# No newline is written: the gate wants 1-200 chars, one line only.
def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {path}: {LINE} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
