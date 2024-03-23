import unittest

from se import solve_square_equation


class TestSE(unittest.TestCase):
    def test_a_is_0(self):
        # AAA = Arrange, Act, Assert
        # Arrange
        a = 0

        # Act
        result = solve_square_equation(a, 0, 0)

        # Assert
        self.assertEqual(result, "error")

    def test_discr_is_positive(self):
        a = 1
        b = 0
        c = -1

        result = solve_square_equation(a, b, c)

        self.assertEqual(result, [-1, 1])

    def test_discr_is_zero(self):
        a = 1
        b = 0
        c = 0

        result = solve_square_equation(a, b, c)

        self.assertEqual(result, [0])

    def test_neg_b_is_very_big(self):
        a = 1
        b = -1E+10 # -10000000000
        c = -1

        result = solve_square_equation(a, b, c)

        # x1*x2 = c
        # x1 + x2 = -b

        self.assertEqual(result[0] + result[1], -b)
        self.assertEqual(result[0] * result[1], c)

        self.assertEqual(result, [-1E-10, 1E+10])
