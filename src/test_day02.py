import unittest
from day02 import level_safe, safe_level_count


class TestDay02(unittest.TestCase):
    def test_level_safe(self):
        self.assertEqual(level_safe([7, 6, 4, 2, 1]), None)
        self.assertEqual(level_safe([1, 2, 7, 8, 9]), 2)
        self.assertEqual(level_safe([9, 7, 6, 2, 1]), 3)
        self.assertEqual(level_safe([1, 3, 2, 4, 5]), 2)
        self.assertEqual(level_safe([8, 6, 4, 4, 1]), 3)
        self.assertEqual(level_safe([1, 3, 6, 7, 9]), None)

    def test_safe_level_count(self):
        levels = [
            [7, 6, 4, 2, 1],
            [1, 2, 7, 8, 9],
            [9, 7, 6, 2, 1],
            [1, 3, 2, 4, 5],
            [8, 6, 4, 4, 1],
            [1, 3, 6, 7, 9],
        ]
        self.assertAlmostEqual(safe_level_count(levels=levels, allow_damper=False), 2)
        self.assertAlmostEqual(safe_level_count(levels=levels, allow_damper= True), 4)