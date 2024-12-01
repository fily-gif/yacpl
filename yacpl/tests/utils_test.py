import unittest
from yacpl.utils import ANSIfy, Color

# yacpl/test_utils.py


class TestANSIfy(unittest.TestCase):

	def test_valid_colors(self):
		result = ANSIfy("Hello", Color.RED, Color.GREEN)
		expected = '\033[31;42mHello\033[0;0m'
		self.assertEqual(result, expected)

	def test_default_background_color(self):
		result = ANSIfy("Hello", Color.BLUE)
		expected = '\033[34;40mHello\033[0;0m'
		self.assertEqual(result, expected)

	def test_invalid_foreground_color(self):
		with self.assertRaises(ValueError):
			ANSIfy("Hello", "InvalidColor")

	def test_invalid_background_color(self):
		with self.assertRaises(ValueError):
			ANSIfy("Hello", Color.RED, "InvalidColor")

if __name__ == '__main__':
	unittest.main()