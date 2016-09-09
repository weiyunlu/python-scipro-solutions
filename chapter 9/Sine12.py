"""
Exercise 9.9: Implement a subclass (functions with 1st and 2nd order derivatives)
Author: Weiyun Lu
"""

from numpy import sin, cos, pi, linspace

class FuncWithDerivatives:
    def __init__(self, h=1.0E-5):
        self.h = h
        
    def __call__(self, x):
        raise NotImplementedError\
        ('__call__ missing in class %s' %self.__class__.__name__)
        
    def df(self, x):
        h = self.h
        return (self(x+h) - self(x-h)) / (2.0*h)
    
    def ddf(self, x):
        h = self.h
        return (self(x+h) - 2*self(x) + self(x-h)) / (float(h)**2)
        
class Sine1(FuncWithDerivatives):
    def __init__(self, h=1.0E-5):
        self.h = h
        
    def __call__(self, x):
        return sin(x)
        
class Sine2(FuncWithDerivatives):
    def __init__(self, h=1.0E-5):
        self.h = h
        
    def __call__(self, x):
        return sin(x)
        
    def df(self, x):
        return cos(x)
        
    def ddf(self, x):
        return -sin(x)
        
sine1 = Sine1()
sine2 = Sine2()
        
print 'Comparing numerical approximation of the derivatives of sin with the analytical derivative.'
X = linspace(-pi, pi, 20)
print '%18s %18s %18s %18s %18s' %('x', 'Approx. dsin(x)', 'Analt. dsin(x)', 'Approx. d2sin(x)',\
    'Analt. d2sin(x)')
print '-'*95
for x in X:
    print '%18g %18g %18g %18g %18g' %(x, sine1.df(x), sine2.df(x), sine1.ddf(x), sine2.ddf(x)) 