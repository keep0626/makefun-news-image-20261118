#!/usr/bin/env python3
"""Build 1024x1024 news infographic for 18 Nov 2026. Deterministic, no network."""
from PIL import Image, ImageDraw, ImageFont
import textwrap, os

W, H = 1024, 1024
BG = (13, 20, 36)
PANEL = (24, 33, 56)
WHITE = (255, 255, 255)
MUTED = (203, 213, 225)
ACCENTS = [(239, 68, 68), (249, 115, 22), (234, 179, 8), (34, 197, 94), (59, 130, 246), (168, 85, 247)]

def font(name, size):
    p = f"/usr/share/fonts/truetype/dejavu/{name}"
    return ImageFont.truetype(p, size)

F_TITLE = font("DejaVuSans-Bold.ttf", 44)
F_SUB = font("DejaVuSans-Bold.ttf", 20)
F_TAG = font("DejaVuSans-Bold.ttf", 17)
F_HEAD = font("DejaVuSans-Bold.ttf", 26)
F_BODY = font("DejaVuSans.ttf", 20)
F_FOOT = font("DejaVuSans.ttf", 15)

stories = [
    ("1  SHENZHEN SUMMIT", "Trump lands for trilateral",
     "Trump arrives in Shenzhen for the first-ever US-China-Russia trilateral summit with Xi and Putin, set for Thursday."),
    ("2  IRAN WAR", "US hits Qeshm; Iran hits back",
     "US jets strike a missile site on Iran's Qeshm Island. Iran's drones hit a US base in Kuwait and a radar site in Bahrain."),
    ("3  UKRAINE", "Kerch Bridge span falls",
     "Ukraine hits the Kerch Bridge a second day running; part of the road span collapses, rail traffic halted."),
    ("4  CYCLONE AKVAN", "47,000 evacuated",
     "Severe Cyclone Akvan bears down on India's east coast. Over 47,000 people evacuated in Odisha; landfall due Friday."),
    ("5  NVIDIA", "Record $115.8bn quarter",
     "Nvidia revenue doubles to $115.8bn, up 103% in a year. Its board rejects ex-chief Jensen Huang's offer to return."),
    ("6  HEALTH", "US loses measles-free status",
     "The US loses its measles elimination status after 26 years, as the virus keeps spreading for over a year."),
]

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
# header
d.rectangle([0, 0, W, 118], fill=(185, 28, 28))
d.text((28, 18), "WORLD NEWS", font=F_TITLE, fill=WHITE)
d.text((28, 72), "WEDNESDAY  18  NOVEMBER  2026  •  6 STORIES IN ONE IMAGE", font=F_SUB, fill=(254, 215, 170))
d.text((W-28, 28), "18 NOV", font=font("DejaVuSans-Bold.ttf", 30), fill=WHITE, anchor="ra")

# grid 2x3
mx, my = 24, 138
gw, gh = 476, 258
gapx, gapy = 24, 18
for i, (tag, head, body) in enumerate(stories):
    col, row = i % 2, i // 2
    x = mx + col * (gw + gapx)
    y = my + row * (gh + gapy)
    accent = ACCENTS[i]
    d.rounded_rectangle([x, y, x+gw, y+gh], radius=14, fill=PANEL, outline=(51, 65, 85), width=1)
    d.rounded_rectangle([x, y, x+gw, y+10], radius=5, fill=accent)
    d.text((x+18, y+22), tag, font=F_TAG, fill=accent)
    lines = textwrap.wrap(head, width=24)
    yy = y + 52
    for ln in lines[:2]:
        d.text((x+18, yy), ln, font=F_HEAD, fill=WHITE)
        yy += 32
    blines = textwrap.wrap(body, width=38)
    yy += 6
    for ln in blines[:4]:
        d.text((x+18, yy), ln, font=F_BODY, fill=MUTED)
        yy += 26

# footer
d.text((28, H-38), "Sources: AP • Reuters • Straits Times • Outlook India  |  18 Nov 2026", font=F_FOOT, fill=(148, 163, 184))

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
img.save(out, "PNG", optimize=True)
print(out, os.path.getsize(out), img.size)
