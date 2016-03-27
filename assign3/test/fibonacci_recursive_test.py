import unittest
from src.fibonacci_recursive import fibonacci_recursive


class FibonacciTest(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(self)

    def test_negative_position_throws_exception(self):
        self.assertRaises(ValueError, fibonacci_recursive, -1)

    def test_position_0_return_1(self):
        self.assertEqual(1, fibonacci_recursive(0))

    def test_position_1_return_1(self):
        self.assertEqual(1, fibonacci_recursive(1))

    def test_position_2_return_2(self):
        self.assertEqual(2, fibonacci_recursive(2))

    def test_position_4_return_5(self):
        self.assertEqual(5, fibonacci_recursive(4))

    def test_position_3_return_3(self):
        self.assertEqual(3, fibonacci_recursive(3))

    def test_position_5_return_8(self):
        self.assertEqual(8, fibonacci_recursive(5))

    def test_position_6_return_13(self):
        self.assertEqual(13, fibonacci_recursive(6))        