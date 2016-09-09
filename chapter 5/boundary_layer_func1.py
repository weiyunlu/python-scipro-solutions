"""
Exercise 5.49: Experience overflow in a function
Author: Weiyun Lu
"""

import math
import numpy as np
from scitools.std import plot, linspace, vectorize

def v_all(x, mu=1E-6, exp=math.exp):
    x = np.float128(x)
    mu = np.float128(mu)
    num = (1 - exp(float(x)/mu))
    denom = (1 - exp(1.0/mu))
    return num, denom, num / denom
           
def v(x, mu=1E-6, exp=math.exp):
    return v_all(x,mu,exp)[2]     

for x in linspace(0,1,25):
    for f in [math.exp, np.exp]:
        try:
            print v_all(x, 1E-3, f)
        except:
            print('Could not compute an instance of v(x).')
            
#This function is subject to overflow.
#Many more instances succeed with float128 than default float64.

x = linspace(0,1,10000)
v = vectorize(v)

plot(x, v(x, 1.0, np.exp), '-r', x, v(x, 0.01, np.exp), '-b', 
     x, v(x, 0.001, np.exp), '-y', xlabel='x', ylabel='v(x)', 
     legend=(['mu=1', 'mu=0.01', 'mu=0.001']))