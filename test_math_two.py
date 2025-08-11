from itertools import product

import pytest

products = [
    (1, 2, 2),
    (2, 3, 6),
    (10, 5, 50),
    (10, 55, 156.3),
    (188, 5, 550),
]

@pytest.mark.parametrize('a, b, result', products)
def test_multiplication(a, b, result):
    assert a * b == result
