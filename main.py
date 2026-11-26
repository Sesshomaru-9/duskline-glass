#!/usr/bin/env python3
"""Duskline Glass — Five Seconds to Explain the Glass.

Writes the single-sentence defence a house cat gives after sweeping a
glass off the table, to $MAKEFUN_OUTPUT_DIR/entry.txt.

The line is fixed text: deterministic, no randomness, no network, no
arguments. It only ever writes inside the output directory named by
$MAKEFUN_OUTPUT_DIR (falling back to /output), and never writes into
the repository directory. If the output directory cannot be written,
it reports the problem on stderr and exits 1 instead of crashing.
"""

import os
import sys

ENTRY = (
    "The glass was hogging the sunny spot and refusing to pay rent, "
    "so I evicted it \u2014 the floor can deal with the paperwork now."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    path = os.path.join(out_dir, "entry.txt")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError as exc:
        print(f"duskline-glass: cannot write {path}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
