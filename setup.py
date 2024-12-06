from setuptools import setup, find_packages

# read the contents of your README file.
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
#print(find_packages(where='yacpl'))
setup(
    name='yacpl',
	version='1.0.8',
    packages=find_packages(where='yacpl'),
	package_dir={'': '.'},
    long_description=long_description,
    long_description_content_type='text/markdown'
)
