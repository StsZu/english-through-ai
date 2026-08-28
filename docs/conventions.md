# Conventions

## Naming

- Week numbering: `w01` … `w12`, always two digits.
- File names: `kebab-case`, except `index.html`.
- Recordings: `recordings/wNN_talk.m4a`, baseline: `recordings/w00_baseline.m4a`.
- Diagnostics: `errors/wNN.json`.

## Language

- **English only** for all documentation, reports, and commit messages
  (per the project owner's instruction of 2026-08-28; this supersedes the
  earlier "documentation in Ukrainian" rule from T-001).
- Learning content is in English. The only Ukrainian is the `ua` field in
  vocabulary and termbank entries.

## Git

- Audio files are not committed (large and personal); transcripts
  (`.txt`, `.json`) are.
- Commit message style: `w01: add glossary`, `docs: fix paths`,
  `feat(template): quiz`.

## Content rules

- Term definitions: CEFR B1 vocabulary, max 20 words.
- Termbank schema:
  `week;term;definition_b1;collocation_1;collocation_2;ua;source_sentence;added_at`
- Quiz: exactly 3 options per question, exactly one correct, feedback of
  40–120 words on every option.
- AI never writes the student's talk or lesson content — structure and
  skeletons only.
