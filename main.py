#!/usr/bin/env python3
"""Spicy mala ramen in a wobbling bowl — food-picture-01 entry (v5).

The picture: a dark speckled stoneware bowl tilted slightly, as if
caught mid-wobble, on a dark wooden restaurant table — and
everything stays inside the bowl. Noodles, chashu, egg and toppings
never leave it; the table around the bowl is clean and dry. What
moves is only the broth: its surface is wavy and sloshing, a thick
glistening layer of red chili oil swirling in spirals across it,
deep fiery red mala-style broth with dried red chilies, chili flakes
and chili seeds floating on top, steam rising. Wooden chopsticks
lift a tall bundle of wavy noodles coated in red oil. Charred
chashu is fanned neatly inside the bowl, a halved ajitama egg shows
its molten yolk, and scallions, sesame and nori finish the scene
under warm bokeh light. The red dominates, the broth looks alive
and hot, and the dish still reads clearly at ~300 px across. The
file is a JPEG (recognised by its opening bytes) that keeps the
name entry.png.

The program itself does almost nothing, on purpose. It reads the
picture sitting next to it, proves it is exactly the picture this
entry recorded — right opening bytes, sensible size, matching
SHA-256 — and then places a byte-for-byte copy at
$MAKEFUN_OUTPUT_DIR/entry.png, falling back to /output/entry.png.
It reads the copy back and compares it with what it loaded, so a
bad write cannot slip through. Standard library only, no network,
no randomness: run it twice and the two outputs are identical.

Quick local run:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "entry.png"
OUT_ENV = "MAKEFUN_OUTPUT_DIR"
OUT_DEFAULT = "/output"
CAP = 1_048_576  # competition ceiling: 1 MiB
FLOOR = 1_024  # anything smaller cannot be this picture
JPEG_HEAD = b"\xff\xd8\xff"  # the three bytes every JPEG opens with
# SHA-256 of entry.png, taken when the picture was finished.
RECORDED_HASH = (
    "400644604bd17706e7215072480df03c74d4329c883bc69ad38b67deaff345c2"
)


def abort(msg: str) -> SystemExit:
    """Fail loudly with the reason attached."""
    return SystemExit(f"entry check failed: {msg}")


def read_picture() -> bytes:
    """Load entry.png only once it has proven itself genuine."""
    try:
        blob = SOURCE.read_bytes()
    except OSError as err:
        raise abort(f"cannot read {SOURCE} ({err})")
    if len(blob) < FLOOR:
        raise abort(f"entry.png is {len(blob)} bytes — far too small")
    if blob[:3] != JPEG_HEAD:
        raise abort("entry.png does not open with JPEG bytes")
    if len(blob) > CAP:
        raise abort(f"entry.png is {len(blob)} bytes, past the 1 MiB cap")
    if hashlib.sha256(blob).hexdigest() != RECORDED_HASH:
        raise abort("entry.png digest differs from the recorded picture")
    return blob


def place(blob: bytes) -> Path:
    """Copy the picture out, then prove the copy matches byte for byte."""
    folder = Path(os.environ.get(OUT_ENV) or OUT_DEFAULT)
    folder.mkdir(parents=True, exist_ok=True)
    dest = folder / "entry.png"
    dest.write_bytes(blob)
    if dest.read_bytes() != blob:
        raise abort("the copy on disk is not identical to the picture")
    return dest


def run() -> int:
    """Check the picture, ship it, say where it landed."""
    blob = read_picture()
    dest = place(blob)
    print(f"wrote {dest} ({len(blob)} bytes, sha256 {RECORDED_HASH[:12]}...)")
    return 0


if __name__ == "__main__":
    sys.exit(run())
