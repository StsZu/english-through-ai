#!/usr/bin/env bash
# Create a new week folder from templates/week-scaffold/.
# Usage: bash scripts/new_week.sh w02
# Substitutes the week number into file contents; never overwrites existing files.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
scaffold="$root/templates/week-scaffold"

week="${1:-}"
if ! [[ "$week" =~ ^w[0-9]{2}$ ]]; then
  echo "Usage: bash scripts/new_week.sh wNN   (e.g. w02)" >&2
  exit 1
fi

dest="$root/lessons/$week"
mkdir -p "$dest/audio"

created=0
skipped=0
while IFS= read -r src; do
  rel="${src#"$scaffold"/}"
  target="$dest/$rel"
  if [[ -e "$target" ]]; then
    echo "skip (exists): lessons/$week/$rel"
    skipped=$((skipped + 1))
    continue
  fi
  mkdir -p "$(dirname "$target")"
  case "$rel" in
    *.md|*.json)
      sed "s/wNN/$week/g" "$src" > "$target"
      ;;
    *)
      cp "$src" "$target"
      ;;
  esac
  echo "created: lessons/$week/$rel"
  created=$((created + 1))
done < <(find "$scaffold" -type f | sort)

echo "Done: $created created, $skipped skipped. Next: fill lessons/$week/lesson.json, then run: python3 scripts/build_lesson.py $week"
