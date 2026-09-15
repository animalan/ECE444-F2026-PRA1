import unittest
from utils import utils


class TestUtils(unittest.TestCase):
    def test_reversed_positive_integer(self):
        result = utils.reversed(12345)
        self.assertEqual(result, 54321)

    def test_reversed_negative_integer(self):
        result = utils.reversed(-12345)
        self.assertEqual(result, -54321)

    # Not supported
    def test_reversed_string(self):
        with self.assertRaises(TypeError):
            utils.reversed("6789")

    # Not supported
    def test_reversed_float(self):
        with self.assertRaises(ValueError):
            utils.reversed(12.34)

    def test_formatter_integer(self):
        result = utils.formatter(14)
        self.assertEqual(result, ("0b1110", "0o16"))

    # Not supported
    def test_formatter_string(self):
        with self.assertRaises(TypeError):
            utils.formatter("14")

    # Not supported
    def test_formatter_float(self):
        with self.assertRaises(TypeError):
            utils.formatter(14.5)


if __name__ == "__main__":
    unittest.main()
