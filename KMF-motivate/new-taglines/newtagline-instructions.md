# New Tagline Instructions

Reference for creating or updating original taglines in this project.

**Expanded stories:** see [taglines-stories-instructions.md](taglines-stories-instructions.md) for the long-form format in `taglines-stories/`.

---

## Files

| File | Purpose |
|------|---------|
| `new-taglines/new-taglines.md` | Master archive — all taglines (numbered 01–156+) |
| `new-taglines/{category}/` | One folder per book — e.g. `motivation/`, `discipline/`, `mindset/` |
| `new-taglines/{category}/new-taglines-{category}.md` | Taglines for that book only |
| `new-taglines/{category}/taglines-stories/` | Expanded stories for that book |
| `new-taglines/taglines-stories/` | Original flat copy of all stories (kept for reference) |
| `new-taglines/tagline-images/` | All social images in one folder |
| `new-taglines/taglines-stories-instructions.md` | Rules for story files |
| `new-taglines/newtagline-instructions.md` | This file — short taglines and bodies |
| `scripts/generate_social_image.py` | Single image generator |
| `scripts/batch_tagline_images.py` | Batch all taglines from `new-taglines/new-taglines.md` |
| `scripts/verify_motivation_book.py` | QA: 101 entries, story files, required sections |

---

## Tagline (title line)

- **3–6 words**
- Punchy and memorable — fine if slightly grammatically awkward
- Original phrasing; do not reuse book chapter titles or author/book names
- Italic in markdown: `*Your Tagline Here*`

---

## Body (paraphrase)

Use **PAR** (Problem → Action → Result). Same as CAR (Challenge → Action → Result).

| Part | What it does |
|------|----------------|
| **Problem** | The struggle, friction, or wrong default (waiting, quitting, noise, fear, etc.) |
| **Action** | What you do instead — the shift in behavior or mindset |
| **Result** | What that gets you — outcome, relief, momentum, clarity |

- Usually **1–2 sentences** total; all three parts can live in one or two sentences
- Second person (“you”) when it fits
- Say the idea clearly; don’t pile on extra metaphors or restate the same point
- If one metaphor is enough, stop there
- **Quick wins** belong where relevant (e.g. long-term goals) — fuel to stay on track, not a substitute for the big aim

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

Body using PAR — problem, action, result in 1–2 sentences.
```

**Category slug** (lowercase after the dash): `motivation`, `discipline`, `mindset`, `resilience`, `peace`, `focus`, `ownership`, `growth` — and `inspiration` when added. Maps to field categories in the table below (e.g. **ownership** = accountability / ownership; **peace** = mindfulness / peace; **focus** = productivity / focus). **Not the same as theme** — see [Themes](#themes-for-grouping) below.

Each story file in `taglines-stories/` gets matching **## Category** and **## Theme** sections (see [taglines-stories-instructions.md](taglines-stories-instructions.md)).

---

## Themes (for grouping)

Seven project themes — **not the same as category** (book). Themes describe *what kind of move* the tagline is. Category describes *which book* it belongs to. A Motivation-book entry can use any theme (e.g. *Own The Morning* → category `motivation`, theme **Daily Discipline**).

1. Start Moving  
2. Daily Discipline  
3. Mind Over Noise  
4. Push Through  
5. Guard Your Ground  
6. Commit & Own It  
7. Trust the Long Road  

When adding a tagline, assign one primary theme in the book file (chapter placement) and in the story **## Theme** section — see [taglines-stories-instructions.md](taglines-stories-instructions.md).

---

## Field categories (self-help / motivation / inspiration)

Broader lanes in this space — useful when brainstorming new taglines and planning **Keep Moving Forward** books by category.

| Category | What it's about | Reader language | Reader question |
|----------|-----------------|-----------------|-----------------|
| **Motivation** | Push to act — urgency, drive, getting started | "I need a push" | How do I get started when I don't feel like it? |
| **Inspiration** | Pull toward a vision — possibility, emotional lift | "I need hope / a vision" | How do I see a future worth moving toward? |
| **Mindset** | Beliefs, self-talk, how you frame things | "I need to think differently" | How do I change the way I think about this? |
| **Discipline / habits** | Consistency, routines, showing up | "I need consistency" | How do I show up even when I don't feel like it? |
| **Resilience / grit** | Setbacks, pain, staying in the fight | "I keep quitting when it gets hard" | How do I keep going when it gets hard? |
| **Confidence** | Self-trust, standards, earning belief | "I don't trust myself" | How do I trust myself? |
| **Purpose / meaning** | Why it matters, values, direction | "I don't know why any of this matters" | How do I find what matters? |
| **Productivity / focus** | Time, energy, getting the right things done | "I can't get the right things done" | How do I focus on what actually matters? |
| **Accountability / ownership** | Responsibility, commitments, results | "I blame everything but me" | How do I take ownership of my results? |
| **Mindfulness / peace** | Calm, boundaries, being present | "I'm burned out / overwhelmed" | How do I find calm and protect my energy? |
| **Growth / learning** | Skills, discomfort, long-term development | "I want to level up over time" | How do I grow into who I'm becoming? |
| **Success / achievement** | Goals, performance, winning the game | "I want to win / hit goals" | How do I reach the goals that matter? |

**Turning reader language into a question:** "I need X" → *How do I get X?* · "I want X" → *How do I achieve X?* · "I can't X" → *How do I X?* · "I don't know X" → *How do I find X?* · "I keep doing X" → *How do I stop X?* · "I'm feeling X" → *How do I get out of X?*

Category slugs in `new-taglines.md` map to these questions: `motivation`, `discipline`, `mindset`, `resilience`, `peace`, `focus`, `ownership`, `growth`, `inspiration`.

**Motivation** = push to act. **Inspiration** = pull toward a vision. The rest are mostly *how* you act, *why* you act, or *what* you build while acting.

**Rough map to project themes:**

| Project theme | Field categories |
|---------------|------------------|
| Start Moving | Motivation |
| Daily Discipline | Discipline / habits |
| Mind Over Noise | Mindset, confidence |
| Push Through | Resilience / grit |
| Guard Your Ground | Mindfulness / peace, productivity / focus |
| Commit & Own It | Accountability / ownership |
| Trust the Long Road | Growth / learning, success / achievement |

---

## Keep Moving Forward — book series

Planned series: **Keep Moving Forward** books at ~150–200 pages each. Each entry (tagline + body + story + takeaway) = **1–3 pages**. Target **50–100 entries per book**; **Motivation** targets **101** (see below).

### Motivation book — chapters = themes

*Keep Moving Forward: Motivation* uses the **7 project themes as chapters**. Tagline stories are **numbered items within each chapter** (continuous book order **01–101**).

| Ch | Theme | Items |
|----|-------|-------|
| 1 | Start Moving | 15 |
| 2 | Daily Discipline | 14 |
| 3 | Mind Over Noise | 14 |
| 4 | Push Through | 15 |
| 5 | Guard Your Ground | 15 |
| 6 | Commit & Own It | 14 |
| 7 | Trust the Long Road | 14 |

Every entry stays **category: motivation**. Theme = chapter + what kind of starting move.

**Overlap policy (Motivation 101):** **Merge** true duplicates (reader would notice sameness). **Reframe** similar entries into a different theme chapter — rewrite body/story for that lens. **Stoic mitigation:** reduce redundant principles; control quality, not every reader reaction. Details: [motivation/motivation-book-101-outline.md](motivation/motivation-book-101-outline.md).

**Markdown in `new-taglines-motivation.md`:**

```markdown
# Chapter 1 — Start Moving

