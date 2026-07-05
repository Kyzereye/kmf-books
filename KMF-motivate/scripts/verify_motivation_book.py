#!/usr/bin/env python3
"""QA checks for Keep Moving Forward: Motivation (101 entries).

Usage:
    python scripts/verify_motivation_book.py

Exit code 0 if all checks pass; 1 otherwise.
Extend this script when new verification rules are needed.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MOTIVATION_MD = ROOT / "new-taglines" / "motivation" / "new-taglines-motivation.md"
STORIES_DIR = ROOT / "new-taglines" / "motivation" / "taglines-stories"

THEMES = {
    "Start Moving",
    "Daily Discipline",
    "Mind Over Noise",
    "Push Through",
    "Guard Your Ground",
    "Commit & Own It",
    "Trust the Long Road",
}

ENTRY_RE = re.compile(r"^## (\d{1,3})\. .+ - motivation\s*$", re.MULTILINE)
THEME_COMMENT_RE = re.compile(r"<!-- theme: (.+?) -->")
STORY_SECTIONS = ("## Category", "## Theme", "## The idea", "## Story", "## Takeaway")


def main() -> int:
    errors: list[str] = []

    if not MOTIVATION_MD.exists():
        errors.append(f"Missing {MOTIVATION_MD}")
        return report(errors)

    text = MOTIVATION_MD.read_text(encoding="utf-8")
    numbers = [int(m.group(1)) for m in ENTRY_RE.finditer(text)]
    expected = list(range(1, 102))

    if len(numbers) != 101:
        errors.append(f"Expected 101 entries in motivation file, found {len(numbers)}")
    if sorted(numbers) != expected:
        missing = set(expected) - set(numbers)
        extra = set(numbers) - set(expected)
        if missing:
            errors.append(f"Missing book numbers: {sorted(missing)}")
        if extra:
            errors.append(f"Unexpected book numbers: {sorted(extra)}")
        if len(numbers) != len(set(numbers)):
            errors.append("Duplicate book numbers in motivation file")

    # Theme comments (optional but recommended)
    themes_found: list[str] = THEME_COMMENT_RE.findall(text)
    if themes_found:
        bad = [t for t in themes_found if t not in THEMES]
        if bad:
            errors.append(f"Unknown theme comments: {bad}")

    # Story files
    if not STORIES_DIR.exists():
        errors.append(f"Missing {STORIES_DIR}")
    else:
        story_files = sorted(
            p for p in STORIES_DIR.glob("*.md") if p.name != "stoic.md"
        )
        if len(story_files) != 101:
            errors.append(
                f"Expected 101 story files (excluding stoic.md), found {len(story_files)}"
            )

        story_nums = []
        for p in story_files:
            m = re.match(r"^(\d{1,3})-", p.name)
            if not m:
                errors.append(f"Bad story filename (expected NN-slug.md): {p.name}")
                continue
            story_nums.append(int(m.group(1)))
            body = p.read_text(encoding="utf-8")
            for section in STORY_SECTIONS:
                if section not in body:
                    errors.append(f"{p.name}: missing {section}")

        if story_nums and sorted(story_nums) != expected:
            errors.append("Story file numbering does not match 01–101")

    return report(errors)


def report(errors: list[str]) -> int:
    if errors:
        print("FAIL — motivation book verification:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("OK — motivation book: 101 entries, story files and required sections present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
