"""
Exercise 8.1: Flip a coin N times
Author: Weiyun Lu
"""

import random

N = eval(raw_input('How many times do you want to flip a coin?'))

heads = 0
tails = 0

for i in xrange(N):
    r = random.randint(0,1)
    if r == 0:
        print 'heads'
        heads += 1
    else:
        print 'tails'
        tails +=1

print('We flipped a coin %d times, got %d heads and %d tails') %(N, heads, tails)