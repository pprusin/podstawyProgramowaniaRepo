import unittest

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class TestPrimeFunction(unittest.TestCase):

    def test_negative_number(self):
        self.assertFalse(is_prime(-10), "-10 should not be prime")

    def test_zero(self):
        self.assertFalse(is_prime(0), "0 should not be prime")

    def test_one(self):
        self.assertFalse(is_prime(1), "1 should not be prime")

    def test_two(self):
        self.assertTrue(is_prime(2), "2 should be prime")

    def test_three(self):
        self.assertTrue(is_prime(3), "3 should be prime")

    def test_four(self):
        self.assertFalse(is_prime(4), "4 should not be prime")

    def test_prime_number(self):
        self.assertTrue(is_prime(13), "13 should be prime")

    def test_non_prime_number(self):
        self.assertFalse(is_prime(15), "15 should not be prime")

    def test_large_prime_number(self):
        self.assertTrue(is_prime(7919), "7919 should be prime")

    def test_large_non_prime_number(self):
        self.assertFalse(is_prime(8000), "8000 should not be prime")

if __name__ == '__main__':
    unittest.main()