## 01. Done Beats Perfect - motivation
...
```

### Two layers — book title vs category tag

Use two layers so content stays organized without feeling diluted:

| Layer | What it is | Example |
|-------|------------|---------|
| **Book title (shelf)** | The life question or skill the reader is buying | *Keep Moving Forward: Money & Work* |
| **Category tag (internal)** | What the entry *does* — motivation, mindset, discipline, etc. | A money tagline tagged **Mindset** |

**Rule:** Book title = the question they're asking. Category = the lens each entry uses. If an entry doesn't serve the book's one-sentence promise, it belongs in a different book.

Each book gets **one sentence** on the cover, e.g.:

- *Motivation* — "Start and keep going when you don't feel like it."
- *Money & Work* — "Handle money and career with clarity and follow-through."
- *Relationships* — "Show up better with the people who matter."

### Two book lines

| Line | Examples | What taglines are about |
|------|----------|-------------------------|
| **How-change** | Motivation, Mindset, Discipline, Inspiration, Resilience | The *skill* — starting, thinking, showing up (any area of life) |
| **Life-pillar** | Money & Work, Relationships, Health & Energy, Purpose | A *part of life* — situations, choices, and friction in that world |

The **current 50** in `new-taglines.md` are mostly **domain-agnostic** — they fit how-change books (Motivation, Mindset, etc.) as-is. They are **not** a filter for life-pillar books; those need their own lists.

### Life questions (reader shelf language)

Common questions self-help answers — useful when naming life-pillar books:

| Life question | Example book title |
|---------------|-------------------|
| How do I start and keep going? | Motivation |
| How do I think differently? | Mindset |
| Why does any of this matter? | Purpose |
| How do I love and relate? | Relationships & Communication |
| How do I take care of myself? | Health, Energy & Body |
| How do I earn and manage life? | Money & Work |
| How do I handle hard times? | Resilience |
| How do I find calm? | Peace & Boundaries |

### What a life-pillar book is

A life-pillar book is **50–100 taglines about that pillar** — not generic taglines sorted into a money folder. Every entry should clearly serve the book's world. Stories use **scenes from that domain** (opening a statement, asking for a raise, a hard conversation with a partner) — not generic examples retagged.

Same format as always: tagline + short body + story + takeaway. Category tags sort entries **inside** the book.

**Example — *Keep Moving Forward: Money & Work*:**

| Sub-area | Example tagline |
|----------|-----------------|
| Earning | *Raise Your Rate* |
| Fear | *Open The Statement* |
| Habits | *Track Before You Judge* |
| Mindset | *Money Is A Tool* |
| Career | *Outgrow The Role* |
| Discipline | *Pay Yourself First* |

**Chapters inside a life-pillar book** — pick one approach:

- **By mechanism** — Motivation & money, Mindset & money, Discipline & money…
- **By topic** — Earning, spending & debt, career moves, fear & avoidance…

Either works if every piece stays clearly about the pillar.

**Reusing how-change content:** A principle like *Earn Your Confidence* can appear in a life-pillar book only if the **story is rewritten** for that domain. Often easier to write a **new pillar-specific tagline** than to force a generic one.

### File structure (multiple books)

**Current layout** (how-change books split by category):

```
new-taglines/
├── new-taglines.md                 # master archive (all 50)
├── taglines-stories/               # original flat copy (reference)
├── tagline-images/                 # all images in one folder
├── motivation/
│   ├── new-taglines-motivation.md
│   └── taglines-stories/
├── discipline/
│   ├── new-taglines-discipline.md
│   └── taglines-stories/
├── mindset/ … resilience/ … ownership/ … growth/ … peace/ … focus/
```

**Future life-pillar books** (e.g. money, relationships) use the same pattern:

```
new-taglines/money-and-work/
├── new-taglines-money-and-work.md
└── taglines-stories/
```

When adding a tagline: update `new-taglines.md` (master), then the category file and story in that book's folder. Keep the master and category lists in sync.

Same rules in this file and in [taglines-stories-instructions.md](taglines-stories-instructions.md).

### Categories underweight in the current 50

Strong categories for **future books** or new tagline batches — thin or absent in the first 50:

| Lane | Notes |
|------|-------|
| **Inspiration** | Pull toward a vision — distinct from motivation (push) |
| **Relationships / communication** | Own book; readers search by name |
| **Health, energy & body** | Own book; distinct from discipline alone |
| **Purpose / meaning** | Life-pillar book; overlaps inspiration but readers want "purpose" on the cover |
| **Money & work** | Own book; don't hide inside "Success" |
| **Courage / fear** | Own book or sharp section inside Mindset |

Confidence, accountability, and productivity often work as **sections inside** other books unless you want a deep single-topic volume.

### Recommended publish order (how-change, one book at a time)

Ship **how-change** books before life-pillar books. Each book needs **50–100 entries** (~150–200 pages); the current 50 are split across categories — assign entries to one book, then write the rest.

| Order | Book | Why start here | Entries in current 50 |
|-------|------|----------------|----------------------|
| 1 | **Motivation** | Best front door; matches *Keep Moving Forward* brand; "I need a push" | **78** in book (`motivation/`) |
| 2 | **Discipline** | Natural sequel — started, now stay consistent | ~8 |
| 3 | **Resilience** | Distinct shelf — "when it gets hard" | ~8 |
| 4 | **Mindset** | Important but thinner today; stronger after 1–3 | ~6 |
| 5 | **Inspiration** | Pull/vision vs push; mostly new writing | ~0 |
| 6 | **Ownership** | Accountability, commitment, stakes | ~9 |

**Do not** publish all 50 as one motivation book — too mixed. Tag each entry, pull what fits the book promise, write new entries to reach 50–100.

**Motivation book:** 78 entries (book order 01–78), ~150–200 pages target at 1–3 pages per story. **Master archive:** 120 taglines total (#61–120 are motivation batch two).

### Second wave (after core how-change)

| Wave | Books | Notes |
|------|-------|-------|
| **How-change depth** | Peace & Boundaries, The Long Game | Fold **peace**, **focus**, and **growth** entries from current 50; expand thin categories |
| **Life-pillar** | Money & Work, Relationships, Health & Energy, Purpose | New taglines written for that domain — not a filter of the current 50 |

---

## Images

- **1080×1080** PNG for Instagram / Facebook feed
- Random **template** (1–5) and **scheme** (light / dark / tan) for variety, or pick explicitly
- Regenerate one: `python3 scripts/generate_social_image.py --tagline "..." --body "..." --template 1 --scheme dark --out-dir new-taglines/tagline-images --prefix "51"`
- Regenerate all: `python3 scripts/batch_tagline_images.py`

---

## Legal / originality

- No author name or book title on public-facing content
- Bodies are original PAR rewrites, not chapter stories
- Taglines are generic self-help phrasing in your voice

---

## Checklist before saving

- [ ] Tagline is 3–6 words and stands alone on a shirt
- [ ] Body has clear Problem, Action, and Result
- [ ] No duplicate of an existing tagline
- [ ] Theme assigned if adding to the themed file
- [ ] Image generated or queued when ready to publish
- [ ] Story file created in `taglines-stories/` if doing the expanded version (see [taglines-stories-instructions.md](taglines-stories-instructions.md))
- [ ] Category slug in heading (`## NN. Title - category`) and **## Category** in story file
- [ ] Book assignment clear if planning for **Keep Moving Forward** series (how-change vs life-pillar; see above)
