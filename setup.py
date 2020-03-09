import os
from setuptools import find_packages
from setuptools import setup

setup(
    name='mpr',
    version=os.popen('git describe').read(),
    author='Andrew Kirkegaard',
    author_email='andrew.kirkegaard@gmail.com',
    url='https://github.com/gumballhead/mpr',
    packages=find_packages(exclude=["test.*", "test"]),
    scripts=['bin/report'],
    entry_points={
        'console_scripts': [
            'cash=mpr.cash_index:main',
            'cutout=mpr.cutout_index:main',
            'purchases=mpr.purchase_index:main'
        ]
    },
    keywords=['usda', 'agriculture', 'livestock', 'commodities', 'trading'],
    include_package_data=True,
    python_requires='>=3.7.*',
    install_requires=['aiohttp', 'numpy', 'pandas', 'isoweek', 'pytz'])
