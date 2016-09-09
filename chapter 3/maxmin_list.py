"""
Exercise 3.22: Find the max and min elements in a list
Author: Weiyun Lu
"""

from math import pi, e

def maxi(a):
    max_elem = a[0] #initialize the max element variable
    for i in range(len(a)):
        if a[i] > max_elem:
            max_elem=a[i]
    return max_elem
    
def mini(a):
    min_elem = a[0] #initialize the max element variable
    for i in range(len(a)):
        if a[i] < min_elem:
            min_elem=a[i]
    return min_elem
    
A = [1, 4, 87, 999, 12, -43, 72, 32, 124123, -444, 0, 0, -4, -909, 71, 17.4, pi]

print 'Consider the list', A, '.'
print 'The max element is %f and the min element is %f.' %(maxi(A), mini(A))