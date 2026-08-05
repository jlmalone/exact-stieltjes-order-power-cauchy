# AGENTS.md

## Scope

This repository contains a mathematical research note and its verification
materials. The proof in `paper/exact_stieltjes_order_power_cauchy.tex` is the
source of mathematical authority.

## Repository rules

- `master` is the canonical branch.
- `ROADMAP.md` owns current release state and the next action.
- Keep the theorem statement, Markdown note, and LaTeX manuscript consistent.
- State novelty as provisional until a full-text literature audit and
  independent expert review are complete.
- Treat computational checks as transcription and falsification aids. They do
  not replace proof.
- Keep generated LaTeX files out of version control. A release PDF may be
  tracked after it is rendered and inspected.
- In resource-constrained mode, use static review only. Record the exact future
  commands instead of running the manuscript build or verification program.

## Static acceptance

Before committing in resource-constrained mode:

1. inspect every changed file;
2. run `git diff --check`;
3. confirm the theorem constants agree across the README, note, manuscript,
   and verifier;
4. record unexecuted checks in `verification/README.md`.
