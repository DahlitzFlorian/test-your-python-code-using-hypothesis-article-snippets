# test_div.py

from hypothesis import example
from hypothesis import given
import hypothesis.strategies as st

from div import div


@given(dividend=st.integers(), divisor=st.integers())
@example(1, 0)
def test_div(dividend, divisor):
    if divisor == 0:
        expected = -1
    else:
        expected = dividend // divisor
    actual = div(dividend, divisor)
    assert actual == expected
