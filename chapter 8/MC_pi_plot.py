"""
Exercise 8.29: Compute pi by a random sum
Author: Weiyun Lu
"""

import numpy as np
import matplotlib.pyplot as plt

N = 1000000
x_values = np.random.uniform(0, 1, N)
f = lambda x : np.sqrt(1 - x**2)

def randomsum(n):
    x_values_n = x_values[:n]
    return (4 / float(n+1)) * np.sum(f(x_values_n))

N_values = range(0, N+1, 1000)
SN_values = []
constant_pi = [np.pi] * 1001

for n in N_values:
    SN_value = randomsum(n)
    SN_values.append(SN_value)
    
SN_values = np.array(SN_values)
    
plt.title('Evolution of estimate of pi by random sum')
plt.xlabel('Number of summands')
plt.ylabel('Monte Carlo approximation to pi')
plt.plot(N_values, SN_values)
plt.plot(N_values, constant_pi)
plt.legend(['Approximation', 'Actual value'])
plt.axis([0, 1000000, 3.13, 3.15])