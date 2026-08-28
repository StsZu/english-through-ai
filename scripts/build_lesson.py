#!/usr/bin/env python3
"""Build a lesson: lessons/wNN/lesson.json -> lessons/wNN/index.html.

Usage: python3 scripts/build_lesson.py w01

Reads the lesson data, validates it (JSON Schema if the `jsonschema` package
is available, plus built-in rules that the schema cannot express), embeds the
data into templates/lesson-template.html and writes lessons/wNN/index.html.

Fails loudly on any validation error — it never builds silently from bad data.
Stdlib only, with `jsonschema` as the single optional extra.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "templates" / "lesson-template.html"
SCHEMA = ROOT / "templates" / "lesson.schema.json"
PLACEHOLDER = "__LESSON_DATA__"

FEEDBACK_MIN_WORDS = 40
FEEDBACK_MAX_WORDS = 120


def fail(errors):
    print("BUILD FAILED — lesson.json is invalid:\n", file=sys.stderr)
    for e in errors:
        print(f"  - {e}", file=sys.stderr)
    print(f"\n{len(errors)} error(s). Fix lesson.json and run the build again.",
          file=sys.stderr)
    sys.exit(1)


def validate_schema(data, schema):
    """JSON Schema validation; skipped with a warning if jsonschema is missing."""
    try:
        import jsonschema
    except ImportError:
        print("WARNING: the 'jsonschema' package is not installed — skipping "
              "JSON Schema validation. Built-in rules below still apply.\n"
              "         Install with: pip install jsonschema", file=sys.stderr)
        return []
    validator = jsonschema.Draft7Validator(schema)
    return [f"schema: {'/'.join(str(p) for p in e.absolute_path) or '<root>'}: "
            f"{e.message}" for e in validator.iter_errors(data)]


def validate_rules(data):
    """Rules the schema cannot express. These always run."""
    errors = []
    terms = {v.get("term", "") for v in data.get("vocabulary", [])}

    for q in data.get("quiz", []):
        qid = q.get("id", "<no id>")
        options = q.get("options", [])

        if len(options) != 3:
            errors.append(f"quiz {qid}: expected exactly 3 options, got {len(options)}")

        correct_count = sum(1 for o in options if o.get("correct") is True)
        if correct_count != 1:
            errors.append(f"quiz {qid}: expected exactly 1 correct option, "
                          f"got {correct_count}")

        for o in options:
            oid = o.get("id", "?")
            feedback = o.get("feedback")
            if not isinstance(feedback, str) or not feedback.strip():
                errors.append(f"quiz {qid} option {oid}: feedback is missing or empty "
                              "(every option needs feedback, not only the correct one)")
                continue
            words = len(feedback.split())
            if not FEEDBACK_MIN_WORDS <= words <= FEEDBACK_MAX_WORDS:
                errors.append(f"quiz {qid} option {oid}: feedback is {words} words, "
                              f"must be {FEEDBACK_MIN_WORDS}-{FEEDBACK_MAX_WORDS}")

        for ref in q.get("term_refs", []):
            if ref not in terms:
                errors.append(f"quiz {qid}: term_refs '{ref}' not found in vocabulary "
                              f"(known terms: {', '.join(sorted(terms)) or 'none'})")

    return errors


def build(week):
    lesson_dir = ROOT / "lessons" / week
    lesson_path = lesson_dir / "lesson.json"
    if not lesson_path.is_file():
        sys.exit(f"BUILD FAILED — {lesson_path.relative_to(ROOT)} does not exist.")

    try:
        data = json.loads(lesson_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        sys.exit(f"BUILD FAILED — {lesson_path.relative_to(ROOT)} is not valid JSON: {e}")

    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))

    errors = validate_schema(data, schema) + validate_rules(data)
    if data.get("week") != week:
        errors.append(f"week mismatch: lesson.json says '{data.get('week')}', "
                      f"building '{week}'")
    if errors:
        fail(errors)

    template = TEMPLATE.read_text(encoding="utf-8")
    if PLACEHOLDER not in template:
        sys.exit(f"BUILD FAILED — placeholder {PLACEHOLDER} not found in template.")

    # `</` must be escaped so the JSON can never terminate the <script> block.
    payload = json.dumps(data, ensure_ascii=False, indent=2).replace("</", "<\\/")
    html = template.replace(PLACEHOLDER, payload)

    out = lesson_dir / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"OK — built {out.relative_to(ROOT)} "
          f"({len(data.get('quiz', []))} quiz questions, "
          f"{len(data.get('vocabulary', []))} terms)")


def main():
    if len(sys.argv) != 2 or not re.fullmatch(r"w\d{2}", sys.argv[1]):
        sys.exit("Usage: python3 scripts/build_lesson.py wNN   (e.g. w01)")
    build(sys.argv[1])


if __name__ == "__main__":
    main()
