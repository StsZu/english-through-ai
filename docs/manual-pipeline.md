# Manual Pipeline — weekly runbook

Goal: turn one video module into a complete lesson the student can present
from a single HTML file. Done by hand until `lessonfactory` is written
(meeting #10).

**The main rule:** everything that is annoying during the manual pass goes
into that week's `friction.md`. That file is the specification for the
automation.

Expected time: 30–40 minutes per module, not counting watching the module
itself (that is `prep.md`, day 1).

---

## Step 0. Week folder

```bash
bash scripts/new_week.sh w02
```

Copies `templates/week-scaffold/` into `lessons/w02/` and substitutes the week
number. Never overwrites an existing file — running it twice is safe.

You get:

```
lessons/wNN/
├── lesson.json     # source of truth, pre-filled with TODO placeholders
├── source.md       # raw material from Coursera
├── prep.md         # the student's 3-day preparation plan
├── agenda.md       # sent to the teacher a day before the lesson
├── friction.md     # what was annoying
└── audio/          # mp3 files, not committed to git
```

`index.html` is **generated** by the build (step 5). Never edit it by hand.

`source_prompt.md` is not in the scaffold yet — copy it from a previous week
and update it for the new module.

---

## Step 1. Raw material → `source.md` (10 min)

1. Coursera → video → the **Transcript** tab (not Subtitles).
2. Select all, copy, paste into `lessons/wNN/source.md`.
3. Readings: select the page text and paste it in the same way.
4. Separate each item with a header line, so the origin of every sentence
   stays traceable:

```
--- reading: Introduction to AI Fluency ---
--- video 2: The Four Competencies (07:42) ---
```

Paste verbatim. Do not clean it up: `reading.original` in the lesson is the
uncleaned text, and the gap between it and the B1 version *is* the teaching
material.

Write down the total running time of the module in minutes — step 2 needs it.

---

## Step 2. Speech rate (2 min)

```bash
bash scripts/wpm.sh lessons/wNN/source.md <minutes>
```

`wpm = words / minutes`

| wpm | Verdict for B1 |
|---|---|
| < 130 | comfortable, listen without pausing |
| 130–150 | fine, but pre-teach the vocabulary first |
| > 150 | cut into 3–5 min chunks, listen twice |

Record the number in `friction.md`.

---

## Step 3. Generate the lesson body (5 min)

`lessons/wNN/source_prompt.md` is the prompt. Send it followed by the whole
contents of `source.md` (the prompt ends with `SOURCE MATERIAL:`).

What the prompt encodes, and why it must not be replaced with something
generic:

- **The learner profile** — their tools (CLI agents, routers, drones, the
  typing platform), their goals, and the weaknesses diagnosed from the
  baseline recording (dropped `-ing`, missing articles, no present perfect,
  drifting off the question). Content that ignores this profile is a failure.
- **Hard output rules** the build later enforces: exactly 9 vocabulary items,
  exactly 10 quiz questions at 3 easy / 5 medium / 2 hard, exactly 3 options
  with exactly one correct, `note` ≤ 25 words, `explanation` 80–120 words,
  every `term_refs` entry present in `vocabulary`, correct answers spread
  across a/b/c.

Output is one raw JSON object with the keys `objectives`, `vocabulary`,
`pronunciation_focus`, `reading`, `speaking_prompts`, `homework`, `quiz`.

If a lesson is being regenerated, keep the previous JSON — comparing two
generations is the fastest way to spot which parts the model is guessing at.

---

## Step 4. Review and merge into `lesson.json` (10 min)

**This step is the course.** The model produced a draft; the student decides
what survives. Merge the generated keys into `lessons/wNN/lesson.json`, then:

- **Fill in `ua` by hand.** The prompt forbids Ukrainian in its output, so
  every vocabulary item arrives without it. This is deliberate: writing the
  Ukrainian equivalent yourself is a vocabulary exercise, not clerical work.
- **Cut and replace terms.** The model reliably picks 2–3 words that are too
  easy or too rare. Replace them with words that actually blocked you while
  watching — including non-AI words (`blurry`, `leverage`, `shortcut`).
- **Rewrite `objectives`, `speaking_prompts` and `homework` in your own
  words.** Model versions are a starting skeleton. A speaking prompt you did
  not write is a prompt you will not want to answer.
- **Drop keys `lesson.json` does not define.** The prompt returns
  `pronunciation_focus`, and an `example` field per vocabulary item; neither
  is part of the lesson format (see Known gaps). The build does not reject
  extra keys, but the schema forbids them — keep the file clean.
- Set `week`, `title`, `source`, `duration_min` and the `audio` entries.
  Put mp3 files in `lessons/wNN/audio/` and point `src` at
  `./audio/wNN-v1.mp3`; use `url` for anything hosted elsewhere.

Then append the week's terms to the cumulative master file
`termbank/termbank.csv`, semicolon-separated, one row per term:

```
week;term;definition_b1;collocation_1;collocation_2;ua;source_sentence;added_at
```

---

## Step 5. Build (1 min)

```bash
python3 scripts/build_lesson.py wNN
```

`lesson.json` → validation → `index.html`, plus a progress block showing what
is still `TODO`. Add `--quiet` to suppress the block, or use `--all` to
rebuild every week.

The build **fails and writes nothing** on: a missing top-level key, a `week`
that does not match the folder, an empty quiz, a question without exactly 3
options or without exactly one `correct: true`, a missing or over-long `note`
(max 25 words), an `explanation` outside 80–150 words, an unknown
`difficulty`, or a `term_refs` entry that is not in `vocabulary`.

It **warns but still builds** when the quiz is not exactly 10 questions or
`TODO` markers remain. A work-in-progress lesson is expected to warn; a
lesson you are about to teach from should not.

---

## Step 6. Check in the browser (3 min)

```bash
open lessons/wNN/index.html
```

It must work from `file://` with the network off — no server, no CDN, no
`fetch()`. Walk all seven sections: header, objectives, vocabulary flip cards
and quick quiz, the reading B1/Original toggle (terms should be highlighted),
the quiz, the speaking prompts with their 60-second timer, and the homework
checklist (it persists to `localStorage` under `etai:wNN:*`).

Answer two or three quiz questions deliberately wrong: the options must lock,
the correct one must be revealed even though you did not pick it, and the
explanation must teach you something rather than tell you off.

---

## Step 7. Friction log

Append everything that cost time to `lessons/wNN/friction.md`:

```
- [copy] transcript copied by hand for every video -> needs an export
- [terms] ~20% of terms had to be thrown out -> needs a stop-list
- [ua] filled the ua field by hand for 9 terms -> acceptable, it is an exercise
- [wpm] counted on a calculator -> scripted
```

---

## Readiness checklist

- [ ] `source.md` filled, every item labelled with its origin
- [ ] wpm calculated and written into `friction.md`
- [ ] 9 vocabulary items reviewed by hand, `ua` filled in
- [ ] `reading.b1` read aloud once, then the original read after it
- [ ] quiz has 10 questions and the build reports no warnings
- [ ] `objectives`, `speaking_prompts`, `homework` rewritten in your own words
- [ ] `python3 scripts/termbank_sync.py` run, terms present in
      `termbank/termbank.csv`; reviewed for at least 3 days before the lesson
- [ ] talk rehearsed aloud twice (structure only from AI — see `prep.md`)
- [ ] `friction.md` filled in
- [ ] `agenda.md` sent to the teacher a day before the lesson

---

## Known gaps

Recorded here rather than fixed silently:

- `reading.b1` is 40–60 % below the 400–500 words this runbook's prompt asks
  for in every week from w03 onward. The build warns about it; the readings
  themselves have not been regenerated. See `docs/revision-spec.md` R10.

- `lessons/Outline_course.md` is a rough paste from Coursera and carries stray
  "Success: Complete" lines. The `lesson-builder` skill reads module names from
  it, so it works, but it deserves a clean-up.
- `source_prompt.md` is not part of `templates/week-scaffold/`, so every new
  week starts by copying it from the previous one.

---

## Quiz option references

Options are shuffled every time the quiz is rendered, so an `explanation` or a
`note` must never say "the second option". It names the option by id instead:

- `{{opt:b}}` renders as the ordinal that option currently occupies
- `{{opt:b,c}}` renders as two ordinals in ascending display order

`build_lesson.py` rejects an unknown id and any surviving positional phrase,
and fails the build if one position holds more than half of the correct
answers. The 80–150 word limit on an explanation is measured after the tokens
expand — that is what the student reads.

---

## Publishing to GitHub Pages

The site is pre-built and committed — there is no CI step and no Jekyll build.

1. `python3 scripts/build_lesson.py --all` (regenerates every lesson **and**
   the root `index.html`), then commit.
2. Push to GitHub.
3. Settings → Pages → Source: *Deploy from a branch*, branch `main`, folder
   `/ (root)`.

`.nojekyll` at the root turns Jekyll off, so the committed HTML is served
exactly as it is. Every link is relative, so the same files work offline from
`file://` — the lessons keep their one hard requirement either way.

Rebuild and commit the HTML whenever a `lesson.json` changes; the published
site is only ever as fresh as the last committed build.
