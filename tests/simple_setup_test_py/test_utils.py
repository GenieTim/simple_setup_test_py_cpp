import unittest

from simple_setup_test_py.utils.comp_util import add_numbers


class UtilsCompTestCase(unittest.TestCase):
    def test_sample_class(self):
        self.assertEqual(2, add_numbers(1, 1))
        self.assertEqual(1, add_numbers(0.5, 0.5))
        self.assertEqual(100, add_numbers(10, 90))
