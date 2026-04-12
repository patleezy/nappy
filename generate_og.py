#!/usr/bin/env python3
"""
Generate og-image.png for nappy.digital
Output: 1200×630 px RGB PNG in the same directory as this script.
Requirements: Pillow  (pip install Pillow)
Usage: python3 generate_og.py
"""
from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageFilter
import math, os

SCALE = 3
W, H   = 1200, 630
SW, SH = W * SCALE, H * SCALE

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'og-image.png')

SERIF = '/usr/share/fonts/truetype/freefont/FreeSerifBold.ttf'
SANS  = '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'

# ── 1. Background gradient (warm cream top → slightly deeper bottom) ─────────
grad = Image.new('RGB', (1, SH))
top_c, bot_c = (250, 247, 242), (243, 236, 222)
pix = grad.load()
for y in range(SH):
    t = y / SH
    pix[0, y] = tuple(int(top_c[i] * (1 - t) + bot_c[i] * t) for i in range(3))
img = grad.resize((SW, SH), Image.NEAREST).convert('RGBA')

# ── 2. Amber glow halo behind moon ──────────────────────────────────────────
MCX, MCY, MR = 200 * SCALE, 315 * SCALE, 95 * SCALE
glow = Image.new('RGBA', (SW, SH), (0, 0, 0, 0))
pad = 20 * SCALE
ImageDraw.Draw(glow).ellipse(
    [MCX - MR - pad, MCY - MR - pad, MCX + MR + pad, MCY + MR + pad],
    fill=(200, 150, 58, 90))
glow = glow.filter(ImageFilter.GaussianBlur(radius=35 * SCALE))
img = Image.alpha_composite(img, glow)

# ── 3. Crescent moon via alpha-mask subtraction ──────────────────────────────
outer_mask = Image.new('L', (SW, SH), 0)
ImageDraw.Draw(outer_mask).ellipse(
    [MCX - MR, MCY - MR, MCX + MR, MCY + MR], fill=255)

cutout = Image.new('L', (SW, SH), 0)
DX, DY = 68 * SCALE, -20 * SCALE
ImageDraw.Draw(cutout).ellipse(
    [MCX - MR + DX, MCY - MR + DY, MCX + MR + DX, MCY + MR + DY], fill=255)

moon_mask  = ImageChops.subtract(outer_mask, cutout)
moon_layer = Image.new('RGBA', (SW, SH), (200, 150, 58, 255))
moon_layer.putalpha(moon_mask)
img = Image.alpha_composite(img, moon_layer)

# ── 4. Typography ────────────────────────────────────────────────────────────
draw   = ImageDraw.Draw(img)
font_h = ImageFont.truetype(SERIF, 128 * SCALE)
font_t = ImageFont.truetype(SANS,   40 * SCALE)

TX = 345 * SCALE
draw.text((TX, 248 * SCALE), 'Nappy',
          fill=(74, 56, 40, 255), font=font_h)
draw.text((TX + 2 * SCALE, 391 * SCALE), 'Baby Sleep Planner',
          fill=(138, 114, 96, 255), font=font_t)

# ── 5. Decorative 4-pointed stars in the negative space ──────────────────────
def star(d, cx, cy, r_out, r_in, rgba):
    pts = 4
    verts = []
    for i in range(pts * 2):
        angle = math.pi * i / pts - math.pi / 2
        r = r_out if i % 2 == 0 else r_in
        verts.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
    d.polygon(verts, fill=rgba)

STARS = [
    (820, 120, 10, 4, (229, 150, 122, 130)),
    (980, 185,  7, 3, (200, 150,  58, 110)),
    (1060, 390, 9, 4, (155, 143, 196, 120)),
    (745, 490,  6, 2, (229, 150, 122, 100)),
    (900, 520,  5, 2, (200, 150,  58,  90)),
]
for sx, sy, ro, ri, col in STARS:
    star(draw, sx * SCALE, sy * SCALE, ro * SCALE, ri * SCALE, col)

# ── 6. Downsample + save ─────────────────────────────────────────────────────
out = img.resize((W, H), Image.LANCZOS).convert('RGB')
out.save(OUT, 'PNG', optimize=True)
print(f'Saved {OUT}  ({os.path.getsize(OUT) // 1024} KB)')
