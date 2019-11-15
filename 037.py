"""
David Pratt
for SIAM Fall 2019

========================= PROJECT EULER #37 ============================

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from
left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

========================================================================

The strategy is to generate all right truncatable primes and filter for
the left truncatable primes. We do this because there are only 80 or so
right truncatable primes, while there are thousands of left truncatable
primes.

"""

from math import floor, log10, sqrt


def isprime(n):
    """
    Tests an integer n for primality using trial division and the fact
    that prime numbers are congruent to 1, or -1 modulo 6. An initial
    check for divisibility by 2 or 3 is performed.

    Example:
        >>> isprime(100)
        False
        >>> isprime(101)
        True
    """
    if n <= 1:
        return False

    for k in (2, 3):
        if n % k == 0 and n != k:
            return False

    for i in range(6, 2 + int(sqrt(n)), 6):
        if n % (i - 1) == 0 or n % (i + 1) == 0:
            return False
    return True


def digits(n):
    """
    Calculates the number of digits in a non-negative integer n.

    Example:
        >>> digits(128)
        3
    """
    return 1 + floor(log10(n)) if n != 0 else 1


def truncate_left(n):
    """
    Returns a single left truncation of n.

    Example:
        >>> truncate_left(9137)
        137
    """
    return n % pow(10, digits(n) - 1)


def left_truncates(n):
    """
    Generates all left truncates of an integer n.

    Example:
        >>> list(left_truncates(9137))
        [9137, 137, 37, 7]
    """
    for _ in range(digits(n)):
        yield n
        n = truncate_left(n)


def is_left_truncatable(n):
    """
    Determines whether n is a left truncatable prime number.

    Example:
        >>> is_left_truncatable(9137)
        True
    """
    return all(map(isprime, left_truncates(n)))


def right_truncatable_primes():
    """
    Generates all right truncatable prime numbers.
    Assumes that single-digit primes are not truncatable.
    """

    # Prime numbers with more than one digit can only end in a 1, 3, 7,
    # or 9.
    DIGITS = [1, 3, 7, 9]

    # Begin initialy with the single digit prime numbers. From these we
    # can construct all right truncatable primes.
    truncatable_primes = [2, 3, 5, 7]

    # while the truncatable_primes stack is non-empty:
    while truncatable_primes:
        prime = truncatable_primes.pop()
        for d in DIGITS:
            # A possible right truncatable prime is any right 
            # truncatable prime concatenated with a digit 1, 3, 7, or 9
            candidate = 10 * prime + d

            # If the candidate is prime, then it is a right truncatable
            # prime, so we add it to the truncatable_primes stack and
            # yield it.
            if isprime(candidate):
                truncatable_primes.append(candidate)
                yield candidate


def main():
    return sum(filter(is_left_truncatable, right_truncatable_primes()))


if __name__ == '__main__':
    # runtime ~ 3.9 ms
    ans = main()
    print(ans)
