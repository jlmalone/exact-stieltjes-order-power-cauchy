# Publication Roadmap and Session Handoff

## Snapshot

Status recorded 5 August 2026.

- The public repository is `jlmalone/exact-stieltjes-order-power-cauchy`.
- `master` is the canonical branch.
- The initial research package is commit `6879b08`.
- The local and remote branches were synchronized and the worktree was clean
  before this handoff update.
- The LaTeX manuscript is the mathematical source of authority.
- No verifier, LaTeX build, rendered-page inspection, preprint deposit, DOI,
  journal submission, or independent expert review has been completed.
- Novelty and publication suitability remain provisional.

This file owns current release state, the next action, and the conditions for
calling the project submission-ready. Durable proofs remain in the manuscript;
literature evidence remains in `literature_audit.md`.

## What exists

The repository contains a coherent short-paper package:

1. An exact orbital representation for the shifted power-Cauchy determinant.
2. A proof that its minimal generalized Stieltjes order is
   $n(a+n-1)$.
3. The full support, mean, and variance of the compact representing law.
4. Support-and-moment determinant bounds and a strict Hausdorff hierarchy.
5. An extension to Chebyshev-Markov determinants and confluent Wronskians,
   including an explicit positive representing mixture.
6. Independent normalization derivations from large-shift asymptotics, the
   $a=1$ Cauchy identity, and double confluence.
7. A readable Markdown note, a LaTeX manuscript, a bibliography, a novelty
   audit, exact-arithmetic checks, and proposed submission metadata.

Static review has checked the central constants, the HCIZ sign cancellation,
the radial exponent, the Laguerre normalization, the exact-order contradiction,
the moment calculation, and the confluence normalization. Static review is not
independent proof verification.

## Immediate next action

After resource-constrained mode ends, start from a clean checkout and run:

```sh
./FUTURE_VERIFICATION.sh
```

This command runs the exact-arithmetic checks and builds the manuscript. A
successful command is necessary but not sufficient. Then inspect the PDF using
the commands and visual checklist in `verification/README.md`.

If any check fails, correct the mathematical source first, keep the Markdown
note synchronized, rerun the full gate, and commit the repair before proceeding.

## Submission-ready gates

The project is submission-ready only when every gate below is closed.

| Gate | Acceptance condition | Where to record it |
|---|---|---|
| Exact arithmetic | `verification/exact_checks.py` completes without an assertion failure | `verification/README.md` |
| Manuscript build | `latexmk` resolves the bibliography and exits successfully | `verification/README.md` |
| Rendered document | Every page is visually inspected with no clipping, overflow, broken references, or malformed equations | `verification/README.md` |
| Mathematical correctness | An independent analyst checks every item in the referee checklist below | This file and a dated review note |
| Novelty | The collision audit below is completed using full texts and specialist databases | `literature_audit.md` |
| Metadata | Owner-approved author, affiliation, contact, subject classification, and rights information are supplied | `submission/metadata.md` |
| Release | The inspected PDF and its source commit are packaged in a versioned release | Release notes |
| Submission | A preprint or journal system returns a durable receipt or identifier | `submission/metadata.md` |

Do not translate a passing computation, a clean PDF, or a search-engine result
into a claim of proof, novelty, publication, or acceptance.

## Independent mathematical referee checklist

The reviewer should attempt to falsify each item rather than merely follow the
derivation.

1. Re-derive the Gamma-Laplace and Andréief reduction, including the factor
   $1/(n!\Gamma(a)^n)$.
2. Check the HCIZ convention, both Vandermonde orientations, the factor
   $C_n=\prod_{j=1}^{n-1}j!$, and cancellation of the two signs.
3. Recompute the radial exponent
   $n(a-1)+(n-1)+n(n-1)=n(a+n-1)-1$.
4. Recompute the fixed-trace Laguerre normalization and confirm
   $c_{a,n}=\prod_{k=0}^{n-1}(a)_k/k!$.
5. Verify that the pushforward law has the claimed full support, including
   endpoints obtained only through support closure.
6. Verify that the asymptotic argument excludes every lower Stieltjes order,
   including representations with infinite total mass.
7. Re-derive the Haar variance identity and the fixed-trace purity formula.
8. Check integration by parts when $0<a<1$ and all boundary terms explicitly.
9. Check the Jensen, chord, and variance-refined determinant bounds.
10. Check the forward-difference sign convention and strict Hausdorff moment
    claims.
11. Re-derive the Andréief composition for a strict oriented Chebyshev system.
12. Check the confluent limit, factorial normalization, positivity of its
    mixture, and exact-order asymptotic.
