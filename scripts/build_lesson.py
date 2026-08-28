#!/usr/bin/env python3
"""Build a lesson: lessons/wNN/lesson.json -> lessons/wNN/index.html.

Usage:
    python3 scripts/build_lesson.py w01            build one week + progress block
    python3 scripts/build_lesson.py w01 --quiet    build without the progress block
    python3 scripts/build_lesson.py --all          rebuild every week, one line each

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

NOTE_MAX_WORDS = 25
EXPLANATION_MIN_WORDS = 80
EXPLANATION_MAX_WORDS = 150
QUIZ_EXPECTED = 10
DIFFICULTIES = ("easy", "medium", "hard")

REQUIRED_TOP = ("week", "title", "source", "duration_min", "objectives",
                "vocabulary", "reading", "audio", "quiz",
                "speaking_prompts", "homework")


def words(s):
    return len(s.split())


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
            elif words(note) > NOTE_MAX_WORDS:
                errors.append(f"{week} {qid} option {oid} note: {words(note)} "
                              f"words, max {NOTE_MAX_WORDS}")

        explanation = q.get("explanation")
        if not isinstance(explanation, str) or not explanation.strip():
            errors.append(f"{week} {qid} explanation: missing or empty")
        elif not EXPLANATION_MIN_WORDS <= words(explanation) <= EXPLANATION_MAX_WORDS:
            errors.append(f"{week} {qid} explanation: {words(explanation)} words, "
                          f"must be {EXPLANATION_MIN_WORDS}-{EXPLANATION_MAX_WORDS}")

        difficulty = q.get("difficulty")
        if difficulty is not None and difficulty not in DIFFICULTIES:
            errors.append(f"{week} {qid} difficulty: '{difficulty}' is not one of "
                          f"{', '.join(DIFFICULTIES)}")

        for ref in q.get("term_refs", []):
            if ref not in terms:
                errors.append(f"{week} {qid} term_refs: '{ref}' not found in "
                              "vocabulary")

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


def main():
    args = sys.argv[1:]
    quiet = "--quiet" in args
    args = [a for a in args if a != "--quiet"]

    if args == ["--all"]:
        weeks = sorted(p.parent.name for p in (ROOT / "lessons").glob("w*/lesson.json"))
        if not weeks:
            sys.exit("No lessons/wNN/lesson.json found.")
        failed = [w for w in weeks if build(w, summary_only=True) is None]
        if failed:
            sys.exit(f"\n{len(failed)} week(s) failed: {', '.join(failed)}")
        return

    if len(args) != 1 or not re.fullmatch(r"w\d{2}", args[0]):
        sys.exit("Usage: python3 scripts/build_lesson.py wNN [--quiet] | --all")
    if build(args[0], quiet=quiet) is None:
        sys.exit(1)


if __name__ == "__main__":
    main()
