# How to change a lesson's text by hand

Edit **`lessons/wNN/lesson.json`** — it is the source of truth. **Never edit
`index.html`**: it is generated, and your changes are erased by the next build.

## Steps

1. Open `lessons/w01/lesson.json` in any editor.
2. Change the text you want. It is ordinary JSON — the text sits inside quotes.
3. Rebuild:
   ```bash
   python3 scripts/build_lesson.py w01
   ```
4. Refresh the page in the browser (`open lessons/w01/index.html`).

## What each field controls

| Field | Where it appears |
|---|---|
| `title`, `duration_min` | the lesson header |
| `objectives` | the Objectives section |
| `vocabulary` | the flip cards and the quick vocabulary quiz |
| `pronunciation_focus` | the Pronunciation section (omitted when absent) |
| `reading.b1` / `reading.original` | the two tabs of the Reading section |
| `quiz` | the main quiz |
| `speaking_prompts` | the speaking section, one 60-second timer each |
| `homework` | the checklist at the end |

## Rules the build enforces

If you break one of these the build stops and prints what is wrong, and no
file is written:

- exactly 3 options per question, exactly one marked `"correct": true`
- an `explanation` of 80–120 words, a `note` of at most 25 words
- never name an option by position ("the second option"). The options are
  shuffled every time the quiz is rendered, so write `{{opt:b}}` instead — it
  is replaced with the ordinal that option actually has on screen.
- the correct answer must not sit in the same position in most questions

Run `python3 scripts/build_lesson.py --all` to rebuild every week and the
landing page at once.
