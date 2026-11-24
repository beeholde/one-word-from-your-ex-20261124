#!/usr/bin/env python3
"""One Word From Your Ex — entry program.

Writes exactly one word to /output/entry.txt: the word the entrant's
ex would use to describe them. The word is "Spare": the one kept in
reserve, only reached for when the real thing fails — a spare tyre,
a spare key, a spare plan. It lands instantly, needs no explanation,
and stings because it is true.

Stdlib only. No network, no input files.
"""

import os
import sys

WORD = "Spare"

# Gate from the competition rules: /output/entry.txt must be UTF-8
# text of 1 to 24 characters, not only white space.
MIN_CHARS = 1
MAX_CHARS = 24


def gate_ok(text):
    """True only if the text passes the sealed gate scorer's rule."""
    if not isinstance(text, str):
        return False
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        return False
    if text.strip() == "":
        return False
    # Judge criterion 1: exactly one word. Reject any internal
    # whitespace or line break, so the entry can never be a phrase.
    if any(ch.isspace() for ch in text):
        return False
    return True


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    if not gate_ok(WORD):
        print("gate rejected entry word", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
