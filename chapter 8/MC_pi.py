"""
Exercise 8.27: Compute pi by a Monte Carlo method
Author: Weiyun Lu
"""

import random
from math import pi

N = 100000
points_inside = 0

for i in range(N):
    x, y = random.uniform(-1, 1), random.uniform(-1, 1)
    inside_circle = x**2 + y**2 < 1
    points_inside += inside_circle

points_inside_ratio = points_inside / float(N)    
rectangle_area = 4
pi_estimate = float(points_inside_ratio) * rectangle_area
error = abs(pi - pi_estimate)

print('We approximate pi by throwing %d random darts the rectangle [-1,1] x [-1,1]).  The area of the\
 unit circle is pi; the ratio of darts inside the circle times the rectangle area should be\
 approximately pi.  Our simulation calculation estimates pi to be %g, which has an error of %g.')\
 %(N, pi_estimate, error)