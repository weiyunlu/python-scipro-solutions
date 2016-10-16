"""
Exercise 8.2: Compute a probability
Author: Weiyun Lu
"""

import random

def select_count(N):
    M = 0
    for i in range(N):
        r = random.random()
        if 0.5 <= r <= 0.6:
            M += 1
    return M/float(N)
    
i_vals = [1, 2, 3, 6]

print 'We compute the empirical probability that a randomly chosen number in [0,1] lies in [0.5,0.6].'
print '%15s %15s' %('No. of simulations', 'Observed ratio')
print '-'*30

for i in i_vals:
    N = 10**i
    prob = select_count(N)
    print '%15g %15g' %(N, prob)