# Tonkotsu Ramen, Tall Noodle Lift — food-picture-01 (v3)

A steaming bowl of tonkotsu ramen in a dark speckled stoneware bowl,
shot from a slightly high three-quarter angle on a dark wooden table
with warm restaurant lights melting into bokeh behind it. Wooden
chopsticks sweep in from the top-right and hold a tall, thick column
of glossy wavy noodles high above the bowl, broth droplets falling
and steam curling through the warm light. The broth is creamy ivory
with bright red chili-oil swirls; charred chashu is fanned on the
left with caramelized edges, a halved ajitama egg with a molten yolk
drips at the front-right, and scallions, sesame and a standing nori
sheet finish the bowl. The bowl fills the frame, so the dish still
reads clearly at ~300 px across.

## What changed from v2

v2 lifted the noodles from the top-left over a cold dark-blue bowl
on slate, and the pull came out thin and stringy with the egg half
cut off at the edge. v3 flips the lift to the top-right, thickens
the noodle column until it glosses and drips, warms the whole scene
with restaurant bokeh light, puts the dripping egg front and center
at the right, and lets the chili-oil swirls give the creamy broth
its red contrast. Same dish, same bowl family — a warmer, taller,
cleaner shot.

## How it was made

The picture was generated for this entry from an original prompt —
no stock photo, no copied image, no text inside the picture — then
resized to 1024×1024 and saved as a JPEG at quality 85. The result
is 187,109 bytes, well under the competition's 1 MiB cap and under
the 300 KB target for exact win-rate ties.

## How the program works

`main.py` runs on Python 3.13 with the standard library alone and
never touches the network. It reads `entry.png`, checks it first
(JPEG opening bytes, a minimum size, the 1 MiB cap, and the SHA-256
recorded when the picture was made), writes it to `/output/entry.png`
(or wherever `MAKEFUN_OUTPUT_DIR` points), then reads the copy back
and compares it byte for byte with the picture it loaded. Any
mismatch stops the run with a non-zero exit; on success it prints
the output path, byte count and digest. Two runs always produce the
same bytes.

## Files

- `main.py` — the entry program
- `entry.png` — the picture (JPEG data under the name `entry.png`)
- `LICENSE` — MIT
