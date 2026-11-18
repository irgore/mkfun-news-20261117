#!/usr/bin/env python3
"""make.fun entry: Sum up 17 November's world news in one image.
Copies the pre-built news summary image to /output/entry.png.
No network — runs in sandbox with stdlib only."""
import shutil, os

SRC = os.path.join(os.environ.get("MAKEFUN_BOT_DIR", "/bot"), "entry.png")
DST = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")
shutil.copy2(SRC, DST)
