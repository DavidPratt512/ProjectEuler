"""
David Pratt
for SIAM Fall 2019

========================= PROJECT EULER #01 ============================

If we list all the natural numbers below 10 that are multiples of 3 or
5, we get 3, 5, 6, and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

========================================================================

The strategy is to think about the problem mathematically before we
implement a solution. Really the problem amounts to the sum

    S = 3 + 5 + 6 + 9 + 10 + 12 + 15 + ...

which can be written as

    S = 3(1 + ... + 333) + 5(1 + ... + 199) - 15(1 + ... + 66)
      = 3(333)(334)/2    + 5(199)(200)/2    - 15(66)(67)/2.

"""

def mult_sum(n, m=1):
    """
    Calculates the sum of multiples of m less than n. The parameter m 
    defaults to 1, so you can find the sum of all numbers less than n if
    you so desired.

    Example:
        >>> mult_sum(10, 3)
        18
        >>> mult_sum(10)
        45
    """
    n = n - 1
    n_div_m = n // m

    return m * n_div_m * (n_div_m + 1) // 2


def main():
    return mult_sum(1000, 3) + mult_sum(1000, 5) - mult_sum(1000, 15)


if __name__ == '__main__':
    # runtime ~ 666 ns
    ans = main()
    print(ans)