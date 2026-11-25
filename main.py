#!/usr/bin/env python3
"""The Router Confesses — make.fun entry.

Writes one line, a home Wi-Fi router's excuse for dropping the
connection at the climax of a movie, to /output/entry.txt.
Python 3.13 stdlib only, no network, deterministic.
"""

import os

ENTRY = (
    "Climax? Sweetheart, I've held this household together for six years "
    "\u2014 tonight I decided to be the plot twist."
)


def main() -> None:
    # Gate guard: the entry must be a single line of 1-200 characters.
    lines = ENTRY.splitlines()
    assert len(lines) == 1, "entry must be exactly one line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")
    os.chmod(path, 0o644)
    print(ENTRY)


if __name__ == "__main__":
    main()
