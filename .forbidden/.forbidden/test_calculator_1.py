from calculator.calculator import Calculator, Action


# Test to verify the initial value set in the calculator
def test_initial_value():
    # Create a calculator instance with an initial value of 5
    calc = Calculator(5)
    # Assert that the value retrieved from the calculator matches the initial value set
    assert calc.get_value() == 5


# Test to validate the addition operation in the calculator
def test_calculate_sum():
    # Create a calculator instance with an initial value of 3
    calc = Calculator(3)
    # Perform a summation operation of adding 1 to the current value
    calc.calculate(Action.SUM, 1)
    # Assert that the value retrieved from the calculator is the result of the addition
    assert calc.get_value() == 4


# Test to validate the subtraction operation in the calculator
def test_calculate_subtract():
    # Create a calculator instance with an initial value of 4
    calc = Calculator(4)
    # Perform a subtraction operation of subtracting 2 from the current value
    calc.calculate(Action.SUBTRACT, 2)
    # Assert that the value retrieved from the calculator is the result of the subtraction
    assert calc.get_value() == 2


# Test to validate the multiplication operation in the calculator
def test_calculate_multiply():
    # Create a calculator instance with an initial value of 3
    calc = Calculator(3)
    # Perform a multiplication operation of multiplying the current value by 2
    calc.calculate(Action.MULTIPLY, 2)
    # Assert that the value retrieved from the calculator is the result of the multiplication
    assert calc.get_value() == 6
