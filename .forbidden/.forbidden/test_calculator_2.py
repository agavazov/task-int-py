import pytest
from calculator.calculator import Calculator, Action


def square_callback(value: int) -> int:
    return value ** 2


# Test to verify error handling for an invalid action
def test_calculate_invalid_action():
    # Create a calculator instance with an initial value of 3
    calc = Calculator(3)
    # Verify that attempting an invalid action raises a ValueError
    with pytest.raises(ValueError):
        calc.calculate("INVALID_ACTION", 2)


# Test to validate the callback functionality in the calculator
def test_calculate_callback():
    # Create a calculator instance with an initial value of 4
    calc = Calculator(4)
    # Perform a callback action using the square_callback function
    calc.calculate(Action.CALLBACK, square_callback)
    # Assert that the value retrieved from the calculator reflects the result of the callback operation
    assert calc.get_value() == 16
