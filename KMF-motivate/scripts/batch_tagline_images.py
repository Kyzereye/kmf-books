#!/usr/bin/env python3
"""Generate one social image per entry in new-taglines.md with random template + color."""

from __future__ import annotations

import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from generate_social_image import SCHEMES, generate_image, slugify  # noqa: E402

TAGLINES_MD = ROOT / "new-taglines" / "new-taglines.md"
OUT_DIR = ROOT / "new-taglines" / "tagline-images"


def parse_taglines(path: Path) -> list[tuple[str, str, str]]:
    """Return list of (number, tagline, body)."""
    text = path.read_text(encoding="utf-8")
    parts = re.split(r"^## (\d{2})\. (.+)$", text, flags=re.MULTILINE)
    entries: list[tuple[str, str, str]] = []

    for i in range(1, len(parts), 3):
        num, _title, block = parts[i], parts[i + 1], parts[i + 2]
        lines = [ln.strip() for ln in block.strip().splitlines() if ln.strip() and not ln.strip().startswith("---")]
        if len(lines) < 2:
            continue
        tagline = lines[0].strip("*").strip()
        body = " ".join(lines[1:])
        entries.append((num, tagline, body))

    return entries


def main() -> None:
    entries = parse_taglines(TAGLINES_MD)
    if not entries:
        raise SystemExit(f"No taglines found in {TAGLINES_MD}")

    templates = list(range(1, 6))
    schemes = list(SCHEMES.keys())
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    for num, tagline, body in entries:
        template = random.choice(templates)
        scheme = random.choice(schemes)
        filename = f"{num}-{slugify(tagline)}.png"
        out_path = OUT_DIR / filename
        generate_image(tagline, body, template, scheme, out_path)
        print(f"{filename}  template={template}  scheme={scheme}")

    print(f"\nGenerated {len(entries)} images in {OUT_DIR}")


if __name__ == "__main__":
    main()
