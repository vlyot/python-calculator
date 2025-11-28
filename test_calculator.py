import pytest
from calculator import add, subtract, multiply, divide, power


@pytest.mark.basic_operations
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


@pytest.mark.basic_operations
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-3, -2) == -1


@pytest.mark.basic_operations
def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0


@pytest.mark.edge_cases
def test_divide():
    assert divide(8, 2) == 4
    assert divide(9, 3) == 3
    assert divide(-10, 2) == -5


@pytest.mark.edge_cases
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


@pytest.mark.performance
def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(4, 0.5) == 2
