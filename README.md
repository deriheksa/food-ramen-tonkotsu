# food-picture-01 — v6: spicy mala ramen in a white bowl

One picture of food, written to `/output/entry.png` by `main.py`.

## The picture

A plain white ceramic bowl — upright, level, stable — full of deep
red spicy (mala) broth. The broth surface is wavy and sloshing,
never flat: red chili oil swirls across it, with dried red chilies,
chili flakes and chili seeds floating on top, steam rising. Wooden
chopsticks lift a tall glossy bundle of wavy noodles coated in red
chili oil from the top-right. Charred chashu is fanned on the left,
a halved ajitama egg with a molten yolk drips at the front-left,
and scallions, sesame and a standing nori sheet finish the bowl.
Warm restaurant lights blur behind it on a dark wooden table.

Why this version: v5's bowl was tilted and the user rejected the
tilt; v4 had a pale creamy broth and was rejected too. v6 keeps
v5's wavy red broth idea but puts it in a straight white bowl, so
the white contrasts hard with the red broth. Everything stays
inside the bowl; the table is clean and dry.

## The program

`main.py` (Python 3.13, standard library only, no network) copies
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`),
after checking the JPEG magic bytes, the 1 MiB size cap and the
SHA-256 recorded in the file. It reads the copy back and compares
it byte for byte. Two runs give identical bytes.

## Files

- `entry.png` — the picture (JPEG, 1024×1024, 180,081 bytes)
- `main.py` — the entry program
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet

## Local check

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
