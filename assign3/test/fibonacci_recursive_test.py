import unittest
from src.fibonacci_recursive import fibonacci_recursive
from test.fibonacci_test import fibonacciTest


class FibonacciRecursiveTest(unittest.TestCase, fibonacciTest):

    def setUp(self):
        self.fibonacci = fibonacci_recursive
