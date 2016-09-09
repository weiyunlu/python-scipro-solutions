"""
Exercise 2.6': Generate equally space coordinates (using a list comprehension)
Author: Weiyun Lu
"""

a = 0.0 #start point
b = 100 #end point
n = 6 #how many subintervals to have
l = (b-a)/n #length of a subinterval
coor = [a + i*l for i in range(0,n+1)]
for x in coor:
    print '%2f' % (x),