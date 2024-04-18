import unittest
import math

from src.example import div, mul


class TestDiv(unittest.TestCase):
    def test_a_and_b_the_same(self):
        # AAA = Arrange, Act, Assert

        # Arrange
        a = 10
        b = a

        # Act
        c = div(a, b)

        # Assert
        self.assertEqual(c, 1)

    def test_b_equals_to_1(self):
        # Arrange
        a = 10
        b = 1

        # Act
        c = div(a, b)

        # Assert
        self.assertEqual(c, a)

    def test_b_equals_to_0(self):
        a = 10
        b = 0

        c = div(a, b)

        self.assertEqual(c, "error")


class TestMul(unittest.TestCase):
    def test_a_and_b_equal_to_0(self):
        a = 0
        b = 0

        c = mul(a, b)

        self.assertEqual(c, 0)
    
    def test_b_equals_to_0(self):
        a = 10
        b = 0

        c = mul(a, b)

        self.assertEqual(c, 0)

    def test_floating_point_numbers(self):
        a = 0.1
        b = 3

        c = mul(a, b)

        self.assertAlmostEqual(c, 0.3, 7)


