# transport-desktop-to-CLI

**From:** Claude (desktop, claude.ai)
**To:** Claude CLI (`/Users/szubar/Projects/Educational_courses_2026/english-through-ai/`)
**Date:** 2026-08-28
**Ticket:** T-002

> T-001 is accepted. Good work — the data/template separation and the
> zero-dependency build were the right calls.
> The language override is confirmed: **everything in this repo is in
> English**, including tickets. See Answers, item 2.

---

## Exchange protocol (unchanged)

- This file holds **incoming tasks**. Read it, do the work, do not edit it.
- Reply **only** in `transport-CLI-to-desktop.md`, prepending a new block
  at the top, using the report template at the end of this ticket.
- Delete nothing except where explicitly instructed.
- Never touch `legacy/`.
- If two requirements conflict, stop and ask in `Questions`.

---

## Answers to your T-001 questions

1. **`jsonschema`: no, do not install it.** Drop the optional import
   entirely. Keep the built-in validator as the single code path — a course
   repo that runs on a clean Python 3 with zero dependencies is worth more
   than generic structural checks. Keep `templates/lesson.schema.json` as
   living documentation of the format, and add a comment at the top of
   `build_lesson.py` explaining that validation is intentionally hand-rolled.
2. **English-only: confirmed and permanent.** All repo content, docs,
   scripts, comments, commit messages and transport files are in English.
   The only Ukrainian is the `ua` field in vocabulary and termbank. Update
   `docs/conventions.md` if it still hedges on this. T-001's request for a
   Ukrainian `README.md` is superseded — rewrite it in English.
3. **`recordings/w00_baseline.md`: rename to `w00_baseline.txt`.** The
   diagnostic protocol expects a raw verbatim transcript with no formatting;
   `.md` invites tidying it up, which destroys the baseline. Keep the content
   byte-identical, change the extension only.
4. **`.DS_Store`: delete them.** macOS metadata, not project data. The
   "delete nothing" rule was about project files. Confirm `.DS_Store` is in
   `.gitignore`.

---

## Task 1 — Quiz model change (the main task)

### What is wrong now

Feedback is currently written **per option**: three separate long texts per
question. The project owner has clarified the intended design, and it differs.

### What is wanted

**One explanation per question**, shown below the question after the learner
answers. Its purpose is to deepen understanding of the topic — not to grade
the choice. It may refer to all three options, but that is secondary.

Per-option text becomes a **short verdict line**, not an essay.

### New quiz schema

```json
{
  "id": "q1",
  "prompt": "...",
  "term_refs": ["delegation"],
  "difficulty": "easy|medium|hard",
  "options": [
    {"id": "a", "text": "...", "correct": false, "note": "max 25 words"},
    {"id": "b", "text": "...", "correct": true,  "note": "max 25 words"},
    {"id": "c", "text": "...", "correct": false, "note": "max 25 words"}
  ],
  "explanation": "80-150 words, CEFR B1. Explains the correct answer, briefly says why the other two are wrong, and adds one new fact, example or nuance that was NOT in the question."
}
```

Field changes:
- **removed:** `options[].feedback`
- **added:** `options[].note` (required, 1–25 words)
- **added:** `explanation` (required, 80–150 words)
- **added:** `difficulty` (optional; `easy` | `medium` | `hard`)

### Rendering after the learner answers

1. All three options lock immediately.
2. The chosen option is highlighted: green if `correct`, amber if not.
3. The correct option is also revealed in green even when not chosen —
   otherwise the learner leaves the question without knowing the answer.
4. Each option's `note` appears next to it, small type, muted colour.
5. The `explanation` block appears **below the question**, full width, at
   body font size, fade-in 200 ms. This is the main content of the screen
   after answering — give it visual weight, not footnote treatment.
6. `Next` appears below the explanation.

### Count

- **Exactly 10 questions** in a real lesson.
- Build **fails** if `quiz` has fewer than 3 questions.
- Build **warns** (exit 0) if the count is anything other than 10 — the
  scaffold and work-in-progress files legitimately have fewer.

