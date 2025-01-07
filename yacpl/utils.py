from enum import Enum

class Fg(Enum):
	BLACK = "\033[30m"
	RED = "\033[31m"
	GREEN = "\033[32;0m"
	YELLOW = "\033[33;0m"
	BLUE = "\033[34;0m"
	MAGENTA = "\033[35;0m"
	CYAN = "\033[36;0m"
	WHITE = "\033[97;0m"
	RESET = "\033[0m"

class Bg(Enum):
	BLACK = 40
	RED = 41
	GREEN = 42
	YELLOW = 43
	BLUE = 44
	MAGENTA = 45
	CYAN = 46
	WHITE = 107
	RESET = 0

def colorize(text, fg=Fg.RESET, bg=Bg.RESET):
	return f"\033[{fg.value};{bg.value}m{text}\033[0m"