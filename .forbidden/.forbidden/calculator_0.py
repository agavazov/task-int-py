from enum import Enum


class Action(Enum):
    SUM = 1
    SUBTRACT = 2
    MULTIPLY = 3


class Calculator:
    def __init__(self, initial_value):
        self.value = initial_value

    def get_value(self):
        return self.value

    def calculate(self, event, value):
        """ @todo write the body """
