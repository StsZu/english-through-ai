# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Language

**English only.** All documentation, reports, commit messages, and generated
files are written in English. (This overrides the earlier "docs in Ukrainian"
convention from T-001.) The only Ukrainian that appears is the `ua` field in
vocabulary/termbank entries — the learner is a Ukrainian speaker.

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
- Do not install dependencies without asking in `Questions` first.
- No external libraries/CDN in lesson HTML under any circumstances.

## Structure

- `docs/` — methodology: `course-idea.md`, `manual-pipeline.md` (weekly runbook for turning a video module into lesson materials), `baseline-protocol.md` (progress measurement and error loop), `conventions.md`
- `lessons/wNN/` — week folder: `index.html` (generated), `lesson.json` (source of truth), `prep.md`, `agenda.md`, `friction.md`, `audio/`
- `templates/` — `lesson-template.html`, `lesson.schema.json` (draft-07), `week-scaffold/`
- `scripts/` — `build_lesson.py`, `new_week.sh`
- `termbank/termbank.csv` — cumulative master term file
- `recordings/`, `errors/` — talk recordings and JSON error diagnostics
- `legacy/` — archive, do not touch

## Commands

```bash
python3 scripts/build_lesson.py w01   # build a lesson: lesson.json → schema validation → index.html
bash scripts/new_week.sh w02          # create a new week folder from the scaffold (never overwrites)
open lessons/w01/index.html           # open a lesson (must work from file://, offline)
```

The build script uses stdlib + `jsonschema` only (falls back to built-in
validation if `jsonschema` is not installed). On invalid `lesson.json` it must
**fail with a clear error**, never build silently.

## Lesson architecture

A lesson is **one self-contained HTML file** the student opens from `file://`
with no server, no build tooling, no internet. Consequences:

- CSS and JS are inline; vanilla JS, no frameworks (the student must be able to understand the code).
- Lesson data is embedded in `<script id="lesson-data" type="application/json">` — `fetch()` of an external JSON fails on `file://` due to CORS.
- `lesson.json` next to `index.html` is the source of truth; edit the JSON, regenerate the HTML with the build script.
- `localStorage` for progress, keys `etai:wNN:*`.

Quiz (the most important mechanic; full spec in T-001): exactly 3 options,
exactly one correct, feedback of 40–120 words on **all three** options —
it explains and adds new information; after answering, options lock and
cannot be re-selected.

## Conventions

- Weeks: `w01`…`w12`, always two digits. Files: `kebab-case`, except `index.html`.
- Recordings: `recordings/wNN_talk.m4a`, `recordings/w00_baseline.m4a`; diagnostics: `errors/wNN.json`. Audio files are not committed (large and personal); transcripts (`.txt`, `.json`) are.
- Commits: `w01: add glossary`, `docs: fix paths`, `feat(template): quiz`.
- Anything annoying during manual material preparation goes into that week's `friction.md` — it is the spec for future automation (`lessonfactory`).
- Term definitions: CEFR B1, max 20 words; termbank schema: `week;term;definition_b1;collocation_1;collocation_2;ua;source_sentence;added_at`.
