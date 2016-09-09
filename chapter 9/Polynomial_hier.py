"""
Exercise 9.4: Create an alternative class hierarchy for polynomials
Author: Weiyun Lu
"""

import numpy
from Polynomial import Polynomial

class Parabola(Polynomial):
    def __init__(self, c0, c1, c2):
        Polynomial.__init__(self, [c0, c1, c2])

class Line(Parabola):
    def __init__(self, c0, c1):
        Parabola.__init__(self, c0, c1, 0)
        
if __name__ == '__main__':
    f = Parabola(1, 2, 3) #fx = 3x^2 + 2x + 1
    g = Line (3, 4) #gx = 4x + 3
    m = f + g
    print 'f =', f.coeff
    print 'g =', g.coeff
    print 'f+g =', m.coeff #(f+g)x = 3x^2 + 6x + 4