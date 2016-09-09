"""
Exercise 5.25: Investigate the behaviour of Langrange's interpolating polynomials
Author: Weiyun Lu
"""

import Lagrange_poly2
from scitools.std import hold, figure

figure()
for n in [2,4,6,10]:
    Lagrange_poly2.graph(abs, n, -2, 2)
    hold('on')   
hold('off')

figure()
for n in [13,20]:
    Lagrange_poly2.graph(abs, n, -2, 2)
    hold('on')
hold('off')