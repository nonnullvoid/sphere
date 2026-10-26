#!/usr/bin/env bash
# Fail if any tracked file (or, with --history, any commit) matches a private pattern.
# Patterns live outside version control: $SPHERE_LEAK_PATTERNS, else .leakscan-patterns (gitignored).
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"
patterns="${SPHERE_LEAK_PATTERNS:-.leakscan-patterns}"

if [[ ! -s "$patterns" ]]; then
  echo "leak-scan: no patterns file at '$patterns' — refusing to pass without one." >&2
  exit 2
fi

regex="$(grep -v -e '^[[:space:]]*#' -e '^[[:space:]]*$' "$patterns" | paste -sd'|' -)"

case "${1:-}" in
  --history) hits="$(git rev-list --all | while read -r rev; do git grep -I -n -i -E "$regex" "$rev" -- . ":!$patterns" || true; done | sort -u)" ;;
  --range)   read -r -a revs <<< "${2:?usage: --range <rev-range>}"
             hits="$(git rev-list "${revs[@]}" | while read -r rev; do git grep -I -n -i -E "$regex" "$rev" -- . ":!$patterns" || true; done | sort -u)" ;;
  --staged)  hits="$(git grep --cached -I -n -i -E "$regex" -- . ":!$patterns" || true)" ;;
  "")        hits="$(git grep -I -n -i -E "$regex" -- . ":!$patterns" || true)" ;;
  *) echo "usage: $0 [--staged|--history|--range <rev-range>]" >&2; exit 2 ;;
esac

if [[ -n "$hits" ]]; then
  echo "leak-scan: private patterns found:" >&2
  echo "$hits" >&2
  exit 1
fi
echo "leak-scan: clean"
