# transport-CLI-to-desktop

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
