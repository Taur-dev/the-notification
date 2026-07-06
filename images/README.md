# Images — The Notification

Where the plates live, and how to name them so the page can find them.

## Folders

- **`images/source/`** — full-resolution originals straight from Midjourney (PNG/JPG).
  Keep these; they're the masters. Name them the same base name as the web version.
- **`images/`** (this folder) — web-optimized **WebP** used by `index.html`.

## Naming

Numbered in story order, lowercase, hyphenated. Use these exact names so the page wiring
is predictable (`index.html` will reference `images/<name>.webp`):

| # | Web file (`images/`) | Source (`images/source/`) | Plate | --ar |
|---|---|---|---|---|
| 01 | `01-notification.webp` | `01-notification.png` | The Notification | 2:1 |
| 02 | `02-everywhere.webp` | `02-everywhere.png` | Everywhere at Once | 16:9 |
| 03 | `03-drive.webp` | `03-drive.png` | No Particular Direction | 2:1 |
| 04 | `04-ox-in-road.webp` | `04-ox-in-road.png` | The Ox in the Road | 2:1 |
| 05 | `05-mirror.webp` | `05-mirror.png` | The Mirror | 3:2 |
| 06 | `06-field.webp` | `06-field.png` | After, in the Field | 2:1 |
| 07 | `07-console.webp` | `07-console.png` | The Console | 16:9 |
| 08 | `08-four-stars.webp` | `08-four-stars.png` | Four Stars | 4:5 |

**Variants / retries:** keep alternates in `images/source/` with a suffix, e.g.
`04-ox-in-road-alt2.png`, and just copy the chosen one to the plain `04-ox-in-road.png`
name (and export the WebP). That way the "winner" filename never changes.

## Getting to WebP

Drop the PNGs in `images/source/` and I can convert + resize them to WebP for the web
folder (target ~1600px on the long edge, quality ~82). Or do it yourself with:

```
cwebp -q 82 images/source/04-ox-in-road.png -o images/04-ox-in-road.webp
```

Once the `images/` folder has the eight WebP files by these names, tell me and I'll wire
the scroll fade-ins into `index.html`.
