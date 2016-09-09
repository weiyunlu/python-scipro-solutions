"""
Exercise 5.26: Plot a wave packet
Author: Weiyun Lu
"""

from scitools.std import exp, sin, pi, linspace, plot

f = lambda x, t : exp(-(x-3*t)**2) * sin(3*pi*(x-t))

xp = linspace(-4,4,100)
yp = f(xp, 0)

plot(xp, yp , '-b', title='A wave localized in space')