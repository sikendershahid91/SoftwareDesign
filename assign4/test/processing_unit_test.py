import unittest
from src.processing_unit import ProcessingUnit
from test.char_blocker_test import CharBlockTest


class ProcessingUnitTest(unittest.TestCase, CharBlockTest):

    def setUp(self):
        self.processing_unit = ProcessingUnit
        self.test_block = self.processing_unit.char_blocker
