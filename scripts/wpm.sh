#!/usr/bin/env bash
# Words-per-minute check for a source transcript.
# Usage: bash scripts/wpm.sh lessons/w01/source.md 25
set -euo pipefail

file="${1:-}"
minutes="${2:-}"
if [[ -z "$file" || -z "$minutes" ]] || ! [[ "$minutes" =~ ^[0-9]+([.][0-9]+)?$ ]]; then
  echo "Usage: bash scripts/wpm.sh <file> <minutes>" >&2
  exit 1
fi
if [[ ! -f "$file" ]]; then
  echo "No such file: $file" >&2
  exit 1
fi

words=$(wc -w < "$file" | tr -d ' ')
wpm=$(awk -v w="$words" -v m="$minutes" 'BEGIN { printf "%.0f", w / m }')

if   (( wpm < 130 )); then verdict="<130 comfortable"
elif (( wpm <= 150 )); then verdict="130-150 needs pre-teaching"
else verdict=">150 split into 3-5 min chunks"
fi

echo "words: $words"
echo "wpm:   $wpm"
echo "verdict: $verdict"
