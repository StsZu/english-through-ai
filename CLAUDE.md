# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Language

**English only.** All documentation, reports, commit messages, and generated
files are written in English. (This overrides the earlier "docs in Ukrainian"
convention from T-001.) The only Ukrainian that appears is the `ua` field in
vocabulary/termbank entries — the learner is a Ukrainian speaker.

Still in Ukrainian and pending translation: `scripts/instruction.md`. Do not
copy its style; if you touch it, translate it.

## What this project is

This is **not application code** — it is the content repository for the
"English Through AI" course: a B1-level learner (Ukrainian speaker) studies
English through AI materials. Format: 1:1 with a teacher, 12 weeks, 90-minute
sessions, student-led. Primary source: Coursera → Anthropic →
*AI Fluency: Framework & Foundations*.

## Transport protocol (the main workflow)

Tasks are exchanged between Claude desktop and Claude CLI via two files:

- `transport-desktop-to-CLI.md` — **incoming tasks**. Read and execute, **never edit**.
- `transport-CLI-to-desktop.md` — **reports**. Prepend a new block at the **top** (newest first), following the report template at the end of the incoming file (sections: Done / Tree after / Decisions / Questions / Blockers / Files changed).

If requirements contradict each other — do not guess; record the question in
the `Questions` section of the report.

## Hard rules

- **Never delete anything.** Only move, create, append. If something looks redundant — raise it in `Questions`.
- **Never touch `legacy/`** — it is an archive.
- **Never invent learning content** (texts, terms, quiz questions). Build structure and mechanics with `TODO` placeholders only; filling in content is the student's job — that is the whole point of the course.
- Do not install dependencies without asking in `Questions` first. `build_lesson.py` is stdlib-only by decision (T-002) and must stay that way.
- No external libraries/CDN in lesson HTML under any circumstances.

## Commands

```bash
python3 scripts/build_lesson.py w01           # lesson.json → validate → index.html + progress block
python3 scripts/build_lesson.py w01 --quiet   # same, without the progress block
python3 scripts/build_lesson.py --all         # rebuild every week + the landing page
python3 scripts/build_lesson.py --index       # rebuild only the landing page (root index.html)
bash scripts/new_week.sh w02                  # scaffold a week folder (never overwrites)
bash scripts/wpm.sh lessons/w01/source.md 25  # words / wpm / listening-difficulty verdict
python3 scripts/termbank_sync.py             # lesson.json vocabulary -> termbank/termbank.csv
python3 scripts/termbank_sync.py --check     # report drift, write nothing
open lessons/w01/index.html                   # must work from file://, offline
open index.html                              # course landing page (also the GitHub Pages entry point)
```

There is no test suite, linter, or CI. Verification is: run the build (it must
exit 0 with no `error:` lines) and open the resulting `index.html` from
`file://`.

## Content pipeline (how a week is actually made)

`docs/manual-pipeline.md` is the runbook and is current. In short:

1. `source.md` — raw Coursera transcript + readings, pasted verbatim.
2. `bash scripts/wpm.sh` on it → note the verdict in `friction.md`.
3. `source_prompt.md` — the generation prompt. It carries the **learner
   profile** (tools they use, diagnosed speaking weaknesses from the baseline
   recording) and is what makes content specific rather than generic. Read it
   before doing anything content-shaped.
4. The prompt's JSON output is pasted into `lesson.json` by the student, who
   edits it — objectives, speaking prompts and homework are written by hand.
5. `python3 scripts/build_lesson.py wNN` → `index.html`.
6. Anything annoying in the manual pass goes into that week's `friction.md` —
   that file is the spec for the future `lessonfactory` automation.

Known gaps are listed at the end of `docs/manual-pipeline.md` — chiefly that
`reading.b1` runs 40–60 % short of the length the prompt asks for from w03
onward. `docs/revision-spec.md` is the audit that found these and records what
was fixed.

## Lesson architecture

A lesson is **one self-contained HTML file** the student opens from `file://`
with no server, no build tooling, no internet. Consequences:

- CSS and JS are inline; vanilla JS, no frameworks (the student must be able to understand the code).
- Lesson data is embedded in `<script id="lesson-data" type="application/json">` — `fetch()` of an external JSON fails on `file://` due to CORS.
- `lesson.json` next to `index.html` is the source of truth. **Never hand-edit `index.html`** — it is generated; edit the JSON and rebuild.
- `localStorage` keys are namespaced `etai:<week>:<key>` via the `LS()` helper (currently only the homework checklist persists).

