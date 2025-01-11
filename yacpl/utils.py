from enum import Enum

class Fg(Enum):
	BLACK = 30
	RED = 31
	GREEN = 32
	YELLOW = 33
	BLUE = 34
	MAGENTA = 35
	CYAN = 36
	WHITE = 97
	RESET = 0

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

def _construct(fg, bg):
	if not bg:
		result = f"\033[{fg}m"
	result = f"\033[{fg};{bg}m"
	#print(f'con {result}')
	return result

def colorize(text, fg=Fg.RESET, bg=Bg.RESET):
	test = _construct(fg.value, bg.value)
	#print(f"color {test}")
	return f"{test}{text}\033[0m"