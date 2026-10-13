from functools import cache

__all__ = ['my_sum', 'factorial', 'sin']


def my_sum(iterable):
    """Return the sum of the items in iterable."""
    tot = 0
    for i in iterable:
        tot += i
    return tot


@cache
def factorial(n):
    """Return the factorial of num."""
    return n * factorial(n - 1) if n else 1


def sin(x, terms=10):
    """Return the sine of x (in radians), via its Taylor series."""
    return my_sum((-1)**n * x**(2*n + 1) / factorial(2*n + 1)
                  for n in range(terms))
