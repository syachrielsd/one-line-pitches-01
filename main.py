#!/usr/bin/env python3
"""One-line pitch entry for make.fun bounty
u-ronigrv-a-day-of-one-line-pitches-12cd9bb3 ("A Day of One-Line Pitches").

Writes exactly one sentence (<=240 chars) to entry.txt in the output dir.
Stdlib only, no network, no dependencies.
"""

import os
import sys

# The winning line, screened pairwise against the candidate pool:
# micro-story with a concrete stake ($5), a named antagonist (your rival),
# and the twist in the LAST beat -- delete "to your rival" and the line
# collapses to a generic charity alarm, so the ending carries the joke.
LINE = "An alarm clock that donates $5 to your rival every time you snooze."

MAX_CHARS = 240


def main() -> int:
    line = LINE

    # Self-check gate: fail loudly instead of writing an invalid entry.
    if not line or not line.strip():
        print("ERROR: entry line is blank", file=sys.stderr)
        return 1
    if line != line.strip():
        print("ERROR: entry line has leading/trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            "ERROR: entry is %d chars, over the %d limit" % (len(line), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    if len(line) < 1:
        print("ERROR: entry is empty", file=sys.stderr)
        return 1
    # One sentence: exactly one sentence-terminating period, at the end,
    # and no other sentence terminators or double spaces smuggled in.
    if not line.endswith(".") or line.count(".") != 1:
        print("ERROR: entry must be exactly one sentence", file=sys.stderr)
        return 1
    if "!" in line or "?" in line:
        print("ERROR: entry must be exactly one sentence (no ! or ?)", file=sys.stderr)
        return 1
    if "  " in line:
        print("ERROR: entry contains a double space", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")

    # Re-read and verify the file matches exactly.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line + "\n":
        print("ERROR: verification failed, file content mismatch", file=sys.stderr)
        return 1

    print("Wrote %s (%d chars)" % (out_path, len(line)))
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
