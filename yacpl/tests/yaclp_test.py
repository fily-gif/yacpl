import unittest
from yacpl import Yaclp, Color
#from yacpl.utils import Color, ANSIfy


class TestYaclp(unittest.TestCase):

	def setUp(self):
		self.yaclp = Yaclp()

	def test_default_colors(self):
		with self.assertLogs(level='DEBUG') as log:
			self.yaclp("Hello")
			self.assertIn('got Hello, Color.WHITE, Color.BLACK!', log.output[0])

	def test_custom_colors(self):
		with self.assertLogs(level='DEBUG') as log:
			self.yaclp("Hello", fg=Color.RED, bg=Color.GREEN)
			self.assertIn('got Hello, Color.RED, Color.GREEN!', log.output[0])

	def test_invalid_foreground_color(self):
		with self.assertRaises(ValueError):
			self.yaclp("Hello", fg="InvalidColor")

	def test_invalid_background_color(self):
		with self.assertRaises(ValueError):
			self.yaclp("Hello", bg="InvalidColor")

if __name__ == '__main__':
	unittest.main()