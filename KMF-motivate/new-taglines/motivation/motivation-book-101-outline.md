# Motivation Book — 101 Outline

**Book:** *Keep Moving Forward: Motivation*  
**Status:** Implemented — 101 entries, 101 story files (+ `stoic.md` reference)  
**Structure:** 7 chapters = **7 project themes**. Continuous book order **01–101**.

**QA:** `python scripts/verify_motivation_book.py`

---

## Theme distribution (flexible)

Counts are **close, not even** — Start Moving is heavier because this is the starting book.

| Ch | Theme | Items | Book # |
|----|-------|-------|--------|
| 1 | Start Moving | 17 | 01–17 |
| 2 | Daily Discipline | 14 | 18–31 |
| 3 | Mind Over Noise | 15 | 32–46 |
| 4 | Push Through | 16 | 47–62 |
| 5 | Guard Your Ground | 14 | 63–76 |
| 6 | Commit & Own It | 13 | 77–89 |
| 7 | Trust the Long Road | 12 | 90–101 |

Extra entries in a theme are fine when they fit better there than elsewhere.

---

## Overlap policy: merge vs reframe

| Situation | Action |
|-----------|--------|
| **True duplicate** — reader would say *"same one"* | **Merge** into keeper; fold good lines into body/story |
| **Similar surface** — same kind of action, different blocker | **Reframe** — keep entry, assign **theme** (chapter), rewrite body/story for that lens |

**Stoic mitigation:** Reduce redundancy on purpose. Some readers will still group ideas; control what you can.

### Merged away (13) — deleted

Folded into keepers; story files removed.

| Keeper | Merged away |
|--------|-------------|
| Done Beats Perfect | Let Done Lead, Stop Courting Perfect |
| Speak Less Do More | Lead With Action |
| Do The Hard Thing | Choose The Hard Door |
| Do The Next Small Thing | Shrink It And Start, Lower The Starting Bar, Finish The First Inch |
| Begin Badly On Purpose | Start Messy Stay Honest |
| Run The First Lap | Trust The First Step |
| Open The Document | Open The Damn File |
| Ten Minutes Counts | Give It Five Minutes |
| Move Your Feet First | Press Start On You |
| Close The Escape Hatch | Drop The Exit Strategy |

### Reframed (kept) — theme reassignment

Same tagline family, different chapter lens — stories updated with **## Theme**.

Examples: *One Brave Minute* → Push Through; *Stop Researching Start* → Mind Over Noise; *Win Hour One* → Guard Your Ground; *Flip The Switch* → Start Moving; *Answer The Hard Email* → Push Through.

---

## New entries (36)

Master **#121–#156** in `new-taglines.md`. Book **#27–31, 42–46, 62, 69–76, 81–89, 94–101**.

---

## Implementation checklist

- [x] Merge 13 duplicates
- [x] Reframe similar entries across themes
- [x] `new-taglines-motivation.md` — 101 by chapter
- [x] Master archive #121–#156
- [x] 101 story files with Category + Theme
- [x] `scripts/verify_motivation_book.py`
- [x] Sync flat `taglines-stories/` archive (new entries #121–#156)

---

## Notes

- **Eat The Frog** and **Do The Hard Thing** stay separate.
- **Ship At Seventy Percent** stays separate from **Done Beats Perfect**.
- `stoic.md` remains private reference — not a published chapter.
