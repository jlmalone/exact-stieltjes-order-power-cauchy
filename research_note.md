# Exact Stieltjes Order of Power-Cauchy Minors via Fixed-Trace Unitary Orbits

## Abstract

Let $a>0$, let $t_1<\cdots<t_n$ and $x_1<\cdots<x_n$, and suppose
$t_1+x_1\ge 0$. We prove that

\[
K_{a,n}(s)=\det[(s+t_i+x_j)^{-a}]_{i,j=1}^{n}
\]

is a generalized Stieltjes transform of exact order
$\lambda=n(a+n-1)$. Its representing probability variable is the sum of
two independent unitary-orbital linear statistics conditioned on a common
fixed-trace Laguerre spectrum. We compute the support, mean, and variance of
that variable. Consequences include explicit determinant bounds, a strict
Hausdorff-moment hierarchy, and an exact-order theorem for Chebyshev-Markov
determinants and their confluent Wronskians.

## 1. Definitions

For $\alpha>0$, the generalized Stieltjes class $\mathcal S_\alpha$
consists of functions

\[
f(s)=c+\int_{[0,\infty)}(s+y)^{-\alpha}\,\nu(dy),\qquad s>0,
\]

where $c\ge0$ and $\nu$ is a positive measure for which the integral is
finite. For a nonzero function belonging to at least one such class, define

\[
\alpha_*(f)=\inf\{\alpha>0:f\in\mathcal S_\alpha\}.
\]

The quantity $\alpha_*(f)$ is its exact Stieltjes order.

For a vector $z=(z_1,\ldots,z_n)$, write

\[
\Delta(z)=\prod_{1\le i<j\le n}(z_j-z_i).
\]

## 2. Orbital representation and exact order

### Theorem 2.1

Let $a>0$, $n\ge1$, and

\[
t_1<\cdots<t_n,\qquad x_1<\cdots<x_n,
\]

with $t_1+x_1\ge0$. Put

\[
\lambda=n(a+n-1),\qquad
c_{a,n}=\prod_{k=0}^{n-1}\frac{(a)_k}{k!}.
\]

Let $V=\operatorname{diag}(v_1,\ldots,v_n)$, where $v$ has density

\[
\frac{1}{Z_{a,n}}\Delta(v)^2\prod_{i=1}^n v_i^{a-1}
\]

on the simplex $v_i>0$, $\sum_i v_i=1$, and

\[
Z_{a,n}=
\frac{\prod_{j=1}^{n}\Gamma(j+1)\Gamma(a+j-1)}
     {\Gamma(\lambda)}.
\]

Let $U,W$ be independent normalized-Haar unitary matrices, independent of
$V$, and define

\[
T=\operatorname{diag}(t_1,\ldots,t_n),\qquad
X=\operatorname{diag}(x_1,\ldots,x_n),
\]

\[
Y=\operatorname{tr}(TUVU^*)+\operatorname{tr}(XWVW^*).
\]

Then

\[
\boxed{
K_{a,n}(s)
=c_{a,n}\Delta(t)\Delta(x)\mathbb E(s+Y)^{-\lambda}.
}
\]

Consequently,

\[
\boxed{\alpha_*(K_{a,n})=n(a+n-1).}
\]

The support of $Y$ is

\[
[t_1+x_1,t_n+x_n].
\]

For $n=1$, this is the singleton containing $t_1+x_1$.

### Proof

The Gamma-Laplace formula gives

\[
(s+t_i+x_j)^{-a}
=\frac1{\Gamma(a)}\int_0^\infty
 e^{-(s+t_i+x_j)u}u^{a-1}\,du.
\]

Andréief's identity therefore yields

\[
K_{a,n}(s)
=\frac1{n!\Gamma(a)^n}
\int_{(0,\infty)^n}
\det[e^{-t_i u_k}]\det[e^{-x_j u_k}]
e^{-s\sum_k u_k}\prod_k u_k^{a-1}\,du.
\tag{2.1}
\]

Set

\[
r=\sum_{k=1}^n u_k,\qquad u_k=rv_k.
\]

The simplex Jacobian is $r^{n-1}$. Let

\[
N=\frac{n(n-1)}2,\qquad C_n=\prod_{j=1}^{n-1}j!.
\]

The HCIZ formula, with the increasing-order convention for the Vandermonde,
is

\[
\det[e^{-rt_i v_j}]
=\frac{(-r)^N\Delta(t)\Delta(v)}{C_n}
\int_{U(n)}e^{-r\operatorname{tr}(TUVU^*)}\,dU.
\tag{2.2}
\]

