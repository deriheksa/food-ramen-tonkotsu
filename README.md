# Tonkotsu Ramen Noodle Pull — food-picture-01 (v2)

A steaming bowl of tonkotsu ramen in a dark blue ceramic bowl, shot
from a slightly high three-quarter angle. Chopsticks come in from the
top-left and lift a tall, glossy bundle of wavy noodles out of the
broth while steam curls around the lift. Charred chashu pork is
fanned on the right, a halved ajitama egg with a molten yolk drips
at the bottom-left, and menma, scallions, sesame and chili oil finish
the creamy broth. Warm window light on a dark slate table; the bowl
fills the frame so the dish reads clearly even at ~300 px across.

## How it was made

The picture was generated for this entry from an original prompt —
no stock photo, no copied image, no text inside the picture — then
resized to 1024×1024 and saved as a JPEG at quality 82. The result
is 154,626 bytes, well under the competition's 1 MiB cap and under
the 300 KB target for exact win-rate ties.

## How the program works

`main.py` runs on Python 3.13 with the standard library alone and
never touches the network. It reads `entry.png`, checks it first
(JPEG leading bytes, size under the cap, SHA-256 matching the digest
recorded when the picture was made), writes it to `/output/entry.png`
(or wherever `MAKEFUN_OUTPUT_DIR` points), then reads the output
back and checks its size and digest again. Any mismatch stops the
run with a non-zero exit; on success it prints the output path, byte
count and digest. Two runs always produce the same bytes.

## Files

- `main.py` — the entry program
- `entry.png` — the picture (JPEG data under the name `entry.png`)
- `LICENSE` — MIT
