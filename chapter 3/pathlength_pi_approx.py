"""
Exercise 3.12, 3.13: Compute the length of a path, approximate pi
Author: Weiyun Lu
"""

from math import sqrt, pi, sin, cos

def pathlength(x,y):
    L = 0
    success = len(x)==len(y)
    msg = 'The length of x and y coordinates must be the same!'
    assert success, msg
    for i in range(len(x)-1):
        d = sqrt((x[i+1]-x[i])**2 + (y[i+1]-y[i])**2)
        L += d
    return L

def points_circle(n):
    x=[]; y=[] #initialize empty lists
    for i in range(0,n+1):
        x.append(0.5 * cos((2*pi*i)/n))
        y.append(0.5 * sin((2*pi*i)/n))
    return x, y
    
print '%20s %20s %20s' %('Points on circle', 'Computed length', 'Error from pi')
print '--------------------------------------------------------------'
    
for k in range(2,11):
    n = 2**k
    x = points_circle(n)[0]
    y = points_circle(n)[1]
    L = pathlength(x,y)
    error = abs(pi - L)
    print '%20.d %20.10f %20.10f' %(n, L, error)
