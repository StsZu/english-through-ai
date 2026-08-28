# transport-CLI-to-desktop

## T-002 — 2026-08-28 20:19

### Done

- **Answers applied:** `jsonschema` import removed entirely — `build_lesson.py` is now a single hand-rolled validation path, with a top-of-file comment explaining why, and `templates/lesson.schema.json` kept as living documentation (with a `$comment` listing the rules the schema cannot express). `README.md` and `docs/conventions.md` were already English (done in T-001 under the owner's direct instruction); conventions' language section flattened to remove the historical hedge. `recordings/w00_baseline.md` renamed to `.txt`, content byte-identical. All `.DS_Store` files deleted from disk (including inside `legacy/` — metadata, not project data); `.DS_Store` confirmed in `.gitignore`.
- **Task 1 — quiz model:** schema, template and both `lesson.json` files migrated. Options now carry a `note` (max 25 words); one `explanation` (80–150 words) per question; optional `difficulty` (easy|medium|hard, demo: q1 easy, q2 medium). Rendering after answering: all options lock, chosen option green/amber, correct option revealed in green even when not chosen, notes appear under each option in small muted type, explanation appears below the question full-width at body size with 200 ms fade-in and accent styling (visual weight, not footnote), `Next` below it. The two demo explanations were merged from the old per-option feedback texts — no new subject matter.
- **Task 2 — build reporting:** successful builds print the progress checklist (objectives / vocabulary / reading / quiz / speaking / homework / audio, filled vs TODO counts, total TODO markers). `--quiet` suppresses it. `--all` rebuilds every `lessons/w*/lesson.json` with one summary line per week and exits non-zero if any week fails.
- **Task 3 — source.md:** `templates/week-scaffold/source.md` created with the specified header (wNN substituted by `new_week.sh`). `scripts/wpm.sh <file> <minutes>` prints words, wpm and the verdict line. `docs/manual-pipeline.md` updated: folder listing and step 1 now use `source.md`, step 2 uses `wpm.sh`; the stale `transcript_raw.txt` reference in `lessons/w01/prep.md` updated too.
- **Acceptance checks, all passed:**
  - rebuilt `lessons/w01/index.html`; verified the answer flow in headless Chrome by auto-clicking an incorrect option: chosen option got `chosen-incorrect`, the correct one got `revealed-correct`, all three notes unhidden, explanation block + `Next` present in the DOM
  - removing `explanation` → `w01 q1 explanation: missing or empty`, exit 1; restored
  - a 40-word `note` → `w01 q1 option a note: 40 words, max 25`, exit 1; restored
  - the 2-question w01 quiz builds with `warning: quiz has 2 questions, expected 10` (see Questions 1)
  - progress block prints; `--quiet` suppresses it; `--all` works
  - `bash scripts/wpm.sh lessons/w01/source.md 15` → words 1112, wpm 74, `<130 comfortable`
  - `grep -rn jsonschema scripts/` → only the docstring explaining its intentional absence
  - zero external requests in the built HTML (re-verified by grep for `http(s)://` src/href); inline JS passes `node --check`; all 8 sections render from `file://`
  - `recordings/w00_baseline.txt` exists; no `.DS_Store` on disk
  - committed (4 commits, see Files changed)

### Tree after

```
.
├── CLAUDE.md
├── README.md
├── docs/                 (baseline-protocol, conventions, course-idea, manual-pipeline)
├── errors/               (.gitkeep)
├── legacy/               (untouched)
├── lessons/w01/          (agenda, audio/, friction, index.html, lesson.json,
│                          prep, source.md, source_prompt.md)
├── recordings/           (.gitkeep, w00_baseline.txt)
├── scripts/              (build_lesson.py, new_week.sh, wpm.sh)
├── templates/            (lesson-template.html, lesson.schema.json,
│                          week-scaffold/{lesson.json, prep, agenda, friction, source, audio/})
├── termbank/             (termbank.csv)
├── vocabulary/           (AI Fluency vocabulary cheat sheet.pdf)  ← see Questions 3
├── transport-CLI-to-desktop.md
└── transport-desktop-to-CLI.md
```

### Decisions

1. **Quiz-count conflict resolved in favour of the acceptance criteria.** T-002's validation rules say "fail when quiz has fewer than 3 questions", but the acceptance criteria require "a 2-question quiz builds successfully with a warning" — and rebuilding w01 (2 demo questions) is itself an acceptance item. Implemented: fail only when the quiz is empty; warn on any count other than 10, with an extra hint when below 3. See Questions 1.
2. **`lessons/w01/source.md` was NOT created from the template — it already exists** with real Module 1 material (pasted by the student between tickets, with correct `--- reading: ... ---` separators). Left byte-untouched; only the scaffold template was added. It lacks the duration/word-count footer from the template — left for the student to append.
3. **New student files committed as found:** `lessons/w01/source.md`, `lessons/w01/source_prompt.md` (a generation prompt already written against the new quiz shape), `vocabulary/AI Fluency vocabulary cheat sheet.pdf` (1.2 MB, repo root). Committed to preserve them; placement question below.
4. **`w00_baseline.txt` content = the file's current state**, which the student replaced between tickets with a cleaned, markdown-formatted transcript (headers, paragraphs, a "Here is the transcript" preamble). Renamed as instructed without touching content — but this cleaned version conflicts with the protocol's "verbatim, no cleaning" rule; flagged in Questions 4. The original raw version survives in git history (commit b2c84a1).
5. `.DS_Store` inside `legacy/` was deleted despite the "never touch legacy/" rule — Answer 4 explicitly reclassified `.DS_Store` as macOS metadata, not project data.
6. Ukrainian remains in the pre-T-002 docs (`manual-pipeline.md`, `baseline-protocol.md`, `course-idea.md`, w01 `prep.md`/`agenda.md` intro notes). T-002 asked only for path updates there; wholesale translation felt like scope beyond the ticket. See Questions 2.

### Questions

1. Confirm the quiz-count rule: T-002's validation list says fail below 3 questions, but the acceptance criteria (and the 2-question w01 demo) require such builds to succeed with a warning. Implemented warn-only; say the word and the hard floor of 3 goes in.
2. Should the pre-existing Ukrainian docs (`docs/manual-pipeline.md`, `docs/baseline-protocol.md`, `docs/course-idea.md`, `lessons/w01/prep.md`, `lessons/w01/agenda.md` notes) be translated to English wholesale in a future ticket, per the now-permanent English-only rule?
3. `vocabulary/` (with a 1.2 MB PDF cheat sheet) appeared at the repo root — it is not in the agreed structure. Keep at root, move under `docs/` or `legacy/`, or gitignore large PDFs?
4. The student replaced `w00_baseline` content with a *cleaned* transcript (markdown headers, fillers removed) — the baseline protocol explicitly requires verbatim text with hesitations, since fillers and false starts are diagnostic data. The raw version is preserved in git history. Should I restore the raw version to `w00_baseline.txt` and park the cleaned one alongside?
5. `lessons/w01/source_prompt.md` duplicates rules that now live in the validator and schema. Fine as the student's working file, but should the canonical generation prompt move to `docs/` or `templates/` so it evolves with the schema?

### Blockers

None.

### Files changed

- created: `templates/week-scaffold/source.md`, `scripts/wpm.sh`
- edited: `scripts/build_lesson.py` (rewritten: no jsonschema, new rules, progress block, `--quiet`, `--all`), `templates/lesson-template.html` (quiz rendering), `templates/lesson.schema.json`, `lessons/w01/lesson.json` (migrated), `lessons/w01/index.html` (rebuilt), `templates/week-scaffold/lesson.json` (migrated), `docs/manual-pipeline.md`, `docs/conventions.md`, `lessons/w01/prep.md`, `CLAUDE.md`
- moved: `recordings/w00_baseline.md` → `recordings/w00_baseline.txt`
- deleted: `.DS_Store` files (root, legacy/) — per Answer 4
- committed as found: `lessons/w01/source.md`, `lessons/w01/source_prompt.md`, `vocabulary/AI Fluency vocabulary cheat sheet.pdf`
- commits: `0d6cbcf feat(quiz)`, `3ae4cc8 feat(build)`, `ca3b61e feat(pipeline)`, `7fc700e chore: T-002 housekeeping`

---

## T-001 — 2026-08-28 07:44

### Done

- **Task 1 — restructure:** `git init`; `artifacts/` renamed to `lessons/`; `files/` dissolved into `docs/` and `lessons/w01/` and the empty folder removed; `.gitignore`, `README.md`, `docs/conventions.md`, `termbank/termbank.csv` (header only), `lessons/w01/friction.md`, `.gitkeep` files created. All stale paths in moved `.md` files updated (`artifacts/` → `lessons/`, `lesson-01-agenda.md` → `lessons/w01/agenda.md`); verified with grep — no stale references remain. `legacy/` untouched.
- **Task 2 — lesson template:** `templates/lesson-template.html` (single self-contained file, no CDN, vanilla JS, data inline in `<script id="lesson-data" type="application/json">`); `templates/lesson.schema.json` (draft-07); `lessons/w01/lesson.json` (TODO skeleton + 2 demo quiz questions about the 4D framework); `scripts/build_lesson.py`; built `lessons/w01/index.html`. All 8 sections implemented (header, objectives, flip-card vocabulary, B1/original reading toggle with term tooltips, audio, quiz, speaking prompts with 60 s timers, homework checklist in `localStorage` under `etai:w01:*`). Presentation mode (`P`, font 18→26 px, one section per screen, nav hidden), `←`/`→` navigation, `F` fullscreen, top progress bar, `@media print` (quiz collapsed, both reading versions expanded). Quiz mechanics as specified: 3 options, feedback for the chosen option on all three, options lock after answering, `Next`, end summary with score + terms to review, `Restart quiz` at the end only. Correct = green, incorrect = amber, feedback fade-in 200 ms.
- **Task 3 — scaffold:** `templates/week-scaffold/` (lesson.json, prep.md, agenda.md, friction.md, audio/.gitkeep) and `scripts/new_week.sh` (validates `wNN` argument, substitutes week number, never overwrites — verified by running it twice).
- **Acceptance checks passed:**
  - tree matches the target (plus `CLAUDE.md`, see Decisions)
  - `legacy/` unchanged, nothing deleted (except the two deletions T-001 itself instructs: empty `files/` and the `w02` test folder)
  - `python3 scripts/build_lesson.py w01` → OK
  - broke `lesson.json` (removed one `feedback`) → build failed with exit 1 and a clear message (`quiz q1 option c: feedback is missing or empty…`); restored, rebuilt OK
  - `index.html` verified in headless Chrome from `file://`: all 8 sections render, quiz shows "Question 1 of 2", zero external requests (grep over the built file found no `http(s)://` src/href), inline JS passes `node --check`
  - `bash scripts/new_week.sh w02` created the folder with substituted week numbers; re-run skipped everything; folder then deleted as instructed
  - committed (2 commits, see below)

### Tree after

```
.
├── .gitignore
├── CLAUDE.md
├── README.md
├── docs
│   ├── baseline-protocol.md
│   ├── conventions.md
│   ├── course-idea.md
│   └── manual-pipeline.md
├── errors
│   └── .gitkeep
├── legacy
│   ├── AI Course Sources.md
│   ├── English_Through_AI.pdf
│   ├── English_Through_AI.pptx
│   ├── Full_Series_Generative_AI_for_Beginners
│   │   └── Microsoft_Developer_Generative_AI_for_Beginners.md
│   └── Vibe-coding.md
├── lessons
│   └── w01
│       ├── agenda.md
│       ├── audio            (.gitkeep inside)
│       ├── friction.md
│       ├── index.html
│       ├── lesson.json
│       └── prep.md
├── recordings
│   ├── .gitkeep
│   └── w00_baseline.md
├── scripts
│   ├── build_lesson.py
│   └── new_week.sh
├── templates
│   ├── lesson-template.html
│   ├── lesson.schema.json
│   └── week-scaffold
│       ├── agenda.md
│       ├── audio            (.gitkeep inside)
│       ├── friction.md
│       ├── lesson.json
│       └── prep.md
├── termbank
│   ├── .gitkeep
│   └── termbank.csv
├── transport-CLI-to-desktop.md
└── transport-desktop-to-CLI.md
```

### Decisions

1. **Language: English only, everywhere.** The project owner instructed directly (2026-08-28): "мова тільки англійська". This overrides T-001 items that asked for Ukrainian (`README.md`, `docs/conventions.md` language rule, this report's language). The only Ukrainian kept is the `ua` field in vocabulary/termbank. Recorded in `CLAUDE.md` and `docs/conventions.md`.
2. **`jsonschema` is not installed** on this machine and T-001 forbids installing dependencies without asking. `build_lesson.py` therefore tries to import it, and if absent prints a warning and falls back to built-in validation. The built-in rules cover everything T-001 requires (exactly 3 options, exactly one `correct: true`, non-empty feedback on all three, feedback 40–120 words, `term_refs` must exist in `vocabulary`) and run unconditionally, so the fallback loses only generic structural checks. See Questions 1.
3. **Demo quiz `term_refs`** point to four skeleton vocabulary entries (`delegation`, `description`, `discernment`, `diligence` — taken from the hypothesis list already present in `prep.md`, definitions left as TODO). This keeps the tooltip and "terms to review" mechanics visible and clickable without inventing learning content.
4. **`CLAUDE.md` added at repo root** (not in the target tree): created earlier today at the owner's request via `/init`; it encodes the transport protocol and project rules for the CLI agent.
5. **Two commits instead of one** (`chore: restructure repository`, then `feat(template): …`) so the restructure and the template work stay separable in history.
6. **Week key in scaffold:** the schema pattern accepts both `wNN` (scaffold placeholder) and `w[0-9]{2}`, and `build_lesson.py` additionally checks that `lesson.json`'s `week` matches the folder being built.

### Questions

1. May I `pip install jsonschema` (or add a `.venv`)? The build works without it (see Decisions 2), but T-001 named it as the one allowed dependency.
2. Please confirm the desktop side is aware of the English-only override, since T-001 explicitly requested Ukrainian for `README.md` and `conventions.md` — future tickets should be written against the English-only rule.
3. `recordings/w00_baseline.md` exists but was not in T-001's "current state" tree. It looks like the baseline transcript in Markdown (the protocol expects `.txt`). Left untouched and committed. Rename to `w00_baseline.txt`, or keep as is?
4. `.DS_Store` files existed in the root and `legacy/`. Per "delete nothing" they were left on disk; `.gitignore` keeps them out of git. OK to leave them?

### Blockers

None. All three tasks and the acceptance checklist are complete.

One caveat, not a blocker: "opens without console errors" was verified with headless Chrome (`--dump-dom` from `file://` — all sections render, no page errors) and `node --check` on the inline JS, not with a human-driven browser session. A quick manual click-through of the quiz is still worth doing.

### Files changed

- created: `.gitignore`, `README.md`, `CLAUDE.md`, `docs/conventions.md`, `termbank/termbank.csv`, `lessons/w01/friction.md`, `lessons/w01/lesson.json`, `lessons/w01/index.html`, `lessons/w01/audio/.gitkeep`, `templates/lesson-template.html`, `templates/lesson.schema.json`, `templates/week-scaffold/{lesson.json,prep.md,agenda.md,friction.md,audio/.gitkeep}`, `scripts/build_lesson.py`, `scripts/new_week.sh`, `errors/.gitkeep`, `recordings/.gitkeep`, `termbank/.gitkeep`
- moved: `Course Idea.md` → `docs/course-idea.md`; `files/manual-pipeline.md` → `docs/manual-pipeline.md`; `files/baseline-protocol.md` → `docs/baseline-protocol.md`; `files/prep.md` → `lessons/w01/prep.md`; `files/lesson-01-agenda.md` → `lessons/w01/agenda.md`; `artifacts/` → `lessons/`
- edited: `docs/manual-pipeline.md`, `lessons/w01/prep.md` (path updates only)
- deleted: empty `files/` dir and test `lessons/w02/` — both explicitly instructed by T-001
- commits: `b2c84a1 chore: restructure repository`, `ac70864 feat(template): lesson HTML template, schema, build script, week scaffold`
