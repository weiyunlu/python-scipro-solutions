"""
Exercise 8.15: Vectorize flipping a coin
Author: Weiyun Lu
"""

import numpy as np

def flip_coin(n):
    trials = np.random.randint(0, 2, n)
    heads = np.sum(trials)
    return heads

N = 100000
headcount = flip_coin(N)

print("We flipped a coin %d times and got %d heads.") %(N, headcount)