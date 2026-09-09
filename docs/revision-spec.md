# Course Material Revision — Technical Specification

Date: 2026-09-09
Scope: `lessons/w01`…`lessons/w14`, `scripts/build_lesson.py`,
`templates/lesson-template.html`, `lessons/w*/source.md`, `termbank/`.

Audit basis: all 14 `lesson.json` files, all 14 `source.md` files, the build
script, the lesson template, and a full `--all` build run.

---

## Summary of findings

| # | Finding | Severity | Weeks affected |
|---|---|---|---|
| R1 | Correct quiz answer is always option `a` (first position) | blocker | w03–w14 (120 of 140 questions) |
| R2 | Explanations reference options by position ("the second option") — hard-coupled to answer order | blocker | w03–w14 (202 references) |
| R3 | `source.md` contains the scaffold's own instructions as if it were course text | high | w03, w05, w06 |
| R4 | `source.md` contains the generator's meta-sentence "Here is the polished transcript…" | high | w03, w09, w10, w12, w13 |
| R5 | `lessons/w00 copy/` breaks `build_lesson.py --all` | high | build |
| R6 | `source.md` front-matter format is inconsistent; some metrics are impossible | medium | all |
| R7 | `w13/source.md` starts mid-word: "y the end of this lesson" | medium | w13 |
| R8 | `termbank/termbank.csv` holds only its header — 155 terms exist in `lesson.json` but were never collected | medium | all |
| R9 | `prep.md` still instructs the student to produce artefacts of the retired flow | medium | all 14 |
| R10 | `reading.b1` is 40–60 % below the length `source_prompt.md` requires | medium | w03–w14 |
| R11 | w07–w14 `prep.md` / `agenda.md` / `friction.md` were cloned from w06 and still name w06 | high | w07–w14 (24 files) |

---

## R1 + R2 — The quiz (the core defect)

### What is wrong

`source_prompt.md:130` already states the rule, marked *"this is mandatory and
has been violated before"*: the correct option must be spread across `a`, `b`
and `c`, 3–4 times each per 10 questions. The generator ignored it in every
week from w03 onward. Measured distribution of the correct option:

```
w01  a:3  b:3  c:4     OK
w02  a:4  b:3  c:3     OK
w03  a:10 b:0  c:0     degenerate
…
w14  a:10 b:0  c:0     degenerate
```

The template renders `q.options` in stored order (`lesson-template.html:413`),
so the student can score 10/10 on twelve consecutive lessons by always clicking
the top button. The quiz measures nothing.

The rule was written into the prompt and violated anyway. **A prompt is not an
enforcement mechanism.** The fix must live in the build.

### Why it cannot be fixed by shuffling alone

202 explanations identify distractors by their position:

> "…The **second option** is false because modern transformers require massive
> compute clusters…"

Shuffle the options and every one of those sentences becomes a lie. R1 and R2
must be solved together.

### Required solution

**1. Option references become symbolic, not positional.**

In `lesson.json`, a positional reference inside `explanation` is replaced by a
token naming the option's stable `id`:

```
"The second option is false because…"   →   "The {{opt:b}} option is false because…"
"The second and third options are…"     →   "The {{opt:b,c}} options are…"
```

The token carries no wording of its own: it is resolved at render time to the
ordinal word matching where that option actually sits on screen. No explanation
text is rewritten, invented or shortened — only the referring expression is
made position-independent.

**2. The template shuffles options on every attempt.**

`lesson-template.html` shuffles `q.options` per question render (Fisher–Yates)
and resolves `{{opt:…}}` against that display order. Re-taking a quiz
re-randomises it. Multi-id tokens render their ordinals in ascending display
order, so the sentence always reads naturally ("first and third", never
"third and first").

**3. Stored order is also de-degenerated.**

The options in `lesson.json` are permuted with a deterministic per-week seed so
that the correct answer occupies each of the three positions 3–4 times, as
`source_prompt.md` demands. Option `id`s are reassigned to match the new
position, and `{{opt:…}}` tokens are remapped accordingly. This keeps the
source data honest for anyone reading the JSON and for the print path.

