"""
David Pratt
for SIAM Fall 2019

========================= PROJECT EULER #35 ============================

The number 197 is called a circular prime because all rotations of the
digits: 197, 971, and 719 are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31,
37, 71, 73, 79, and 97.

How many circular primes are there below one million?

========================================================================

The strategy is to generate all candidates for circular primes without
having to iterate over all the numbers from 1 to 1 million. Since prime
numbers cannot end in an even digit or the digit 5, circular primes can
not contain these numbers. This fact will help us generate all possible
candidates below 1 million.

"""

from math import floor, log10, sqrt
from itertools import product


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


def tuple_to_int(t):
    """
    Converts a tuple of integers to an integer.

    Example:
        >>> tuple_to_int( (2, 7, 1, 8) )
        2718
    """
    return sum(digit * pow(10, p) for p, digit in enumerate(reversed(t)))


def rotate(n):
    """
    Returns a single back-to-front rotation of n.

    Example:
        >>> rotate(197)
        719
    """
    head, tail = divmod(n, 10)
    return tail * pow(10, digits(head)) + head


def rotations(n):
    """
    Generates all unique rotations of a number n.

    Example:
        >>> list(rotations(197))
        [197, 719, 971]
    """
    for _ in range(digits(n)):
        yield n
        n = rotate(n)


def circular_primes_range(p):
    """
    Calculates all circular primes less than a given power of 10.
    Returns a set of all such primes.

    Example:
        >>> circular_primes_range(6)
        {2, 3, 5, ..., 999331}
    """
    # Circular primes cannot contain even numbers or the digit 5, so the
    # only digits allowable in a circular prime are:
    DIGITS = [1, 3, 7, 9]

    # We make an exception for the single digit circular primes, 2 and 5
    # It is also imperative we use a set to store circular primes due to
    # the fact that we will be performing lookups repeatedly.
    circular_primes = {2, 5}

    # We look for circular primes less than 10**p, meaning numbers with
    # a digit count of 1 through p (inclusive).
    for num_digits in range(1, p + 1):
        # The product() function is an implementation of the Cartesian
        # Product. In our case, it will produce...
        #
        # product(DIGITS, repeat=1) -> (1,),      (3,),      ...
        # product(DIGITS, repeat=2) -> (1, 1),    (1, 3),    ...
        # product(DIGITS, repeat=3) -> (1, 1, 1), (1, 1, 3), ...
        # ... and so on ...
        #
        # Since product() produces tuples, we map each of the tuples to
        # an integer by using the map function.
        nums = map(tuple_to_int, product(DIGITS, repeat=num_digits))

        for n in nums:
            # If n has not already been found to be a circular prime
            # and is prime itself...
            if n not in circular_primes and isprime(n):
                # Collect the rotations of n in a set rots. If all of
                # the rotations are prime, add them all to the set of
                # circular primes.
                rots = set(rotations(n))
                if all(map(isprime, rots)):
                    circular_primes.update(rots)

    return circular_primes


def main():
    return len(circular_primes_range(6))


if __name__ == '__main__':
    # runtime ~ 48.1 ms
    ans = main()
    print(ans)
