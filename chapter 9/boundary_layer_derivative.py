"""
Exercise 9.8: Explore the accuracy of difference formulas
Author: Weiyun Lu
"""

from Diff2 import *
from numpy import exp

class v:
    def __init__(self, mu):
        self.mu = float(mu)
    
    def __call__(self, x):
        mu = self.mu
        return (1 - exp(x/mu)) / (1 - exp(1/mu))
        
methods = [Backward1, Forward1, Forward3, Central2, Central4, Central6]
x_vals = [0.0, 0.9]
mu_vals = [1.0, 0.01]

def dvdx_exact(mu, x):
    return exp(x/mu) / (mu*(exp(1/mu)-1))

def table(f, x_values, mu_values, methods, dfdx=dvdx_exact):
    print '%-10s %-10s' %('mu', 'x'),
    for method in methods:
        print '%-15s' % method.__name__,
    print  # newline
    for mu in mu_values:
        v = f(mu) #creates an instance of the v function with fixed mu
        for x in x_values:    
            print '%-10f %-10f' %(mu, x),
            for method in methods:
                 d = method(v, h=1E-5, dfdx_exact=dvdx_exact)
                 output = abs(d(x) - d.exact(mu, x))
                 print '%12.8E' % output,
        print  # newline

print 'Comparing numerical derivative errors for v(x,mu) = (1 - exp(x/mu)) / (1 - exp(1/mu))'
table(v, x_vals, mu_vals, methods)