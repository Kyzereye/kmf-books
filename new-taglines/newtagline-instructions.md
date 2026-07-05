# New Tagline Instructions

Reference for creating or updating original taglines in this project.

**Expanded stories:** see [taglines-stories-instructions.md](taglines-stories-instructions.md) for the long-form format in `taglines-stories/`.

---

## Files

| File | Purpose |
|------|---------|
| `new-taglines/new-taglines.md` | Master archive — all taglines (100 entries: Proofread + New Ones) |
| `new-taglines/{category}/` | One folder per book — e.g. `motivation/`, `discipline/`, `mindset/` |
| `new-taglines/{category}/new-taglines-{category}.md` | Taglines for that book only |
| `new-taglines/{category}/taglines-stories/` | Expanded stories for that book |
| `new-taglines/taglines-stories/` | Original flat copy of all stories (kept for reference) |
| `new-taglines/tagline-images/` | All social images in one folder |
| `new-taglines/taglines-stories-instructions.md` | Rules for story files |
| `new-taglines/newtagline-instructions.md` | This file — short taglines and bodies |
| `scripts/generate_social_image.py` | Single image generator |
| `scripts/batch_tagline_images.py` | Batch images per KMF book (`--book focus`) or all books (`--all`) |
| `scripts/verify_motivation_book.py` | Legacy QA for old 101-entry motivation book layout (optional) |

---

## Tagline (title line)

- **3–6 words**
- Punchy and memorable — fine if slightly grammatically awkward
- Original phrasing; do not reuse book chapter titles or author/book names
- Italic in markdown: `*Your Tagline Here*`

---

## Body (paraphrase)

Bodies are **short and punchy** — usually **1–2 sentences**. Say the idea clearly; don't pile on extra metaphors.

**PAR** (Problem → Action → Result) is a useful mental check, not a length requirement:

| Part | What it does |
|------|----------------|
| **Problem** | The struggle, friction, or wrong default |
| **Action** | What you do instead |
| **Result** | What that gets you — outcome, relief, momentum, clarity |

- Second person (“you”) when it fits
- If one metaphor is enough, stop there
- Respect the language — don't stretch words into meanings they don't carry

### PAR example (Play The Long Game)

**Problem:** Short-term wins pull you off direction; long stretches get frustrating.  
**Action:** Think long-term, stack small wins along the way.  
**Result:** You stay in the game and build something that lasts.

**Draft body:**

> Short-term wins are seductive but long-term thinking is what builds something that lasts. Stack small wins to stay motivated when the payoff is still far off — they ease a long frustrating stretch without replacing the destination. Play long enough and you'll still be standing when others chase quick results and walk away.

---

## Markdown entry format

```markdown
## NN. Title Case Name - category

*Tagline Words Here*

Short punchy body — 1–2 sentences.
```

