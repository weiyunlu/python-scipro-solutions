"""
Exercise 3.23: Implement the Heaviside function
Author: Weiyun Lu
"""

def H(x):
    if x < 0:
        return 0
    elif x >= 0:
        return 1

testvalues = [-10, -1e-15, 0, 1e-15, 10]

for x in testvalues:
    print 'H of', x, 'is', H(x), '.'
