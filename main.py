#!/usr/bin/env python3
"""Entry program for u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163.

Writes one original single-line excuse (<=200 characters) to the grader's
designated output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt. The grader's repo directory is read-only, so this program writes
nowhere else. Python standard library only.
"""

import os

LINE = (
    "Sorry \u2014 my Wi-Fi is fine, my camera works, my mic works. "
    "I've run out of technical excuses, so here's the honest one: "
    "I just don't want to be there."
)


def validate_entry(text):
    """Check the excuse is one clean line within the length limit."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line with no line breaks")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters long")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")


def write_entry(path):
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    os.chmod(path, 0o644)


def main():
    validate_entry(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    write_entry(os.path.join(output_dir, "entry.txt"))


if __name__ == "__main__":
    main()
