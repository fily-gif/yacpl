import logging
from enum import Enum
logger = logging.getLogger('yacpl')
#logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s") # tbf i never used 

class Color(Enum):
	BLACK = 30, 40 # NOTE: fg, bg (e.g list(Color.BLACK.value)[1] will return int(30))
	RED = 31, 41
	GREEN = 32, 42
	YELLOW = 33, 43
	BLUE = 34, 44
	MAGENTA = 35, 45
	CYAN = 36, 46
	WHITE = 97, 107
	RESET = 0, 0 # i guess we doing strings now (its way easier to just do this tbh)

def tuple_to_list(tup) -> list:
	if not isinstance(tup, tuple):
		raise ValueError(f'Invalid type: {type(tuple)}')
	else:
		#print(tup)
		listified = list(tup)
		#print(listified)
		return listified

def ANSIfy(string, fg, bg=Color.BLACK) -> str | None:
	"""
	Converts a given string to an ANSI colored string using the specified foreground and background colors.

	Args:
		string (str): The string to be colored.
		fg (Color): The foreground color as an instance of the Color enum.
		bg (Color, optional): The background color as an instance of the Color enum. Defaults to Color.BLACK.

	Returns:
		str | None: The ANSI colored string if successful, otherwise None.

	Raises:
		ValueError: If there is an issue with converting the colors or formatting the string.
	"""
	try:
		if not isinstance(fg, Color):
			raise ValueError(f'Invalid color: {fg}')
		elif not isinstance(bg, Color):
			raise ValueError(f'Invalid color: {bg}')
		else:
			fg_list = tuple_to_list(fg.value)
			#print(f'fg:{fg_list}')
			bg_list = tuple_to_list(bg.value)
			#print(f'bg:{bg_list}')
			reset = Color.RESET
			reset = tuple_to_list(reset.value)
			final_string = f'\033[{fg_list[0]};{bg_list[1]}m{string}\033[{reset[0]}m'
			#logging.debug(str(final_string))
			return final_string
	except ValueError as ve:
		logging.error(f'Something went extremely wrong! {ve}')
		logging.debug(ve)
		raise ValueError(f'Something went wrong! {ve}')



if __name__ == '__main__':
	pass