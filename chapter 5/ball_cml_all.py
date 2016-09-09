"""
Exercise 4.11, 4.12, 4.13: Use exceptions to handle wrong input, test validity of input data,\
    raise an exception in case of wrong input
Author: Weiyun Lu
"""

import sys

g = 9.81

def t_test(t,v0):
    if not (0 <= t <= 2.0*v0/g):
        print 'Time must be between 0 and 2*v0/g!'
        sys.exit(1)

try:
    v0 = float(sys.argv[1])
    t = float(sys.argv[2])
    t_test(t,v0)
    y = v0*t - 0.5*g*t**2
    print 'The height at that time is %6f.' %(y)
except IndexError:
    print 'You need to give me the missing values!'
    v0 = float(raw_input('v0=?'))
    t = float(raw_input('t=?'))
    t_test(t,v0)
    y = v0*t - 0.5*g*t**2
    print 'The height at that time is %6f.' %(y)
except ValueError:
    print 'You have to give me two numbers!'