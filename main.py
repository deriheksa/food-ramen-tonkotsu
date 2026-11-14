#!/usr/bin/env python3
"""food-picture-01 entry, v7: spicy ramen with sausage and meatballs.

What the picture shows: a white porcelain bowl standing straight
and level on a dark wooden table, decorated all around with a bold
red-and-gold oriental pattern — a golden dragon winding between
big red peonies — so the bowl itself is a piece of art, not a
blank cup. Inside it, a deep red mala broth sloshes in waves,
never sitting flat: glossy red chili oil spirals over the surface,
dried red chilies, chili flakes and chili seeds drift on top, and
steam curls upward. Wooden chopsticks come in from the top-right,
holding a tall, shiny bundle of wavy noodles slick with chili oil.
Charred chashu pork is fanned out on the left. There is no egg
anywhere in the picture; in its place, glossy sliced sausage
rounds and plump round meatballs (bakso) sit neatly in the broth,
with scallions, sesame and a standing sheet of nori to finish.
Warm restaurant lights blur in the dark background.

The file is a JPEG even though it is called entry.png — the
competition tells PNG and JPEG apart by the first bytes of the
file, and a JPEG is what we ship.

This script has a single job: put that exact picture into the
output folder (the folder named by MAKEFUN_OUTPUT_DIR, or
/output when that variable is not set). Before writing anything
it proves the file is the right one: it must open with the JPEG
signature bytes, stay under the 1 MiB competition ceiling, and
match the SHA-256 fingerprint written below. After writing, it
reads the copy back and makes sure every byte is identical.
Only the Python standard library is used; nothing is downloaded,
nothing is random, so running it twice gives the same bytes twice.

To try it:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import sys
from pathlib import Path

SOURCE_DIR = Path(__file__).resolve().parent
PICTURE_FILE = SOURCE_DIR / "entry.png"
OUTPUT_VAR = "MAKEFUN_OUTPUT_DIR"
DEFAULT_OUTPUT = "/output"
SIZE_LIMIT = 1_048_576  # 1 MiB, the competition's ceiling
JPEG_SIGNATURE = b"\xff\xd8\xff"  # the bytes that open a JPEG file
# SHA-256 fingerprint of entry.png, taken when the picture was done.
# If the file's fingerprint differs, it is not this entry's picture.
PICTURE_FINGERPRINT = (
    "7899c0a491821d0f963eb6c6796f9d4e4a8c66c5d1ea5b716a0f5a49a3b2bbb2"
)


def abort(message: str) -> "SystemExit":
    """Stop the run with a clear reason when a check fails."""
    return SystemExit(f"entry check failed: {message}")


def fetch_picture() -> bytes:
    """Read entry.png after proving it is the picture we mean.

    A missing file, an empty file, a file that does not open with
    the JPEG signature, a file past the size ceiling, or a file
    whose fingerprint is not PICTURE_FINGERPRINT all end the run
    here, before a single byte is written anywhere.
    """
    try:
        content = PICTURE_FILE.read_bytes()
    except OSError as problem:
        raise abort(f"cannot read {PICTURE_FILE} ({problem})")
    if len(content) == 0:
        raise abort("entry.png is empty")
    if content[:3] != JPEG_SIGNATURE:
        raise abort("entry.png does not open with JPEG bytes")
    if len(content) > SIZE_LIMIT:
        raise abort(
            f"entry.png is {len(content)} bytes, past the {SIZE_LIMIT} cap"
        )
    if hashlib.sha256(content).hexdigest() != PICTURE_FINGERPRINT:
        raise abort("entry.png fingerprint does not match the recorded one")
    return content


def deliver_picture(content: bytes) -> Path:
    """Drop the picture into the output folder and check it landed.

    The destination is read back after writing; if the copy is not
    byte-for-byte the same as what was checked, the run fails
    instead of shipping a damaged file.
    """
    folder = Path(os.environ.get(OUTPUT_VAR) or DEFAULT_OUTPUT)
    folder.mkdir(parents=True, exist_ok=True)
    destination = folder / "entry.png"
    destination.write_bytes(content)
    if destination.read_bytes() != content:
        raise abort("the copy in the output folder is not identical")
    return destination


def run() -> int:
    """Check the picture, deliver it, and say where it went.

    The printed fingerprint prefix is only a short label so the
    operator can tell at a glance which picture was delivered;
    the full fingerprint is checked inside fetch_picture().
    """
    content = fetch_picture()
    destination = deliver_picture(content)
    print(
        f"delivered {destination} "
        f"({len(content)} bytes, sha256 {PICTURE_FINGERPRINT[:12]}...)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(run())
