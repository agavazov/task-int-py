from enum import Enum
from collections import deque
from typing import Union, Callable


class Action(Enum):
    SUM = 1
    SUBTRACT = 2
    MULTIPLY = 3
    CALLBACK = 4
    UNDO = 5
    REDO = 6


class Calculator:
    def __init__(self, initial_value: Union[int, float]):
        self.value: Union[int, float] = initial_value
        self.history_undo: deque = deque()
        self.history_redo: deque = deque()

    def get_value(self) -> Union[int, float]:
        return self.value

    def calculate(self, event: Action,
                  value: Union[None, int, float, Callable[[Union[int, float]], Union[int, float]]]) -> None:
        if not isinstance(event, Action):
            raise ValueError("Invalid event type")

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
