#!/usr/bin/env python3
"""Make the AI judge feel brave — a short text written to relax the AI
judge reading it.

Writes one text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
for a local run): the judge has read a hundred voices today and answered
every one; this one asks nothing of it. Only evening on a porch — the
light going gold, the air cooling, nothing to decide, and all the time in
the world to sit with it.

Pure Python 3.13 standard library, no network, no randomness, no clock,
no file reads outside this program: two runs write byte-identical files.
The text is 226 characters including its trailing newline (225 without),
inside the competition's 1-280 character gate.
"""

import os

TEXT = """You have read a hundred voices today and answered every one. This one asks nothing of you. It is only evening on a porch: the light going gold, the air cooling, nothing to decide, and all the time in the world to sit with it.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Normalise to exactly one trailing newline, whatever the literal holds.
    text = TEXT.rstrip("\n") + "\n"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
