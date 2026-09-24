import unittest

from config import timeout


class ConfigTests(unittest.TestCase):
    def test_explicit_value(self):
        self.assertEqual(timeout("12"), 12)

    def test_invalid_value(self):
        with self.assertRaises(ValueError):
            timeout("invalid")
