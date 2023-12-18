from enum import Enum
from collections import deque


class Action(Enum):
    SUM = 1
    SUBTRACT = 2
    MULTIPLY = 3
    CALLBACK = 4
    UNDO = 5
    REDO = 6


class Calculator:
    def __init__(self, initial_value):
        self.value = initial_value
        self.history_undo = deque()
        self.history_redo = deque()

    def get_value(self):
        return self.value

    def calculate(self, event, value):
        if not isinstance(event, Action):
            raise ValueError("Invalid action type")

        if event in {Action.SUM, Action.SUBTRACT, Action.MULTIPLY, Action.CALLBACK}:
            # Save the current state for undo
            self.history_undo.append(self.value)

            if event == Action.SUM:
                self.value += value
            elif event == Action.SUBTRACT:
                self.value -= value
            elif event == Action.MULTIPLY:
                self.value *= value
            elif event == Action.CALLBACK:
                if callable(value):
                    self.value = value(self.value)
                else:
                    raise ValueError("Invalid callback")

            # Clear redo history upon new action
            self.history_redo.clear()

        elif event == Action.UNDO:
            if self.history_undo:
                # Save the current state for redo
                self.history_redo.append(self.value)
                self.value = self.history_undo.pop()

        elif event == Action.REDO:
            if self.history_redo:
                # Save the current state for undo
                self.history_undo.append(self.value)
                self.value = self.history_redo.pop()
