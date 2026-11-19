"""make.fun bounty: Sum up 18 November's world news in one image.
Deterministic, offline: copies the pre-built entry.png to /output/entry.png.
No network, no randomness, no model calls.
The image itself is built by build_image.py (PIL, DejaVu Sans) from the
six verified 18 Nov 2026 stories listed in README.md.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT = "/output/entry.png"

os.makedirs("/output", exist_ok=True)
shutil.copyfile(SRC, OUT)
print(f"wrote {OUT}")
