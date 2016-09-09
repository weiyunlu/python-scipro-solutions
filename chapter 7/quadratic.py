"""
Author: Weiyun Lu
Exercise 7.5: Make a class for quadratic functions
"""

from numpy import linspace, sqrt

class quadratic:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def value(self,x):
        return self.a * x**2 + self.b * x + self.c
    
    def table(self,L,R,n):
        X = linspace(L,R,n)
        print '%15s %15s' %('x', 'f(x)')
        print '-'*34
        for x in X:
            print '%15.8f %15.8f' %(x, self.value(x))
    
    def roots(self):
        a = self.a
        b = self.b
        c = self.c
        x1 = (-b + sqrt(b**2 - 4*a*c)) / float(2*a)
        x2 = (-b - sqrt(b**2 - 4*a*c)) / float(2*a)
        return x1, x2
    
    def __str__(self):
        return '%fx^2 + %fx + %f' %(self.a, self.b, self.c)