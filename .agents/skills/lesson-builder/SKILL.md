---
name: lesson-builder
description: End-to-end scaffolder, generator, and validator for weekly lessons in English Through AI. Use when scaffolding a new week ("зроби шаблон wNN") or building a lesson ("збери урок wNN").
---

# Lesson Builder Skill — English Through AI

This skill provides two automated workflows for the weekly lesson lifecycle in English Through AI:
1. **Scaffold Workflow (`"зроби шаблон wNN"`):** Prepares folders, templates, outline lookup, and prompt files.
2. **Build Workflow (`"збери урок wNN"`):** Converts `lessons/wNN/source.md` into `lesson.json` and compiles `lessons/wNN/index.html`.

---

## 1. Scaffold Workflow (`"зроби шаблон wNN"` / `"підготуй папку wNN"`)

When the user asks to create a template or scaffold a new week (e.g. `w05`):

1. **Create folder from template:**
   ```bash
   bash scripts/new_week.sh wNN
   ```
2. **Copy prompt file:**
   ```bash
   cp lessons/w01/source_prompt.md lessons/wNN/source_prompt.md
   ```
3. **Lookup title from `lessons/Outline_course.md`:**
   - Find the corresponding module title and estimated reading duration.
   - Update `"title"` in `lessons/wNN/lesson.json` with the real module name.
4. **Report readiness to user:**
   - Confirm that `lessons/wNN/` is ready.
   - Remind the user to paste the raw text from Coursera into `lessons/wNN/source.md`.

---

## 2. Build Workflow (`"збери урок wNN"` / `"згенеруй wNN"`)

When `lessons/wNN/source.md` is populated and the user asks to build the lesson:

### Step 1: Calculate WPM & Update Footer
1. Check module duration from `Outline_course.md` (e.g. 15 min).
2. Run WPM calculation:
   ```bash
   bash scripts/wpm.sh lessons/wNN/source.md <duration_minutes>
   ```
3. Insert or update metadata in `lessons/wNN/source.md`:
   ```markdown
   ---
   Total video duration in this module: <duration> min
   Word count (wc -w): <words>
   Words per minute: <wpm>
   Verdict: <verdict>
   ---
   ```

### Step 2: Vocabulary Extraction (12 terms)
For each term in `vocabulary`:
- **`term`**: Domain-specific word or phrase. Skip words transparent to Ukrainian speakers (e.g., *system, problem, process*).
- **`definition_b1`**: Maximum 20 words, strictly CEFR B1 vocabulary.
- **`collocations`**: Exactly 2 natural phrases with this term.
- **`ua`**: Accurate, natural Ukrainian translation.
- **`source_sentence`**: Verbatim sentence from `source.md`.

### Step 3: B1 Reading Adaptation (`reading.b1`)
- 400–500 words, CEFR B1 level.
- **Bold every technical term** (`**term**`).
- Sentences under 15 words.
- Preserve ALL key concepts, facts, and structure from `source.md`.
- Keep the raw text in `reading.original`.

### Step 4: Quiz Generation (`quiz`) — 10 Questions
Exactly 10 questions: 3 easy, 5 medium, 2 hard.
- **`id`**: `"q1"` to `"q10"`.
- **`prompt`**: Clear situational or conceptual question.
- **`difficulty`**: `"easy"`, `"medium"`, `"hard"`.
- **`term_refs`**: 1–3 terms matching items in `vocabulary`.
- **`options`**: Exactly 3 options (`"a"`, `"b"`, `"c"`), exactly one with `"correct": true`.
- **`options[].note`**: Short verdict line shown next to the option (1–25 words).
- **`explanation`**: **80–150 words**, CEFR B1. Explains why correct answer is right, why others are wrong, and adds **one new technical fact, example, or nuance** (e.g. CLI agents, Git branches, network configs, API keys).

### Step 5: Objectives, Speaking Prompts & Homework
- **`objectives`**: 3 statements starting with `"By the end of this lesson I can..."`.
- **`speaking_prompts`**: Array of 3–5 **plain strings** (NOT objects) requiring vocabulary usage.
- **`homework`**: Array of 3 **plain strings** (Anki review, pronunciation recording, 90s retell).

### Step 6: Write `lesson.json` & Build HTML
Write complete `lessons/wNN/lesson.json` and compile:
```bash
python3 scripts/build_lesson.py wNN
```

Verify build output has `0 error(s)` and `0 TODO marker(s) remaining`.
