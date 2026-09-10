#!/usr/bin/env python3
"""Build a lesson: lessons/wNN/lesson.json -> lessons/wNN/index.html.

Usage:
    python3 scripts/build_lesson.py w01            build one week + progress block
    python3 scripts/build_lesson.py w01 --quiet    build without the progress block
    python3 scripts/build_lesson.py --all          rebuild every week + the index
    python3 scripts/build_lesson.py --index        rebuild only the landing page

Validation is intentionally hand-rolled (T-002): the repo must run on a clean
Python 3 with zero dependencies, so there is no `jsonschema` import. The rules
below are the single code path; templates/lesson.schema.json stays in the repo
as living documentation of the data format, not as executable validation.

Fails loudly on any validation error — it never builds silently from bad data.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "templates" / "lesson-template.html"
PLACEHOLDER = "__LESSON_DATA__"
INDEX_TEMPLATE = ROOT / "templates" / "index-template.html"
INDEX_PLACEHOLDER = "__COURSE_DATA__"
INDEX_OUT = ROOT / "index.html"
COURSE_LEAD = ("A B1 English course built on the AI Fluency framework: one "
               "90-minute lesson a week, student-led, each week a single "
               "self-contained page that works offline.")

NOTE_MAX_WORDS = 25
EXPLANATION_MIN_WORDS = 80
EXPLANATION_MAX_WORDS = 120   # same number source_prompt.md asks for
QUIZ_EXPECTED = 10
DIFFICULTIES = ("easy", "medium", "hard")
# source_prompt.md asks for 400-500 words, up to 700 when the facts need it.
READING_MIN_WORDS = 400
READING_MAX_WORDS = 700

REQUIRED_TOP = ("week", "title", "source", "duration_min", "objectives",
                "vocabulary", "reading", "audio", "quiz",
                "speaking_prompts", "homework")

# Explanations must point at options symbolically ({{opt:b}}, {{opt:b,c}}), never
# by position: the template shuffles the options on every attempt, so any
# "the second option" in the text is wrong as soon as it is rendered.
OPT_TOKEN = re.compile(r"\{\{opt:([a-z](?:,[a-z])*)\}\}")
POSITIONAL_REF = re.compile(
    r"\b(?:first|second|third)\s+(?:and\s+(?:first|second|third)\s+)?options?\b",
    re.IGNORECASE)


def words(s):
    return len(s.split())


def rendered(text):
    """Text as the learner sees it: {{opt:b,c}} becomes 'second and third'.

    Length limits describe what is read on screen, so they are measured after
    the option tokens expand, not on the shorthand stored in the JSON.
    """
    return OPT_TOKEN.sub(
        lambda m: " and ".join(["second"] * len(m.group(1).split(","))), text)


def is_todo(s):
    return isinstance(s, str) and "TODO" in s


def iter_strings(node):
    """Yield every string value anywhere in the JSON tree."""
    if isinstance(node, str):
        yield node
    elif isinstance(node, dict):
        for v in node.values():
            yield from iter_strings(v)
    elif isinstance(node, list):
        for v in node:
            yield from iter_strings(v)


def validate(week, data):
    """Return (errors, warnings). Errors stop the build; warnings do not."""
    errors, warnings = [], []

    for key in REQUIRED_TOP:
        if key not in data:
            errors.append(f"{week}: top-level field '{key}' is missing")
    if errors:
        return errors, warnings

    if data["week"] != week:
        errors.append(f"{week}: lesson.json says week '{data['week']}', "
                      f"building '{week}'")

    terms = {v.get("term", "") for v in data["vocabulary"]}
    quiz = data["quiz"]

    if len(quiz) == 0:
        errors.append(f"{week}: quiz has no questions")
    elif len(quiz) != QUIZ_EXPECTED:
        detail = " (work in progress is fine; a real lesson needs 10)" \
            if len(quiz) < 3 else ""
        warnings.append(f"{week}: quiz has {len(quiz)} questions, "
                        f"expected {QUIZ_EXPECTED}{detail}")

    for q in quiz:
        qid = q.get("id", "<no id>")

        options = q.get("options", [])
        if len(options) != 3:
            errors.append(f"{week} {qid} options: expected exactly 3, "
                          f"got {len(options)}")

        correct = sum(1 for o in options if o.get("correct") is True)
        if correct != 1:
            errors.append(f"{week} {qid} correct: expected exactly one "
                          f"'correct: true', got {correct}")

        for o in options:
            oid = o.get("id", "?")
            note = o.get("note")
            if not isinstance(note, str) or not note.strip():
                errors.append(f"{week} {qid} option {oid} note: missing or empty")
            elif words(rendered(note)) > NOTE_MAX_WORDS:
                errors.append(f"{week} {qid} option {oid} note: "
                              f"{words(rendered(note))} words, "
                              f"max {NOTE_MAX_WORDS}")

        explanation = q.get("explanation")
        if not isinstance(explanation, str) or not explanation.strip():
            errors.append(f"{week} {qid} explanation: missing or empty")
        elif not (EXPLANATION_MIN_WORDS <= words(rendered(explanation))
                  <= EXPLANATION_MAX_WORDS):
            errors.append(f"{week} {qid} explanation: "
                          f"{words(rendered(explanation))} words, must be "
                          f"{EXPLANATION_MIN_WORDS}-{EXPLANATION_MAX_WORDS}")

        difficulty = q.get("difficulty")
        if difficulty is not None and difficulty not in DIFFICULTIES:
            errors.append(f"{week} {qid} difficulty: '{difficulty}' is not one of "
                          f"{', '.join(DIFFICULTIES)}")

        for ref in q.get("term_refs", []):
            if ref not in terms:
                errors.append(f"{week} {qid} term_refs: '{ref}' not found in "
                              "vocabulary")

        option_ids = {o.get("id") for o in options}
        for field, text in [("explanation", q.get("explanation") or "")] + \
                [(f"option {o.get('id', '?')} note", o.get("note") or "")
                 for o in options]:
            for token in OPT_TOKEN.findall(text):
                for ref in token.split(","):
                    if ref not in option_ids:
                        errors.append(f"{week} {qid} {field}: {{{{opt:{token}}}}} "
                                      f"refers to option '{ref}', which does not "
                                      "exist")
            hit = POSITIONAL_REF.search(text)
            if hit:
                errors.append(f"{week} {qid} {field}: '{hit.group(0)}' names an "
                              "option by position; options are shuffled at "
                              "render time — use {{opt:<id>}} instead")

    # The correct answer must not cluster in one position. source_prompt.md has
    # required this from the start and it was violated in every week w03-w14:
    # a prompt is not an enforcement mechanism, so the build checks it.
    if quiz:
        counts = [0] * max(len(q.get("options", [])) for q in quiz)
        for q in quiz:
            for i, o in enumerate(q.get("options", [])):
                if o.get("correct") is True:
                    counts[i] += 1
        shape = "/".join(str(c) for c in counts)
        worst = max(counts)
        if worst > (len(quiz) + 1) // 2:
            errors.append(f"{week} quiz: the correct answer sits in the same "
                          f"position {worst} times out of {len(quiz)} "
                          f"(a/b/c = {shape}); spread it across the options")
        elif len(quiz) == QUIZ_EXPECTED and not all(3 <= c <= 4 for c in counts):
            warnings.append(f"{week} quiz: correct-answer spread is {shape}; "
                            "source_prompt.md asks for 3-4 per position")

    for i, item in enumerate(data.get("pronunciation_focus") or []):
        if not isinstance(item, dict):
            errors.append(f"{week} pronunciation_focus[{i}]: expected an object")
            continue
        for field in ("word", "stress", "why"):
            if not str(item.get(field, "")).strip():
                errors.append(f"{week} pronunciation_focus[{i}]: "
                              f"'{field}' is missing or empty")

    b1 = data.get("reading", {}).get("b1")
    if isinstance(b1, str) and not is_todo(b1):
        n_words = words(b1)
        if not READING_MIN_WORDS <= n_words <= READING_MAX_WORDS:
            warnings.append(f"{week}: reading.b1 is {n_words} words; "
                            f"source_prompt.md asks for "
                            f"{READING_MIN_WORDS}-{READING_MAX_WORDS}")

    todo_total = sum(s.count("TODO") for s in iter_strings(data))
    if todo_total:
        warnings.append(f"{week}: {todo_total} TODO marker(s) remaining")

    return errors, warnings


def progress_block(data):
    """Human-readable preparation checklist for a built lesson."""
    lines = []

    def row(label, text):
        lines.append(f"  {label:<17} {text}")

    def filled_row(label, items):
        todo = sum(1 for i in items if any(is_todo(s) for s in iter_strings(i)))
        filled = len(items) - todo
        row(label, f"{filled}/{len(items)} filled" +
            (f"      {todo} TODO" if todo else ""))

    filled_row("objectives", data["objectives"])
    filled_row("vocabulary", data["vocabulary"])
    row("reading.b1", "TODO" if is_todo(data["reading"]["b1"]) else "filled")
    row("reading.original",
        "TODO" if is_todo(data["reading"]["original"]) else "filled")
    n_quiz = len(data["quiz"])
    row("quiz", f"{n_quiz}/{QUIZ_EXPECTED} questions" +
        ("" if n_quiz == QUIZ_EXPECTED else f"   (warning: expected {QUIZ_EXPECTED})"))
    filled_row("speaking_prompts", data["speaking_prompts"])
    filled_row("homework", data["homework"])
    n_audio = sum(1 for a in data["audio"] if a.get("src") or a.get("url"))
    row("audio", f"{n_audio} item{'' if n_audio == 1 else 's'}")

    todo_total = sum(s.count("TODO") for s in iter_strings(data))
    lines.append("")
    lines.append(f"  {todo_total} TODO marker{'' if todo_total == 1 else 's'} remaining")
    return "\n".join(lines)


def build(week, quiet=False, summary_only=False):
    """Build one week. Returns a one-line summary string, or None on failure."""
    lesson_dir = ROOT / "lessons" / week
    lesson_path = lesson_dir / "lesson.json"
    rel = lesson_path.relative_to(ROOT)
    if not lesson_path.is_file():
        print(f"{week} FAILED — {rel} does not exist", file=sys.stderr)
        return None

    try:
        data = json.loads(lesson_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"{week} FAILED — {rel} is not valid JSON: {e}", file=sys.stderr)
        return None

    errors, warnings = validate(week, data)
    if errors:
        print(f"{week} BUILD FAILED — lesson.json is invalid:\n", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        print(f"\n{len(errors)} error(s). Fix lesson.json and run the build again.",
              file=sys.stderr)
        return None

    template = TEMPLATE.read_text(encoding="utf-8")
    if PLACEHOLDER not in template:
        print(f"{week} BUILD FAILED — placeholder {PLACEHOLDER} not found in "
              "template", file=sys.stderr)
        return None

    # `</` must be escaped so the JSON can never terminate the <script> block.
    payload = json.dumps(data, ensure_ascii=False, indent=2).replace("</", "<\\/")
    out = lesson_dir / "index.html"
    out.write_text(template.replace(PLACEHOLDER, payload), encoding="utf-8")

    todo_total = sum(s.count("TODO") for s in iter_strings(data))
    summary = (f"{week} built -> {out.relative_to(ROOT)}   "
               f"quiz {len(data['quiz'])}/{QUIZ_EXPECTED}, {todo_total} TODO")

    if summary_only:
        print(summary)
    else:
        print(f"{week} built -> {out.relative_to(ROOT)}")
        if not quiet:
            print()
            print(progress_block(data))
    for w in warnings:
        print(f"  warning: {w}", file=sys.stderr)
    return summary


def build_index():
    """Generate the course landing page at the repo root (for GitHub Pages).

    Like a lesson, it is derived from the lesson.json files and must never be
    edited by hand. Weeks whose JSON does not parse are skipped and reported;
    a broken week must not take the whole index down.
    """
    template = INDEX_TEMPLATE.read_text(encoding="utf-8")
    if INDEX_PLACEHOLDER not in template:
        print(f"index BUILD FAILED — placeholder {INDEX_PLACEHOLDER} not found "
              f"in {INDEX_TEMPLATE.relative_to(ROOT)}", file=sys.stderr)
        return None

    weeks, skipped = [], []
    for lesson_path in sorted((ROOT / "lessons").glob("w[0-9][0-9]/lesson.json")):
        week = lesson_path.parent.name
        try:
            data = json.loads(lesson_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            skipped.append(week)
            continue
        if not (lesson_path.parent / "index.html").is_file():
            skipped.append(week)
            continue

        reading = data.get("reading", {}).get("b1", "")
        weeks.append({
            "week": week,
            "title": data.get("title", week),
            "href": f"lessons/{week}/index.html",
            "duration_min": data.get("duration_min", 0),
            "vocabulary": len(data.get("vocabulary", [])),
            "quiz": len(data.get("quiz", [])),
            "homework": len(data.get("homework", [])),
            "reading_words": words(reading) if isinstance(reading, str) else 0,
            "terms": [
                {"term": v.get("term", ""),
                 "definition": v.get("definition_b1", "")}
                for v in data.get("vocabulary", [])
                if v.get("term") and "TODO" not in v.get("term", "")
            ],
        })

    if not weeks:
        print("index BUILD FAILED — no built lesson found", file=sys.stderr)
        return None

    sources = {w.get("source") for w in
               [json.loads((ROOT / "lessons" / wk["week"] / "lesson.json")
                           .read_text(encoding="utf-8")) for wk in weeks]}
    payload = {
        "source": sorted(sources)[0] if len(sources) == 1 else "Multiple sources",
        "lead": COURSE_LEAD,
        "weeks": weeks,
    }
    body = json.dumps(payload, ensure_ascii=False, indent=2).replace("</", "<\\/")
    INDEX_OUT.write_text(template.replace(INDEX_PLACEHOLDER, body), encoding="utf-8")

    print(f"index built -> {INDEX_OUT.relative_to(ROOT)}   "
          f"{len(weeks)} lesson(s), "
          f"{sum(len(w['terms']) for w in weeks)} term(s)")
    for week in skipped:
        print(f"  warning: {week} left out of the index (no index.html or "
              "unreadable lesson.json)", file=sys.stderr)
    return True


def main():
    args = sys.argv[1:]
    quiet = "--quiet" in args
    args = [a for a in args if a != "--quiet"]

    if args == ["--index"]:
        if build_index() is None:
            sys.exit(1)
        return

    if args == ["--all"]:
        weeks = sorted(p.parent.name for p in (ROOT / "lessons").glob("w*/lesson.json"))
        if not weeks:
            sys.exit("No lessons/wNN/lesson.json found.")
        failed = [w for w in weeks if build(w, summary_only=True) is None]
        if build_index() is None:
            failed.append("index")
        if failed:
            sys.exit(f"\n{len(failed)} week(s) failed: {', '.join(failed)}")
        return

    if len(args) != 1 or not re.fullmatch(r"w\d{2}", args[0]):
        sys.exit("Usage: python3 scripts/build_lesson.py wNN [--quiet] "
                 "| --all | --index")
    if build(args[0], quiet=quiet) is None:
        sys.exit(1)


if __name__ == "__main__":
    main()
