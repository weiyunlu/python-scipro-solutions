"""
Exercise 9.2: Make polynomial subclasses of parabolas
Author: Weiyun Lu
"""

class Line:
    def __init__(self, c0, c1):
        self.c0, self.c1 = c0, c1
        
    def __call__(self, x):
        return self.c0 + self.c1*x
    
    def table(self, L, R, n):
        """Return a table with n points for L <= x <= R."""
        s = ''
        import numpy as np
        for x in np.linspace(L, R, n):
            y = self(x)
            s += '(%12g, %12g)\n' %(x, y)
        return s
        
class Parabola(Line):
    def __init__(self, c0, c1, c2):
        Line.__init__(self, c0, c1)
        self.c2 = c2
        
    def __call__(self, x):
        return Line.__call__(self, x) + self.c2*x**2
        
class Cubic(Parabola):
    def __init__(self, c0, c1, c2, c3):
        Parabola.__init__(self, c0, c1, c2)
        self.c3 = c3
        
    def __call__(self, x):
        return Parabola.__call__(self, x) + self.c3*x**3
        
class Poly4(Cubic):
    def __init__(self, c0, c1, c2, c3, c4):
        Cubic.__init__(self, c0, c1, c2, c3)
        self.c4 = c4
        
    def __call__(self, x):
        return Cubic.__call__(self, x) + self.c4*x**4
        
if __name__ == '__main__':
    f = Poly4(1, 3, 0, -1, 2) #initializes the polynomial 2x^4 - x^3 + 3x + 1
    print 'f is a degree 4 polynomial with coefficients', f.__dict__
    print 'f(2) =', f(2) # 2(2^4) - 2^3 + 3(2) + 1 = 32 - 8 + 6 + 1 = 31
    print 'Here are some points on the graph of f:'
    print f.table(-10, 10, 25)