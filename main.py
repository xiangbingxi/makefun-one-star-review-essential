"""Write the one-star review entry to /output/entry.txt.

The review text is fixed verbatim, supplied by the user. This program
writes it exactly as given: UTF-8, no trailing newline, no external
files read, no network access.

After writing, it reads the file back and verifies it matches the
entry character for character. Any mismatch is a hard failure: the
program prints the difference to stderr and exits non-zero instead
of silently leaving a wrong entry behind.
"""

import os
import sys

ENTRY = "Water, 1/5 stars: I've been drinking it for years and somehow I'm still on the free trial of being hydrated."

MAX_CHARS = 160


def main():
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        print(
            f"entry is {len(ENTRY)} characters, outside the 1-{MAX_CHARS} range",
            file=sys.stderr,
        )
        raise SystemExit(1)
    if "\n" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        raise SystemExit(1)

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    with open("/output/entry.txt", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        print("verification failed: /output/entry.txt differs from ENTRY", file=sys.stderr)
        print(f"expected: {ENTRY!r}", file=sys.stderr)
        print(f"got:      {written!r}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
