import os
from re import match

from setuptools import find_packages
from setuptools import setup

tag = os.popen('git describe').read()
version = '0.0.0' if match(r"v[\d\.]+", tag) is None else tag[1:]

setup(
    name='mpr',
    version=version,
    author='Andrew Kirkegaard',
    author_email='andrew.kirkegaard@gmail.com',
    url='https://github.com/gumballhead/mpr',
    packages=find_packages(exclude=['test.*', 'test']),
    entry_points={
        'console_scripts': [
            'bacon=mpr.bacon_index:main',
            'cash=mpr.cash_index:main',
            'cutout=mpr.cutout_index:main',
            'purchases=mpr.purchase_index:main'
        ]
    },
    keywords=['usda', 'agriculture', 'livestock', 'commodities', 'trading'],
    include_package_data=True,
    python_requires='>=3.7.*',
    install_requires=[
        'aiohttp >3.6, <4.0',
        'isoweek >1.3.0, <1.4.0',
        'numpy >1.15.0, <1.19.0', 
        'pandas >1.0.0, <1.1.0', 
        'python-dateutil >2.8.0, <2.9.0'
    ],
    setup_requires=['wheel'])
