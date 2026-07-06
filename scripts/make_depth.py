#!/usr/bin/env python3
"""
Generate depth maps for The Notification plates using Depth-Anything V2
(the official HuggingFace Space depth-anything/Depth-Anything-V2).

Run this LOCALLY — it needs internet (Claude's sandbox can't reach HuggingFace).

    pip install gradio_client pillow numpy
    python scripts/make_depth.py

If the Space errors out with a vague AppError, it's usually the anonymous
ZeroGPU quota being exhausted. Get a free read token at
https://huggingface.co/settings/tokens and export it before running:

    export HF_TOKEN=hf_xxxxxxxx
    python scripts/make_depth.py

For each plate in images/source/ it writes:
    images/<name>-depth.png          -> 8-bit, sized to the color plate, web-ready
    images/source/<name>-depth-raw.png -> the raw 16-bit master from the model

Then just tell Claude "depth maps are in" and they get wired into index.html.

Notes
-----
- Depth-Anything returns disparity: brighter = NEARER, black = far. That's the
  polarity the parallax shader expects, so no inversion needed. If a given map
  ever looks inside-out, set INVERT = True below.
- You can also do this by hand: open the Space in a browser, drop each image,
  download the "16-bit raw depth" file, and save it as images/<name>-depth.png.
  https://huggingface.co/spaces/depth-anything/Depth-Anything-V2
"""

import os
import shutil
import numpy as np
from PIL import Image
from gradio_client import Client, handle_file

INVERT = False

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES = os.path.join(HERE, "images")
SRC = os.path.join(IMAGES, "source")

PLATES = [
    "01-notification", "02-everywhere", "03-drive", "04-ox-in-road",
    "05-mirror", "06-field", "07-console", "08-four-stars",
]


def find_source(name):
    for ext in (".png", ".webp", ".jpg", ".jpeg"):
        p = os.path.join(SRC, name + ext)
        if os.path.exists(p):
            return p
    return None


def main():
    client = Client("depth-anything/Depth-Anything-V2", token=os.environ.get("HF_TOKEN"))
    for name in PLATES:
        src = find_source(name)
        if not src:
            print("skip (no source found):", name)
            continue
        print("depth:", name, "...", flush=True)

        result = client.predict(image=handle_file(src), api_name="/on_submit")
        raw16 = result[2]  # filepath to the 16-bit raw depth (disparity)

        # keep the raw master
        shutil.copy(raw16, os.path.join(SRC, name + "-depth-raw.png"))

        # build a web-ready 8-bit map, sized to the color plate
        color = Image.open(src)
        d = Image.open(raw16).convert("I").resize(color.size, Image.LANCZOS)
        a = np.asarray(d).astype(np.float32)
        a = (a - a.min()) / (a.max() - a.min() + 1e-6)
        if INVERT:
            a = 1.0 - a
        out = os.path.join(IMAGES, name + "-depth.png")
        Image.fromarray((a * 255).astype("uint8")).save(out)
        print("  ->", out)

    print("\ndone. tell Claude the depth maps are in images/ and they'll be wired up.")


if __name__ == "__main__":
    main()
