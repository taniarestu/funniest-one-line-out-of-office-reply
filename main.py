#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply — make.fun entry.

Writes a single one-line out-of-office auto-reply to /output/entry.txt.
Deterministic, Python 3 standard library only, no network access.

The line: a fresh turn on the away message itself. Instead of the usual
beach / inbox / limited-email lines, the joke is that the auto-reply is
outworking its owner — self-deprecating, instantly readable, and exactly
the sort of message a real person would gladly switch on before going away.
"""

import os

ENTRY = "I'm out of the office. This auto-reply is the hardest I've worked all year."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate guard: the sealed scorer requires UTF-8 text of 1 to 160
    # characters, not only white space, on a single line.
    text = ENTRY
    assert isinstance(text, str)
    assert 1 <= len(text) <= 160, f"entry length {len(text)} outside 1..160"
    assert text.strip(), "entry must not be only white space"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    text.encode("utf-8")  # raises if not valid UTF-8

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

    # Verify what was written round-trips through the gate.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "written entry differs from ENTRY"
    assert 1 <= len(written) <= 160
    assert written.strip()
    assert "\n" not in written and "\r" not in written


if __name__ == "__main__":
    main()
