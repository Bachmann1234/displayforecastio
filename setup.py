#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='displayforecastio',
    version='1.2',
    author='Matt Bachmann',
    url='https://github.com/Bachmann1234/displayforecastio',
    description='Display the current weather in your terminal',
    license='Apache 2.0',
    packages=find_packages(),
    install_requires=['requests==2.32.4'],
    entry_points={
        'console_scripts': ['forecastio = displayforecastio.app:run'],
    }
)
