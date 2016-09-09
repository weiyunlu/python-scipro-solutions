"""
Exercise 9.3: Implement a class for a function as a subclass
Author: Weiyun Lu
"""

from Cubic_Poly4 import Line, Parabola
from numpy import sin, linspace

class sinquad(Parabola): #class for functions of the form f(x) = Asin(wx) + ax^2 + bx + c
    def __init__(self, A, w, a, b, c):
        Parabola.__init__(self, c, b, a)
        self.A, self.w = A, w
        
    def __call__(self, x):
        return Parabola.__call__(self, x) + self.A*sin(self.w*x)
        
    def table(self, L, R, n):
        """Return a table with n points for L <= x <= R."""
        s = ''
        for x in linspace(L, R, n):
            y = self(x)
            s += '(%12g, %12g)\n' %(x, y)
        return s
        
if __name__ == '__main__':
    from numpy import pi
    f = sinquad(0.5, pi, 1, 2, 3) #f(x) = 0.5*sin(pi*x) + x^2 + 2x + 3
    print 'f is a function of form Asin(wx) + (c2)x^2 + (c1)x + c0 with', f.__dict__
    print 'f(2) =', f(0.5) #f(0.5) = 0.5*sin(0.5*pi) + 0.5^2 + 2(0.5) + 3 = 4.75
    print 'Here are some points on the graph of f:'
    print f.table(-10, 10, 25)