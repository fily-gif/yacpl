from yacpl import Yacpl, Color
from time import sleep as sl

yacpl = Yacpl()

yacpl("Hello, World!", fg=Color.RED, bg=Color.WHITE)
sl(1)
yacpl("this is a test", fg=Color.YELLOW, bg=Color.BLUE)
sl(0.5)
yacpl("made in pure python", fg=Color.BLUE, bg=Color.MAGENTA)
sl(0.4)
yacpl("...with no external dependencies!", fg=Color.MAGENTA, bg=Color.CYAN)
sl(0.4)
yacpl("...for Hackclub High Seas!", bg=Color.GREEN)
