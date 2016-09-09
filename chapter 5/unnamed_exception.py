"""
Exercise 4.18: Why we test for specific exception types
Author: Weiyun Lu
"""

import sys

try:
    C = float(sys.argv[1])
except IndexError:
    print 'C must be provided as command-line argument.'
    sys.exit(1)
except ValueError:
    print 'You have to give me a number as input.'
    sys.exit(1)