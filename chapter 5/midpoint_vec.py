"""
Exercise 5.22: Vectorize the midpoint rule for integration
Author: Weiyun Lu
"""

from scitools.std import array
import numpy as np

def midpointint(f,a,b,n):
    h = float(b - a) / n
    s = 0
    for i in range(1,n+1):
        s += f(a - 0.5*h + i * h)
    s *= h
    return s

def midpointsum_py(f,a,b,n):
    h = float(b - a) / n
    x = array([f(a-0.5*h + i * h) for i in range(1,n+1)])
    s = h * sum(x[i] for i in range(len(x)))
    return s
    
def midpointsum_num(f,a,b,n):
    h = float(b - a) / n
    x = array([f(a-0.5*h + i * h) for i in range(1,n+1)])
    s = h * np.sum(x[i] for i in range(len(x)))
    return s

# %timeit results with f(x)=x^2, 0, 10, 100
# midpointint: 10000 loops, best of 3: 125 microseconds per loop
# midpointsum_py: 10000 loops, best of 3: 185 microseconds per loop
# midpointsum_num: 10000 loops, best of 3: 179 microseconds per loop