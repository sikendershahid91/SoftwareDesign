import unittest
import src.color_selection

class CodeSelectionTest(unittest.TestCase):
	def setUp(self):
		self.colorSelection = src.color_selection.ColorSelection()

	def tearDown(self):
		pass

	def test_new_selection_contains_0_colors(self):
		self.assertEqual(0, self.colorSelection.number_of_colors)
		

		

