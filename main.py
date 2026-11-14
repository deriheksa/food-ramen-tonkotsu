#!/usr/bin/env python3
"""Tonkotsu ramen, close up — make.fun food-picture-01 entry.

The picture: a close-up photograph of a bowl of tonkotsu ramen in a
deep red ceramic bowl. Chopsticks lift glossy noodles out of a creamy
broth, steam curling upward; a halved soft egg with a golden jammy
yolk, slices of chashu pork, scallions and a sheet of nori finish the
bowl. The artwork lives in entry.png beside this file. Its bytes are
JPEG (the rules allow a PNG or a JPEG, told apart by the leading
bytes), and the filename stays entry.png.

What this program does: it streams that artwork to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output) and then proves the
copy is byte-for-byte identical, so a truncated or corrupted output
can never reach the judge. Python 3.13, standard library only, no
network access, fully deterministic — the same input bytes always
produce the same output file.

Local try-out:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

from __future__ import annotations

import hashlib
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"

OUTPUT_ENV_VAR = "MAKEFUN_OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"

MAX_BYTES = 1 << 20  # 1 MiB, the competition's file-size cap
JPEG_SIGNATURE = b"\xff\xd8\xff"  # first three bytes of any JPEG
CHUNK_SIZE = 1 << 16  # 64 KiB per read/write step


class ArtworkError(Exception):
    """The artwork cannot be delivered intact."""


def destination_path() -> Path:
    """Where the copy goes: $MAKEFUN_OUTPUT_DIR/entry.png."""
    directory = Path(os.environ.get(OUTPUT_ENV_VAR, DEFAULT_OUTPUT_DIR))
    return directory / SOURCE.name


def inspect_source() -> int:
    """Check the artwork before copying; return its size in bytes.

    Rejects anything that is not a JPEG and anything over the cap, so
    a bad input fails fast instead of producing a bad output.
    """
    size = SOURCE.stat().st_size
    with SOURCE.open("rb") as handle:
        if handle.read(len(JPEG_SIGNATURE)) != JPEG_SIGNATURE:
            raise ArtworkError("entry.png is not a JPEG (bad magic bytes)")
    if size > MAX_BYTES:
        raise ArtworkError(
            f"entry.png is {size} bytes, over the {MAX_BYTES}-byte limit"
        )
    return size


def copy_with_digest(destination: Path) -> tuple[str, int]:
    """Stream SOURCE to destination, hashing every chunk on the way.

    Returns the hex digest of exactly the bytes written, plus the
    number of bytes written.
    """
    digest = hashlib.sha256()
    total = 0
    with SOURCE.open("rb") as reader, destination.open("wb") as writer:
        while chunk := reader.read(CHUNK_SIZE):
            digest.update(chunk)
            writer.write(chunk)
            total += len(chunk)
    return digest.hexdigest(), total


def verify_copy(destination: Path, expected_size: int, digest: str) -> None:
    """Confirm the copy on disk matches the artwork byte for byte."""
    if not destination.is_file():
        raise ArtworkError("output file did not appear after copying")
    actual_size = destination.stat().st_size
    if actual_size != expected_size:
        raise ArtworkError(
            f"output is {actual_size} bytes, "
            f"expected {expected_size} — copy stopped early"
        )
    reference = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    if digest != reference:
        raise ArtworkError("output hash differs from entry.png — copy is corrupt")


def run() -> int:
    """Deliver the artwork and verify it; 0 on success, 1 on failure."""
    destination = destination_path()
    destination.parent.mkdir(parents=True, exist_ok=True)
    try:
        size = inspect_source()
        digest, copied = copy_with_digest(destination)
        verify_copy(destination, size, digest)
    except ArtworkError as problem:
        print(f"error: {problem}", file=sys.stderr)
        return 1
    print(
        f"wrote {destination} "
        f"({copied} bytes, sha256 {digest[:12]}...)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
