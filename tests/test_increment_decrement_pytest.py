# test_increment_decrement_pytest.py
from increment_decrement import decrement
from increment_decrement import increment


def test_increment():
    x = 5
    expected = 6
    actual = increment(x)
    assert actual == expected


def test_decrement():
    x = 5
    expected = 4
    actual = decrement(x)
    assert actual == expected
