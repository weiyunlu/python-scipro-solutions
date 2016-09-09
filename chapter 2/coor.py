"""
Exercise 2.6: Generate equally space coordinates
Author: Weiyun Lu
"""

a = 0.0 #set a startpoint
b = 100.0 #set an endpoint
n = 6 #how many subintervals to have
coor = []
l = (b-a)/n #length of a subinterval
i = 0 #initialize index
while i <= n:
    x = a + i*l
    coor.append(x)
    i = i+1
for num in coor:
    print '%.4f' % (num),