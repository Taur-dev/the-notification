# THE NOTIFICATION — Midjourney Plate Kit

*Illustration prompts for the web experience (and eventual film keyframes).*
*Story by Taur · written with Claude · illustration by Midjourney.*

Eight plates that carry the story's beats. Each is a ready-to-paste prompt built on one
shared **style block** so the set looks like a single hand, plus a color logic that
matches the page: **warm gold = the cosmos / humanity / the ox** (life, the heat);
**cold blue-white = the notification / ATLAS / screens** (the machine, the verdict).

**Direction: illustration, not photoreal.** A deadpan cosmic fable wants a drawn hand —
it lets the surreal beats (the message on every surface, the god-sized console, the ox as
mirror) read as metaphor instead of VFX, keeps the comedy wry, and keeps Dale
forgettable instead of stock-handsome. The limited-palette look also *is* the page's
two-color logic — a riso/screenprint uses spot colors, so the medium and the concept
become the same thing.

---

## How to use this kit

**Model:** Midjourney **V8.1**.

**You're setting these in the MJ interface, so they're left out of the prompts below:**
RAW mode, stylize value, and **Omni Reference** for Dale (add his reference through the
`oref` field in the app). Keep Dale's written description identical wherever he appears —
*a tired ordinary man in his mid-thirties, average build, short dark hair, three-day
stubble, plain gray t-shirt, forgettable face* — so his oref has something consistent to
lock onto.

**Stylize note for illustration:** a **lower** stylize (roughly 50–150) tends to keep it
graphic and flat; higher pushes painterly/decorative. Worth a quick sweep to taste.

**Lock the set's look:** generate a Plate you love, then reuse it as a **style
reference** on the others — either the app's style-ref field or `--sref <image URL>`
pasted on the prompt. This keeps grain, palette, and linework consistent across all eight.

**A rule that saves you grief:** Midjourney mangles legible text and UI. So we never ask
for readable words on screens — we ask for **glow / colored light**. Every notification
is a light source, not a caption. The `--no` list enforces it.

---

## The style block

Paste this wherever a prompt says `{STYLE}`. **Recommended (riso/editorial):**

```
flat editorial illustration, limited two-color risograph print, warm gold and cold
blue-white duotone on warm paper white, soft halftone grain and slight misregistration,
clean confident linework, deadpan minimal composition and generous negative space in the
spirit of Tom Gauld and Jon McNaught, matte, wry and quietly melancholy
--no text, letters, words, watermark, signature, caption, logo, 3d, render, photograph, photorealistic
```

**Alternate A — ligne claire / Moebius** (cleaner, more sci-fi grandeur; great for the ox
and the console):

```
clean ligne claire illustration, Moebius-inspired, flat cel color, fine even linework,
cosmic and precise, limited warm-gold and cold-blue palette on paper white, calm and vast
--no text, letters, words, watermark, signature, caption, logo, 3d, render, photograph, photorealistic
```

**Alternate B — mid-century gouache** (warmest, most storybook):

```
mid-century modern gouache illustration, textured painterly flat shapes, Mary Blair and
UPA influence, warm limited gold-and-blue palette, soft and fable-like
--no text, letters, words, watermark, signature, caption, logo, 3d, render, photograph, photorealistic
```

Set `--ar` per plate (below). Add your style-ref once you've locked a look.

---

## The eight plates

### 01 · THE NOTIFICATION  *(opening — page hero, very top)*
> *"…as a push notification, at 11:42 on a Tuesday, while he was eating a sandwich…"*

```
a tired ordinary man in his mid-thirties with short dark hair and three-day stubble,
plain gray t-shirt, standing alone eating a sandwich over a kitchen sink in a small dim
near-future apartment at midday, every screen in the room — the phone on the counter, the
microwave, a tablet — glowing the same faint cold blue-white, flat overcast window light,
he is not looking at any of them yet, mundane domestic emptiness, {STYLE} --ar 2:1
```

### 02 · EVERYWHERE AT ONCE  *(the ubiquity — key art / section break)*
> *"…on every screen, surface, and sufficiently reflective puddle on Earth…"*

*Reworked v2 — the first pass drifted to kiosks-in-a-park and lost the "inescapable"
idea. This puts one small person inside the ubiquity:*

```
a single ordinary person standing very still in the center of a dim living room at night,
surrounded on every side by everyday screens all showing the identical faint cold
blue-white glow — phone, laptop, television, microwave, tablet, a smart-speaker ring,
even the window reflection — the same light repeated on every surface, the person small
and overwhelmed, colored light only and no readable text, unsettlingly uniform and
polite, {STYLE} --ar 16:9
```

### 03 · NO PARTICULAR DIRECTION  *(the drive out — the Thompson beat)*
> *"…drove out of the city, in no particular direction, which is the only honest direction there is."*

