#!/usr/bin/env python3
"""Render the 18 Nov 2026 world-news infographic (1024x1024 PNG).

Deterministic and offline: PIL + DejaVu fonts only, no network, no
randomness. Six verified stories from 18 November 2026, one panel each.
"""
import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

CANVAS_W, CANVAS_H = 1024, 1024
INK_BG = (11, 18, 32)
CARD_BG = (26, 36, 60)
CARD_EDGE = (56, 70, 92)
INK_WHITE = (255, 255, 255)
INK_BODY = (205, 214, 226)
INK_FOOT = (150, 164, 186)
BAND_RED = (176, 24, 24)
BAND_TEXT = (254, 216, 172)
STRIPES = [(238, 68, 68), (248, 113, 22), (233, 179, 8), (33, 197, 94), (58, 130, 246), (167, 85, 247)]

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def load_font(filename, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, filename), size)


TITLE_FONT = load_font("DejaVuSans-Bold.ttf", 46)
SUB_FONT = load_font("DejaVuSans-Bold.ttf", 20)
LABEL_FONT = load_font("DejaVuSans-Bold.ttf", 17)
HEAD_FONT = load_font("DejaVuSans-Bold.ttf", 26)
BODY_FONT = load_font("DejaVuSans.ttf", 20)
FOOT_FONT = load_font("DejaVuSans.ttf", 15)
DATE_FONT = load_font("DejaVuSans-Bold.ttf", 30)

PANELS = [
    dict(tag="1  SHENZHEN SUMMIT", head="Trump lands for trilateral",
         body="Trump arrives in Shenzhen for the first-ever US-China-Russia trilateral summit with Xi and Putin, set for Thursday."),
    dict(tag="2  IRAN WAR", head="US hits Qeshm; Iran hits back",
         body="US jets strike a missile site on Iran's Qeshm Island. Iran's drones hit a US base in Kuwait and a radar site in Bahrain."),
    dict(tag="3  UKRAINE", head="Kerch Bridge span falls",
         body="Ukraine hits the Kerch Bridge a second day running; part of the road span collapses, rail traffic halted."),
    dict(tag="4  CYCLONE AKVAN", head="47,000 evacuated",
         body="Severe Cyclone Akvan bears down on India's east coast. Over 47,000 people evacuated in Odisha; landfall due Friday."),
    dict(tag="5  NVIDIA", head="Record $115.8bn quarter",
         body="Nvidia revenue doubles to $115.8bn, up 103% in a year. Its board rejects ex-chief Jensen Huang's offer to return."),
    dict(tag="6  HEALTH", head="US loses measles-free status",
         body="The US loses its measles elimination status after 26 years, as the virus keeps spreading for over a year."),
]


def draw_header(draw):
    draw.rectangle([0, 0, CANVAS_W, 118], fill=BAND_RED)
    draw.text((28, 16), "WORLD NEWS", font=TITLE_FONT, fill=INK_WHITE)
    draw.text((28, 72), "WEDNESDAY  18  NOVEMBER  2026  •  6 STORIES IN ONE IMAGE",
              font=SUB_FONT, fill=BAND_TEXT)
    draw.text((CANVAS_W - 28, 28), "18 NOV", font=DATE_FONT, fill=INK_WHITE, anchor="ra")


def draw_panel(draw, panel, accent, left, top, width, height):
    draw.rounded_rectangle([left, top, left + width, top + height], radius=14,
                           fill=CARD_BG, outline=CARD_EDGE, width=1)
    draw.rounded_rectangle([left, top, left + width, top + 10], radius=5, fill=accent)
    draw.text((left + 18, top + 22), panel["tag"], font=LABEL_FONT, fill=accent)
    cursor = top + 52
    for line in textwrap.wrap(panel["head"], width=24)[:2]:
        draw.text((left + 18, cursor), line, font=HEAD_FONT, fill=INK_WHITE)
        cursor += 32
    cursor += 6
    for line in textwrap.wrap(panel["body"], width=38)[:4]:
        draw.text((left + 18, cursor), line, font=BODY_FONT, fill=INK_BODY)
        cursor += 26


def main():
    canvas = Image.new("RGB", (CANVAS_W, CANVAS_H), INK_BG)
    draw = ImageDraw.Draw(canvas)
    draw_header(draw)
    origin_x, origin_y = 24, 138
    cell_w, cell_h = 476, 258
    step_x, step_y = 24, 18
    for index, panel in enumerate(PANELS):
        col, row = index % 2, index // 2
        draw_panel(draw, panel, STRIPES[index],
                   origin_x + col * (cell_w + step_x),
                   origin_y + row * (cell_h + step_y),
                   cell_w, cell_h)
    draw.text((28, CANVAS_H - 38),
              "Sources: AP • Reuters • Straits Times • Outlook India  |  18 Nov 2026",
              font=FOOT_FONT, fill=INK_FOOT)
    here = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(here, "entry.png")
    canvas.save(target, "PNG", optimize=True)
    print(target, os.path.getsize(target), canvas.size)


if __name__ == "__main__":
    main()
