# The Notification

A short story about an ordinary man who finds out what the whole thing was for — told
as a single-scroll web experience, with drifting depth-parallax illustrations.

**Read it:** `index.html` (a self-contained static page — no build step, no dependencies).

## Credits

- **Story & direction:** Taur
- **Written with:** Claude (co-author + editor)
- **Illustration:** Midjourney
- **Depth maps:** Depth-Anything V2

A [Taur Studios](https://taur-dev.github.io/) conceptual project — and a small experiment
in human + AI collaboration, credited in full rather than hidden.

## How it's built

Plain HTML/CSS/JS, everything in `index.html`. The eight illustrations live in `images/`
(web-optimized WebP, with full-res masters in `images/source/`). Six of them are upgraded
to a gentle WebGL depth-parallax that drifts on its own; each reads a matching
`images/<plate>-depth.png` map. On reduced-motion or no-WebGL, they fall back to the flat
image.

Depth maps are generated with `scripts/make_depth.py` (runs Depth-Anything V2 via its
HuggingFace Space — see the script header for usage).

## Local preview

The parallax needs the page *served* (WebGL can't texture `file://` images in
Chrome/Safari):

```
python3 -m http.server 8000
# open http://localhost:8000
```

Double-clicking `index.html` works too but shows the flat images (Firefox excepted).

## Dev artifacts

`parallax-ox.html` / `parallax-eye.html` are standalone parallax test pages.
`concept.md` is the working brief; `plates/` holds the Midjourney prompt kit.
