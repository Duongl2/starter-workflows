import unittest
from calculator import average


class TestAverage(unittest.TestCase):
    def test_average_of_multiple_scores(self):
        self.assertEqual(average([8, 10, 6]), 8)

    def test_average_of_one_score(self):
        self.assertEqual(average([7]), 7)

    def test_empty_scores_raise_error(self):
        with self.assertRaises(ValueError):
            average([])

    def test_score_below_zero_raises_error(self):
        with self.assertRaises(ValueError):
            average([-1, 8])

    def test_score_above_ten_raises_error(self):
        with self.assertRaises(ValueError):
            average([8, 11])


if __name__ == "__main__":
    unittest.main()