**4. The build enforces all of it.** New rules in `scripts/build_lesson.py`:

- **error** — a `{{opt:X}}` token naming an id that is not among the options.
- **error** — a surviving bare positional reference ("the second option") in an
  `explanation` or a `note`; it would be wrong the moment options are shuffled.
- **error** — one position holds more than half of the correct answers
  (this is what catches the all-`a` case).
- **warning** — in a 10-question quiz, any position outside the 3–4 band.

`templates/lesson.schema.json` is updated in the same pass — it is living
documentation and must not drift from the validator.

### Acceptance criteria

- `python3 scripts/build_lesson.py --all` exits 0 with no `error:` line.
- No `lesson.json` has more than 4 correct answers in any one position.
- `grep -c "the second option" lessons/*/lesson.json` returns 0.
- Opening any `lessons/wNN/index.html` from `file://` twice shows the options
  in a different order, and the explanation's ordinal matches what is on screen.
- Reverting the validator alone makes the old data fail the build.

---

## R3 + R4 — Instruction text leaking into course material

`lessons/w03/source.md:3-15` is the scaffold's own instruction block, sitting
above the lesson as though it were something to read:

```
Raw text collected from Coursera. No editing, no cleaning.
Readings: select the page text and paste it.
Videos: use the Transcript tab under the player, not Subtitles.

Separator format:
--- reading: <title> ---
--- video N: <title> (MM:SS) ---

Total video duration in this module: ___ min
```

w05 and w06 carry the same block **and** an already-filled metrics header, so
each states its word count twice — once correctly, once as `___`.

w03, w09, w10, w12 and w13 additionally contain the generator's own voice:
"Here is the polished transcript, kept as close as possible to the original
spoken structure." That is a message to the operator, not to the learner.

**Required:** remove the scaffold instruction block and the meta-sentence from
`source.md`. Course text only, plus the metrics header defined in R6. The
scaffold copy in `templates/week-scaffold/` keeps the instructions — that is
where they belong.

This is the one place in the revision that removes text, which the repository
rule otherwise forbids. It is done on the explicit instruction of the student,
it removes no learning content, and git history retains it.

---

## R5 — `lessons/w00 copy/` breaks the build

`build_lesson.py --all` globs `lessons/w*/lesson.json`, so the stray directory
is picked up and fails validation twice (its `week` field says `w06`; its one
explanation is 42 words against a floor of 80). The command exits non-zero even
though all 14 real weeks build cleanly — which trains the operator to ignore a
red build.

**Required:** rename to `lessons/_w00_copy/` so it falls outside the glob.
Nothing is deleted.

---

## R6 — `source.md` header format

Three shapes are in use: YAML front-matter with metrics (w04–w14), an
`# wNN — source material` heading (w02, w03), and neither (w01). `wpm.sh`
output is pasted by hand, and three weeks record an impossible reading rate:

| Week | words | stated duration | wpm | plausible? |
|---|---|---|---|---|
| w07 | 620 | 20 min | 31 | no |
| w11 | 562 | 30 min | 19 | no |
| w09 | 2486 | 10 min | 249 | no |

31 wpm is not speech. The stated duration is the whole Coursera module,
including exercises, while the word count covers only the transcript — so the
verdict ("comfortable") is derived from an invalid ratio and is not
trustworthy for the three weeks above.

**Required:**
- One format for every week: YAML front-matter carrying
  `week`, `total_video_min`, `word_count`, `wpm`, `verdict`.
- The three impossible values are marked `verdict: TODO — duration mismatch,
  re-measure` rather than being guessed. The true video durations are a fact
  only the student can read off Coursera; inventing them would be worse than
  flagging them.

---

## R7 — `w13/source.md` truncated first line

Line 8 reads `y the end of this lesson, you will be able to:` — a lost "B" from
the paste. **Required:** restore to "By the end of this lesson, you will be
able to:".

---

## R8 — The termbank was never populated

