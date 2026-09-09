#!/usr/bin/env python3
"""Collect vocabulary from every lessons/wNN/lesson.json into the termbank.

Usage:
    python3 scripts/termbank_sync.py            rewrite termbank/termbank.csv
    python3 scripts/termbank_sync.py --check    report drift, write nothing

The termbank is what makes the course cumulative rather than fourteen isolated
lessons, so it is derived from the lesson files rather than maintained by hand.
Rows already present keep their original `added_at`; only new terms are stamped
with today's date. Nothing is ever dropped: a term that disappears from a
lesson.json is kept and reported, never silently removed.

Stdlib only, by the same decision as build_lesson.py (T-002).
"""

import csv
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BANK = ROOT / "termbank" / "termbank.csv"
FIELDS = ["week", "term", "definition_b1", "collocation_1", "collocation_2",
          "ua", "source_sentence", "added_at"]


def read_existing():
    if not BANK.is_file():
        return {}
    with BANK.open(encoding="utf-8", newline="") as fh:
        return {(r["week"], r["term"]): r
                for r in csv.DictReader(fh, delimiter=";")
                if r.get("term")}


def collect():
    rows, seen_terms = [], {}
    for lesson in sorted((ROOT / "lessons").glob("w[0-9][0-9]/lesson.json")):
        week = lesson.parent.name
        data = json.loads(lesson.read_text(encoding="utf-8"))
        for entry in data.get("vocabulary", []):
            term = (entry.get("term") or "").strip()
            if not term or "TODO" in term:
                continue
            colls = entry.get("collocations") or []
            rows.append({
                "week": week,
                "term": term,
                "definition_b1": entry.get("definition_b1", ""),
                "collocation_1": colls[0] if len(colls) > 0 else "",
                "collocation_2": colls[1] if len(colls) > 1 else "",
                "ua": entry.get("ua", ""),
                "source_sentence": entry.get("source_sentence", ""),
                "added_at": "",
            })
            seen_terms.setdefault(term.lower(), []).append(week)
    return rows, seen_terms


def main():
    check = "--check" in sys.argv[1:]
    existing = read_existing()
    rows, seen_terms = collect()

    today = date.today().isoformat()
    new = 0
    for row in rows:
        prior = existing.get((row["week"], row["term"]))
        if prior and prior.get("added_at"):
            row["added_at"] = prior["added_at"]
        else:
            row["added_at"] = today
            new += 1

    keys = {(r["week"], r["term"]) for r in rows}
    orphans = [k for k in existing if k not in keys]

    if check:
        print(f"{len(rows)} term(s) in lessons, {len(existing)} in termbank, "
              f"{new} would be added")
    else:
        BANK.parent.mkdir(parents=True, exist_ok=True)
        with BANK.open("w", encoding="utf-8", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=FIELDS, delimiter=";")
            writer.writeheader()
            writer.writerows(rows)
            # a term the lessons no longer mention is kept, not dropped
            writer.writerows(existing[k] for k in orphans)
        print(f"termbank/termbank.csv — {len(rows)} term(s), {new} new")

    repeats = {t: w for t, w in seen_terms.items() if len(w) > 1}
    if repeats:
        print(f"\n{len(repeats)} term(s) taught in more than one week:")
        for term, weeks in sorted(repeats.items()):
            print(f"  {term} — {', '.join(weeks)}")
    if orphans:
        print(f"\n{len(orphans)} row(s) kept but no longer in any lesson.json:")
        for week, term in sorted(orphans):
            print(f"  {week} {term}")


if __name__ == "__main__":
    main()
