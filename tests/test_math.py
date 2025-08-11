import pytest

# doing  a simple test to check if 1 + 1 equals 2 - passed scenario
def test_one_plus_one():
    assert 1 + 1 == 2, "1 + 1 should equal 2"

# doing a simples test to check if 1 + 2 equals 3 - failed scenario
def test_one_plus_two():
    a = 1
    b = 2
    c = 0
    assert a + b == c

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0  # This should raise a ZeroDivisionError
    assert 'division by zero' in str (e.value)