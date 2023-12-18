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
        if event == Action.SUM:
            self.value += value
        elif event == Action.SUBTRACT:
            self.value -= value
        elif event == Action.MULTIPLY:
            self.value *= value
