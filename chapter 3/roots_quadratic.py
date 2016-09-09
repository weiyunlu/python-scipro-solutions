"""
Exercise 3.3: Write a function for solving quadratics
Author: Weiyun Lu
"""

from cmath import sqrt

def roots(a,b,c):
    root1 = (-b + sqrt(b**2 - 4*a*c)) / 2.0*a
    root2 = (-b - sqrt(b**2 - 4*a*c)) / 2.0*a
    return root1, root2

a = 1
b = 0
c = 1

def test_roots_float(a,b,c): #we check if imaginary component is zero; if so, return reals
    (root1, root2) = roots(a,b,c)
    print 'The roots are',
    if root1.imag != 0:
        print root1,; print 'and',; print root2
    else:
        root1 = root1.real; root2 = root2.real
        print root1,; print 'and',; print root2

test_roots_float(a,b,c)