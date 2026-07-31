# Literature and novelty audit

## Safe contribution boundary

The manuscript does not claim novelty for any of these ingredients:

- generalized Stieltjes classes or exact Stieltjes order;
- total positivity or sign regularity of power-Cauchy kernels;
- Andréief's determinant integration identity;
- the HCIZ orbital-integral formula;
- fixed-trace Laguerre eigenvalue laws;
- the fact that certain determinants of Laplace transforms remain Laplace
  transforms;
- complete monotonicity of Wronskians of Laplace transforms.

The claim requiring independent novelty confirmation is:

> Strictly ordered minors of the shifted power-Cauchy kernel, viewed as
> functions of the common shift, have an explicit fixed-trace unitary-orbital
> representing measure of exact generalized Stieltjes order
> $n(a+n-1)$. This exact order persists for the associated nonconfluent
> Chebyshev-Markov determinants and confluent Wronskians. The orbital law has
> the stated support, mean, and variance and yields the determinant bounds and
> Hausdorff coefficient inequalities in the manuscript.

## Closest located work

Search snapshot: 31 July 2026. Metadata, abstracts, and the linked open texts
were searched where accessible. A listed work is not described as fully
excluded unless the discussion below says its complete text was checked.

### Exact generalized Stieltjes order

D. Karp and E. Prilepkina introduce and analyze exact Stieltjes order, provide
criteria, and study representative examples:

- [Generalized Stieltjes transforms: basic aspects](https://arxiv.org/abs/1111.4271)

A. D. Sokal and, later, S. Koumandos and H. L. Pedersen give real-variable
characterizations of generalized Stieltjes functions:

- [Real-variables characterization of generalized Stieltjes functions](https://arxiv.org/abs/0902.0065)
- [On generalized Stieltjes functions](https://arxiv.org/abs/1706.00606)

A. Gomilko and Y. Tomilov study representing measures for products of
generalized Stieltjes transforms. Product closure does not directly cover the
alternating determinant for general $a$:

- [To the theory of generalized Stieltjes transforms](https://arxiv.org/abs/2210.03474)

No determinant theorem with the order $n(a+n-1)$ was located in these
sources.

### Total positivity and power-Cauchy kernels

H. Dette and A. Munk determine sign-regularity properties for a generalized
Cauchy kernel. This is a direct warning against claiming determinant
positivity as new:

- [Sign regularity of a generalized Cauchy kernel with applications](https://doi.org/10.1016/0378-3758(95)00108-5)

K. I. Gross and D. St. P. Richards relate determinant integral
representations, total positivity, spherical series, and hypergeometric
functions of matrix argument:

- [Total positivity, spherical series, and hypergeometric functions of matrix argument](https://doi.org/10.1016/0021-9045(89)90153-6)

Their complete paper is the highest-priority collision check. Under the
substitution

\[
(s+t_i+x_j)^{-a}
=(s+t_i)^{-a}
\left(1+\frac{x_j}{s+t_i}\right)^{-a},
\]

the determinant enters the analytic product-kernel framework considered in
that literature. The full text must be checked for an Euler or orbital
representation equivalent to the one in the manuscript.

### Determinants and Wronskians of Laplace transforms

C. C. Kokonendji and V. Seshadri prove that determinants built from Laplace
transform derivatives and moment matrices are themselves Laplace transforms,
extending Lindsay-transform results:

- [On the determinant of the second derivative of a Laplace transform](https://doi.org/10.1214/aos/1032298297)

D. K. Dimitrov and Y. Xu show that Wronskians of Laplace transforms of
positive measures are completely monotone. Their Gamma example evaluates a
Wronskian as a power with exponent $n(n+\alpha)$, corresponding to
$n(a+n-1)$ after $a=\alpha+1$:

- [Wronskians of Fourier and Laplace Transforms](https://arxiv.org/abs/1606.05011)

The manuscript therefore claims neither complete monotonicity of Laplace
Wronskians nor the double-confluent power evaluation. Its new target is exact
generalized Stieltjes order for the nonconfluent family and the
Chebyshev-Markov extension.

### HCIZ and fixed-trace Laguerre ensembles

The orbital integral is standard. A proof and normalization reference is:

- [The Harish-Chandra integral: An introduction with examples](https://arxiv.org/abs/1806.11155)

Fixed-trace Laguerre ensembles arise as eigenvalue distributions of random
density matrices. Relevant references include:

- [Statistical properties of random density matrices](https://arxiv.org/abs/quant-ph/0405031)
- [Integrability enabled computations relating to the fixed trace Laguerre ensemble](https://arxiv.org/abs/2601.01711)

The fixed-trace density and mean-purity formula are established objects. The
manuscript also supplies a short integration-by-parts derivation of the one
purity moment it uses.

## Searches performed

The web and metadata search used combinations of:

- `generalized Stieltjes determinant exact order`
- `Stieltjes order Wronskian`
- `determinant (x_i+y_j)^(-a)`
- `power Cauchy kernel determinant Laplace transform`
- `compound Stieltjes kernel determinant`
- `Lindsay transform generalized Stieltjes`
- `HCIZ fixed trace Laguerre determinant inverse powers`
- the literal exponent `n(a+n-1)`

No exact statement matching the safe contribution boundary was located. Search
engine non-detection is weak evidence and does not establish novelty.

## Mandatory independent checks

1. Search MathSciNet and zbMATH by formula, keywords, authors, and citation
   chains from Karp-Prilepkina, Gross-Richards, Dette-Munk, Dimitrov-Xu, and
   Kokonendji-Seshadri.
2. Read the full Gross-Richards and Dette-Munk articles and compare formulas,
   not abstracts.
3. Search functions-of-matrix-argument references under both real and complex
   normalization conventions.
4. Ask a generalized-Stieltjes specialist whether exact order follows from an
   existing closure theorem not found in the search.
5. Ask a random-matrix specialist whether the shared-spectrum two-orbit law
   has an established name or transform formula.
6. Verify whether the Chebyshev-Markov extension appears in the literature on
   compound kernels or extended complete Chebyshev systems.

## Publication calibration

The orbital representation and exact-order theorem form an elegant short-note
result. By themselves they may be judged as a synthesis of standard tools. The
support and moment calculation, determinant inequalities, Hausdorff hierarchy,
and Chebyshev-system extension make the package more coherent and less
automatic.

A specialist-journal submission is reasonable after the mandatory checks.
No claim of certified novelty or acceptance is warranted before those checks.