**Category slug** (lowercase after the dash): `motivation`, `discipline`, `mindset`, `resilience`, `peace`, `focus`, `ownership`, `growth` — and `inspiration` when added. See [Categories](#categories-books-on-the-shelf) below.

**Theme** = chapter grouping *inside* that category's book — not a second shelf label. See [Themes](#themes-chapters-within-each-book).

Each story file in `taglines-stories/` gets matching **## Category** and **## Theme** sections (see [taglines-stories-instructions.md](taglines-stories-instructions.md)).

---

## Category vs theme

| | **Category** | **Theme** |
|--|--------------|-----------|
| **Answers** | Which book? Which reader struggle? | Which *flavor* of that struggle inside the book? |
| **Scope** | One per entry — shelf / book assignment | One per entry — chapter placement inside the book |
| **Example** | *Eat The Frog* → `motivation` | theme **Move Through Fear** (same book, narrower lens) |

**Do not** use themes that are just the category renamed (e.g. theme “Daily Discipline” inside the Discipline book). Themes are **sub-lenses** on the category's reader question.

Target **~12–13 entries per book**, grouped into **3–4 themes × ~3–4 entries** each.

---

## Categories (books on the shelf)

| Slug | Reader question | Cover promise (example) |
|------|-----------------|-------------------------|
| `motivation` | How do I get started when I don't feel like it? | Start when you don't feel like it |
| `discipline` | How do I show up even when I don't feel like it? | Show up on the days you don't want to |
| `resilience` | How do I keep going when it gets hard? | Stay in the fight when it gets hard |
| `ownership` | How do I take ownership of my results? | Own your outcomes, not your excuses |
| `growth` | How do I grow into who I'm becoming? | Level up over the long haul |
| `mindset` | How do I change the way I think about this? | Change the story in your head |
| `peace` | How do I find calm and protect my energy? | Find calm and protect your energy |
| `focus` | How do I focus on what actually matters? | Focus on what actually matters |
| `inspiration` | How do I see a future worth moving toward? | *(planned — pull toward a vision)* |

**Motivation** = push to act. **Inspiration** = pull toward a vision. The rest are *how* you act, endure, think, calm down, or aim attention.

**Future lanes** (own books later, not in current 100): relationships, health & energy, purpose, money & work, confidence as a deep single-topic volume.

---

## Themes (chapters within each book)

Assign **one primary theme** per entry in the category book file (`new-taglines-{category}.md`) and in the story **## Theme** section.

### Motivation — *How do I get started?*

| Theme | What it covers |
|-------|----------------|
| **Beat Perfection** | Polish, rehearsal, shipping rough work — done over perfect |
| **Shrink The Start** | Task too big; first lap, open the file, one small move |
| **Move Through Fear** | Dread, hard thing first, send it scared, make the call |
| **Act Before Ready** | Waiting on mood, permission, consensus — move anyway |
| **Build Momentum** | Keep moving; morning, snowball, lead with action |

### Discipline — *How do I show up anyway?*

| Theme | What it covers |
|-------|----------------|
| **Structure & Routine** | Same hour, calendar, appointments, rise before excuses |
| **Protect The Streak** | Chains, zero days, prove it daily — don't break the chain |
| **Show Up Anyway** | Tired, boring, flat — minimum reps still count |
| **Hard Now, Easy Later** | Choose hard on purpose, build the muscle, make it inevitable |

### Resilience — *How do I keep going?*

| Theme | What it covers |
|-------|----------------|
| **Stay In The Fight** | Arena, hits, grind — keep playing |
| **Use The Pain** | Pain as fuel, walk through fear, grow through discomfort |
| **After The Fall** | Stumble, bad week, fail forward — come back tomorrow |
| **One More** | Almost quit — give it one more, bend without breaking |

### Ownership — *How do I take ownership?*

| Theme | What it covers |
|-------|----------------|
| **Own The Outcome** | Blame vs responsibility — own the miss, stop the loop |
| **Keep Your Word** | Promises, standards, finish what you start |
| **Put It On The Line** | Stakes, visibility — skin in the game, commit out loud |
| **Let Results Speak** | Outcomes over explanations |

### Growth — *How do I grow over time?*

| Theme | What it covers |
|-------|----------------|
| **Trust The Process** | Boring middle, slow climb, respect the process |
| **Build The Foundation** | Basics, boring drills, stack small skills |
| **Pay Up Front** | Price early, play the long game |
| **Learn In The Open** | Public learning, private grind, stretch the edge |

### Mindset — *How do I change how I think?*

| Theme | What it covers |
|-------|----------------|
| **Change The Story** | Narrative, victim vs empowered, fortune-telling, name the story |
| **Reframe Setbacks** | Failure as data — lesson first, can't → how |
| **Raise Your Standard** | Confidence, doubt, excuses, demand more from you |

### Peace — *How do I find calm?*

| Theme | What it covers |
|-------|----------------|
| **Protect Your Energy** | Finite fuel, off switch, less input |
| **Hold Boundaries** | No, walk away, leave the argument, hold the line |
| **Recover & Reset** | Close the day, silence, body calm, breathe before reply |
| **Cut The Noise** | Feeds, pings, chaos — stop feeding the noise |

### Focus — *How do I focus on what matters?*

| Theme | What it covers |
|-------|----------------|
| **One Thing** | Name the priority, ruthless cut, do one thing first |
| **Block The Noise** | Tabs, pings, doors — close the noise door, cut the ping |
| **Stay On Task** | Thread, lane, depth — blinders on, hold the thread |
| **Finish Before Next** | Switching, fragments — finish before opening the next |

**Markdown in a category book file:**

```markdown
# Chapter 1 — Beat Perfection

## 01. Done Beats Perfect - motivation

*Done Beats Perfect*

Body here.

<!-- theme: Beat Perfection -->
```

---

## Keep Moving Forward — book series

Planned series: **Keep Moving Forward** books at ~150–200 pages each. Each entry (tagline + body + story + takeaway) = **1–3 pages**. Target **50–100 entries per book**.

**Current master archive (`new-taglines.md`):** **100 entries** — 55 Proofread + 45 New Ones, balanced across **8 categories** (~12–13 each). Each category is its own book; **themes** (above) are chapters inside that book.

Grow each category toward **50–100 entries** before publish. Do not mix categories into one motivation mega-book.

### Book title vs category vs theme

| Layer | What it is | Example |
|-------|------------|---------|
| **Book title (shelf)** | The reader question they're buying | *Keep Moving Forward: Discipline* |
| **Category slug** | Which book the entry belongs in | `discipline` |
| **Theme** | Chapter inside that book | Structure & Routine |

**Rule:** Category = which book. Theme = which chapter inside that book. If an entry doesn't serve the category's reader question, move it — don't relabel.

### Two book lines

| Line | Examples | What taglines are about |
|------|----------|-------------------------|
| **How-change** | Motivation, Discipline, Mindset, Resilience, Peace, Focus, Ownership, Growth | The *skill* — starting, showing up, thinking, enduring (any area of life) |
| **Life-pillar** | Money & Work, Relationships, Health & Energy, Purpose | A *part of life* — scenes and friction in that domain |

The **current 100** are **domain-agnostic** how-change entries. Life-pillar books need **new** taglines for that world — not a filter of the master list.

### Life-pillar books (future)

Every entry must serve the pillar. Stories use **scenes from that domain** — not generic examples retagged. Chapters can group by topic (earning, career moves) or by mechanism (mindset & money, discipline & money).

**Reusing how-change content:** Only if the **story is rewritten** for that domain. Usually easier to write a new pillar-specific tagline.

### File structure

```
new-taglines/
├── new-taglines.md                 # master archive (100)
├── taglines-stories/               # flat copy (reference)
├── tagline-images/
├── motivation/
│   ├── new-taglines-motivation.md  # entries grouped by theme chapter
│   └── taglines-stories/
├── discipline/ … mindset/ … resilience/ … ownership/ … growth/ … peace/ … focus/
```

When adding a tagline: update `new-taglines.md` (master), then the category file and story in that book's folder. Keep master and category lists in sync. Same rules in [taglines-stories-instructions.md](taglines-stories-instructions.md).

### Publish order (how-change)

Expand each category from ~13 entries toward **50–100** before publish.

| Order | Book | Entries in master (approx.) |
|-------|------|----------------------------|
| 1 | **Motivation** | 13 |
| 2 | **Discipline** | 12 |
| 3 | **Resilience** | 12 |
| 4 | **Ownership** | 12 |
| 5 | **Mindset** | 13 |
| 6 | **Peace** | 13 |
| 7 | **Focus** | 13 |
| 8 | **Growth** | 12 |
| — | **Inspiration** | 0 (new writing) |

**Second wave:** life-pillar books (Money & Work, Relationships, Health & Energy, Purpose).

---

## Images

- **1080×1080** PNG for Instagram / Facebook feed
- Random **template** (1–3) and **scheme** (light / dark / tan) for variety, or pick explicitly
- Regenerate one: `python3 scripts/generate_social_image.py --tagline "..." --body "..." --template 1 --scheme dark --category peace --out-dir KMF-peace/tagline-images --prefix "N01"`
- Regenerate one book: `python3 scripts/batch_tagline_images.py --book focus`
- Regenerate all KMF books: `python3 scripts/batch_tagline_images.py --all`
- Master archive only: `python3 scripts/batch_tagline_images.py --book master`

---

## Legal / originality

- No author name or book title on public-facing content
- Bodies are original short paraphrases, not chapter stories
- Taglines are generic self-help phrasing in your voice

---

## Checklist before saving

- [ ] Tagline is 3–6 words and stands alone on a shirt
- [ ] Body is short and punchy (1–2 sentences); PAR is a useful check, not a length target
- [ ] No duplicate of an existing tagline
- [ ] Category slug correct (`## NN. Title - category`) and **## Category** in story file
- [ ] Theme assigned — one of that category's chapter themes (see [Themes](#themes-chapters-within-each-book))
- [ ] Image generated or queued when ready to publish
- [ ] Story file created in `taglines-stories/` if doing the expanded version (see [taglines-stories-instructions.md](taglines-stories-instructions.md))