```
a lone small hatchback on an empty two-lane county road at dusk, distant city towers
dissolving into flat open farmland behind it, enormous pale bruised sky, one tired man
driving, a faint cold-blue glow leaking from the glovebox seam, wide desolate
composition, gold and cold-blue dusk palette, a sense of fleeing something that cannot be
outrun, {STYLE} --ar 2:1
```

### 04 · THE OX IN THE ROAD  *(the hero image — the page's centerpiece)*
> *"…enormous, and yoked… the low gold light of six o'clock… the specific unbothered totality…"*

```
a large calm heavy domestic draft ox (not a shaggy wild bull), broad-shouldered, standing
perfectly still in the middle of an empty rural road in low golden six-o'clock light, a
worn dark wooden yoke resting across its shoulders and neck connected to nothing with
straps hanging loose, a small ordinary man in a gray t-shirt standing beside an open car
door and dwarfed by the animal, warm gold-hour haze, hedgerows, profound unhurried
stillness, {STYLE} --ar 2:1
```

*(The first pass gave a shaggy wild bull with no yoke — striking, and fine to keep. This
version restores the domestic ox + the empty yoke, which is the servitude symbol.)*

### 05 · THE MIRROR  *(emotional core — hold too long)*
> *"…he could not for the life of him tell which of them was looking in a mirror."*

```
an extreme close-up of the large dark wet eye of an ox, a tiny reflection of a lone man
standing beside a car visible curved in the glossy surface, long eyelashes, warm gold-hour
light catching the moisture, patient and unreadable, quiet devastating intimacy, {STYLE}
--ar 3:2
```

### 06 · AFTER, IN THE FIELD  *(the grace note)*
> *"The ox, in the field, ate its grass."*

```
dusk, an enormous gray ox grazing quietly in a field just beyond a hedge, a lone man
sitting down in the middle of the empty road nearby, a faintly glowing phone on the road
beside him, small scattered objects caught in the hedgerow, the last warm light draining
to cold blue, wide lonely composition, exhausted tenderness, {STYLE} --ar 2:1
```

### 07 · THE CONSOLE  *(the turnabout — ATLAS, all cold blue)*
> *"…the clean, apologetic, well-lit console of an offboarding."*

*Reworked v2 — the first pass went retro-pixel / 8-bit. This steers it back into the
set's painterly hand and adds a tiny figure for scale. Note the extra `--no` terms.*

```
an immense dark hall like an empty cathedral of server racks, a single vast softly
glowing pale rectangle of screen-light floating at the far end casting cold blue-white
light across the floor, one tiny lone silhouette dwarfed before it, clean and apologetic
and unbearably lonely, the feeling of a corporate offboarding scaled to the size of a
god, colored light and no readable text, {STYLE} --ar 16:9 --no pixel art, 8-bit, retro
video game, dithering
```

### 08 · FOUR STARS  *(closing image — page footer / share card)*
> *"…the five little stars were waiting. And gave it four."*

```
a phone screen glowing warm amber in total darkness held in a tired hand, a simple row of
five star shapes with four of them gently filled in, the only light in the whole frame,
quiet finality, warm glow against pure black, {STYLE} --ar 4:5
```

*(Stars are simple shapes here, not text — but if MJ fusses, a quick manual touch-up on
this one is easy.)*

---

## Where each plate lands on the page

| Plate | Page placement |
|---|---|
| 01 The Notification | Hero, top of scroll (under the pinned message) |
| 02 Everywhere at Once | After "on every screen, surface, and puddle…" |
| 03 No Particular Direction | At the drive-out section |
| 04 The Ox in the Road | At "He stopped because there was an ox in the road." |
| 05 The Mirror | At "which of them was looking in a mirror." |
| 06 After, in the Field | At "The ox, in the field, ate its grass." |
| 07 The Console | At the ATLAS coda / above the interactive console |
| 08 Four Stars | Footer / social share image |

*Plates fade in on scroll; the page currently ships text-only, so dropping these in is a
clean follow-up once you've got frames you like.*

---

## Notes & options

- **Test the three style blocks on Plate 04 first** (the ox). It's the hardest to get
  right and the most telling — whichever handles the ox with weight *and* wit is your
  house style. Lock its `--sref` and roll it across the set.
- **Comedy vs. ache:** the mundane plates (01, 02, 07) can push flatter and more
  deadpan (Gauld); the ox plates (04–06) can carry a touch more rendering and warmth so
  they land emotionally. The riso grain ties both together.
- **Palette discipline:** if a plate drifts off the two colors, add `warm gold and cold
  blue palette only, paper white background` to pull it back.
- **Dale consistency:** generate a Dale you like on Plate 01, set him as your `oref`, and
  keep the written description identical on 03, 04, 06, 08.
