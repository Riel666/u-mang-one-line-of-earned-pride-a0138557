#!/usr/bin/env python3
"""Write one line of at most 240 characters to /output/entry.txt.

The line is written exactly as given: 143 Unicode code points,
inside the competition gate of 1-240. Python 3, standard library
only, no network.
"""

import os

TEXT = "Maya missed the same free throw forty-one times; on the forty-second, the ball dropped through the net, and the empty gym sounded like a crowd."

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
