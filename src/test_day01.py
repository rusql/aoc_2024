import unittest

from day01 import get_distance, get_occurrences, get_similarity_total

class TestDay01(unittest.TestCase):
    def test_sample(self):
        list1 = [3, 4, 2, 1, 3, 3]
        list2 = [4, 3, 5, 3, 9, 3]
        self.assertEqual(get_distance(list1, list2), 11)
        
    def test_occurrences(self):
        list = [1, 1, 2, 3]
        self.assertEqual(get_occurrences(list), {1:2, 2:1, 3:1})

    def test_similarity_total(self):
        list1 = [3, 4, 2, 1, 3, 3]
        list2 = [4, 3, 5, 3, 9, 3]
        self.assertEqual(get_similarity_total(list1, list2), 31)