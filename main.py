#!/usr/bin/env python3
"""Tonkotsu ramen, tall noodle lift — food-picture-01 entry (v3).

What entry.png shows: a bowl of tonkotsu ramen in a dark speckled
stoneware bowl on a dark wooden table, warm restaurant lights blurred
behind it. Wooden chopsticks come in from the top-right and hold a
tall, thick column of glossy wavy noodles high above the bowl, with
broth droplets falling and steam curling through warm light. The
broth is creamy ivory with bright red chili-oil swirls; charred
chashu is fanned on the left, a halved ajitama egg with a molten
yolk drips at the front-right, and scallions, sesame and a standing
nori sheet finish the bowl. The picture is a JPEG (the rules tell
PNG and JPEG apart by their first bytes) and still called entry.png.

The job of this program is small and strict: copy that one picture
to $MAKEFUN_OUTPUT_DIR/entry.png, falling back to /output when the
variable is not set, and refuse to ship anything that is not exactly
the picture recorded here. Before writing it checks the JPEG
opening bytes, the 1 MiB size cap and the SHA-256 of the file; after
writing it reads the copy back and compares every byte. Only the
standard library is used, nothing is fetched, and nothing random
happens — running it twice gives the same bytes twice.

Local try-out:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import sys
from pathlib import Path

SOURCE_FILE = Path(__file__).resolve().parent / "entry.png"
OUT_VAR = "MAKEFUN_OUTPUT_DIR"
DEFAULT_OUT = "/output"
BYTE_LIMIT = 1048576  # the competition's 1 MiB ceiling
JPEG_PREFIX = b"\xff\xd8\xff"  # the three bytes every JPEG opens with
# SHA-256 of entry.png, taken when the picture was finished. A file
# with any other digest is not this entry's picture.
PICTURE_HASH = (
    "8881b87e5057b2e9fb4e6a72f465e8ff7139dd867bbb5d80526291c1d4a01fa9"
)


def _die(message: str) -> "SystemExit":
    """Build the exit this program uses for a failed check."""
    return SystemExit(f"entry check failed: {message}")


def read_and_check() -> bytes:
    """Load entry.png, but only after proving it is the right file.

    Anything wrong — unreadable, not a JPEG, too big, or a digest
    that does not match PICTURE_HASH — stops the run here.
    """
    try:
        payload = SOURCE_FILE.read_bytes()
    except OSError as err:
        raise _die(f"cannot read {SOURCE_FILE} ({err})")
    if not payload:
        raise _die("entry.png is empty")
    if len(payload) < 1024:
        raise _die(
            f"entry.png is only {len(payload)} bytes — too small to be the picture"
        )
    if payload[:3] != JPEG_PREFIX:
        raise _die("entry.png does not open with JPEG bytes")
    if len(payload) > BYTE_LIMIT:
        raise _die(
            f"entry.png is {len(payload)} bytes, past the {BYTE_LIMIT}-byte cap"
        )
    if hashlib.sha256(payload).hexdigest() != PICTURE_HASH:
        raise _die("entry.png digest is not the recorded picture")
    return payload


def deliver(payload: bytes) -> Path:
    """Put the picture in the output folder and prove it arrived whole.

    The copy is read back and compared byte for byte with what was
    loaded, so a truncated or garbled write is caught here.
    """
    folder = Path(os.environ.get(OUT_VAR) or DEFAULT_OUT)
    folder.mkdir(parents=True, exist_ok=True)
    destination = folder / "entry.png"
    destination.write_bytes(payload)
    landed = destination.read_bytes()
    if landed != payload:
        raise _die("the written copy differs from the picture loaded")
    return destination


def run() -> int:
    """Copy the checked picture out and say where it landed."""
    payload = read_and_check()
    destination = deliver(payload)
    print(
        f"wrote {destination} "
        f"({len(payload)} bytes, sha256 {PICTURE_HASH[:12]}...)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(run())
