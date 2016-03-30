import unittest
from src.fibonacci_recursive import Recursive
from test.fibonacci_test import fibonacciTest


class FibonacciRecursiveTest(unittest.TestCase, fibonacciTest):

    def setUp(self):
        self.recursive = Recursive()
        self.fibonacci = self.recursive.fibonacci
