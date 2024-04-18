import unittest


class ClickerWithInitialValue:
    def __init__(self, value: int):
        self.value = value
    
    def click(self) -> None:
        self.value = self.value + 1
    
    def reset(self) -> None:
        self.value = 0
    
    def get_value(self) -> int:
        return self.value


class ClickerUser:
    def __init__(self, clicker: ClickerWithInitialValue):
        self.clicker = clicker
    
    def click_5_times(self) -> int:
        self.clicker.click()
        self.clicker.click()
        self.clicker.click()
        self.clicker.click()
        self.clicker.click()


class TestClickerWithInitialValue(unittest.TestCase):
    def test_clicker_1(self):
        # AAA: Arrange, Act, Assert

        # Arrange
        clicker = ClickerWithInitialValue(0)

        # Act
        clicker.click()
        clicker.click()

        # Assert
        self.assertEqual(2, clicker.get_value())


class TestClickerUser(unittest.TestCase):
    def test_clicker_user_1(self):
        clicker = ClickerWithInitialValue(0)
        clicker_user = ClickerUser(clicker)

        clicker_user.click_5_times()

        self.assertEqual(5, clicker.get_value())

# ---
        
from typing import List, Callable

def to_upper(value: str):
    return value.upper()

def apply(f: Callable, data: List):
    result = []
    for elem in data:
        result.append(f(elem))
    
    return result


class TestToUpper(unittest.TestCase):
    def test_1(self):
        argument = "hi"

        result = to_upper(argument)

        self.assertEqual("HI", result)
    
    def test_2(self):
        argument = ["hi", "bye", "thanks", "welcome"]

        result = apply(to_upper, argument)

        self.assertEqual(['HI', 'BYE', 'THANKS', 'WELCOME'], result)