"""
Exercise 2.19: Explore what zero can be on a computer
Author: Weiyun Lu
"""

eps = 1.0
while 1.0 != 1.0 + eps:
    print '..................', eps
    eps = eps/2.0
print 'final eps:', eps