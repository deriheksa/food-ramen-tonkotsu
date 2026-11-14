#!/usr/bin/env python3
"""Noodle-pull tonkotsu ramen — food-picture-01 entry (v2).

The picture in entry.png: a steaming bowl of tonkotsu ramen in a dark
blue ceramic bowl, photographed from a slightly high three-quarter
angle. Wooden chopsticks come in from the top-left corner and lift a
tall, glossy bundle of wavy noodles; steam curls around the lift.
Charred chashu pork is fanned on the right side of the bowl, a halved
ajitama egg with a molten yolk drips at the bottom-left, and menma,
scallions and chili oil finish the creamy broth. Warm window light on
a dark slate table. The file is a JPEG (the rules accept PNG or JPEG,
told apart by the first bytes) and keeps the name entry.png.

This program does one thing: it puts that picture at
$MAKEFUN_OUTPUT_DIR/entry.png (or /output when the variable is
unset), and it refuses to hand over a damaged copy. It checks the
picture before writing — JPEG header, size under the 1 MiB cap, and
the exact SHA-256 I recorded when the picture was made — then checks
the written file again the same way. Standard library only, no
network, no randomness: the same input always produces the same
output bytes.

Try it locally:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import sys
from pathlib import Path

PICTURE = Path(__file__).resolve().parent / "entry.png"
ENV_DIR = "MAKEFUN_OUTPUT_DIR"
FALLBACK_DIR = "/output"
SIZE_CAP = 1048576  # 1 MiB, the competition's cap
JPEG_HEAD = b"\xff\xd8\xff"  # every JPEG starts with these three bytes
# SHA-256 of entry.png as saved for this entry; the program will not
# ship a picture whose digest differs from this.
EXPECTED_DIGEST = (
    "45ff894c87339fea2f1bbd61b564aa146f2c734d234bd8f8b040f3f2b914e413"
)


def load_picture() -> bytes:
    """Read entry.png and prove it is the picture this entry ships.

    Fails loudly on a missing file, a non-JPEG header, a file over
    the cap, or a digest that does not match EXPECTED_DIGEST.
    """
    try:
        data = PICTURE.read_bytes()
    except OSError as err:
        raise SystemExit(f"cannot read {PICTURE}: {err}")
    if data[:3] != JPEG_HEAD:
        raise SystemExit("entry.png is not a JPEG (bad leading bytes)")
    if len(data) > SIZE_CAP:
        raise SystemExit(
            f"entry.png is {len(data)} bytes, over the {SIZE_CAP}-byte cap"
        )
    if hashlib.sha256(data).hexdigest() != EXPECTED_DIGEST:
        raise SystemExit("entry.png digest mismatch — picture is not the one recorded")
    return data


def place_picture(data: bytes) -> Path:
    """Write the picture to the output directory and prove it landed.

    Returns the output path. The written file is read back and its
    digest compared with the input, so a short or garbled write is
    caught here instead of reaching the judge.
    """
    out_dir = Path(os.environ.get(ENV_DIR, FALLBACK_DIR))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(data)
    written = target.read_bytes()
    if len(written) != len(data):
        raise SystemExit(
            f"output is {len(written)} bytes, expected {len(data)} — write stopped early"
        )
    if hashlib.sha256(written).hexdigest() != EXPECTED_DIGEST:
        raise SystemExit("output digest mismatch — copy did not land intact")
    return target


def main() -> int:
    """Ship the picture; print where it went and how big it is."""
    data = load_picture()
    target = place_picture(data)
    print(f"wrote {target} ({len(data)} bytes, sha256 {EXPECTED_DIGEST[:12]}...)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
