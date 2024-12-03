from setuptools import setup, find_packages

# read the contents of your README file.
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
# trigger gh actions
setup(
    name='yacpl',
	version='1.0.5',
    packages=find_packages('yacpl'),
    long_description=long_description,
    long_description_content_type='text/markdown'
)
