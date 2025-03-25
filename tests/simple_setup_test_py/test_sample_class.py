import unittest

from simple_setup_test_py_cpp import SampleClass


class SampleClassTestCase(unittest.TestCase):
    def test_sample_class(self):
        sample_obj = SampleClass()
        self.assertIsInstance(sample_obj, SampleClass)
        for i in range(10):
            sample_obj.set_value(1)
            self.assertEqual(sample_obj.get_value(), 1)
