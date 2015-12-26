#!/usr/bin/env python

import os
from setuptools import setup

REQUIREMENTS = [line.strip() for line in
                open("requirements.txt").readlines()]
setup(
    name='terminalweather',
    version='1.0',
    author='Matt Bachmann',
    url='https://github.com/Bachmann1234/terminalweather',
    description='Display the current weather in your terminal',
    license='Apache 2.0',
    packages=['terminalweather'],
    install_requires=REQUIREMENTS,
    entry_points={
        'console_scripts': ['terminalweather = terminalweather.app:run'],
    }
)
