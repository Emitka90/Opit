import unittest

from prob_test import square, list_range, even_odd_int


class TestCalcul(unittest.TestCase):

    def test_square(self):
        self.assertEqual(square(4), 16, 'Ошибка!')

    def test_square_type(self):
        self.assertIsInstance(square(4), int, 'Ошибка!')

    def test_list_range(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(list_range(5), nums)

    def test_list_range_type(self):
        self.assertIsInstance(list_range(12), list)

    def test_even_odd(self):
        answer = 'Четное'
        self.assertEqual(even_odd_int(0), answer, 'Ошибка!')


unittest.main()
