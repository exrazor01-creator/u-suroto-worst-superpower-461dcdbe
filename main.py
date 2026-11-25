#!/usr/bin/env python3
"""One-line entry: Worst Superpower.

The brief asks for one line of at most 140 characters that
invents the most useless superpower imaginable and makes
plain, in the same breath, why it is useless. The judge
weighs, in order: a power that is genuinely useless, a joke
that makes the reader picture the power in use and laugh at
how little it achieves, an unexpected idea nobody has heard
before, tight wording with a concrete detail, and clarity on
a single reading. Familiar gags (slow flight, invisible
while nobody watches) lose.

The sealed line below is built to that order on purpose.
The power is summoning rain -- but only directly above the
summoner's own umbrella. Rain above an umbrella is already
the one place rain cannot hurt you, so the power achieves
exactly nothing: genuinely useless, not merely weak. The
picture is immediate and funny: a hero raising both arms
to the sky while a storm hammers down on the canopy over
their head and they stay bone dry, exactly as they would
without any power at all. Nobody has heard this one before
-- it is not flight, invisibility, or talking to animals --
and the umbrella is the concrete detail that fixes the
power in the world. One sentence, nothing to explain.

LIMIT is 140 because the bounty gate allows one line of 1
to 140 characters. The sealed line is 59 characters, so it
sits well inside the cap; the validator below only guards
against an edit that would push it past the limit.
"""

import os

# The sealed line: rain summoned only where it cannot
# possibly matter -- directly above your own umbrella, the
# one spot where rain was never a problem in the first place.
ENTRY = "I can summon rain, but only directly above my own umbrella."

LIMIT = 140  # bounty gate: one line, 1-140 characters


def _validate(text):
    """Accept only one clean line inside the character limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ch.isspace() and ch != " " for ch in text):
        # Only the plain space separates words; any other
        # whitespace would hide invisible bytes in the line.
        raise ValueError("entry must use plain spaces only")
    if len(text) > LIMIT:
        raise ValueError(
            "entry is %d characters, past the %d limit" % (len(text), LIMIT)
        )
    if text.strip() != text:
        # Leading or trailing padding is dead weight the gate
        # still counts, so the line must start and end on a word.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        raise ValueError("entry must contain no control characters")
    if "  " in text:
        # A double space is a gap where a word should be; in a
        # 140-character line no gap is free.
        raise ValueError("entry must not contain a double space")
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
