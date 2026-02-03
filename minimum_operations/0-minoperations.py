#!/usr/bin/python3
"""
Module for calculating minimum operations to achieve n characters.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly
    n 'H' characters in a file.

    Starting with a single 'H', the only operations available are:
    - Copy All: Copy all characters in the file
    - Paste: Paste the previously copied characters

    The solution uses prime factorization. The minimum number of operations
    equals the sum of all prime factors of n.

    Args:
        n (int): Target number of 'H' characters

    Returns:
        int: Minimum number of operations needed, or 0 if impossible

    Algorithm:
        1. If n <= 1, return 0 (impossible or already achieved)
        2. Find all prime factors of n
        3. Sum the prime factors to get minimum operations

    Example:
        >>> minOperations(4)
        4
        >>> minOperations(12)
        7
        >>> minOperations(9)
        6

    Explanation for n=12:
        12 = 2 × 2 × 3
        Operations: 2 + 2 + 3 = 7
        H -> HH (Copy All + Paste = 2 ops)
        HH -> HHHH (Copy All + Paste = 2 ops)
        HHHH -> HHHHHHHHHHHH (Copy All + Paste + Paste = 3 ops)
    """
    if n <= 1:
        return 0
    ops, d = 0, 2
    while n > 1:
        while n % d == 0:
            ops, n = ops + d, n // d
        d += 1
    return ops