Apply (2.2) to both determinants in (2.1). Their signs cancel. The power of
$r$ becomes

\[
n(a-1)+(n-1)+2N
=n(a+n-1)-1
=\lambda-1.
\]

It follows that

\[
\begin{aligned}
K_{a,n}(s)
&=\frac{\Delta(t)\Delta(x)}{n!\Gamma(a)^nC_n^2}
\int_{\sum v_i=1}\Delta(v)^2\prod_i v_i^{a-1}\\
&\quad\times
\mathbb E_{U,W}\int_0^\infty
r^{\lambda-1}e^{-r(s+Y)}\,dr\,dv.
\end{aligned}
\tag{2.3}
\]

The inner integral is $\Gamma(\lambda)(s+Y)^{-\lambda}$.

For completeness, the Laguerre normalization is

\[
\int_{(0,\infty)^n}e^{-\sum u_i}
\Delta(u)^2\prod_i u_i^{a-1}\,du
=n!\prod_{k=0}^{n-1}k!\Gamma(a+k).
\tag{2.4}
\]

To prove (2.4), apply Andréief to the monic Laguerre polynomials for the
weight $u^{a-1}e^{-u}$. Their squared norms are
$k!\Gamma(a+k)$. Radializing (2.4) gives the stated value of $Z_{a,n}$.
Finally,

\[
\frac{\Gamma(\lambda)Z_{a,n}}
{n!\Gamma(a)^nC_n^2}
=\prod_{k=0}^{n-1}\frac{(a)_k}{k!},
\]

which proves the representation.

Because $V$ is positive semidefinite and has trace one,

\[
t_1\le\operatorname{tr}(TUVU^*)\le t_n,
\]

and the analogous inequality holds for $X$. Thus $Y$ lies in the claimed
interval. The closure of the simplex support contains every rank-one spectrum.
Rank-one unitary orbits give every Rayleigh quotient in $[t_1,t_n]$, and the
two Haar matrices are independent. Every point of the sum interval therefore
belongs to the support.

The representation shows that $K_{a,n}\in\mathcal S_\lambda$, and dominated
convergence gives

\[
s^\lambda K_{a,n}(s)
\longrightarrow c_{a,n}\Delta(t)\Delta(x)>0.
\tag{2.5}
\]

Suppose $K_{a,n}\in\mathcal S_\beta$ for some $0<\beta<\lambda$. Since
$K_{a,n}(s)\to0$, the constant term in that representation must vanish. If
$\nu$ is its nonzero representing measure, monotone convergence gives

\[
s^\beta K_{a,n}(s)
=\int\left(\frac{s}{s+y}\right)^\beta\nu(dy)
\longrightarrow\nu([0,\infty))\in(0,\infty].
\]

Equation (2.5) instead implies $s^\beta K_{a,n}(s)\to0$. This contradiction
proves exactness. \(\square\)

## 3. Exact first and second moments

Define

\[
\tau_T=\operatorname{tr}(T^2)-\frac{(\operatorname{tr}T)^2}{n},
\qquad
\tau_X=\operatorname{tr}(X^2)-\frac{(\operatorname{tr}X)^2}{n}.
\]

### Proposition 3.1

The representing variable in Theorem 2.1 satisfies

\[
\mathbb EY=\frac{\operatorname{tr}T+\operatorname{tr}X}{n},
\]

and

\[
\boxed{
\operatorname{Var}Y
=\frac{\tau_T+\tau_X}{n(\lambda+1)}.
}
\]

### Proof

Normalized Haar averaging gives

\[
\mathbb E_U[UVU^*]=\frac{\operatorname{tr}V}{n}I=\frac1n I,
\]

which proves the mean formula.

For $n=1$, $V=(1)$ and the variance formula is immediate. Assume $n\ge2$.
For traceless Hermitian matrices $A_0,B_0$, Schur orthogonality gives

\[
\mathbb E_U
\left[\operatorname{tr}(A_0UB_0U^*)^2\right]
=\frac{\operatorname{tr}(A_0^2)\operatorname{tr}(B_0^2)}{n^2-1}.
\tag{3.1}
\]

Indeed, invariance makes the left-hand side a scalar multiple of
$\operatorname{tr}(A_0^2)$. Summing over an orthonormal basis of the real
Hilbert space of traceless Hermitian matrices shows that the scalar is
$\operatorname{tr}(B_0^2)/(n^2-1)$.

Conditioning on $V$, equation (3.1) shows that

