#!/bin/sh
set -eu

repo_name=exact-stieltjes-order-power-cauchy
repo_root=$(CDPATH= cd "$(dirname "$0")" && pwd -P)

die() {
    printf '%s\n' "verification gate: $*" >&2
    exit 1
}

[ "$(basename "$repo_root")" = "$repo_name" ] || die "unexpected repository name"
git_root=$(git -C "$repo_root" rev-parse --show-toplevel 2>/dev/null) || die "not a Git worktree"
[ "$git_root" = "$repo_root" ] || die "run from the repository checkout"
[ -z "$(git -C "$repo_root" status --porcelain)" ] || die "a clean checkout is required"

command -v python3 >/dev/null 2>&1 || die "Python 3 is required"
command -v latexmk >/dev/null 2>&1 || die "latexmk is required"

git -C "$repo_root" diff --check
python3 "$repo_root/verification/exact_checks.py"

cd "$repo_root/paper"
latexmk -pdf -interaction=nonstopmode -halt-on-error exact_stieltjes_order_power_cauchy.tex

printf '%s\n' "Verification and LaTeX build completed. Rendered-page inspection remains required."
