import unittest
from day02 import level_safe


class TestDay02(unittest.TestCase):
    def test_level_safe(self):
        self.assertEqual(level_safe([7, 6, 4, 2, 1]), True)
        self.assertEqual(level_safe([1, 2, 7, 8, 9]), False)
        self.assertEqual(level_safe([9, 7, 6, 2, 1]), False)
        self.assertEqual(level_safe([1, 3, 2, 4, 5]), False)
        self.assertEqual(level_safe([8, 6, 4, 4, 1]), False)
        self.assertEqual(level_safe([1, 3, 6, 7, 9]), True)
