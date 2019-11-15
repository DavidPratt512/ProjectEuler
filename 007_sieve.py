"""
David Pratt
for SIAM Fall 2019

========================= PROJECT EULER #07 ============================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13.

What is the 10 001st prime number?

========================================================================

The strategy is to use the prime number theorem to obtain an upper bound
for the 10 001st prime number, create a Sieve of Eratosthenes, and count
primes until we have 10 001 prime numbers.

See the Stack Overflow disccusion on Sieve generation here: 

    https://bit.ly/2Qb7WA3

or this Wikipedia article:

    https://bit.ly/2qKFomk

"""

from math import sqrt, floor, log


class Sieve():
    """
    Implementation of the Sieve of Eratosthenes. See the Wikipedia
    article on the Sieve here:

        https://bit.ly/33Dxl9F
    """
    def __init__(self, maxint):
        self.maxint = maxint
        self.sieve = dict.fromkeys(range(maxint+1), True)
        self._make_sieve()

    def _make_sieve(self):
        self.sieve[0] = self.sieve[1] = False

        for i in range(2, 2 + floor(sqrt(self.maxint))):
            # if i is prime
            if self.sieve[i]:
                # start at i**2, go to maxint, step by i
                for j in range(i**2, self.maxint+1, i):
                    self.sieve[j] = False

    def isprime(self, n):
        return self.sieve.get(n)

    def primes(self):
        return filter(self.sieve.get, self.sieve)

    def __repr__(self):
        return f'Sieve({self.maxint})'


def main():
    PRIME = 10_001

    # Upper bound obtained from the Wikipedia article mentioned in the
    # preamble. In it, we find the inequality
    #
    #     p_n < n (log n + log log n)
    #
    # for n >= 6.
    UPPER_BOUND = round(PRIME * (log(PRIME) + log(log(PRIME))))
    
    primes = Sieve(UPPER_BOUND).primes()

    for _ in range(PRIME):
        p = next(primes)
    return p


if __name__ == '__main__':
    # runtime ~ 35 ms
    ans = main()
    print(ans)