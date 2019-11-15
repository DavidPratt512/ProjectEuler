"""
David Pratt
for SIAM Fall 2019

========================= PROJECT EULER #07 ============================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13.

What is the 10 001st prime number?

========================================================================

The strategy is to implement a somewhat efficient elementary primality
test, then iterate to find the 10 001st prime number.

"""

from math import sqrt


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


def main():
    PRIME = 10_001

    # Include 2 and 3 in the initial count
    count = 2
    n = 6

    # Use the fact that primes are adjacent to multiples of 6.
    # Frankly, the code in this loop is close to repeating itself, and
    # could probably be cleaned up.
    while count != PRIME:
        count += isprime(n - 1)
        if count == PRIME:
            return n - 1

        count += isprime(n + 1)
        if count == PRIME:
            return n + 1

        n += 6


if __name__ == '__main__':
    # runtime ~ 75 ms
    ans = main()
    print(ans)