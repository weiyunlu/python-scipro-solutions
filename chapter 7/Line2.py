"""
Author: Weiyun Lu
Exercise 7.7: Flexible handling of function arguments (for straight line class)
"""

class Line:
    def __init__(self,p1,p2):
        if isinstance(p1, (tuple,list)) and isinstance(p2, (tuple,list)): #input two points
            x0 = p1[0]
            y0 = p1[1]
            x1 = p2[0]
            y1 = p2[1]
            self.a = (y1 - y0) / float(x1 - x0)
            self.b = y0 - self.a*x0
        elif isinstance(p1, (tuple,list)) and isinstance(p2, (float,int)):
            self.a = p2
            self.b = p1[1] - p2*p1[0]
        elif isinstance(p1, (float,int)) and isinstance(p2, (float,int)): #input slope & y-int
            self.a = p1
            self.b = p2
        else:
            raise TypeError('You must supply two values to create an instance\
                of Line.  The valid input options are: two points, point + \
                slope, or slope + y-intercept.')
        
    def value(self,x):
        a = self.a
        b = self.b
        y = a*x + b
        return y
        
#test with the line y = 2x + 3 with all three input methods
#value(1) should equal 5
        
def test():
    ans = 5
    l1 = Line((-1,1),(1,5))
    l2 = Line([-1,1],2)
    l3 = Line(2,3)
    ans1 = l1.value(1)
    ans2 = l2.value(1)
    ans3 = l3.value(1)
    eps = 10e-12
    if abs(ans - ans1) > eps:
        print('Uh-oh, entering two points does not work correctly.')
    if abs(ans - ans2) > eps:
        print('Uh-oh, entering in point-slope form does not work correctly.')
    if abs(ans - ans3) > eps:
        print('Uh-oh, entering in slope & y-intercept form does not work correctly.')
    
if __name__ == '__main__':
    test()