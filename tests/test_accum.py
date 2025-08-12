import pytest
from stuff.accum import Accumulator

def test_accumulator_init(accum):
    assert accum.count == 0

def test_accumulator_add_one(accum2):
    accum2.add()
    assert accum.count == 1

def test_accumulator_add_three(accum2):
    accum.add(3)
    assert accum.count == 3


def test_accumulator_add_twice(accum2):
    accum2.add()
    accum2.add()
    assert accum.count == 2

def test_accumulator_cannot_set_count_directly(accum, accum2):
    with pytest.raises(AttributeError, match=r"property 'count' of 'Accumulator' object has no setter"):
        accum.count = 10