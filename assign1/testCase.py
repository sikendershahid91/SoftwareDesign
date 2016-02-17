import GameEngine
import ColorPool
import unittest


class TestCases(unittest.TestCase):

    def TestStartOfGameTwentyChances(self):
        self.assertEqual(20, GameEngine.getRemainingTurns())

    def TestCheckColorPoolContainsTenColors(self):
        self.assertEqual(10, ColorPool.getColorCount())

    def TestInputBoxHighlightedAfterClick(self):
        self.assertEqual()

if __name__ == '__main__':
    unittest.main()