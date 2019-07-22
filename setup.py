from setuptools import setup
from setuptools import find_packages

setup(
  name='mpr',
  version='0.1.1',
  author='Andrew Kirkegaard',
  author_email='andrew@kirke.dev',
  url='https://github.com/gumballhead/mpr',
  packages=find_packages(exclude=['test', 'test.*']),
  include_package_data=True,
  python_requires='>=3.7.*',
  test_suite="test",
  install_requires=['aiohttp', 'numpy', 'pandas', 'statsmodels', 'tables', 'behave'],
  extra_requires=['jupyter', 'seaborn'])
