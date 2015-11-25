#! /usr/bin/env python
import os
import sys

sys.path.append(os.path.join('..', 'terminalweather'))

from terminalweather.app import main

if __name__ == '__main__':
    sys.exit(main())
