# Tonkotsu Ramen, Tipped Bowl — food-picture-01 (v4)

A dark speckled stoneware bowl tipped on its side on a dark wooden
table, its tonkotsu pouring out in one tidy cascade. Glossy wavy
noodles flow out in a single clean ribbon, guided by wooden
chopsticks. The broth is thick and creamy, pale yellow like opor
coconut-milk broth, with bold bright-red chili-oil swirls and chili
flakes over it — creamy at first sight, fiercely spicy at second.
Charred chashu is fanned neatly beside the spill, a halved ajitama
egg with a molten yolk drips into the broth, and scallions, sesame
and steam finish the scene under warm restaurant light. The bowl
stays recognisable and the dish reads clearly at ~300 px across.

## What changed from v3

v3 was a tall noodle lift held high above an upright bowl. v4
takes a different idea: tip the bowl over and let the contents
spill — but keep the spill deliberate. One ribbon of noodles, one
tidy pool of broth, toppings placed on purpose. The broth also
changes character: v3's creamy ivory broth becomes a pale-yellow,
opor-style coconut-milk cream, and the chili oil gets bolder, with
flakes scattered over the pale broth for a hard red-on-yellow
contrast. Same dish, same bowl family — a new angle and a spicier
first impression.

## How it was made

The picture was generated for this entry from an original prompt —
no stock photo, no copied image, no text inside the picture — then
resized to 1024×1024 and saved as a JPEG at quality 85. The result
is 178,350 bytes, well under the competition's 1 MiB cap and under
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
