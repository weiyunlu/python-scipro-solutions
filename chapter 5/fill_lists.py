"""
Exercise 5.1: Fill lists with function values
Author: Weiyun Lu
"""

from math import pi, exp, sqrt

h = lambda x : (1/(sqrt(2*pi))) * exp(-0.5*x**2)

i = 8.0 / 40 #length of each subinterval
xlist = [-4 + i*n for n in range(41)]
hlist = [h(x) for x in xlist]
pairs = zip(xlist,hlist)

print pairs