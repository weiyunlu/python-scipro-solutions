"""
Author: Weiyun Lu
Exercise 7.1: Make a function class
"""

from math import sin, exp

class F:
    def __init__(self,a,w):
        self.a = a
        self.w = w
    def value(self,x):
        a = self.a
        w = self.w
        return exp(-a*x) * sin(w*x)