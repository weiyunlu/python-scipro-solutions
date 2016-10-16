"""
Exercise 8.17: Throw dice and compute a small probability
Author: Weiyun Lu
"""

import numpy as np

def rollsevensixes_prob(n):
    rolls = np.random.randint(1, 7, size = (n, 7)) #array of n arrays of 6 rolls
    sixes = np.sum(rolls == 6, axis = 1) #counts instances of value being six within each subarray
    seven_sixes = np.sum(sixes == 7) #counts how many of the trials had all seven rolls as 6
    return seven_sixes/float(n)
    
N = 100000000
prob = rollsevensixes_prob(N)

print('We estimate the probability of getting all sixes when rolling 7 dice at a time.  With a simulation\
 of %d trials, the chance appears to be around %g.') %(N, prob)