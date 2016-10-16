"""
Exercise 8.30: 1D random walk with drift
Author: Weiyun Lu
"""

import random
import numpy
import sys

if len(sys.argv) >= 2:
    np = sys.argv[1]            # no of particles read from the command line
else:
    np = 1000                   #default to 1000 particles

ns = 100                        # no of steps

def walk(r):                        #do a random walk with proability r of going right, 1-r of going left
    positions = numpy.zeros(np)     # all particles start at x=0
    for step in range(ns):
        for p in range(np):
            direction = random.uniform(0,1)
            if direction <= r:
                positions[p] += 1   # one unit length to the right
            else:
                positions[p] -= 1   # one unit length to the left
    return positions
    
def theoretical_convergence(r):
    return r*ns - (1-r)*ns
    
r_values = numpy.linspace(0,1,101)

print '-' * 90
print 'Theoretical and simulated random walk with 100 steps, %d particles and probability r.' %(np)
print '-' * 90
print '%10s %35s %35s' %('r', 'Simulated average position', 'Theoretical convergence position')
for r in r_values:
    average_position = numpy.sum(walk(r))/float(np)
    theoretical_position = theoretical_convergence(r)
    print '%10f, %35f %35f' %(r, average_position, theoretical_position)
print '-' * 90