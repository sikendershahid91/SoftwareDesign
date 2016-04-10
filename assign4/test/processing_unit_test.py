import unittest
from src.processing_unit import ProcessingUnit


class ProcessingUnitTest(unittest.TestCase):


    def test_canary(self):
        self.assertTrue(self)


    def setUp(self):
        self.processing_unit = ProcessingUnit()
        

    def test_blank_unit_process_input_1_return_1(self):
        self.assertEqual(self.processing_unit.process('a'), 'a')

