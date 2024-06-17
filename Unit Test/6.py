import unittest
import math

def calculate_square_root(value):
    return math.sqrt(value)

class TestFloatingPointCalculations(unittest.TestCase):
    def test_square_root_of_positive_number(self):
        result = calculate_square_root(25.0)
        self.assertAlmostEqual(result, 5.0, places=7)
    
    def test_square_root_of_zero(self):
        result = calculate_square_root(0.0)
        self.assertAlmostEqual(result, 0.0, places=7)
    
    def test_square_root_of_small_number(self):
        result = calculate_square_root(0.0001)
        self.assertAlmostEqual(result, 0.01, places=7)
    
    def test_square_root_of_large_number(self):
        result = calculate_square_root(1e10)
        self.assertAlmostEqual(result, 1e5, places=7)

if __name__ == '__main__':
    unittest.main()
