# YACPL

> `Yet Another Color Print Library` A simple `print()`-esque library that supports ***<u>colors</u>***!
> 
###### yes i know that this is like the simplest project that does the same as colorama and i really dont care tbh

![yacpl intro gif](.assets/yacpl-intro.gif)
###### NOTE: this gif is horrible.
## Installation:

```bash
$ python3 -m pip install yacpl
```

## Usage:

```python
from yacpl import Bg, Fg, Printer
yacpl = Printer()

yacpl("Hello, world!", Bg.CYAN, Fg.RED)
```

## Development:

```bash
$ git clone https://github.com/fily-gif/yacpl.git # or `gh repo clone fily-gif/yacpl`
$ python3 -m pip install -r requirements.txt
# do your thing
# to test your changes: do
$ python3 -m pip install -e . 
```