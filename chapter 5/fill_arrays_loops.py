"""
Exercise 5.2: Fill arrays; loop version
Author: Weiyun Lu
"""

from scitools.std import sqrt, pi, exp, zeros

h = lambda x : (1/(sqrt(2*pi))) * exp(-0.5*x**2)
n = 8.0 / 40 #length of each subinterval
xlist = zeros(41,float)
hlist = zeros(41,float)

for i in range(41):
    xlist[i] = -4 + i*n
    hlist[i] = h(xlist[i])
    
pairs = zip(xlist,hlist)
print pairs