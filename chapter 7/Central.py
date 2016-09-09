"""
Author: Weiyun Lu
Exercise 7.16: Implement a class for numerical differentiation
"""

from numpy import *
from scitools.std import StringFunction

class Central: #numerical differention - centered formula
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)
        
    def __call__(self,x):
        f, h = self.f, self.h
        return (f(x+h) - f(x-h)) / (2*h)
        
def table(f, X, h=1E-5): #supply the function as a string
    x = sympy.Symbol('x')
    df_expr = sympy.diff(f)
    df_true = sympy.lambdify([x], df_expr)
    f_func = StringFunction(f)
    df_appr = Central(f_func)
    print '%18s %18s %18s %18s' %('x', 'df(x) approx', 'df(x) actual', 'error')
    print '-'*75
    for x in X:
        er = abs(df_appr(x)-df_true(x))
        print '%18.14f %18.14f %18.14f %18.14f' %(x, df_appr(x), df_true(x), er)
        
#This approximate differentiation is exact on quadratics, so we test.
        
def test_Central():
    f = Central(lambda x : x**2 + 3*x - 5)
    x = 5
    ans = 13
    msg = 'The central approximation was not implemented properly.'
    eps = 1E-8
    success = abs(f(x) - ans) < eps
    assert success, msg

if __name__ == '__main__':
    test_Central()
    
    def f(x):
        return 0.25*x**4
        
    df = Central(f)
    x = 2
    print 'df(%g)=%g' %(x, df(x))
    print 'exact:', x**3
    
    X = linspace(-pi, pi, 25)
    table('sin(x)*cos(x) + log(x**2)', X)
    