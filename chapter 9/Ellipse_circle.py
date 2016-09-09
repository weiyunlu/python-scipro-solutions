"""
Exercise 9.5: Make circle a subclass of an ellipse
Author: Weiyun Lu
"""

from numpy import pi, sqrt

class Ellipse:
    def __init__(self, x0, y0, a, b):
        self.x0, self.y0, self.a, self.b = x0, y0, a, b
        
    def area(self):
        return pi*self.a*self.b
        
    def circumference(self):
        a, b = self.a, self.b
        return pi * (3*(a+b) - sqrt((3*a+b)*(a+3*b)))
        
    def __str__(self):
        return 'An ellipse with x-radius %g and y-radius %g at (%g,%g) has area %g and circumference %g.'\
        %(self.a, self.b, self.x0, self.y0, self.area(), self.circumference())
        
class Circle(Ellipse):
    def __init__(self, x0, y0, R):
        Ellipse.__init__(self, x0, y0, R, R)
        
    def __str__(self):
        return 'A circle with radius %g at (%g,%g) has area %g and circumference %g.'\
        %(self.a, self.x0, self.y0, self.area(), self.circumference())
        
if __name__ == '__main__':
    a = 3
    b = 4
    E = Ellipse(0, 0, 3, 4)
    print E
    R = 1
    C = Circle(0, 0, R)
    print C