13. Test the edge cases $n=1$, $a=1$, $t_1+x_1=0$, a measure with exactly
    $n$ support points, and simultaneous coalescence of both spectra.

An acceptable review either confirms each item with its own derivation or
identifies a precise statement that must be weakened or repaired.

## Novelty collision audit

The current web and metadata search did not locate the exact theorem. That is
weak evidence. Before submission:

1. Search MathSciNet and zbMATH by formula, terminology, author citation
   chains, and classifications around generalized Stieltjes transforms, total
   positivity, and functions of matrix argument.
2. Read the complete Gross-Richards and Dette-Munk papers. Compare displayed
   determinant and Euler-integral formulas, not titles or abstracts.
3. Follow citations from Karp-Prilepkina, Dimitrov-Xu,
   Kokonendji-Seshadri, and Gomilko-Tomilov.
4. Search under alternate language: compound kernels, Pólya frequency
   kernels, sign-regular Cauchy kernels, hypergeometric functions of two matrix
   arguments, orbital convolution, fixed-trace Wishart ensembles, random
   density matrices, Lindsay transforms, and Markov-system determinants.
5. Ask a generalized-Stieltjes specialist whether an order-raising or product
   closure theorem already implies the minimal order.
6. Ask a random-matrix specialist whether the shared-spectrum two-orbit law
   has a standard name or an existing transform formula.

For every close source, add a page, theorem, or equation-level comparison to
`literature_audit.md`. If an equivalent representation or exact-order theorem
is found, narrow the contribution immediately. Positivity, complete
monotonicity, or a double-confluent Wronskian alone does not collide with the
current safe contribution boundary.

## Stronger directions if the core result is not enough

Do not expand the paper until the collision audit is complete. If the core
theorem survives but an editor or expert judges the note too light, pursue one
focused strengthening rather than accumulating routine corollaries.

Priority order:

1. Derive the representing density explicitly for $n=2$, including endpoint
   behavior. This is the most tractable route to a genuinely new structural
   result.
2. Compute a usable third cumulant or a general higher-moment scheme from
   unitary integration and fixed-trace Laguerre moments.
3. Determine whether the Chebyshev-Markov theorem extends cleanly to extended
   complete Chebyshev systems or noncompact measures under sharp integrability
   hypotheses.
4. Investigate orthogonal and symplectic analogues only after identifying a
   replacement for the determinantal unitary HCIZ step. Do not advertise a
   beta-generalization without that mechanism.
5. Add applications only when the orbital law produces an inequality or
   extremal statement not already automatic from total positivity.

The best current publication shape is a focused specialist short paper. If a
close theorem absorbs the orbital representation and exact order, the project
needs one of the first three strengthenings before submission.

## Owner decisions before release

The following choices cannot be inferred safely:

- final author name, affiliation, contact address, and optional ORCID;
- repository and manuscript license;
- whether to seek an independent review before or after the $n=2$
  strengthening;
- preprint venue and target journal;
- whether the first public release should be source-only or include the
  inspected PDF.

The repository is public but currently has no license. Public visibility does
not grant reuse rights, so choose the license deliberately before inviting
external redistribution.

## Recommended release sequence

1. Run the recorded verifier and manuscript build outside resource-constrained
   mode.
2. Render and inspect every PDF page.
3. Repair all errors and commit a clean verified state.
4. Obtain the independent mathematical review.
5. Close the full-text novelty audit and revise the contribution statement.
6. Supply owner-approved metadata and licensing.
7. Tag a versioned source commit and attach the inspected PDF to the release.
8. Deposit the preprint and record its durable identifier.
9. Select and submit to a specialist journal using the final novelty
   comparison.

## Do not break

- Keep the theorem constant $n(a+n-1)$ and
  $c_{a,n}=\prod_{k=0}^{n-1}(a)_k/k!$ synchronized everywhere.
- Preserve the fact that the two orbital statistics are independent only
  conditionally on their shared spectrum.
- Keep established ingredients separate from the provisional contribution.
- Do not track a generated PDF until it has been built from the recorded
  source commit and visually inspected.
- Do not call the result novel, peer reviewed, submitted, published, or
  accepted without direct evidence for that exact state.

## Clean continuation point

The next session should begin by reading `AGENTS.md`, this file,
`verification/README.md`, and `literature_audit.md`. The first executable step
is `./FUTURE_VERIFICATION.sh` after resource-constrained mode has ended. Until
then, the project is a complete research package awaiting dynamic verification
and independent review, not a released or submitted paper.
