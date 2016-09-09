"""
Exercise 2.18: Explore round-off errors from a large number of inverse operations
Author: Weiyun Lu
"""

from math import sqrt
for n in range(1,60):
    r = 2.0
    for i in range(n):
        r = sqrt(r)
    for i in range(n):
        r = r**2
    print '%d times sqrt and **2: %.16f' % (n, r)
    
#investigate...
    
n = 52
r = 2.0
for i in range(n):
    r = sqrt(r)
    print 'the root of 2 %d times yields %.24f' % (i, r)
for i in range(n):
    r = r**2
    print r