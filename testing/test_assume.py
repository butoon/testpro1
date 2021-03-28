import pytest

def test_a():
    pytest.assume(1 == 1)
    pytest.assume(1 == 2)
    pytest.assume(True == False)
    pytest.assume(2 == 2)