\[
\operatorname{Var}
\left(\operatorname{tr}(TUVU^*)\mid V\right)
=\frac{\tau_T(\operatorname{tr}V^2-1/n)}{n^2-1}.
\tag{3.2}
\]

To compute the remaining expectation, return to the unconstrained Laguerre
variables $u_i=rv_i$. Integration by parts in

\[
\partial_{u_i}\left(
u_i^2e^{-\sum_k u_k}\Delta(u)^2\prod_k u_k^{a-1}
\right)
\]

is valid for every $a>0$. Summing over $i$, the pair terms simplify by

\[
2\sum_{i<j}\frac{u_i^2-u_j^2}{u_i-u_j}
=2(n-1)\sum_i u_i.
\]

Since $r$ is Gamma distributed with shape $\lambda$, this gives

\[
\mathbb E\sum_i u_i^2
=\lambda(a+2n-1),
\]

and hence

\[
\mathbb E\operatorname{tr}V^2
=\frac{a+2n-1}{\lambda+1}.
\]

Therefore

\[
\mathbb E\left(\operatorname{tr}V^2-\frac1n\right)
=\frac{n^2-1}{n(\lambda+1)}.
\]

The two orbital terms are conditionally independent, and their conditional
means do not depend on $V$. Taking expectations in (3.2) and adding the two
conditional variances proves the result. \(\square\)

## 4. Determinant bounds

Let

\[
L=t_1+x_1,\qquad U_0=t_n+x_n,
\qquad m=\frac{\operatorname{tr}T+\operatorname{tr}X}{n},
\]

and normalize

\[
H(s)=\frac{K_{a,n}(s)}{c_{a,n}\Delta(t)\Delta(x)}.
\]

For $n\ge2$, convexity of $y\mapsto(s+y)^{-\lambda}$ gives

\[
(s+m)^{-\lambda}
\le H(s)
\le
\frac{U_0-m}{U_0-L}(s+L)^{-\lambda}
+\frac{m-L}{U_0-L}(s+U_0)^{-\lambda}.
\tag{4.1}
\]

The two sides are the optimal bounds available from support and mean alone.
The lower estimate admits the variance refinement

\[
H(s)\ge
(s+m)^{-\lambda}
+\frac{\lambda(\tau_T+\tau_X)}{2n}
(s+U_0)^{-\lambda-2}.
\tag{4.2}
\]

Indeed, the second derivative of the integrand is at least

\[
\lambda(\lambda+1)(s+U_0)^{-\lambda-2}
\]

throughout the support. Taylor's theorem at the mean, followed by Proposition
3.1, proves (4.2).

## 5. Hausdorff constraints on the expansion

Assume $n\ge2$, let $d=U_0-L$, and put

\[
Z=\frac{Y-L}{d},\qquad \eta_k=\mathbb EZ^k.
\]

Write $(\Delta_f\eta)_k=\eta_{k+1}-\eta_k$ for the forward-difference
operator. Then $Z$ has full support $[0,1]$, and for $s+L>d$,

\[
(s+L)^\lambda H(s)
=\sum_{k=0}^\infty
(-1)^k\frac{(\lambda)_k}{k!}\eta_k
\left(\frac{d}{s+L}\right)^k.
\tag{5.1}
\]

The coefficient sequence is a strict Hausdorff moment sequence:

\[
(-1)^r\Delta_f^r\eta_k
=\mathbb E[Z^k(1-Z)^r]>0
\qquad(k,r\ge0).
\tag{5.2}
\]

Full support also makes every Hankel and interval-localizing moment matrix
positive definite. Thus the determinant's normalized asymptotic coefficients
satisfy an infinite family of strict finite-difference and determinant
inequalities.

## 6. Chebyshev-Markov determinants

Let $I\subset[0,\infty)$ be compact. Let $\mu$ be a finite positive measure
whose support contains at least $n$ points. Suppose continuous functions
$\phi_1,\ldots,\phi_n$ form a strict oriented Chebyshev system on that
support:

\[
\det[\phi_i(y_j)]_{i,j=1}^{n}>0
\quad\text{for }y_1<\cdots<y_n.
\tag{6.1}
\]

Define

\[
m_i(s;t)=\int_I\phi_i(y)(s+t+y)^{-a}\,\mu(dy).
\]

### Theorem 6.1

For $t_1<\cdots<t_n$ with $t_1+\min I\ge0$,

\[
D(s)=\det[m_i(s;t_j)]_{i,j=1}^{n}
\]

