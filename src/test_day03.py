import unittest
import day03 as day


class TestDay03(unittest.TestCase):
    def test_total(self):
        self.assertEqual(
            day.get_mull_match_total(
                r"xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
            ),
            161,
        )
        
    def test_trimmed_total(self):
        input = day.remove_donts(r"xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
        self.assertEqual(
            day.get_mull_match_total(input),
            48,
        )
