"""
Exercise 1.17: Find errors in the coding of a formula
Author: Weiyun Lu
"""

a = 2; b = 1; c = 2
from cmath import sqrt
q = b*b - 4*a*c
q_sr = sqrt(q)
x1 = (-1*b + q_sr)/2*a
x2 = (-1*b - q_sr)/2*a
print x1, x2