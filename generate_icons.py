#!/usr/bin/env python3
"""
Generate the PWA / Apple touch icons for nappy.digital
Output: icon-180.png, icon-192.png, icon-512.png (same directory as this script)
Style matches generate_og.py: warm cream background, amber crescent moon.
The moon stays inside the central ~60% so the icons are safe as "maskable".
Requirements: Pillow  (pip install Pillow)
Usage: python3 generate_icons.py
"""
from PIL import Image, ImageDraw, ImageFilter
import os

HERE = os.path.dirname(os.path.abspath(__file__))
BG, BG2 = (250, 247, 242), (243, 236, 222)
MOON, GLOW = (200, 150, 58), (200, 150, 58, 80)

def make(size):
    S = 4                       # supersample for smooth edges
    N = size * S
    # vertical cream gradient
    img = Image.new('RGBA', (N, N))
    px = img.load()
    for y in range(N):
        t = y / N
        c = tuple(int(BG[i] * (1 - t) + BG2[i] * t) for i in range(3)) + (255,)
        for x in range(N):
            px[x, y] = c
    cx, cy, r = N * 0.5, N * 0.5, N * 0.27
    # soft glow
    glow = Image.new('RGBA', (N, N), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse([cx - r * 1.25, cy - r * 1.25, cx + r * 1.25, cy + r * 1.25], fill=GLOW)
    glow = glow.filter(ImageFilter.GaussianBlur(radius=N * 0.06))
    img = Image.alpha_composite(img, glow)
    # crescent = outer disc minus offset disc
    mask = Image.new('L', (N, N), 0)
    d = ImageDraw.Draw(mask)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=255)
    ox, oy = r * 0.45, -r * 0.30
    d.ellipse([cx - r + ox, cy - r + oy, cx + r + ox, cy + r + oy], fill=0)
    moon = Image.new('RGBA', (N, N), MOON + (255,))
    img.paste(moon, (0, 0), mask)
    return img.resize((size, size), Image.LANCZOS).convert('RGB')

for s in (180, 192, 512):
    out = os.path.join(HERE, f'icon-{s}.png')
    make(s).save(out, optimize=True)
    print('wrote', out)
