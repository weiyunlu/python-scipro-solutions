"""
Exercise 4.2: Read a number from the command line
Author: Weiyun Lu
"""

import sys

try:
    F = float(sys.argv[1])
    C = (5.0/9) * (F - 32)
    print C
except IndexError:
    raise IndexError('You need to give me a value!')