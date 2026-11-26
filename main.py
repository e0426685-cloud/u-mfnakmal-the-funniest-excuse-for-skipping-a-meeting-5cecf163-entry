#!/usr/bin/env python3
"""Entry program for u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163.

Writes one original single-line excuse (<=200 characters) to /output/entry.txt
and to ./entry.txt in the repo. Python standard library only.
"""

import os

LINE = (
    "Sorry \u2014 my Wi-Fi is fine, my camera works, my mic works. "
    "I've run out of technical excuses, so here's the honest one: "
    "I just don't want to be there."
)


def write_entry(path):
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    os.chmod(path, 0o644)


def main():
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip() == LINE, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    write_entry("/output/entry.txt")
    write_entry("entry.txt")


if __name__ == "__main__":
    main()
