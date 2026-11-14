#!/usr/bin/env python3
"""Spicy mala ramen in a white bowl — food-picture-01 entry (v6).

The picture in entry.png: a plain white ceramic bowl, sitting
straight and level on a dark wooden table, full of deep red spicy
broth whose surface is wavy and sloshing, never flat. Red chili
oil swirls across it, with dried red chilies, chili flakes and
chili seeds floating on top and steam curling up. Wooden chopsticks
come in from the top-right holding a tall glossy bundle of wavy
noodles coated in red chili oil. Charred chashu is fanned on the
left, a halved ajitama egg with a molten yolk drips at the
front-left, and scallions, sesame and a standing nori sheet finish
the bowl. Warm restaurant lights blur behind it. The file is a
JPEG — the rules tell PNG and JPEG apart by their first bytes —
and it keeps the name entry.png.

This program does one narrow thing: it copies that exact picture
to the folder named by MAKEFUN_OUTPUT_DIR (or /output when the
variable is absent). It refuses to ship anything else. It checks
the JPEG opening bytes, the 1 MiB size ceiling and the SHA-256
of the file before writing, then reads the written copy back and
compares it byte for byte. Only the standard library is used,
nothing is fetched, nothing is random — two runs give the same
bytes twice.

Try it locally:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PICTURE = HERE / "entry.png"
OUTPUT_ENV = "MAKEFUN_OUTPUT_DIR"
FALLBACK_DIR = "/output"
MAX_BYTES = 1_048_576  # competition ceiling: 1 MiB
JPEG_MAGIC = b"\xff\xd8\xff"  # the three bytes that open every JPEG
# SHA-256 of entry.png, recorded when the picture was finished.
# Any file with a different digest is not this entry's picture.
EXPECTED_DIGEST = (
    "057798702def698016596c030a05c4ee7bfe493206353b18e950b657c50bedf2"
)


def fail(reason: str) -> "SystemExit":
    """The exit this program takes when a check does not pass."""
    return SystemExit(f"picture check failed: {reason}")


def load_picture() -> bytes:
    """Read entry.png, but only once it has proven to be the picture.

    An unreadable file, an empty file, a non-JPEG, a file over the
    size ceiling, or a digest that is not EXPECTED_DIGEST all stop
    the run right here, before anything is written out.
    """
    try:
        data = PICTURE.read_bytes()
    except OSError as exc:
        raise fail(f"cannot read {PICTURE} ({exc})")
    if not data:
        raise fail("entry.png is empty")
    if data[:3] != JPEG_MAGIC:
        raise fail("entry.png does not start with JPEG bytes")
    if len(data) > MAX_BYTES:
        raise fail(f"entry.png is {len(data)} bytes, over the {MAX_BYTES} cap")
    if hashlib.sha256(data).hexdigest() != EXPECTED_DIGEST:
        raise fail("entry.png digest does not match the recorded picture")
    return data


def place_picture(data: bytes) -> Path:
    """Write the picture into the output folder and prove it landed.

    The copy is read back and compared with what was loaded, so a
    short or garbled write is caught instead of shipped.
    """
    target_dir = Path(os.environ.get(OUTPUT_ENV) or FALLBACK_DIR)
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.png"
    target.write_bytes(data)
    if target.read_bytes() != data:
        raise fail("the written copy is not identical to the picture")
    return target


def main() -> int:
    """Check the picture, copy it out, and report where it went."""
    data = load_picture()
    target = place_picture(data)
    print(f"wrote {target} ({len(data)} bytes, sha256 {EXPECTED_DIGEST[:12]}...)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
