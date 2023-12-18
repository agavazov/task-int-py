from calculator.calculator import Calculator, Action


# Test undo functionality for addition operations
def test_undo_sum():
    calc = Calculator(5)
    calc.calculate(Action.SUM, 3)
    calc.calculate(Action.SUM, 4)

    calc.calculate(Action.UNDO, None)
    assert calc.get_value() == 8


# Test undo and redo functionality for addition operations
def test_undo_redo_sum():
    calc = Calculator(5)
    calc.calculate(Action.SUM, 3)
    calc.calculate(Action.SUM, 4)

    calc.calculate(Action.UNDO, None)
    calc.calculate(Action.REDO, None)
    assert calc.get_value() == 12


# Test undo functionality for subtraction operations
def test_undo_subtract():
    calc = Calculator(10)
    calc.calculate(Action.SUBTRACT, 4)
    calc.calculate(Action.SUBTRACT, 3)

    calc.calculate(Action.UNDO, None)
    assert calc.get_value() == 6


# Test undo and redo functionality for subtraction operations
def test_undo_redo_subtract():
    calc = Calculator(12)
    calc.calculate(Action.SUBTRACT, 1)
    calc.calculate(Action.SUBTRACT, 2)

    calc.calculate(Action.UNDO, None)
    calc.calculate(Action.REDO, None)
    assert calc.get_value() == 9


# Test undo functionality for multiplication operations
def test_undo_multiply():
    calc = Calculator(10)
    calc.calculate(Action.MULTIPLY, 2)

    calc.calculate(Action.UNDO, None)
    assert calc.get_value() == 10


# Test undo and redo functionality for multiplication operations
def test_undo_redo_multiply():
    calc = Calculator(10)
    calc.calculate(Action.MULTIPLY, 2)
    calc.calculate(Action.MULTIPLY, 3)

    calc.calculate(Action.UNDO, None)
    calc.calculate(Action.REDO, None)
    assert calc.get_value() == 60


# Test undo functionality for callback operations
def test_undo_callback():
    calc = Calculator(4)
    calc.calculate(Action.CALLBACK, lambda x: x ** 2)

    calc.calculate(Action.UNDO, None)
    assert calc.get_value() == 4


# Test undo and redo functionality for callback operations
def test_undo_redo_callback():
    calc = Calculator(4)
    calc.calculate(Action.CALLBACK, lambda x: x ** 2)

    calc.calculate(Action.UNDO, None)
    calc.calculate(Action.REDO, None)
    assert calc.get_value() == 16
