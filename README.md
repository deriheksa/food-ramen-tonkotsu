# Steaming Ramen Bowl — food-picture-01

One picture of food: a close-up food photograph of a tonkotsu ramen
bowl in a deep red ceramic bowl. Chopsticks lift glossy noodles out
of a creamy broth, steam rising; a halved soft egg with a golden
jammy yolk, slices of chashu pork, scallions and nori complete the
bowl. Warm light, dark wooden table, the bowl filling the frame so
the dish stays clear even at ~300 px.

## Method

The image was generated from an original prompt (no stock photo, no
text in the image), downscaled to 1024×1024 and saved as JPEG quality
92 (262,633 bytes — under the 1 MiB cap). `main.py` is Python 3.13
standard library only, uses no network, and deterministically
stream-copies `entry.png` to `/output/entry.png`, verifying the copy
byte for byte with a SHA-256 integrity check and a size check first.

## Files

- `main.py` — the entry program
- `entry.png` — the picture (JPEG bytes, name stays `entry.png`)
- `LICENSE` — MIT
