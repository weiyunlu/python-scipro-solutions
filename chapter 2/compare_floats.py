"""
Exercise 2.20: Compare two real numbers with a tolerance
Author: Weiyun Lu
"""

a = 1/947.0 * 947
b = 1
tol = 1.0e-16
if abs(a - b) < tol:
    print 'Wrong result!'
else:
    print 'A-okay!'