`termbank/termbank.csv` contains its header row and nothing else, while the 14
`lesson.json` files hold 155 vocabulary entries whose fields map onto the
termbank schema one-to-one (`term`, `definition_b1`, `collocations[0]`,
`collocations[1]`, `ua`, `source_sentence`). The cumulative term file — the
artefact that makes the course cumulative rather than 14 disconnected lessons —
is empty.

**Required:** `scripts/termbank_sync.py`, stdlib-only, consistent with the
`build_lesson.py` decision from T-002. It reads every `lessons/wNN/lesson.json`
and rewrites `termbank/termbank.csv` in week order, stamping `added_at` with
the run date for rows that are new. Existing rows keep their original
`added_at`. It reports duplicate terms across weeks instead of silently
collapsing them — a term repeating in two weeks is a content signal the student
should see.

---

## R9 — `prep.md` describes the retired flow

All 14 `prep.md` files (and `w01/agenda.md`) instruct the student to produce
`transcript_raw.txt`, `terms.json`, `worksheet.md`, `glossary.md`, `talk.md`
and `anki.csv`. None of these exist in the current pipeline, which goes
`source.md → source_prompt.md → lesson.json → index.html`. This is already
recorded as a known gap at the end of `docs/manual-pipeline.md`.

**Required:** update the artefact names in `prep.md` to the current pipeline.
`w01/prep.md` and the note blocks in `w01/agenda.md` are still in Ukrainian and
are translated in the same pass, per the language rule in `CLAUDE.md`.

---

## R10 — `reading.b1` is half the length the prompt asks for

Corrected during execution. `source_prompt.md:78` already sets the target:
*"Target 400–500 words. If keeping every fact requires more, go up to 700.
Never drop a fact to hit the word count."* The generated readings ignore it
from w03 onward:

| Week | words | | Week | words |
|---|---|---|---|---|
| w01 | 692 ✅ | | w08 | 206 ❌ |
| w02 | 622 ✅ | | w09 | 167 ❌ |
| w03 | 253 ❌ | | w10 | 180 ❌ |
| w04 | 222 ❌ | | w11 | 156 ❌ |
| w05 | 234 ❌ | | w12 | 194 ❌ |
| w06 | 212 ❌ | | w13 | 155 ❌ |
| w07 | 169 ❌ | | w14 | 158 ❌ |

Twelve of fourteen readings are 40–60 % below the stated minimum — the same
failure mode as R1: the prompt states a rule, the generator ignores it,
nothing checks. Since "never drop a fact to hit the word count" is explicit,
these readings are likely missing facts, not merely terse.

**Done:** the build now warns when `reading.b1` falls outside 400–700 words.
**Not done, and deliberately:** the readings themselves are not rewritten.
Regenerating them is content work, which belongs to the student. The warning
now names the twelve weeks that need it.

---

## R11 — w07–w14 student files still carry w06's identity

Found during execution. The eight later weeks were scaffolded by copying w06
and were never re-labelled. `lessons/w09/prep.md` opens with `# w06 — Student
preparation` and instructs the student to run
`python3 scripts/build_lesson.py w06`; `agenda.md` and `friction.md` are the
same. 24 files, every self-reference wrong.

A student following w09's own preparation sheet rebuilds w06 and logs their
friction into a file headed w06.

**Required:** re-label every `wNN` self-reference in `prep.md`, `agenda.md` and
`friction.md` to the week that owns the file. `w01`'s references to `w00` are
left alone — they correctly point at the baseline recording and its diagnostic.

---

## Out of scope

- Writing or rewriting learning content (texts, terms, quiz questions) — the
  student's job by design.
- `legacy/` — untouched.
- The real video durations behind R6 — flagged, not guessed.

## Execution order

1. R5 (unblocks a clean `--all`)
2. R1 + R2 (validator, template, data migration)
3. R3, R4, R6, R7 (`source.md` hygiene)
4. R8 (termbank sync)
5. R9, R10, R11 (docs, prompt, week re-labelling)
