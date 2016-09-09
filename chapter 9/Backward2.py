"""
Exercise 9.11: Implement a new subclass for differentiation
Author: Weiyun Lu
"""

from Diff import Diff, Backward1
from numpy import exp

class Backward2(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x-2*h) - 4*f(x-h) + 3*f(x)) / (2*h)
        
def table(g, dgdt_exact, g_string):
    print 'Comparing errors in Backward1 with Backward2 derivative approximation for g(x) = %s' %(g_string)
    print '%15s %15s %15s %15s %15s' %('h', 'Back1 value', 'Back2 value', 'Back1 error', 'Back2 error')
    for k in range(0, 15):
        h0 = 2^(-k)
        b1_g = Backward1(g, h=h0)
        b2_g = Backward2(g, h=h0)
        error1 = abs(dgdt_exact(0) - b1_g(0))
        error2 = abs(dgdt_exact(0) - b2_g(0))
        print '%15s %15g %15g %15g %15g' %('2^(-%d)' %k, b1_g(0), b2_g(0), error1, error2)
        
g = lambda t : exp(-t)
dgdt_exact = lambda t : -exp(-t)
table(g, dgdt_exact, 'exp(-x)')

print

f = lambda t : 3*t**2 + 5*t
dfdt_exact = lambda t : 6*t + 5
table(f, dfdt_exact, '3x^2 + 5x')