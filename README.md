# Spicy Mala Ramen, Wobbling Bowl — food-picture-01 (v5)

A dark speckled stoneware bowl tilted slightly, as if caught
mid-wobble, on a dark wooden restaurant table. Everything stays
inside the bowl — noodles, chashu, egg and toppings never leave it,
and the table around the bowl is clean and dry. What moves is only
the broth: its surface is wavy and sloshing, a thick glistening
layer of red chili oil swirling in spirals across it. Deep fiery
red mala-style broth, dried red chilies, chili flakes and chili
seeds floating on top, steam rising. Wooden chopsticks lift a tall
bundle of wavy noodles coated in red oil. Charred chashu is fanned
neatly inside the bowl, a halved ajitama egg shows its molten yolk,
and scallions, sesame and nori finish the scene under warm bokeh
light. The red dominates; the broth looks alive and hot; the dish
reads clearly at ~300 px across.

## What changed from v4

v4 tipped the bowl over and let pale opor-style broth pool on the
table — the user rejected it: the broth looked creamy, not spicy,
and the tipped bowl read as a mess. v5 corrects both: the bowl only
leans, nothing leaves it, and the broth is deep red and fiery
instead of pale and creamy. The wobble lives in the broth surface
— waves and a chili-oil swirl — not in a spill. Same dish, same
bowl family, a hotter first impression.

## How it was made

The picture was generated for this entry from an original prompt —
no stock photo, no copied image, no text inside the picture — then
resized to 1024×1024 and saved as a JPEG at quality 82. The result
is 191,961 bytes, well under the competition's 1 MiB cap and under
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
