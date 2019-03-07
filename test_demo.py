import pytest


def test_dd():
    # assert (1==4)
    # assert (2==4)
    pytest.assume(1==4)
    pytest.assume(2==4)

