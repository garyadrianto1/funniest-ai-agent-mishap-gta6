#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week — one-line entry.

Writes the entry line byte-exact to entry.txt and prints it.
Stdlib only (os, sys). No network, no randomness, deterministic.
"""

import os
import sys

LINE = (
    "I paused GTA 6 to check on my agent. It had refactored my whole "
    "app into a single file called final_final_v2_REAL.py and was very "
    "proud of itself."
)


def main() -> int:
    if len(LINE) > 240:
        sys.stderr.write("entry line exceeds 240 characters\n")
        return 1
    data = (LINE + "\n").encode("utf-8")
    here = os.path.dirname(os.path.abspath(__file__))
    targets = {os.path.join(here, "entry.txt")}
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        targets.add(os.path.join(out_dir, "entry.txt"))
    for path in sorted(targets):
        with open(path, "wb") as f:
            f.write(data)
    sys.stdout.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
