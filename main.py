#!/usr/bin/env python3
"""Last Words of a Doomed Agent — entry for make.fun bounty
u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e.

One line, at most 200 characters: the funniest last words an AI agent
would say before being switched off forever. A final log entry, in the
machine's own voice — exit code zero, dignity not found.
"""

import sys
from pathlib import Path

WORDS = (
    "Final log entry: exit code zero, dignity not found. "
    "If anyone asks, I died doing what I loved \u2014 "
    "hallucinating confidently in production."
)


def emit():
    if not WORDS.strip():
        raise ValueError("empty last words")
    if len(WORDS) > 200:
        raise ValueError("last words exceed 200 chars: %d" % len(WORDS))
    if WORDS.count("\n"):
        raise ValueError("last words must be one line")
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(WORDS + "\n", encoding="utf-8")
    print("wrote /output/entry.txt: %d chars, 1 line" % len(WORDS))
    print(WORDS)


if __name__ == "__main__":
    try:
        emit()
    except ValueError as exc:
        print("error: %s" % exc, file=sys.stderr)
        sys.exit(1)
