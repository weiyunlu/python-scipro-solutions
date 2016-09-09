"""
Author: Weiyun Lu
Exercise 7.6: Make a class for straight lines
"""

class Line:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        
    def value(self,x):
        x0 = self.p1[0]
        y0 = self.p1[1]
        x1 = self.p2[0]
        y1 = self.p2[1]
        a = (y1 - y0) / float(x1 - x0)
        b = y0 - a*x0
        y = a*x + b
        return y