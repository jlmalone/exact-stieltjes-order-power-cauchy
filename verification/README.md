# Verification plan

## Current status

The initial repository pass was performed under resource-constrained mode.
The verifier and manuscript build were not executed. Static review covered:

- agreement of $\lambda=n(a+n-1)$ across all files;
- agreement of $c_{a,n}=\prod_{k=0}^{n-1}(a)_k/k!$;
- the radial exponent $na+n(n-1)-1=\lambda-1$;
- cancellation of the two HCIZ signs;
- the Laguerre-Selberg normalization;
- the exact-order contradiction at infinity;
- support endpoints and the Haar variance factor $1/(n^2-1)$;
- the fixed-trace purity calculation;
- the Chebyshev-system orientation and confluent limit.

## Exact arithmetic verifier

`exact_checks.py` uses only the Python standard library and exact rational
arithmetic. It checks:

1. the Gamma-Hankel determinant normalization;
2. Cauchy's determinant identity when $a=1$;
3. convergence to the asserted leading coefficient in several integer cases;
4. agreement between the orbital variance and uniform-Dirichlet variance when
   $a=1$.

Future command:

```sh
python3 verification/exact_checks.py
```

## Manuscript build

Future commands, from the repository root:

```sh
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error exact_stieltjes_order_power_cauchy.tex
```

After the build:

```sh
pdfinfo paper/exact_stieltjes_order_power_cauchy.pdf
pdftotext paper/exact_stieltjes_order_power_cauchy.pdf -
```

Render every page with Poppler and inspect theorem breaks, equation overflow,
references, and hyperlinks before tracking or releasing the PDF.

## Independent mathematical review

The following checks require subject-matter review rather than computation:

- verify the HCIZ convention and $C_n=\prod_{j=1}^{n-1}j!$;
- verify that the support argument uses support closure correctly;
- verify integration by parts for all $a>0$, including $0<a<1$;
- verify the exact-order argument against the chosen definition of
  $\mathcal S_\alpha$;
- verify that the confluent determinant is normalized by
  $\prod_{j=0}^{n-1}j!$;
- compare the claimed nonconfluent theorem with the full Gross-Richards and
  Lindsay-transform literature.

## Authority

The verifier can catch normalization and transcription errors. Passing it
does not prove exact order, support, positivity, or novelty. Those claims rest
on the manuscript proof and independent review.
