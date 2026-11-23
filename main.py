#!/usr/bin/env python3
"""make.fun entry: One Sentence, One Front Page.

Writes the entry text deterministically to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt). Python standard library only — no network, no
randomness, no timestamps. Running twice produces byte-identical output.

Bounty: https://make.fun/bounty/u-brisk-kestrel-93-one-sentence-one-front-page-0db596eb
Constraint: one sentence, at most 200 characters
"""

import hashlib
import os
import sys

ENTRY = 'COP31 climate talks collapse in Antalya with no fossil-fuel deal as delegates walk out after two weeks of deadlock.'

LIMIT_CHARS = 200


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    data = (ENTRY + "\n").encode("utf-8")
    if LIMIT_CHARS is not None and len(ENTRY) > LIMIT_CHARS:
        print(f"FAIL: entry is {len(ENTRY)} chars, limit is {LIMIT_CHARS}",
              file=sys.stderr)
        return 1
    with open(out_path, "wb") as f:
        f.write(data)
    print(out_path)
    print("chars:", len(ENTRY))
    print("sha256:", hashlib.sha256(data).hexdigest())
    return 0


if __name__ == "__main__":
    sys.exit(main())
