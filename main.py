#!/usr/bin/env python3
"""Tonkotsu ramen, bowl tipped over — food-picture-01 entry (v4).

The picture: a dark speckled stoneware bowl tipped on its side on a
dark wooden table, its tonkotsu spilling out in one tidy cascade.
Glossy wavy noodles pour out in a single clean ribbon, guided by
wooden chopsticks. The broth is thick and creamy, pale yellow like
opor coconut-milk broth, with bold bright-red chili-oil swirls and
chili flakes scattered over it — creamy at first sight, fiercely
spicy at second. The spill is deliberate, not an accident: one
clean ribbon of noodles, one tidy pool of broth, toppings placed
on purpose, so the picture stays appetising instead of messy.
Charred chashu is fanned neatly beside the spill,
a halved ajitama egg with a molten yolk drips into the broth, and
scallions, sesame and steam finish the scene under warm restaurant
light. The bowl stays recognisable and the dish reads clearly even
at ~300 px across. The file is a JPEG (told apart by its opening
bytes) that keeps the name entry.png.

What the program does is deliberately tiny: it takes that one
picture and places it at $MAKEFUN_OUTPUT_DIR/entry.png, or at
/output/entry.png when the variable is empty. Before it writes
anything it proves the file is the exact picture recorded here —
right opening bytes, inside the size limits, matching SHA-256 — and
after writing it reads the copy back and checks every byte. It
uses only the standard library, never the network, and never any
randomness, so two runs land the same bytes both times.

Quick local run:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PICTURE = HERE / "entry.png"
ENV_OUT = "MAKEFUN_OUTPUT_DIR"
FALLBACK_OUT = "/output"
MAX_BYTES = 1_048_576  # competition ceiling: 1 MiB
MIN_BYTES = 1_024  # anything smaller cannot be this picture
JPEG_OPEN = b"\xff\xd8\xff"  # every JPEG starts with these three bytes
# SHA-256 of entry.png, recorded when the picture was finished.
EXPECTED_DIGEST = (
    "71415606813416647a9d2bc733825717a3a243655d286f74acb1a2b6b2fed113"
)


def fail(reason: str) -> SystemExit:
    """Turn a failed check into the exit this program dies with."""
    return SystemExit(f"picture check failed: {reason}")


def load_picture() -> bytes:
    """Read entry.png, but only after it proves it is the right one."""
    try:
        data = PICTURE.read_bytes()
    except OSError as exc:
        raise fail(f"cannot read {PICTURE} ({exc})")
    if len(data) < MIN_BYTES:
        raise fail(f"entry.png is only {len(data)} bytes — too small")
    if data[:3] != JPEG_OPEN:
        raise fail("entry.png does not start with JPEG bytes")
    if len(data) > MAX_BYTES:
        raise fail(f"entry.png is {len(data)} bytes, over the 1 MiB cap")
    if hashlib.sha256(data).hexdigest() != EXPECTED_DIGEST:
        raise fail("entry.png digest does not match the recorded picture")
    return data


def ship(data: bytes) -> Path:
    """Write the picture out, then read it back and compare bytes."""
    out_dir = Path(os.environ.get(ENV_OUT) or FALLBACK_OUT)
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(data)
    if target.read_bytes() != data:
        raise fail("the written copy is not identical to the picture")
    return target


def main() -> int:
    """Check the picture, ship it, and report where it landed."""
    data = load_picture()
    target = ship(data)
    print(f"wrote {target} ({len(data)} bytes, sha256 {EXPECTED_DIGEST[:12]}...)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
