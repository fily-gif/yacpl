import logging
from .utils import Fg, Bg, colorize

class Printer():
	def __init__(self):
		pass

	def __call__(self, text, fg, bg):
		finished = colorize(text, fg, bg)
		print(finished)