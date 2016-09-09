"""
Exercise 3.21: Find the max and min values of a function
Author: Weiyun Lu
"""

from math import sin, cos, pi

def minmax(f,a,b,n=1000):
    success = (type(a) is int or float) and (type(b) is int or float) and a < b
    msg = "You must feed two numbers with a < b!"
    assert success, msg
    h = (float(b - a)) / (n - 1) #length of the interval
    values = [] #initialize list of values
    for i in range(n):
        x = a + i*h
        values.append(f(x))
    return max(values), min(values)
    
print 'The min of the cosine function on the interval [-pi/2, 2pi] is %.6f.' %(minmax(cos,-pi/2,2*pi)[1])
print 'The max of the cosine function on the interval [-pi/2, 2pi] is %.6f.' %(minmax(cos,-pi/2,2*pi)[0])

print 'The min of the sine function on the interval [-pi/2, 2pi] is %.6f.' %(minmax(sin,-pi/2,2*pi)[1])
print 'The max of the sine function on the interval [-pi/2, 2pi] is %.6f.' %(minmax(sin,-pi/2,2*pi)[0])

print 'Note we are sampling a uniform distribution of 1000 points in the given intervals, so results may be approximate.'