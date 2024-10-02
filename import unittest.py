import unittest
from prime import is_prime


class TestIsPrime(unittest.TestCase):
    def test_less_than_two(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(-5))

    def test_two(self):
        self.assertTrue(is_prime(2))

    def test_prime_numbers(self):
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))

    def test_non_prime_numbers(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))


if __name__ == "__main__":
    unittest.main()
