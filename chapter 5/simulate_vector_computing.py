"""
Exercise 5.6: Simulate by hand a vectorized expression
Author: Weiyun Lu
"""

from scitools.std import array, sin, cos, exp, zeros

x = array([0,2])
t = array([1,1.5])
y = zeros((2,2))
f = lambda x, t : cos(sin(x)) + exp(1.0/t)

for i in range(2):
    for j in range(2):
        y[i][j] = f(x[i],t[j])

print y