import logging
from enum import Enum
logger = logging.getLogger('yaclp')
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
	RESET = '\033[0;0m' # i guess we doing strings now (its way easier to just do this tbh)

def tuple_to_list(tuple) -> list:
	listified = list(tuple)
	print(listified)
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
		fg_list = tuple_to_list(fg.value)
		print(fg_list)
		bg_list = tuple_to_list(bg.value)
		print(bg_list)
		reset = tuple_to_list(reset.value)
		final_string = f'\033[{fg_list[1]};{bg_list[2]}m{string}{reset}'
		logging.debug(str(final_string))
		return final_string
	except ValueError as ve:
		logging.error(f'Something went extremely wrong! {ve}')
		logging.debug(ve)
		raise ValueError(f'Something went wrong! {ve}')

if __name__ == '__main__':
	pass
