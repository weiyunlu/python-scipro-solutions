"""
Exercise 3.1: Write a Fahrenheit-Celcius conversion function
Author: Weiyun Lu
"""

def C(F):
    return (5.0/9) * (F - 32)
    
def F(C):
    return (9.0/5) * C + 32
    
x = 100
print '%.4f degrees Fahrenheit equals %.4f degrees Celcius.' %(x, C(x))

eps = 1.0E-16

if abs (x - C(F(x))) < eps:
    print 'The inverse test to see that this function is correct has succeeded.'
else:
    print 'The inverse test to see that this function is correct did not succeed.'