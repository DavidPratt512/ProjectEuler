"""
David Pratt
for SIAM Fall 2019

========================= PROJECT EULER #10 ============================

The sum of primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all
the primes below two million.

========================================================================

The strategy is to sieve for all of the primes below two million, then
simply sum them.

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
    LIMIT = int(2e6)
    return sum(Sieve(LIMIT).primes())


if __name__ == '__main__':
    # runtime ~ 960 ms
    ans = main()
    print(ans)
