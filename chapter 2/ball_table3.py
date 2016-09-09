"""
Exercise 2.16: Store data in a nested list
Author: Weiyun Lu
"""

g = 9.81 #acceleration due to gravity
v0 = 1.0 #initial velocity
a = 0.0 #start point
b = (2*v0)/g #end point
n = 10 #number of subintervals
l = (b-a)/n #length of a subinterval
t = []; y = []

print '%8s %8s' % ('t', 'y(t)')

for i in range(0,n+1):
    tn = a + i*l
    yn = v0*tn - 0.5*g*tn**2
    t.append(tn); y.append(yn)

ty1 = [t, y]
    
for i in range(len(t)):
    print '%8.4f %8.4f' % (ty1[0][i], ty1[1][i])

print '\n'    
    
ty2 = [[tee, why] for (tee, why) in zip(t,y)]

for i in range (len(t)):
    print '%8.4f %8.4f' % (ty2[i][0], ty2[i][1])