# Tagline Stories Instructions

Reference for creating or updating expanded story files in `taglines-stories/`.

**Related:** short taglines and social bodies → [newtagline-instructions.md](newtagline-instructions.md)

---

## Files

| File | Purpose |
|------|---------|
| `new-taglines/new-taglines.md` | Master archive — all taglines |
| `new-taglines/{category}/new-taglines-{category}.md` | Taglines for one book |
| `new-taglines/{category}/taglines-stories/` | Stories for one book |
| `new-taglines/taglines-stories/` | Original flat copy of all stories (reference) |
| `new-taglines/taglines-stories-instructions.md` | This file |

**Filename:** `NN-slug-from-title.md` (e.g. `03-earn-your-confidence.md`) — for **Motivation book**, `NN` is **book order 01–101** (not master archive number). Other books use their own book order when finalized.

**QA (Motivation):** `python scripts/verify_motivation_book.py`

---

## Difference from `new-taglines/`

| `new-taglines/` | `taglines-stories/` |
|-----------------|---------------------|
| Tagline + 1–2 sentence body | Tagline + body + expanded idea + story + takeaway |
| Images, shirts, social posts | Reading, email, deeper content, long-form posts |
| Punchy | Explanatory + human |

Same tagline number in both folders so they stay linked.

---

## File layout

```markdown
# Title Case Name

*Tagline Words Here*

Short tagline body copied from new-taglines.md — 1–2 sentences, PAR/CAR.

## Category

**Motivation** — One sentence: how this tagline answers the category's reader question (see field categories table in newtagline-instructions.md).

## Theme

**Start Moving** — One sentence: why this entry belongs in this project theme (what kind of move it is — not the same as category).

## The idea

2–4 sentences. Full CAR woven into flowing prose. Clearer and deeper than the short body, but not a repeat of it.

## Story

150–300 words. One person, one moment, one choice. Show the turn.

## Takeaway

2–4 sentences. Application and reflection — what to notice or do when you're in it. Do not repeat the idea or story.
```

### Optional section

```markdown
## Try this

One concrete action for today.
```

Use when you want a direct call to action at the end.

---

## Category vs theme (two different things)

Do not confuse these — both appear in story files, but they answer different questions.

| | **Category** | **Theme** |
|---|-------------|-----------|
| **Question** | Which **book** does this belong to? | What **kind of move** is this? |
| **Example** | `motivation` → *Keep Moving Forward: Motivation* | `Start Moving` → action before you feel ready |
| **In `new-taglines.md`** | Slug on heading: `## NN. Title - motivation` | Not on master heading (theme lives in book file + story) |
| **In story file** | `## Category` — ties to the book's **reader question** | `## Theme` — ties to the **7 project themes** |
| **Count** | One category per entry | One **primary** theme per entry |

**Category** = bookshelf / KMF book (motivation, discipline, mindset, resilience, peace, focus, ownership, growth, inspiration). See field categories in [newtagline-instructions.md](newtagline-instructions.md).

**Theme** = internal grouping across the whole project (not a separate book):

1. **Start Moving** — action, momentum, doing before you feel ready  
2. **Daily Discipline** — habits, consistency, showing up on schedule  
3. **Mind Over Noise** — confidence, standards, clearing mental clutter  
4. **Push Through** — grit, setbacks, pain, staying in the fight  
5. **Guard Your Ground** — energy, time, peace, boundaries  
6. **Commit & Own It** — integrity, accountability, full investment  
7. **Trust the Long Road** — process, patience, fundamentals, playing long  

**Example:** A piece in the **Motivation** book can still be themed **Daily Discipline** if it is about owning the morning — same category, different theme.

**Rules:**

- Every story file gets **one category** and **one primary theme**.
- Category must match the slug on `new-taglines.md` and the book folder (`motivation/`, etc.).
- Theme is chosen by the best fit for what the tagline *does*, not which book it is in.
- Theme also appears in `{category}/new-taglines-{category}.md` (chapter headers / `<!-- theme: -->` comments).

### Similar entries — merge vs reframe (Motivation book)

When auditing overlap in a book (especially Motivation), use two tools before cutting content:

