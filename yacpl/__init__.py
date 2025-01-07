import logging
from .utils import Fg, Bg, colorize

class Printer():
	def __init__(self):
		pass

	def __call__(self, text, fg, bg):
		#print(text, fg, bg)
		#logging.log("sdf")
		finished = colorize(text, fg, bg)
		print(finished)