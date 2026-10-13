import math

import pytest

from simple_functions import my_sum
from simple_functions import factorial
from simple_functions import sin


class TestSimpleFunctions:
    """Tests for the functions in functions1.py."""

    @pytest.mark.parametrize('iterable, expected', [
        ([8, 7, 5], 20),
        ((10, -2, 5, -10, 1), 4),
    ])
    def test_my_sum(self, iterable, expected):
        """my_sum adds up the items of lists and tuples."""
        assert my_sum(iterable) == expected

    @pytest.mark.parametrize('number, expected', [
        (5, 120),
        (3, 6),
        (1, 1),
        (0, 1),
    ])
    def test_factorial(self, number, expected):
        """factorial returns the factorial of a number."""
        assert factorial(number) == expected

    @pytest.mark.parametrize('number, expected', [
        (0, 0),
        (3.14159, 2.65358979335273e-06),
        (1.5708, 0.9999999999932537),
        (-1, -math.sin(1)),
    ])
    def test_sin(self, number, expected):
        """sin returns the sine of a number in radians."""
        assert sin(number) == pytest.approx(expected, abs=1e-6)
