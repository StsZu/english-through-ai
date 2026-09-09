# Week 1 — Student preparation

Source: **Coursera → Anthropic → AI Fluency: Framework & Foundations → Module 1**

Total time: ~3 hours, split across 3 days. Do not do it in one sitting — the
vocabulary will not settle.

---

## Day 1 (≈60 min) — input

- [ ] Work through Module 1 completely. **First pass without subtitles.** Note
      honestly, roughly, what percentage you understood.
- [ ] Second pass with the transcript on. Notice where the gaps were.
- [ ] Paste the raw transcript and readings into `lessons/w01/source.md`
      (`docs/manual-pipeline.md`, step 1)
- [ ] Count wpm (step 2). Write the number down.
- [ ] Take the Module 1 quiz. **Record your score and — more importantly —
      which questions you missed because of the language rather than the
      content.** That is a separate list: `friction.md`, section `[language]`.

**Put every word that blocked your understanding into the termbank.** Not only
AI terms. If `blurry`, `leverage` or `shortcut` stopped you, they belong on the
list too.

---

## Day 2 (≈70 min) — processing

- [ ] Step 3: pull out 12 terms → `lesson.json` (`vocabulary`). **Filter them by hand.**
- [ ] Step 4: the B1 version → `lesson.json` (`reading.b1`). Read it aloud.
- [ ] Step 5: the quiz → `index.html`. **Take it yourself**, then check against
      the explanations.
- [ ] Step 6: run `python3 scripts/termbank_sync.py` to append this week's terms
      to `termbank/termbank.csv`. Start reviewing them today.
- [ ] Fill in `lesson.json` (`vocabulary`) using the template below.

### Starting list of terms to verify

This is a **hypothesis**, not a finished list. Your job is to check against the
transcript which of these are actually used in Module 1, drop the ones that are
not, and add what I missed. That check is itself a reading exercise.

| # | Term | Verified in the transcript? |
|---|---|---|
| 1 | fluency | |
| 2 | framework | |
| 3 | collaboration / collaborate | |
| 4 | delegation / delegate | |
| 5 | description / describe | |
| 6 | discernment / discern | |
| 7 | diligence | |
| 8 | competency | |
| 9 | judgement | |
| 10 | accountability | |
| 11 | output | |
| 12 | workflow | |

Plus the set of four adjectives that runs through the whole course:
**effective / efficient / ethical / safe**. The difference between `effective`
and `efficient` is not obvious at B1 — that is a card of its own.

---

## Day 3 (≈50 min) — output

- [ ] Step 7: the outline of your talk → `lesson.json` (`speaking_prompts`).
      **You write the text yourself; the model gives you structure only.**
- [ ] Write the talk (≈250 words), read it aloud twice, then **close the text
      and tell it in your own words**.
- [ ] Record the rehearsal. Listen back. Do not rewrite it — just notice where
      you stop.
- [ ] Run the baseline per `docs/baseline-protocol.md` (if you have not yet).
      → `recordings/w00_baseline.m4a` + `errors/w00.json`
- [ ] Send `lessons/w01/agenda.md` to the teacher **a day before the lesson**.

---

## Template for `lesson.json` (`vocabulary`)

```markdown
# W01 Glossary — AI Fluency, Module 1

| Term | Definition (B1) | Collocations | UA | From transcript |
|---|---|---|---|---|
| fluency | | | | |
| ... | | | | |

## Words that blocked my understanding (not AI terms)
| Word | Meaning | Where I met it |
|---|---|---|
| | | |

## Questions I could not answer myself
1.
2.
3.
```

That last block is the most valuable one. It is the agenda for the teacher.

---

## What NOT to do

- Do not ask the AI to write the talk. The skeleton yes, the text no.
- Do not prepare a "perfect" lesson. Mistakes are the material.
- Do not translate the whole transcript into Ukrainian. Individual words only.
- Do not skip the quiz. It is your only external check on understanding.
