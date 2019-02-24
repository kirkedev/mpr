from distutils.core import setup

setup(
  name="mpr",
  author="Andrew Kirkegaard",
  author_email="andrew.kirkegaard@gmail.com",
  packages=["mpr"], 
  requires=['tables', 'aiohttp', 'numpy', 'pandas']
)
