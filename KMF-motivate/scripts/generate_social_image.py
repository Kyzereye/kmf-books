#!/usr/bin/env python3
"""Generate 1080x1080 social images with 5 border templates and 3 color schemes."""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1080
MARGIN = 48
LINE_W = 3
DASH_HALF = 52
DEPTH_STEP = 24  # inset between border levels
LEVEL_ARMS = (132, 102, 72)  # corner arm length per depth (outer → inner)
LEVEL_WIDTHS = (3, 2, 1)

SCHEMES = {
    "light": {
        "bg": (250, 248, 244),
        "text": (18, 18, 22),
        "subtext": (55, 52, 48),
        "accent": (168, 132, 78),  # tan — visible on white
    },
    "dark": {
        "bg": (18, 18, 22),
        "text": (245, 242, 235),
        "subtext": (200, 196, 188),
        "accent": (212, 168, 83),  # gold/tan — visible on black
    },
    "tan": {
        "bg": (210, 186, 152),
        "text": (18, 18, 22),
        "subtext": (45, 40, 36),
        "accent": (18, 18, 22),  # black — visible on tan
    },
}

# Border template → default color scheme
TEMPLATE_SCHEME = {
    1: "dark",   # corner L-brackets
    2: "light",  # full frame
    3: "tan",    # double corner ticks
    4: "dark",   # top/bottom bars
    5: "light",  # broken frame
}


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Georgia Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Georgia.ttf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def draw_center_dashes(draw: ImageDraw.ImageDraw, accent: tuple, margin: int = MARGIN) -> None:
    y_top = margin + 20
    y_bot = H - margin - 20
    draw.line([(W // 2 - DASH_HALF, y_top), (W // 2 + DASH_HALF, y_top)], fill=accent, width=2)
    draw.line([(W // 2 - DASH_HALF, y_bot), (W // 2 + DASH_HALF, y_bot)], fill=accent, width=2)


def level_inset(base: int, level: int) -> int:
    """level 0 = outer, 1 = middle, 2 = inner"""
    return base + level * DEPTH_STEP


def draw_corner_Ls(
    draw: ImageDraw.ImageDraw,
    accent: tuple,
    inset: int,
    arm: int,
    width: int = 2,
) -> None:
    """L-brackets at all four corners for one depth level."""
    draw.line([(inset, inset), (inset + arm, inset)], fill=accent, width=width)
    draw.line([(inset, inset), (inset, inset + arm)], fill=accent, width=width)
    draw.line([(W - inset, inset), (W - inset - arm, inset)], fill=accent, width=width)
    draw.line([(W - inset, inset), (W - inset, inset + arm)], fill=accent, width=width)
    draw.line([(inset, H - inset), (inset + arm, H - inset)], fill=accent, width=width)
    draw.line([(inset, H - inset), (inset, H - inset - arm)], fill=accent, width=width)
    draw.line([(W - inset, H - inset), (W - inset - arm, H - inset)], fill=accent, width=width)
    draw.line([(W - inset, H - inset), (W - inset, H - inset - arm)], fill=accent, width=width)


def draw_off_center_edge_dashes(
    draw: ImageDraw.ImageDraw,
    accent: tuple,
    inset: int,
    dash_half: int = 34,
    width: int = 2,
) -> None:
    """Longer dashes along each edge, offset from center — no crosses."""
    positions = (0.24, 0.76)
    for t in positions:
        x = int(W * t)
        y = int(H * t)
        draw.line([(x - dash_half, inset), (x + dash_half, inset)], fill=accent, width=width)
        draw.line([(x - dash_half, H - inset), (x + dash_half, H - inset)], fill=accent, width=width)
        draw.line([(inset, y - dash_half), (inset, y + dash_half)], fill=accent, width=width)
        draw.line([(W - inset, y - dash_half), (W - inset, y + dash_half)], fill=accent, width=width)


def draw_three_level_corners(draw: ImageDraw.ImageDraw, accent: tuple, base: int = MARGIN) -> None:
    """Nested L-brackets — three depths, progressively shorter arms."""
    for level in range(3):
        inset = level_inset(base, level)
        arm = LEVEL_ARMS[level]
        width = LEVEL_WIDTHS[level]
        draw_corner_Ls(draw, accent, inset, arm, width)
        draw_off_center_edge_dashes(draw, accent, inset, dash_half=30 - level * 4, width=max(1, width))


def draw_three_level_frames(draw: ImageDraw.ImageDraw, accent: tuple, base: int = MARGIN) -> None:
    """Nested full rectangles — three depths."""
    for level in range(3):
        inset = level_inset(base, level)
        width = LEVEL_WIDTHS[level]
        draw.rectangle([inset, inset, W - inset, H - inset], outline=accent, width=width)
        draw_off_center_edge_dashes(draw, accent, inset, dash_half=32 - level * 4, width=max(1, width))


def draw_border(template: int, draw: ImageDraw.ImageDraw, accent: tuple) -> None:
    m = MARGIN

    if template == 1:
        # Three nested corner L-bracket levels
        draw_three_level_corners(draw, accent, m)
        draw_center_dashes(draw, accent)

    elif template == 2:
        # Three nested full frames
        draw_three_level_frames(draw, accent, m)
        draw_center_dashes(draw, accent)

    elif template == 3:
        # Three stepped corner tick layers with long arms
        for level in range(3):
            inset = level_inset(m, level)
            arm = LEVEL_ARMS[level]
            width = LEVEL_WIDTHS[level]
            draw_corner_Ls(draw, accent, inset, arm, width)
            # second pass: parallel offset ticks for depth
            if level < 2:
                inner = inset + 12
                short = int(arm * 0.72)
                draw_corner_Ls(draw, accent, inner, short, max(1, width - 1))
            draw_off_center_edge_dashes(draw, accent, inset, dash_half=30 - level * 4, width=max(1, width))
        draw_center_dashes(draw, accent)

    elif template == 4:
        # Three nested top/bottom bar pairs + long side accents (level 2 only)
        mid_y = H // 2
        for level in range(3):
            inset = level_inset(m + 8, level)
            width = LEVEL_WIDTHS[level]
            bar_span = W - inset * 2
            draw.line([(inset, inset), (inset + bar_span, inset)], fill=accent, width=width)
            draw.line([(inset, H - inset), (inset + bar_span, H - inset)], fill=accent, width=width)
            tick = 40 - level * 8
            for x in (inset, inset + bar_span):
                draw.line([(x, inset), (x, inset + tick)], fill=accent, width=max(1, width))
                draw.line([(x, H - inset), (x, H - inset - tick)], fill=accent, width=max(1, width))
            if level == 1:
                side_span = 280
                draw.line([(inset, mid_y - side_span // 2), (inset, mid_y + side_span // 2)], fill=accent, width=width)
                draw.line([(W - inset, mid_y - side_span // 2), (W - inset, mid_y + side_span // 2)], fill=accent, width=width)
            draw_off_center_edge_dashes(draw, accent, inset, dash_half=28 - level * 4, width=max(1, width))
        draw_center_dashes(draw, accent)

    elif template == 5:
        # Three nested broken frames — longer runs, smaller gaps on inner levels
        gaps = (96, 72, 52)
        for level in range(3):
            inset = level_inset(m, level)
            gap = gaps[level]
            width = LEVEL_WIDTHS[level]
            mid_x, mid_y = W // 2, H // 2
            # Top & bottom
            draw.line([(inset, inset), (mid_x - gap, inset)], fill=accent, width=width)
            draw.line([(mid_x + gap, inset), (W - inset, inset)], fill=accent, width=width)
            draw.line([(inset, H - inset), (mid_x - gap, H - inset)], fill=accent, width=width)
            draw.line([(mid_x + gap, H - inset), (W - inset, H - inset)], fill=accent, width=width)
            # Left & right
            draw.line([(inset, inset), (inset, mid_y - gap)], fill=accent, width=width)
            draw.line([(inset, mid_y + gap), (inset, H - inset)], fill=accent, width=width)
            draw.line([(W - inset, inset), (W - inset, mid_y - gap)], fill=accent, width=width)
            draw.line([(W - inset, mid_y + gap), (W - inset, H - inset)], fill=accent, width=width)
            corner = LEVEL_ARMS[level] // 3
            for x, y, dx, dy in (
                (inset, inset, 1, 1),
                (W - inset, inset, -1, 1),
                (inset, H - inset, 1, -1),
                (W - inset, H - inset, -1, -1),
            ):
                draw.line([(x, y), (x + dx * corner, y)], fill=accent, width=max(1, width))
                draw.line([(x, y), (x, y + dy * corner)], fill=accent, width=max(1, width))
            draw_off_center_edge_dashes(draw, accent, inset, dash_half=28 - level * 4, width=max(1, width))
        draw_center_dashes(draw, accent)

    else:
        raise ValueError(f"Unknown template: {template}")


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current: list[str] = []
    for word in words:
        test = " ".join(current + [word])
        if draw.textlength(test, font=font) <= max_width:
            current.append(word)
        else:
            if current:
                lines.append(" ".join(current))
            current = [word]
    if current:
        lines.append(" ".join(current))
    return lines


def generate_image(
    tagline: str,
    body: str,
    template: int,
    scheme_name: str | None = None,
    out_path: str | Path | None = None,
) -> Image.Image:
    if template not in range(1, 6):
        raise ValueError("template must be 1–5")
    scheme_name = scheme_name or TEMPLATE_SCHEME[template]
    scheme = SCHEMES[scheme_name]

    img = Image.new("RGB", (W, H), scheme["bg"])
    draw = ImageDraw.Draw(img)
    draw_border(template, draw, scheme["accent"])

    title_font = load_font(72, bold=True)
    body_font = load_font(34, bold=False)

    pad_x = 120
    max_text_w = W - pad_x * 2
    body_lines = wrap_text(draw, body, body_font, max_text_w)

    title_bbox = draw.textbbox((0, 0), tagline, font=title_font)
    title_h = title_bbox[3] - title_bbox[1]
    body_block_h = len(body_lines) * 46
    gap = 36
    total_h = title_h + gap + body_block_h
    start_y = (H - total_h) // 2

    title_w = draw.textlength(tagline, font=title_font)
    draw.text(((W - title_w) / 2, start_y), tagline, font=title_font, fill=scheme["text"])

    y = start_y + title_h + gap
    for line in body_lines:
        line_w = draw.textlength(line, font=body_font)
        draw.text(((W - line_w) / 2, y), line, font=body_font, fill=scheme["subtext"])
        y += 46

    if out_path:
        Path(out_path).parent.mkdir(parents=True, exist_ok=True)
        img.save(out_path, "PNG", optimize=True)

    return img


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[-\s]+", "-", text).strip("-")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate social quote images")
    parser.add_argument("--tagline", required=True)
    parser.add_argument("--body", required=True)
    parser.add_argument("--template", type=int, choices=range(1, 6))
    parser.add_argument("--scheme", choices=list(SCHEMES.keys()))
    parser.add_argument("--all-templates", action="store_true")
    parser.add_argument("--out-dir", default="images")
    parser.add_argument("--prefix", default="")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    slug = slugify(args.tagline)
    prefix = f"{args.prefix}-" if args.prefix else ""

    if args.all_templates:
        for t in range(1, 6):
            scheme = args.scheme or TEMPLATE_SCHEME[t]
            name = f"{prefix}{slug}-template{t}-{scheme}.png"
            path = out_dir / name
            generate_image(args.tagline, args.body, t, scheme, path)
            print(path)
    else:
        t = args.template or 1
        scheme = args.scheme or TEMPLATE_SCHEME[t]
        name = f"{prefix}{slug}-template{t}-{scheme}.png"
        path = out_dir / name
        generate_image(args.tagline, args.body, t, scheme, path)
        print(path)


if __name__ == "__main__":
    main()
