"""
Exercise 2.7: Make a table of values from a formula
Author: Weiyun Lu
"""

g = 9.81 #acceleration due to gravity
v0 = 1.0 #initial velocity
a = 0.0 #start point
b = (2*v0)/g #end point
n = 10 #number of subintervals
l = (b-a)/n #length of a subinterval

print '%8s, %8s' % ('t', 'y(t)')

for i in range(0,n+1):
    t = a + i*l
    y = v0*t - 0.5*g*t**2
    print '%8.4f %8.4f' % (t, y)