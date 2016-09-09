"""
Exercise 5.50: Apply a function to a rank 2 array
Author: Weiyun Lu
"""

import numpy as np

A = np.array([[0, 2, -1], [-1, -1, 0], [0, 5, 0]])
f = lambda x : x**3 + x*np.exp(x) + 1
A_comp = A**3 + A*np.exp(A) + 1

print 'The array expression A**3 + A*exp(A) + 1 yields\n', A_comp
print 'Hitting A with a function directly yields\n', f(A)