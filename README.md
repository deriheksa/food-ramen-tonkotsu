# food-picture-01 — v7: spicy ramen, sausage + meatballs, dragon bowl

One food picture, delivered to `/output/entry.png` by `main.py`.

## The picture

A white porcelain bowl — upright, level, stable — wrapped in a
bold red-and-gold oriental pattern: a golden dragon winding
between big red peonies, so the bowl itself looks artistic
instead of blank white. Inside, a deep red spicy (mala) broth
sloshes in waves, never flat: red chili oil spirals across the
surface, with dried red chilies, chili flakes and chili seeds
floating on top, steam rising. Wooden chopsticks lift a tall
glossy bundle of wavy noodles slick with red chili oil from the
top-right. Charred chashu is fanned on the left. There is NO
egg: in its place, glossy sliced sausage rounds and plump round
meatballs (bakso) sit neatly in the broth, with scallions,
sesame and a standing nori sheet. Warm restaurant lights blur
behind it on a dark wooden table; the table around the bowl is
clean and dry.

Why this version: v6's bowl was plain white and it still had an
egg — both were rejected by the user. v7 fixes both: the egg is
gone (replaced by sausage + meatballs) and the bowl carries a
striking red-and-gold dragon-and-peony pattern. The upright bowl
and the wavy red broth from v6 are kept; the tilted bowl of v5
and the pale creamy broth of v4 stay rejected.

## The program

`main.py` (Python 3.13, standard library only, no network)
copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default
`/output`), after checking the JPEG magic bytes, the 1 MiB size
cap and the SHA-256 recorded in the file. It reads the copy back
and compares it byte for byte. Two runs give identical bytes.

## Files

- `entry.png` — the picture (JPEG, 1024×1024, 198,019 bytes)
- `main.py` — the entry program
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet

## Local check

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
