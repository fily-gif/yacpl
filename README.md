# YACPL

> `Yet Another Color Print Library` A simple `print()`-esque library that supports ***colors***!

###### yes i know that this is like the simples project that does the same as colorama and i really dont care tbh

## Installation

```bash
$ python3 -m pip install yacpl
```

## Usage:

```python
from yacpl import Yacpl, Color

yacpl = Yacpl()

yacpl("Hello, World!", fg=Color.RED, bg=Color.WHITE) # bg is optional as it defaults to `Color.BLACK`
# vscode should automatically pick up the colors too
```
