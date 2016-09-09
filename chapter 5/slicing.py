"""
Exercise 5.7: Demonstrate array slicing
Author: Weiyun Lu
"""

from scitools.std import linspace

w = linspace(0,3,31)
print w

print w[:] #should just be the whole thing
print w[:-2] #up to but not including 2nd last, so should be up to 2.8
print w[::5] #every fifth element starting with 0
print w[2:-2:6] #start with 0.2 and up to 2.8; every 6th element