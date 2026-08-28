# English Through AI

A 12-week, student-led English course (B1 → B2) built on AI learning
materials. Primary source: Coursera → Anthropic → *AI Fluency: Framework &
Foundations*. Each week the student prepares a lesson from one video module
and presents it to the teacher from a single self-contained HTML file.

## Structure

```
docs/        methodology: course idea, weekly pipeline, baseline protocol, conventions
lessons/     one folder per week (w01…w12): lesson.json, index.html, prep, agenda, friction, audio
templates/   lesson HTML template, JSON schema, week scaffold
scripts/     build_lesson.py (lesson.json → index.html), new_week.sh
termbank/    termbank.csv — cumulative master file of terms
recordings/  talk recordings (audio not in git) and transcripts
errors/      JSON diagnostics of spoken errors, per week
legacy/      archive of earlier course materials — do not modify
```

## Run a lesson

```bash
open lessons/w01/index.html
```

Works offline from `file://` — no server, no build step, no internet needed.

## Edit a lesson

`lessons/wNN/lesson.json` is the source of truth. After editing, rebuild:

```bash
python3 scripts/build_lesson.py w01
```

The script validates the JSON (quiz rules, term references) and embeds it
into the template. It fails loudly on invalid data.

## Add a new week

```bash
bash scripts/new_week.sh w02
```

Copies `templates/week-scaffold/` into `lessons/w02/` and substitutes the
week number. Never overwrites existing files.

## Docs

- [Course idea](docs/course-idea.md)
- [Weekly manual pipeline](docs/manual-pipeline.md)
- [Baseline & error loop protocol](docs/baseline-protocol.md)
- [Conventions](docs/conventions.md)
