#https://github.com/olliegaming2201-ux/Lab11-Oliver-Fuentes.git

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 4), 12)
        self.assertEqual(calculator.multiply(-2, 5), -10)

    def test_divide(self):
        self.assertAlmostEqual(calculator.divide(2, 10), 5)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(0, 5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 5)
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(25), 5)
        with self.assertRaises(ValueError):
            calculator.square_root(-9)


# Do not touch this
if __name__ == "__main__":
    unittest.main()
