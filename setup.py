from setuptools import find_packages
from setuptools import setup

setup(
    name='mpr',
    version='0.1.1',
    author='Andrew Kirkegaard',
    author_email='andrew.kirkegaard@gmail.com',
    url='https://github.com/gumballhead/mpr',
    packages = find_packages(exclude=["test.*", "test"]),
    scripts=['bin/cash', 'bin/cutout', 'bin/purchases', 'bin/report'],
    keywords=['usda', 'agriculture', 'livestock', 'commodities', 'trading'],
    include_package_data=True,
    python_requires='>=3.7.*',
    install_requires=['aiohttp', 'numpy', 'pandas', 'isoweek', 'pytz'])
