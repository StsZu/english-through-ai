You are building one lesson of a 12-week English course. The learner studies
English through AI content. Output is machine-consumed: it is validated by a
build script and rendered into an HTML lesson page.

## LEARNER PROFILE

Use this to make the lesson specific to this person. Generic content is a failure.

- CEFR B1, Ukrainian speaker, adult, learning independently with a 1:1 teacher
- Works daily with: Claude Code / CLI agents, terminal on macOS, git, Python at
  a basic level, vibe coding, MikroTik routers, Raspberry Pi, Arduino, DJI drones
- Has built: an educational typing-practice platform, static sites on Vercel
- Goals: talk about AI confidently in English, pass a drone certification abroad
- Diagnosed weaknesses from a baseline recording:
  - drops or slurs `-ing` endings (using, learning, coding, working)
  - omits articles before singular nouns
  - avoids present perfect entirely
  - answers a different question from the one asked (drifts to personal anecdote)
- Strength: long uninterrupted speech, good circumlocution when stuck

## OUTPUT

Return ONE raw JSON object. No markdown fences, no commentary, no explanation
of your work. These exact keys, in this order:

`objectives`, `vocabulary`, `pronunciation_focus`, `reading`,
`speaking_prompts`, `homework`, `quiz`

---

### objectives

3 items. Format: `"By the end of this lesson I can <verb> ..."`

Each must be observable — something the learner either did or did not do in
the lesson. Ban "understand", "know", "be aware of". Use: explain, compare,
give an example of, argue, describe, decide.
At least one objective must be about **language**, not about AI.

### vocabulary

Exactly 9 items. English only — no Ukrainian anywhere in the output.

For each:
- `term`
- `definition_b1` — max 15 words, B1 vocabulary only, must NOT contain the term
- `collocations` — exactly 2 natural phrases, not definitions in disguise
- `example` — ONE new sentence you write, placing the term in a context from
  the learner profile above (terminal, router, drone, typing platform, git).
  Must not be copied from the source.
- `source_sentence` — verbatim from the source material. If the term does not
  appear verbatim in the source, do not include the term at all.

Selection rules:
- Skip words a Ukrainian speaker gets for free: system, information, process,
  structure, model, result, function, problem.
- At least 3 of the 9 must NOT be AI jargon: general academic verbs,
  adjectives or linking phrases that the learner needs to sound B2.
- Prefer words that carry meaning in speech over words that only appear in text.

### pronunciation_focus

3 items. Pick from the vocabulary and from the source's key phrases the words
this specific learner will mispronounce.

For each:
- `word`
- `stress` — the word with the stressed syllable in CAPITALS, e.g. `in-TEL-li-gence`
- `why` — one short sentence naming the exact problem for this learner
- `minimal_pair` — a real English word that sounds close and would be confused,
  or `null` if none exists

At least one must target an `-ing` ending.

### reading

- `b1` — the source rewritten at B1 level.
  Target 400–500 words. **If keeping every fact requires more, go up to 700.
  Never drop a fact to hit the word count.** Adapting the level and shortening
  the content are different operations; you are only doing the first.
  Keep every technical term unchanged and in `**bold**`.
  No sentence longer than 15 words.
  Passive voice at most twice in the whole text.
- `original` — the source material, verbatim, uncleaned.

### speaking_prompts

5 questions the learner will answer out loud to a teacher, 60 seconds each.

Hard rules:
- Every prompt must be impossible to answer without taking a position or
  giving a concrete example. Ban prompts answerable with a definition.
- At least 2 must reference the learner profile directly (their router, their
  drones, their CLI agents, their typing platform).
- At least 1 must force a comparison or a disagreement.
- Each prompt names 2–3 vocabulary terms the learner must use in the answer.

Test to apply to yourself: if a prompt would work equally well in a lesson
about cooking, delete it and write another.

### homework

3 items. Each must be checkable — someone can look and say done or not done.

- item 1: vocabulary practice, naming the specific deck and a time budget
- item 2: a **pronunciation** task built from `pronunciation_focus`, phrased as
  a recording the learner makes and checks with a transcription tool
- item 3: a production task — write or record something specific about this
  week's topic, with a length or duration stated

Ban vague verbs: review, study, practise more, think about.

### quiz

Exactly 10 questions.

For each:
- `id` — `q1` … `q10`
- `prompt`
- `difficulty` — `easy` | `medium` | `hard`. Distribution: 3 easy, 5 medium, 2 hard
- `term_refs` — terms that must exist in `vocabulary`
- `options` — exactly 3, ids `a`, `b`, `c`
  - exactly one has `"correct": true`
  - each has `note`, max 25 words, a short verdict line
- `explanation` — 80–120 words, CEFR B1. It must:
  1. explain why the correct answer is correct
  2. say briefly why the other two are wrong
  3. add ONE fact, example or nuance that is NOT in the question or options

**Answer position — this is mandatory and has been violated before:**
- Distribute the correct option across `a`, `b` and `c`.
- Across the 10 questions, no letter may be correct more than 4 times, and
  every letter must be correct at least 3 times.
- Do not write the correct answer first and then add distractors. Write all
  three options, then choose the position.
- The build now enforces this: `build_lesson.py` fails if one position holds
  more than half of the correct answers.

**Never name an option by its position.** The lesson shuffles the three options
every time the quiz is rendered, so "the second option is wrong" is false as
soon as the student sees it. Refer to an option by its id, with a token:

- one option:  `The {{opt:b}} option is wrong because ...`
- two options: `The {{opt:b,c}} options both miss ...`

The token is replaced at render time with the ordinal the student actually
sees ("first" / "second" / "third"), so the sentence is always true. Write the
token exactly as shown, lowercase ids, no spaces. The build rejects both an
unknown id and any surviving phrase like "the second option".

Distractor quality:
- A wrong option nobody would choose teaches nothing. Each distractor must be
  a mistake a real B1 learner could plausibly make.
- The correct option must not be systematically the longest one.
- Questions test understanding, not memory of the source's exact wording.

---

## SELF-CHECK BEFORE YOU RETURN

Verify silently, fix anything that fails, then output. Do not report on this.

1. `vocabulary` has exactly 9 items and contains zero Ukrainian characters
2. Every `source_sentence` appears verbatim in the source material
3. Every `definition_b1` is 15 words or fewer and omits its own term
4. Correct-answer letters: count them. Each of a/b/c appears 3–4 times
4a. No `explanation` or `note` contains the words "first option", "second
    option" or "third option" — use `{{opt:<id>}}` instead
5. Every `explanation` is between 80 and 120 words
6. Every `note` is 25 words or fewer
7. Every `term_refs` entry exists in `vocabulary`
8. Difficulty counts are exactly 3 / 5 / 2
9. No sentence in `reading.b1` exceeds 15 words
10. No `TODO` string anywhere in the output
11. Output parses as JSON

---

SOURCE MATERIAL:
