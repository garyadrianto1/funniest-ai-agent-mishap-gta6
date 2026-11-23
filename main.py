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
    # Write ONLY to the output dir: the grading sandbox mounts the repo
    # read-only, so a write next to this script exits 1 (fix 2026-11-24).
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(data)
    sys.stdout.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
