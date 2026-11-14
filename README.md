# Tonkotsu Ramen, Close Up — food-picture-01

A single food photograph, taken tight on the bowl: tonkotsu ramen
served in a deep red ceramic bowl. Chopsticks are lifting glossy
noodles from a creamy broth while steam rises; beside them sit a
halved soft egg with a golden jammy yolk, slices of chashu pork,
scallions and nori. Warm light on a dark wooden table, the bowl
filling the frame so the dish reads clearly even when the picture is
shown small.

## How it was made

The picture was created from an original prompt written for this
entry — no stock photo, no text inside the image — then downscaled to
1024×1024 and saved as a JPEG at quality 92. The result is 262,633
bytes, comfortably under the competition's 1 MiB file-size cap.

## How the program works

`main.py` runs on Python 3.13 with the standard library alone and
never touches the network. It copies `entry.png` to
`/output/entry.png` (or wherever `MAKEFUN_OUTPUT_DIR` points) in
64 KiB chunks, hashing each chunk as it goes, and afterwards checks
the copy against the original: same byte count and same SHA-256
digest. Before copying it also confirms the file really is a JPEG by
its leading bytes and that it fits under the 1 MiB cap. Any failure
prints an error and exits non-zero; on success it prints the output
path, byte count and digest. Running it twice always produces the
same bytes.

## Files

- `main.py` — the entry program
- `entry.png` — the picture (JPEG data under the name `entry.png`)
- `LICENSE` — MIT