`templates/index-template.html` builds the landing page the same way, from a
`__COURSE_DATA__` token: week titles, counts and the full vocabulary list,
derived from the `lesson.json` files. It links to `lessons/wNN/index.html` with
relative paths, so the site works both from `file://` and from GitHub Pages,
and it reads each week's `etai:<week>:homework` key to show progress — every
read is wrapped in try/catch, because `file://` blocks `localStorage`.

`templates/lesson-template.html` is the template for a lesson. The build substitutes
the literal token `__LESSON_DATA__` with the JSON payload (`</` escaped so the
payload cannot terminate the `<script>` block) — if you edit the template, that
token must survive. The template renders these sections from the data, in
order: Header, Objectives, Vocabulary (flip cards + quick quiz, with the
optional per-term `example` on the card back), Pronunciation (only when the
week supplies `pronunciation_focus`), Reading (B1/Original toggle with
vocabulary terms highlighted), Quiz, Speaking prompts (60 s timer each),
Homework (persisted checklist).

## Build validation

Validation in `scripts/build_lesson.py` is intentionally hand-rolled — no
`jsonschema` import. `templates/lesson.schema.json` (draft-07) is **living
documentation, not executed**; if you change the data format, update both.

**Errors** (build fails, nothing is written):

- a missing top-level key of `week, title, source, duration_min, objectives, vocabulary, reading, audio, quiz, speaking_prompts, homework`
- `week` in the JSON not matching the week being built
- an empty `quiz`
- a question without exactly 3 options, or without exactly one `correct: true`
- an option with a missing/empty `note`, or a `note` over 25 words
- an `explanation` that is missing, empty, or outside 80–120 words
  (measured after `{{opt:...}}` tokens expand)
- an `explanation` or `note` naming an option by position ("the second
  option"); options are shuffled at render time, so references use
  `{{opt:<id>}}` / `{{opt:<id>,<id>}}` tokens instead
- a `{{opt:X}}` token naming an option id that does not exist
- a quiz whose correct answer sits in one position more than half the time
- a `difficulty` that is not `easy` / `medium` / `hard`
- a `term_refs` entry not present in `vocabulary`

**Warnings** (build still succeeds): quiz length ≠ 10, remaining `TODO`
markers, a correct-answer spread outside 3–4 per position, and a `reading.b1`
outside 400–700 words. A real lesson has exactly 10 questions — 3 easy,
5 medium, 2 hard.

The quiz is the most important mechanic: options are shuffled on every render,
they lock after answering, the correct option is revealed even when not chosen,
and the single per-question explanation is shown below the question. It
teaches, it does not grade.

## Structure

- `docs/` — methodology: `course-idea.md`, `manual-pipeline.md`, `baseline-protocol.md` (progress measurement and error loop), `conventions.md`
- `lessons/wNN/` — `lesson.json` (source of truth), `index.html` (generated), `source.md`, `source_prompt.md`, `prep.md`, `agenda.md`, `friction.md`, `audio/`
- `index.html` — generated course landing page at the repo root; the GitHub Pages entry point. Built from every `lesson.json` by `build_lesson.py --index`. **Never hand-edit it**, exactly like a lesson.
- `templates/` — `lesson-template.html`, `index-template.html`, `lesson.schema.json`, `week-scaffold/`
- `scripts/` — `build_lesson.py`, `termbank_sync.py`, `new_week.sh`, `wpm.sh`
- `termbank/termbank.csv` — cumulative master term file
- `recordings/`, `errors/` — talk recordings and JSON error diagnostics
- `legacy/` — archive, do not touch

## Conventions

- Weeks: `w01`…`w12`, always two digits. Files: `kebab-case`, except `index.html`.
- Recordings: `recordings/wNN_talk.m4a`, `recordings/w00_baseline.m4a`; diagnostics: `errors/wNN.json`. **None of it is committed** — not the audio, not the transcripts, not the error diagnostics. They are recordings of the learner's own speech and the repository is public. They live on disk only.
- Commits: `w01: add glossary`, `docs: fix paths`, `feat(template): quiz`.
- Term definitions: CEFR B1, max 20 words; termbank schema: `week;term;definition_b1;collocation_1;collocation_2;ua;source_sentence;added_at`.
