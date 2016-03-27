import unittest
from src.fibonacci_iterative import fibonacci_iterative
from test.fibonacci_test import fibonacciTest


class FibonacciIterativeTest(unittest.TestCase, fibonacciTest):
    def test_canary(self):
        self.assertTrue(self)

    def setUp(self):
        self.fibonacci = fibonacci_iterative
