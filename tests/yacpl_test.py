import unittest
from yacpl import Yacpl, Color
#from yacpl.utils import Color, ANSIfy

class Testyacpl(unittest.TestCase):

	def setUp(self):
		self.yacpl = Yacpl()

	def test_default_colors(self):
		with self.assertLogs(level='DEBUG') as log:
			self.yacpl("Hello")
			print(f"log: {log.output[0]}")
			self.assertIn('got Hello, Color.WHITE, Color.BLACK!', log.output[0])

	def test_custom_colors(self):
		with self.assertLogs(level='DEBUG') as log:
			self.yacpl("Hello", fg=Color.RED, bg=Color.GREEN)
			self.assertIn('got Hello, Color.RED, Color.GREEN!', log.output[0])

	def test_invalid_foreground_color(self):
		with self.assertRaises(ValueError):
			self.yacpl("Hello", fg="InvalidColor")

	def test_invalid_background_color(self):
		with self.assertRaises(ValueError):
			self.yacpl("Hello", bg="InvalidColor")

if __name__ == '__main__':
	unittest.main()