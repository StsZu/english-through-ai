# Baseline & Error Loop — protocol

Goal: get a measurable zero point, then see the delta every week in numbers
rather than in feelings.

---

## Part 1. Baseline (done ONCE, before the first lesson)

### Rules

1. **In English. Spoken. Recorded.** A written text will not do — it diagnoses
   neither tenses, nor articles, nor speed, nor pronunciation.
2. **No notes, no plan, no preparation.**
3. **No second take.** The first take is the baseline. Hesitation is data,
   not failure.
4. Exactly 3 minutes. Use a timer.

### Procedure

1. Voice recorder on your phone. File → `recordings/w00_baseline.m4a`
2. The question: **"What do you know about AI?"**
3. Talk for 3 minutes. If you do not know a word, describe it another way and
   move on.
4. Stop. Do not listen back. Do not redo it.

### Transcription

Upload the audio to ChatGPT or Gemini:

```
Transcribe this audio verbatim, including hesitations, false starts,
repetitions and grammatical errors. Do not correct anything.
Do not clean it up. Output plain text only.
```

→ `recordings/w00_baseline.txt` (kept on disk only — it is not committed)

### Diagnosis

Transcript → Claude Project:

```
You are an ESL diagnostician. Learner level: B1. Target: B2.

TRANSCRIPT OF A SPOKEN MONOLOGUE:
<<<paste>>>

DURATION_SECONDS: <<<number>>>

Return ONLY JSON, no fences:
{
 "wpm": int,
 "cefr_estimate": "A2|B1|B1+|B2",
 "type_token_ratio": float,
 "filler_count": int,
 "errors": [
   {"type":"tense|article|preposition|word_order|lexis|pronunciation",
    "utterance":"...",
    "correction":"...",
    "why_b1":"one short explanation a B1 learner will understand"}
 ],
 "top5_drill": ["five specific things to practise before the next session"],
 "strengths": ["..."],
 "content_accuracy": [
   {"claim":"...","verdict":"correct|imprecise|wrong","fix":"..."}
 ]
}
```

→ `errors/w00.json` (also kept on disk only)

**The `content_accuracy` block matters as much as the grammar.** It catches
conceptual mistakes — for example, confusing `training` (the model's weights,
permanent) with the `runtime loop` (the context window, gone after the
session).

---

## Part 2. Error Loop (every week)

After each 3-minute talk in the lesson:

```
recordings/wNN_talk.m4a
   -> transcription (the same prompt)
   -> diagnosis (the same prompt plus the block below)
   -> errors/wNN.json
```

Add to the diagnosis prompt:

```
RECURRING ERRORS FROM PREVIOUS SESSIONS:
<<<paste the "errors" arrays from earlier errors/*.json>>>

For every error, set "recurring": true if it appears in the history above.
Sort the output so recurring errors come first.
```

Errors marked `recurring: true` go into the 10–20 minute block of the next
lesson. That is the personal grammar syllabus, assembled from real data rather
than from a textbook.

---

## Part 3. Progress metrics

Every 4 weeks, collect them in `errors/progress.md`:

| Metric | w00 | w04 | w08 | w12 | Direction |
|---|---|---|---|---|---|
| wpm | | | | | up (target 110–130) |
| type_token_ratio | | | | | up |
| filler_count | | | | | down |
| errors total | | | | | down |
| recurring errors | | | | | down faster than the total |
| terms in active use | | | | | up |

**Final measurement (week 12):** the same recording, the same question —
"What do you know about AI?" — and the same diagnosis. Compare against w00.

---

## A note on privacy

The recordings, their transcripts and the `errors/*.json` diagnostics are
records of the learner's own speech. The repository is public, so none of them
are committed — `.gitignore` covers `recordings/*` and `errors/*.json`. They
live on disk only.
