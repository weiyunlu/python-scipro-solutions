"""
Exercise 5.3: Fill arrays; vectorized (plot)
Author: Weiyun Lu
"""

from scitools.std import sqrt, pi, exp, linspace, plot

h = lambda x : (1/(sqrt(2*pi))) * exp(-0.5*x**2)
xlist = linspace(-4,4,41)
hlist = h(xlist)
pairs = zip(xlist,hlist)

plot(xlist, hlist, axis=[xlist[0], xlist[-1], 0, 0.5], xlabel='x', \
    ylabel='h(x)', title='Standard Gaussian')