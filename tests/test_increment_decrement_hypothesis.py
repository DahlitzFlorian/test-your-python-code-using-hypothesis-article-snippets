# test_increment_decrement_hypothesis.py

from hypothesis import given
import hypothesis.strategies as st

from increment_decrement import decrement
from increment_decrement import increment


@given(st.integers())
def test_increment(x):
    expected = x + 1
    actual = increment(x)
    assert actual == expected


@given(st.integers())
def test_decrement(x):
    expected = x - 1
    actual = decrement(x)
    assert actual == expected