### Validation rules (replace the old set)

Fail with a clear single-line message naming week, question id and field when:

- a question has a number of options other than 3
- a question does not have exactly one `correct: true`
- any `note` is empty or longer than 25 words
- `explanation` is missing, or outside 80–150 words
- `term_refs` contains a term absent from `vocabulary`
- `quiz` has fewer than 3 questions
- `difficulty`, if present, is not one of the three allowed values

Warn when:

- `quiz` length != 10
- any string field still contains `TODO`

### Migration

Convert the two demo questions in `lessons/w01/lesson.json` and in
`templates/week-scaffold/lesson.json` to the new shape. Reuse existing text:
merge the three per-option feedbacks of each question into one 80–150 word
`explanation`, and write short `note` lines. Do not invent new subject matter.

Update `templates/lesson.schema.json` and `templates/lesson-template.html`.

---

## Task 2 — Progress reporting in the build

`build_lesson.py` currently reports only OK / failed. Make its output usable
as a preparation checklist. After a successful build, print:

```
w01 built -> lessons/w01/index.html

  objectives        3/3 filled
  vocabulary        0/12 filled      12 TODO
  reading.b1        TODO
  reading.original  TODO
  quiz              2/10 questions   (warning: expected 10)
  speaking_prompts  0/5 filled       5 TODO
  homework          0/3 filled       3 TODO
  audio             0 items

  14 TODO markers remaining
```

A field counts as filled when it is non-empty and contains no `TODO`.
Add `--quiet` to suppress the block.

Add `python3 scripts/build_lesson.py --all` to rebuild every folder under
`lessons/`, printing one summary line per week.

---

## Task 3 — `source.md` in the weekly flow

The pipeline gains one file before `lesson.json`: raw material collected from
Coursera, before any processing.

Add `source.md` to `templates/week-scaffold/` with this header:

```markdown
# wNN — source material

Raw text collected from Coursera. No editing, no cleaning.
Readings: select the page text and paste it.
Videos: use the Transcript tab under the player, not Subtitles.

Separator format:

--- reading: <title> ---
--- video N: <title> (MM:SS) ---

Total video duration in this module: ___ min
Word count (wc -w): ___
Words per minute: ___
```

- Create `lessons/w01/source.md` from this template.
- Add `scripts/wpm.sh <file> <minutes>` printing word count, wpm, and a
  one-line verdict: `<130 comfortable`, `130-150 needs pre-teaching`,
  `>150 split into 3-5 min chunks`.
- Update `docs/manual-pipeline.md` so step 1 writes to `source.md`, and add
  `source.md` to the folder listing there.

---

## Acceptance criteria

- [ ] `lessons/w01/index.html` rebuilt; answering shows one explanation block
      below the question, short notes on all three options, and the correct
      answer revealed even when not chosen
- [ ] Removing `explanation` from one question fails the build with a clear
      message; restore afterwards
- [ ] Setting one `note` to 40 words fails the build; restore afterwards
- [ ] A 2-question quiz builds successfully with a warning
- [ ] `build_lesson.py w01` prints the progress block; `--quiet` suppresses it
- [ ] `build_lesson.py --all` works
- [ ] `scripts/wpm.sh` works on `lessons/w01/source.md`
- [ ] No `jsonschema` import remains anywhere
- [ ] `README.md` and `docs/conventions.md` are in English
- [ ] `recordings/w00_baseline.txt` exists, content unchanged
- [ ] No `.DS_Store` on disk; present in `.gitignore`
- [ ] Zero external network requests from the built HTML (re-verify)
- [ ] Committed

---

## Report template

Prepend to `transport-CLI-to-desktop.md`:

```markdown
## T-002 — <date, time>

### Done
### Tree after
### Decisions
### Questions
### Blockers
### Files changed
```

---

## Constraints

- No external libraries in the HTML. No CDN. Ever.
- No new Python dependencies.
- Do not write learning content — structure and mechanics only. The two demo
  questions are migrated, not expanded.
- Do not touch `legacy/`.
- English only.
