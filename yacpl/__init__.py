import logging
from .utils import Color, ANSIfy
logging.getLogger(__name__)

class Yacpl:
	def __init__(self):
		pass
	def __call__(self, text, fg: Color = Color.WHITE, bg: Color = Color.BLACK):
		"""
		Call method to print text with specified foreground and background colors.

		Args:
			text (str): The text to be printed.
			fg (Color, optional): The foreground color. Defaults to Color.WHITE.
			bg (Color, optional): The background color. Defaults to Color.BLACK.

		Raises:
			ValueError: If there is an error during the ANSIfy process.

		Returns:
			None
		"""
		logging.debug(f'got {text}, {fg}, {bg}!')
		try:
			ansified = ANSIfy(text, fg, bg)
			print(ansified)
		except ValueError as ve:
			logging.error(f'Something went extremely wrong! {ve}')
			logging.debug(ve)
			raise ValueError(f'Something went extremely wrong! {ve}')