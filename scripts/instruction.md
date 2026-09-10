# Week 1 — quick start

The short version of `docs/manual-pipeline.md`, kept for the first week.

## 1. Generate the content (pipeline step 2)

- You already have `lessons/w01/source_prompt.md`.
- Copy the prompt from that file plus the whole text of `source.md` into a
  Claude chat (or ask for it to be generated here).
- You get back a JSON structure with 12 terms (`vocabulary`), the adapted text
  (`reading.b1`) and 10 quiz questions (`quiz`).

## 2. Fill in the lesson (steps 3–4)

- Read the terms you got back and replace the ones you do not like.
- Paste the generated blocks into `lessons/w01/lesson.json`.
- Write `objectives`, `speaking_prompts` and `homework` in your own words.
  These are yours — do not let the model write them.

## 3. Build and check (steps 5–6)

```bash
python3 scripts/build_lesson.py w01
open lessons/w01/index.html
```

The build must exit with no `error:` lines. Warnings are advice, not failure.
