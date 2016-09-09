"""
Exercise 5.41: Plot functions from the command line
Author: Weiyun Lu
"""

import sys
from scitools.std import StringFunction, plot, linspace
from numpy import *

try:
    f = StringFunction(sys.argv[1])
    f = vectorize(f)
    min = eval(sys.argv[2])
    max = eval(sys.argv[3])
except IndexError:
    print('You must supply a function, a minimum value, and a maximum value!')
    sys.exit(1)
except ValueError or TypeError:
    print('You must supply a function (as a string), and valid min and max',
          'numerical values!')
    sys.exit(1)
    
if sys.argv[4] != None:
    n = eval(sys.argv[4])
else:
    n = 501

x = linspace(min, max, n)
plot(x, f(x), xlabel='x', ylabel='f(x)', title='f(x)=%s' % sys.argv[1])