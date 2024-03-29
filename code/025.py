"""
David Pratt
for SIAM Fall 2019

========================= PROJECT EULER #25 ============================

The Fibonacci sequence is defined by the recurrence relation:

    F[n] = F[n[1]] + F[n[2]], where F[1] = 1 and F[2] = 1.

Hence the first 12 terms will be:

    F[1]  =   1
    F[2]  =   1
    F[3]  =   2
    F[4]  =   3
    F[5]  =   5
    F[6]  =   8
    F[7]  =  13
    F[8]  =  21
    F[9]  =  34
    F[10] =  55
    F[11] =  89
    F[12] = 144

The 12th term, F[12], is the first term to contain three digits. What is
the first term in the Fibonacci sequence to contain 1000 digits?

========================================================================

The strategy is to use the generator function from Problem 2. We should
be careful to note the indices, though.

"""

from math import log10, floor


def fib():
    """
    Generates all Fibonacci numbers. Note here that the 0th index
    Fibonacci number is 1, the 1st index is 2, etc.

    Example:
        >>> for i, f in enumerate(fib()):
                print(i, f)
                if i > 4: break
        0 1
        1 2
        2 3
        3 5
        4 8
        5 13
    """
    # Use simultaneous assignment
    small_fib, big_fib = 1, 1
    while True:
        small_fib, big_fib = big_fib, small_fib + big_fib
        yield small_fib


def digits(n):
    """
    Calculates the number of digits in a non-negative integer n.

    Example:
        >>> digits(128)
        3
    """
    return 1 + floor(log10(n)) if n != 0 else 1


def main():
    DIGITS = 1000
    # Use the start= parameter of enumerate to match the indices given
    # in the problem statement to the indices of our generator function.
    for i, f in enumerate(fib(), start=2):
        if digits(f) >= DIGITS:
            return i


if __name__ == '__main__':
    # runtime ~ 2.28 ms
    ans = main()
    print(ans)