has exact generalized Stieltjes order $\lambda=n(a+n-1)$. For every fixed
$t+\min I\ge0$, the confluent Wronskian

\[
W(s)=\det\left[
\frac{\partial_s^{j-1}m_i(s;t)}{(j-1)!}
\right]_{i,j=1}^{n}
\]

has the same exact order.

### Proof

Andréief's identity gives

\[
D(s)=\frac1{n!}\int_{I^n}
\det[\phi_i(y_k)]
\det[(s+t_j+y_k)^{-a}]
\,\mu^{\otimes n}(dy).
\tag{6.2}
\]

The product of determinants is symmetric and nonnegative. On strictly ordered
tuples it is positive. Applying Theorem 2.1 to the second determinant in
(6.2) produces a finite, nonzero positive mixture of order-$\lambda$
Stieltjes kernels. Moreover,

\[
\lim_{s\to\infty}s^\lambda D(s)
=\frac{c_{a,n}\Delta(t)}{n!}
\int_{I^n}\det[\phi_i(y_k)]\Delta(y)
\,\mu^{\otimes n}(dy)>0.
\tag{6.3}
\]

The exactness argument from Theorem 2.1 applies.

Divide (6.2) by $\Delta(t)$ and let $t_j\to t$. Compactness permits passage
to the limit, and the standard confluent alternant formula gives $W(s)$.
More explicitly, if $Y_y=\operatorname{diag}(y_1,\ldots,y_n)$, then

\[
W(s)=\frac{c_{a,n}}{n!}\int_{I^n}
\det[\phi_i(y_k)]\Delta(y)
\mathbb E_{V,Q}\left(s+t+\operatorname{tr}(Y_yQVQ^*)\right)^{-\lambda}
\,\mu^{\otimes n}(dy),
\tag{6.4}
\]

where $Q$ is normalized-Haar unitary and independent of $V$. The weight
$\det[\phi_i(y_k)]\Delta(y)$ is symmetric and nonnegative, and its integral
is finite and strictly positive. Thus (6.4) is a finite, nonzero positive
mixture of order-$\lambda$ Stieltjes kernels. Its leading mass is the positive
quantity in (6.3) after removing $\Delta(t)$, so the exactness argument from
Theorem 2.1 applies. \(\square\)

## 7. Independent checks

### The one-dimensional case

For $n=1$, $V=(1)$, $c_{a,1}=1$, and

\[
K_{a,1}(s)=(s+t_1+x_1)^{-a}.
\]

### Cauchy's formula at $a=1$

The classical Cauchy determinant gives

\[
\frac{K_{1,n}(s)}{\Delta(t)\Delta(x)}
=\prod_{i,j=1}^{n}(s+t_i+x_j)^{-1}.
\]

The uniform Dirichlet identity on $n^2$ coordinates represents the product
as an order-$n^2$ generalized Stieltjes transform. This agrees with
$\lambda=n^2$ and, by uniqueness, identifies a second construction of the
law of $Y$ in this special case.

### Double-alternant asymptotics

Expanding the kernel at infinity and applying the confluent double-alternant
formula gives

\[
\lim_{s\to\infty}
\frac{s^\lambda K_{a,n}(s)}{\Delta(t)\Delta(x)}
=\det\left[\frac{(a)_{p+q}}{p!q!}\right]_{p,q=0}^{n-1}.
\]

The Gamma-moment determinant

\[
\det[(a)_{p+q}]_{p,q=0}^{n-1}
=\prod_{k=0}^{n-1}k!(a)_k
\]

reduces the right-hand side to $c_{a,n}$. This derivation does not use HCIZ
and independently confirms the exponent and normalization.

### Double confluence

Letting both spectra coalesce after division by their Vandermonde factors
gives

\[
\lim_{t_i\to t,\ x_i\to x}
\frac{K_{a,n}(s)}{\Delta(t)\Delta(x)}
=c_{a,n}(s+t+x)^{-\lambda}.
\]

This agrees with the known Wronskian evaluation for a Gamma-Laplace kernel.

## 8. Scope of the contribution

Classical work already covers total positivity and sign regularity of
power-Cauchy kernels, determinant constructions that preserve the Laplace
transform property, and complete monotonicity of Laplace-transform
Wronskians. The contribution asserted here is the explicit compact orbital
representing law, its minimal Stieltjes order, the exact support and two
moments, and the extension of that exact-order result to nonconfluent
Chebyshev-Markov determinants.

The literature comparison remains provisional until the full-text checks in
`literature_audit.md` are complete.
