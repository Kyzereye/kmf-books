#!/usr/bin/env python3
"""Generate 1080x1080 social images with 3 border templates and 3 color schemes."""

from __future__ import annotations

import argparse
import os
import random
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1080
MARGIN = 48
BRAND_TEXT = "Motivational Inspiration"
BRAND_FONT_SIZE = 24
BRAND_PAD = 16
FRAME_WIDTH = 2
DOUBLE_GAP = 18
TRIPLE_GAP = 14
TEMPLATES = (1, 2, 3)  # 1=double broken, 2=triple lines, 3=stepped double

SCHEMES = {
    "light": {
        "bg": (250, 248, 244),
        "text": (18, 18, 22),
        "subtext": (55, 52, 48),
        "accent": (168, 132, 78),
    },
    "dark": {
        "bg": (18, 18, 22),
        "text": (245, 242, 235),
        "subtext": (200, 196, 188),
        "accent": (212, 168, 83),
    },
    "tan": {
        "bg": (210, 186, 152),
        "text": (18, 18, 22),
        "subtext": (45, 40, 36),
        "accent": (18, 18, 22),
    },
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


def inner_inset(template: int) -> int:
    """Innermost frame edge — brand text sits inside this."""
    if template == 1:
        return MARGIN + DOUBLE_GAP
    if template == 2:
        return MARGIN + TRIPLE_GAP * 2
    if template == 3:
        return MARGIN + DOUBLE_GAP + 10
    raise ValueError(f"Unknown template: {template}")


def draw_rect_frame(draw: ImageDraw.ImageDraw, inset: int, accent: tuple, width: int = FRAME_WIDTH) -> None:
    draw.rectangle([inset, inset, W - inset, H - inset], outline=accent, width=width)


def draw_corner_L(
    draw: ImageDraw.ImageDraw,
    inset: int,
    accent: tuple,
    arm: int,
    width: int = FRAME_WIDTH,
) -> None:
    for x, y, dx, dy in (
        (inset, inset, 1, 1),
        (W - inset, inset, -1, 1),
        (inset, H - inset, 1, -1),
        (W - inset, H - inset, -1, -1),
    ):
        draw.line([(x, y), (x + dx * arm, y)], fill=accent, width=width)
        draw.line([(x, y), (x, y + dy * arm)], fill=accent, width=width)


def draw_broken_frame(
    draw: ImageDraw.ImageDraw,
    inset: int,
    accent: tuple,
    gap: int,
    width: int = FRAME_WIDTH,
) -> None:
    mx, my = W // 2, H // 2
    draw.line([(inset, inset), (mx - gap, inset)], fill=accent, width=width)
    draw.line([(mx + gap, inset), (W - inset, inset)], fill=accent, width=width)
    draw.line([(inset, H - inset), (mx - gap, H - inset)], fill=accent, width=width)
    draw.line([(mx + gap, H - inset), (W - inset, H - inset)], fill=accent, width=width)
    draw.line([(inset, inset), (inset, my - gap)], fill=accent, width=width)
    draw.line([(inset, my + gap), (inset, H - inset)], fill=accent, width=width)
    draw.line([(W - inset, inset), (W - inset, my - gap)], fill=accent, width=width)
    draw.line([(W - inset, my + gap), (W - inset, H - inset)], fill=accent, width=width)
    draw_corner_L(draw, inset, accent, arm=36, width=width)


def draw_stepped_corners(
    draw: ImageDraw.ImageDraw,
    inset: int,
    accent: tuple,
    step: int = 14,
    run: int = 52,
    width: int = FRAME_WIDTH,
) -> None:
    draw_rect_frame(draw, inset, accent, width)
    for x, y, sx, sy in (
        (inset, inset, 1, 1),
        (W - inset, inset, -1, 1),
        (inset, H - inset, 1, -1),
        (W - inset, H - inset, -1, -1),
    ):
        draw.line([(x, y), (x + sx * run, y)], fill=accent, width=width)
        draw.line([(x, y), (x, y + sy * run)], fill=accent, width=width)
        draw.line([(x + sx * step, y + sy * step), (x + sx * run, y + sy * step)], fill=accent, width=width)
        draw.line([(x + sx * step, y + sy * step), (x + sx * step, y + sy * run)], fill=accent, width=width)


def draw_border(template: int, draw: ImageDraw.ImageDraw, accent: tuple) -> None:
    m = MARGIN

    if template == 1:
        # Double broken frame
        draw_broken_frame(draw, m, accent, gap=80)
        draw_broken_frame(draw, m + DOUBLE_GAP, accent, gap=64)

    elif template == 2:
        # Triple thin lines
        draw_rect_frame(draw, m, accent, width=1)
        draw_rect_frame(draw, m + TRIPLE_GAP, accent, width=1)
        draw_rect_frame(draw, m + TRIPLE_GAP * 2, accent, width=1)

    elif template == 3:
        # Stepped corners + inner frame
        draw_stepped_corners(draw, m, accent)
        draw_rect_frame(draw, m + DOUBLE_GAP + 10, accent, width=1)

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


def brand_line(category: str | None = None) -> str:
    if category:
        return f"{BRAND_TEXT} - {category.strip().title()}"
    return BRAND_TEXT


def generate_image(
    tagline: str,
    body: str,
    template: int,
    scheme_name: str | None = None,
    out_path: str | Path | None = None,
    category: str | None = None,
) -> Image.Image:
    if template not in TEMPLATES:
        raise ValueError(f"template must be one of {TEMPLATES}")
    scheme_name = scheme_name or random.choice(list(SCHEMES.keys()))
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
    gap = 36
    total_h = title_h + gap + len(body_lines) * 46
    start_y = (H - total_h) // 2

    title_w = draw.textlength(tagline, font=title_font)
    draw.text(((W - title_w) / 2, start_y), tagline, font=title_font, fill=scheme["text"])

    y = start_y + title_h + gap
    for line in body_lines:
        line_w = draw.textlength(line, font=body_font)
        draw.text(((W - line_w) / 2, y), line, font=body_font, fill=scheme["subtext"])
        y += 46

    brand_font = load_font(BRAND_FONT_SIZE, bold=False)
    brand_label = brand_line(category)
    brand_bbox = draw.textbbox((0, 0), brand_label, font=brand_font)
    brand_h = brand_bbox[3] - brand_bbox[1]
    brand_inset = inner_inset(template) + BRAND_PAD
    draw.text(
        (brand_inset, H - brand_inset - brand_h),
        brand_label,
        font=brand_font,
        fill=scheme["accent"],
    )

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
    parser.add_argument("--template", type=int, choices=TEMPLATES)
    parser.add_argument("--scheme", choices=list(SCHEMES.keys()))
    parser.add_argument("--all-templates", action="store_true")
    parser.add_argument("--out-dir", default="images")
    parser.add_argument("--prefix", default="")
    parser.add_argument("--category", help="Category slug for brand line, e.g. peace")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    slug = slugify(args.tagline)
    prefix = f"{args.prefix}-" if args.prefix else ""

    if args.all_templates:
        for t in TEMPLATES:
            scheme = args.scheme or random.choice(list(SCHEMES.keys()))
            name = f"{prefix}{slug}-template{t}-{scheme}.png"
            path = out_dir / name
            generate_image(args.tagline, args.body, t, scheme, path, category=args.category)
            print(path)
    else:
        t = args.template or 1
        scheme = args.scheme or random.choice(list(SCHEMES.keys()))
        name = f"{prefix}{slug}-template{t}-{scheme}.png"
        path = out_dir / name
        generate_image(args.tagline, args.body, t, scheme, path, category=args.category)
        print(path)


if __name__ == "__main__":
    main()