| Situation | Action |
|-----------|--------|
| **True duplicate** — same obstacle, same action, same takeaway; a reader would say *"this is the same one"* | **Merge** into the stronger keeper; fold any good lines into body or story |
| **Similar surface** — same size of action (one minute, open file, first hour) but a **different blocker** (fear vs schedule vs mental noise vs energy) | **Reframe** — keep the entry, assign a **different theme** (chapter), rewrite body and story for that lens |

**Reframe example:** *Ten Minutes Counts* (Daily Discipline — scheduled block) vs *One Brave Minute* (Push Through — courage on the hard thing) vs merging *Give It Five Minutes* into *Ten Minutes Counts* (true duplicate).

**Merge example:** *Open The Document* and *Open The Damn File* — same metaphor, same moment; merge.

**Stoic mitigation:** Reduce redundancy on purpose — control what you can (distinct principles per chapter) rather than padding the book with rephrased starts. Some readers will still group ideas together; that is fine. The goal is to make that as rare as possible without killing useful angles.

Full Motivation 101 map: [motivation/motivation-book-101-outline.md](motivation/motivation-book-101-outline.md).

---

## Section guide

### Title + tagline + body

- **Title** — matches the entry heading in `new-taglines.md`
- **Tagline** — italic, 3–6 words, same as master list
- **Body** — copy the short body from `new-taglines.md` exactly (update both files if the body changes)

### Category

- Placed **after the short body, before ## Theme**
- Format: `**Category Name** —` one sentence explaining **how this tagline answers that category's reader question** (not a repeat of the body or PAR)
- Example (Motivation): *Done Beats Perfect* answers "How do I get started when I don't feel like it?" by making shipping the rough version the first move instead of waiting to feel ready.
- Must match the category slug on the `new-taglines.md` heading (e.g. `- motivation`)
- Reader questions and slug map: [newtagline-instructions.md](newtagline-instructions.md) → Field categories table

### Theme

- Placed **after ## Category, before ## The idea**
- Format: `**Theme Name** —` one sentence explaining **why this entry fits this project theme** (what kind of principle it is)
- Use one of the **7 theme names** exactly (see table above)
- Example: *Own The Morning* is in the **Motivation** book (category) but themes as **Daily Discipline** because it is about winning the first hour with routine, not a generic push to act.
- Theme is for chapters inside the book file and in the story — not for replacing the category slug

### The idea

- **2–4 sentences** in complete, flowing prose
- Use **CAR** (Challenge → Action → Result) — same as PAR in the short body
- Do **not** label the parts (no "Challenge:" headers)
- Expand beyond the short body; explain the principle for someone reading slowly
- The short body is the poster. This section is the explanation.

| Part | What it does |
|------|----------------|
| **Challenge** | What goes wrong by default — the friction, fear, or wrong habit |
| **Action** | The shift in behavior or mindset |
| **Result** | What changes — outcome, relief, momentum, clarity |

### Story

- **150–300 words**
- **Full sentences** — readable at a calm pace; no choppy fragments or rushed run-ons
- Stories can be real, composite, or hypothetical — make it feel true, not like a fable

**CAR/PAR belongs in the tagline body and in ## The idea — not in every story plot.** The default story shape (person stalled for months → insight → modest win) repeats quickly across a book. Vary **story structure**; keep the principle clear through a different reading experience.

Optional internal tag (not published): `<!-- story shape: Juxtaposition -->` on the line after `## Story`.

#### Story shapes (pick one per entry)

Assign a shape **before** writing. Avoid the same shape on **back-to-back** entries in a chapter.

| Shape | What it is | When it fits |
|-------|------------|--------------|
| **Juxtaposition** | Two people or paths, same situation, different move | Contrast shows the tagline without one hero's journey |
| **In medias res** | Open mid-action; context arrives in fragments | Starting is the scene — skip the long stall setup |
| **Before / after** | Two tight scenes, little or no bridge | Reader fills the gap; less hand-holding |
| **Dialogue** | Scene carried by two voices | Commitment, excuses, friction in the lines |
| **Chronicle** | Several short beats over days (montage in prose) | Small steps, discipline, compound starts |
| **Anti-climax** | They start; little drama; that's the point | Boring or flat starts that still count |
| **Object story** | Orbit one thing (file, shoes, envelope, tab) | Physical "open/send/close" taglines |
| **Observation** | Narrator watches someone; infers the lesson | Less inner monologue, more witness |
| **Question structure** | Story unfolds as questions the character asks | Mind noise, indecision, self-talk |
| **Second person scene** | Specific "you" in one moment | Immediate, not generic advice voice |
| **Failure / near-miss** | Cost of not starting, or a late start | Honest stakes; break the triumph template |
| **Message / thread** | Text, note, calendar entry, voice memo | Announcements vs action, promises |

