"""
Exercise 9.6: Make a super- and subclass for a point
Author: Weiyun Lu
"""

from numpy import sin, cos, pi

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
        
    def __str__(self):
        return '(%g,%g)' %(self.x, self.y)
        
class PolarPoint(Point):
    def __init__(self, r, theta):
        self.r, self.theta = r, theta
        Point.__init__(self, r*cos(theta), r*sin(theta))

if __name__ == '__main__':        
    a = PolarPoint(2, pi/4)
    print 'The point 2e^(i*pi/4) is at', a