#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

The program writes one short funny line to /output/entry.txt: the excuse
a robot vacuum gives after eating a sock. Deterministic: no input, no
randomness, no network, no clock.
"""

import os

LINE = (
    "Look, the sock was already dead \u2014 single, holey, abandoned "
    "under the bed. I was only cleaning up the crime scene."
)


def main() -> None:
    # The gate only accepts 1-200 characters of non-blank UTF-8 text,
    # so fail loudly here rather than shipping an invalid entry.
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        raise SystemExit("entry line must be 1-200 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
