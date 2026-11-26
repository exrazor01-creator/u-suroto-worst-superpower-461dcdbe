#!/usr/bin/env python3
"""Worst Superpower: the most useless superpower, in one line.

Brief: invent the most useless superpower imaginable, in a
single line of 1-140 characters, and make the uselessness
obvious from the line itself. Judging, in order: the power
must be genuinely useless (not merely weak); the line must
make the reader picture it in use and laugh at how little
it does; the idea must be unexpected; the wording must be
tight, with one concrete detail; and it must be clear on a
single reading. Familiar gags -- slow flight, invisibility
nobody notices -- lose.

Why this line works, in that order: summoning rain only
directly above your own umbrella is useless by
construction, because rain above an umbrella is the one
place it was never a problem; the power changes nothing.
The picture is instantly funny: a hero with both arms
raised while a storm pounds the canopy overhead, bone dry,
exactly as dry as without any power at all. The idea is
fresh -- no flight, no invisibility, no talking animals --
and the umbrella is the one concrete detail that anchors
it. One sentence, 59 characters, nothing to explain.
The validator below guards only against an edit that would
push the sealed line past the 140-character gate.
"""

from pathlib import Path

MAX_CHARS = 140  # bounty gate: one line of 1-140 characters

# Sealed entry: rain summoned only where it cannot matter.
ENTRY = (
    "I can summon rain, but only directly above my own umbrella."
)

OUT_PATH = Path("/output/entry.txt")


def _reject(message):
    raise ValueError(message)


def check_entry(text):
    """Return text unchanged when it is one clean line within the gate."""
    if not isinstance(text, str):
        _reject("entry must be text")
    if text == "":
        _reject("entry must not be empty")
    if text.strip() == "":
        _reject("entry must not be only white space")
    if any(c in text for c in "\r\n"):
        _reject("entry must be exactly one line")
    if any(c.isspace() and c != " " for c in text):
        # Any whitespace other than a plain space would hide
        # invisible bytes inside the line.
        _reject("entry must use plain spaces only")
    if len(text) > MAX_CHARS:
        _reject(
            "entry is %d characters, past the %d limit" % (len(text), MAX_CHARS)
        )
    if text != text.strip():
        # Padding at either end is dead weight the gate counts.
        _reject("entry must not pad itself with spaces")
    if not text.isprintable():
        _reject("entry must contain no control characters")
    if "  " in text:
        # In a 140-character line, no gap is free.
        _reject("entry must not contain a double space")
    return text


def run():
    line = check_entry(ENTRY)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(line, encoding="utf-8")
    print(line)


if __name__ == "__main__":
    run()
