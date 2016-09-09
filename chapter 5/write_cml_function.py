"""
Exercise 5.15: Write function data to file
Author: Weiyun Lu
"""

from scitools.std import *
import sys

if len(sys.argv) is 1:
    print 'Give f, a, b, n, in that order, on the command line.'
    sys.exit(1)
    
def StringIn(x):
    return StringFunction(x) #this is so that we call a StringFunction that has math stuff imported

def FloatIn(x):
    return eval(x)

try:
    f = StringIn(sys.argv[1])
    a = FloatIn(sys.argv[2])
    b = FloatIn(sys.argv[3])
    n = int(sys.argv[4])
except ValueError:
    print 'You have to give f as a string, then a, b as reals and n as an integer!'
    sys.exit(1)
except IndexError:
    print 'You must give f, a, b, n all on one line!'
    sys.exit(1)
    
x = linspace(a,b,n)
y = f(x)

outfile = open('cml_output.txt', 'w')
outfile.write('%16s %16s \n' %('x', 'f(x)'))
outfile.write('--------------------------------------\n')
for i in range(len(x)):
    outfile.write('%16.10f %16.10f \n' %(x[i], y[i]))
outfile.close()