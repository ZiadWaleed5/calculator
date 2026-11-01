import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import cal

class TestCalculator(unittest.TestCase):
    
    def test_addition_positive_numbers(self):
        result = cal.calculate(10, 5, "+")
        self.assertEqual(result, 15, "10 + 5 should equal 15")

    def test_addition_negative_numbers(self):
        result = cal.calculate(-3, -7, "+")
        self.assertEqual(result, -10, "-3 + -7 should equal -10")

if __name__ == '__main__':
    unittest.main()