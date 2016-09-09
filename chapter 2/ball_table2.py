"""
Exercise 2.8: Store values from a formula in lists
Author: Weiyun Lu
"""

g = 9.81 #acceleration due to gravity
v0 = 1.0 #initial velocity
a = 0.0 #start point
b = (2*v0)/g #end point
n = 10 #number of subintervals
l = (b-a)/n #length of a subinterval
t = []; y = []

print '%8s, %8s' % ('t', 'y(t)')

for i in range(0,n+1):
    tn = a + i*l
    yn = v0*tn - 0.5*g*tn**2
    t.append(tn); y.append(yn)
    
for (ti, yi) in zip(t,y):
    print '%8.4f %8.4f' % (ti,yi)