**Endings** do not all need relief or modest triumph. Unresolved, flat, or ironic is fine when it serves the tagline.

**Red flags** (vary or rewrite): opens with "[Name] had been [verb]ing for [months]"; ends with "It was not perfect. It was enough"; same CAR beat order as the previous entry in the chapter.

**Pilot — Chapter 1 (Start Moving):** shape assignments and test rewrites in [motivation/start-moving-story-pilot.md](motivation/start-moving-story-pilot.md). Stories use **varied shapes** but **flowing prose** — no choppy fragments, screenplay lines, or bold log entries.

#### Legacy note (avoid as default)

- ~~One person, one moment, one clear choice~~ — still valid sometimes, not for every entry
- ~~Show the turn: what happened when they acted~~ — not every story needs a spelled-out turn
- ~~Second person or close third person (one named character)~~ — one of many options

### Takeaway

- **2–4 sentences** — filled out, not a single punch line
- Point forward: what to notice, question, or apply
- **Do not regurgitate** what you already said in The idea or Story

---

## What makes the story motivational

1. **Specific** — "Tuesday, the report due Friday, still tweaking the intro" beats "someone procrastinated."
2. **Relatable friction** — reader should think "that's me."
3. **A clear choice** — easy path vs right path, not vague struggle.
4. **Show the turn** — what happened when they acted (or didn't).
5. **Earned ending** — result follows from action, not luck.
6. **Second person or close third** — keeps it immediate.

---

## Length guide

| Section | Length |
|---------|--------|
| Body (from master list) | 1–2 sentences |
| Category | 1 sentence (how this tagline answers the category reader question) |
| Theme | 1 sentence (why this entry fits this project theme) |
| The idea | 2–4 sentences |
| Story | 150–300 words |
| Takeaway | 2–4 sentences |
| Try this (optional) | 1 sentence |

---

## Voice and pace

- Short bodies in `new-taglines.md` stay **punchy** — image-ready
- Stories are the **slow read** layer — the reader should not feel rushed
- Write so someone can move through it calmly, one thought at a time
- Match the tone of existing stories in this folder before inventing a new style

---

## Folder organization

**Per book** (primary):

```
new-taglines/motivation/taglines-stories/
├── 01-done-beats-perfect.md
├── 10-move-before-ready.md
└── ...
```

**Master reference** (all stories, flat):

```
new-taglines/taglines-stories/
├── 01-done-beats-perfect.md
└── ...
```

---

## Workflow when adding a new tagline

1. Add tagline + short body to `new-taglines.md` (master) — see [newtagline-instructions.md](newtagline-instructions.md)
2. Add the same entry to `{category}/new-taglines-{category}.md` under the correct theme chapter
3. Generate social image (into `tagline-images/`)
4. Create story in `{category}/taglines-stories/` using the layout above (**Category** + **Theme** sections)
5. Optionally mirror to flat `taglines-stories/` if keeping archive in sync

When updating a short body, sync master, category file, and story file.

---

## Checklist before saving

- [ ] Category slug matches `new-taglines.md` heading and **## Category** section in story file
- [ ] **## Theme** section uses one of the 7 project themes with a clear one-sentence fit
- [ ] Entry placed under the correct theme chapter in `{category}/new-taglines-{category}.md`
- [ ] Short body matches `new-taglines.md` exactly
- [ ] The idea has CAR in flowing prose — not a repeat of the short body
- [ ] Story is 150–300 words and uses a **distinct story shape** (not default CAR plot; see Story shapes above)
- [ ] Story shape differs from the **previous entry** in the same chapter (when batch-writing)
- [ ] Takeaway is 2–4 sentences and does not repeat idea or story
- [ ] No author name or book title on public-facing content
