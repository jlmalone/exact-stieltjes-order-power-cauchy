#!/usr/bin/env python3
"""Exact-arithmetic transcription checks for the research note.

These checks support falsification and normalization review. The proofs in the
manuscript remain authoritative.
"""

from fractions import Fraction
from math import factorial


def rising(a: int, k: int) -> int:
    value = 1
    for offset in range(k):
        value *= a + offset
    return value


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    """Fraction-free Bareiss determinant."""

    size = len(matrix)
    if size == 0:
        return Fraction(1)

    work = [[Fraction(entry) for entry in row] for row in matrix]
    sign = 1
    previous_pivot = Fraction(1)

    for pivot_index in range(size - 1):
        pivot_row = next(
            (row for row in range(pivot_index, size) if work[row][pivot_index]),
            None,
        )
        if pivot_row is None:
            return Fraction(0)
        if pivot_row != pivot_index:
            work[pivot_index], work[pivot_row] = work[pivot_row], work[pivot_index]
            sign *= -1

        pivot = work[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = (
                    work[row][column] * pivot
                    - work[row][pivot_index] * work[pivot_index][column]
                )
                work[row][column] = numerator / previous_pivot
        previous_pivot = pivot

    return Fraction(sign) * work[-1][-1]


def vandermonde(values: tuple[int, ...]) -> int:
    product = 1
    for left in range(len(values)):
        for right in range(left + 1, len(values)):
            product *= values[right] - values[left]
    return product


def kernel_minor(
    s: int, a: int, t: tuple[int, ...], x: tuple[int, ...]
) -> Fraction:
    matrix = [
        [Fraction(1, (s + row_shift + column_shift) ** a) for column_shift in x]
        for row_shift in t
    ]
    return determinant(matrix)


def leading_constant(a: int, n: int) -> Fraction:
    result = Fraction(1)
    for k in range(n):
        result *= Fraction(rising(a, k), factorial(k))
    return result


def check_gamma_hankel() -> None:
    for a in range(1, 7):
        for n in range(1, 7):
            matrix = [
                [Fraction(rising(a, row + column)) for column in range(n)]
                for row in range(n)
            ]
            expected = 1
            for k in range(n):
                expected *= factorial(k) * rising(a, k)
            assert determinant(matrix) == expected


def check_cauchy_case() -> None:
    cases = [
        (3, (0,), (2,)),
        (5, (0, 2), (1, 4)),
        (7, (0, 1, 4), (2, 5, 9)),
        (11, (-2, 1, 6), (3, 7, 10)),
    ]
    for s, t, x in cases:
        minor = kernel_minor(s, 1, t, x)
        denominator = 1
        for row_shift in t:
            for column_shift in x:
                denominator *= s + row_shift + column_shift
        expected = Fraction(vandermonde(t) * vandermonde(x), denominator)
        assert minor == expected


def check_large_shift_coefficient() -> None:
    cases = [
        (2, (0, 2), (1, 4)),
        (3, (0, 1, 4), (2, 5, 9)),
        (1, (-2, 1, 6), (3, 7, 10)),
    ]
    s = 1_000_000
    for a, t, x in cases:
        n = len(t)
        lam = n * (a + n - 1)
        scaled = (
            kernel_minor(s, a, t, x)
            * (s**lam)
            / (vandermonde(t) * vandermonde(x))
        )
        expected = leading_constant(a, n)
        relative_error = abs(scaled - expected) / expected
        assert relative_error < Fraction(1, 1_000)


def spectral_variance(values: tuple[int, ...]) -> Fraction:
    n = len(values)
    total = sum(values)
    return Fraction(sum(value * value for value in values)) - Fraction(total * total, n)


def dirichlet_linear_variance(coefficients: tuple[int, ...]) -> Fraction:
    dimension = len(coefficients)
    total = sum(coefficients)
    square_total = sum(value * value for value in coefficients)
    numerator = dimension * square_total - total * total
    return Fraction(numerator, dimension * dimension * (dimension + 1))


def check_a_one_variance() -> None:
    cases = [
        ((0, 1), (0, 1)),
        ((-2, 1, 6), (3, 7, 10)),
        ((0, 2, 5, 9), (1, 3, 4, 8)),
    ]
    for t, x in cases:
        n = len(t)
        coefficients = tuple(row + column for row in t for column in x)
        dirichlet_variance = dirichlet_linear_variance(coefficients)
        orbital_formula = Fraction(
            spectral_variance(t) + spectral_variance(x),
            n * (n * n + 1),
        )
        assert dirichlet_variance == orbital_formula


def main() -> None:
    check_gamma_hankel()
    check_cauchy_case()
    check_large_shift_coefficient()
    check_a_one_variance()
    print("exact arithmetic checks passed")


if __name__ == "__main__":
    main()
