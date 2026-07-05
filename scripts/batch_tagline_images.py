#!/usr/bin/env python3
"""Generate one social image per tagline entry from KMF book files or the master archive."""

from __future__ import annotations

import argparse
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from generate_social_image import SCHEMES, TEMPLATES, generate_image, slugify  # noqa: E402

ENTRY_RE = re.compile(r"^## (N?\d+)\. .+ - (\w+)\s*$")
HEADER_RE = re.compile(r"^#{1,3} ")

KMF_BOOKS: dict[str, tuple[str, str]] = {
    "motivation": ("KMF-motivate", "new-taglines-motivation.md"),
    "discipline": ("KMF-discipline", "new-taglines-discipline.md"),
    "resilience": ("KMF-resilience", "new-taglines-resilience.md"),
    "ownership": ("KMF-ownership", "new-taglines-ownership.md"),
    "growth": ("KMF-growth", "new-taglines-growth.md"),
    "mindset": ("KMF-mindset", "new-taglines-mindset.md"),
    "peace": ("KMF-peace", "new-taglines-peace.md"),
    "focus": ("KMF-focus", "new-taglines-focus.md"),
}

BOOKS: dict[str, tuple[str, str]] = {
    **KMF_BOOKS,
    "master": ("new-taglines", "new-taglines.md"),
}


def parse_taglines(path: Path) -> list[tuple[str, str, str, str]]:
    """Return list of (id, tagline, body, category)."""
    lines = path.read_text(encoding="utf-8").splitlines()
    entries: list[tuple[str, str, str, str]] = []
    i = 0

    while i < len(lines):
        line = lines[i]
        m = ENTRY_RE.match(line)
        if not m:
            i += 1
            continue

        entry_id = m.group(1)
        category = m.group(2)
        i += 1
        content_lines: list[str] = []
        while i < len(lines):
            nxt = lines[i]
            if ENTRY_RE.match(nxt):
                break
            if HEADER_RE.match(nxt):
                break
            stripped = nxt.strip()
            if stripped and not stripped.startswith("---"):
                content_lines.append(stripped)
            i += 1

        if len(content_lines) < 2:
            continue
        tagline = content_lines[0].strip("*").strip()
        body = " ".join(content_lines[1:])
        entries.append((entry_id, tagline, body, category))

    return entries


def generate_for_book(
    book_slug: str,
    *,
    input_path: Path | None = None,
    out_dir: Path | None = None,
    skip_existing: bool = False,
) -> int:
    folder, filename = BOOKS[book_slug]
    taglines_md = input_path or (ROOT / folder / filename)
    images_dir = out_dir or (ROOT / folder / "tagline-images")

    if not taglines_md.is_file():
        raise SystemExit(f"Taglines file not found: {taglines_md}")

    entries = parse_taglines(taglines_md)
    if not entries:
        raise SystemExit(f"No taglines found in {taglines_md}")

    templates = list(TEMPLATES)
    schemes = list(SCHEMES.keys())
    images_dir.mkdir(parents=True, exist_ok=True)

    generated = 0
    skipped = 0

    print(f"\n[{book_slug}] {taglines_md.relative_to(ROOT)} → {images_dir.relative_to(ROOT)}")

    for entry_id, tagline, body, category in entries:
        filename_out = f"{entry_id}-{slugify(tagline)}.png"
        out_path = images_dir / filename_out

        if skip_existing and out_path.exists():
            skipped += 1
            print(f"  skip {filename_out} (exists)")
            continue

        template = random.choice(templates)
        scheme = random.choice(schemes)
        generate_image(tagline, body, template, scheme, out_path, category=category)
        print(f"  {filename_out}  template={template}  scheme={scheme}")

        generated += 1

    print(f"Generated {generated} images for {book_slug}" + (f" ({skipped} skipped)" if skipped else ""))
    return generated


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Batch-generate social images from KMF book tagline files or the master archive.",
    )
    parser.add_argument(
        "--book",
        choices=sorted(BOOKS.keys()),
        action="append",
        dest="books",
        metavar="BOOK",
        help="Book to process (repeatable). Choices: " + ", ".join(sorted(BOOKS.keys())),
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Process all eight KMF book folders (not master).",
    )
    parser.add_argument("--input", type=Path, help="Override taglines markdown file (single --book only).")
    parser.add_argument("--out-dir", type=Path, help="Override output directory (single --book only).")
    parser.add_argument("--skip-existing", action="store_true", help="Skip PNGs that already exist.")
    args = parser.parse_args()

    if args.all and args.books:
        raise SystemExit("Use either --all or --book, not both.")
    if args.input or args.out_dir:
        if not args.books or len(args.books) != 1:
            raise SystemExit("--input and --out-dir require exactly one --book.")
    if not args.all and not args.books:
        parser.print_help()
        raise SystemExit("\nSpecify --book <name> or --all.")

    book_slugs = list(KMF_BOOKS.keys()) if args.all else args.books
    total = 0

    for slug in book_slugs:
        total += generate_for_book(
            slug,
            input_path=args.input,
            out_dir=args.out_dir,
            skip_existing=args.skip_existing,
        )

    print(f"\nDone — {total} images across {len(book_slugs)} book(s).")


if __name__ == "__main__":
    main()
