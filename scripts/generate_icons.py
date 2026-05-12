"""Generate extension icons (16/32/48/128 px) into ../icons/.

Design: white return-arrow on dark background, with a red "no" overlay
(red circle + diagonal slash) to convey "Enter disabled".
"""

from __future__ import annotations

import os
from PIL import Image, ImageDraw

SIZES = (16, 32, 48, 128)
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "icons")

BG = (33, 33, 33, 255)        # near-black
ARROW = (240, 240, 240, 255)  # near-white
BAN = (220, 38, 38, 255)      # red


def draw_return_arrow(draw: ImageDraw.ImageDraw, size: int) -> None:
    """Draw a stylized return / enter arrow (↵)."""
    s = size
    # Stroke width scales with size.
    w = max(1, round(s * 0.09))

    # Top-right horizontal segment.
    x_right = round(s * 0.78)
    x_left = round(s * 0.32)
    y_top = round(s * 0.28)
    y_bot = round(s * 0.62)

    # Vertical down stroke (right side).
    draw.line([(x_right, y_top), (x_right, y_bot)], fill=ARROW, width=w)
    # Horizontal bottom stroke.
    draw.line([(x_right, y_bot), (x_left, y_bot)], fill=ARROW, width=w)

    # Arrow head at left end (pointing left).
    head = round(s * 0.18)
    draw.line([(x_left, y_bot), (x_left + head, y_bot - head)], fill=ARROW, width=w)
    draw.line([(x_left, y_bot), (x_left + head, y_bot + head)], fill=ARROW, width=w)


def draw_ban(draw: ImageDraw.ImageDraw, size: int) -> None:
    """Draw a red prohibition circle with a diagonal slash."""
    s = size
    pad = max(1, round(s * 0.06))
    ring = max(1, round(s * 0.10))
    bbox = (pad, pad, s - pad - 1, s - pad - 1)
    draw.ellipse(bbox, outline=BAN, width=ring)
    # Diagonal slash (top-left to bottom-right).
    inset = round(s * 0.18)
    draw.line(
        [(pad + inset, pad + inset), (s - pad - 1 - inset, s - pad - 1 - inset)],
        fill=BAN,
        width=ring,
    )


def make_icon(size: int) -> Image.Image:
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Rounded square background.
    radius = max(2, round(size * 0.18))
    draw.rounded_rectangle((0, 0, size - 1, size - 1), radius=radius, fill=BG)

    draw_return_arrow(draw, size)
    draw_ban(draw, size)
    return img


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    for size in SIZES:
        path = os.path.join(OUT_DIR, f"icon{size}.png")
        make_icon(size).save(path, format="PNG", optimize=True)
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
