"""
Exercise 5.31: Animate a wave packet
Author: Weiyun Lu
"""

from scitools.std import exp, sin, pi, linspace, plot, movie
import time
import glob
import os

f = lambda x, t : exp(-(x-3*t)**2) * sin(3*pi*(x-t))
fps = float(1/6)

xp = linspace(-6, 6, 1001)
tp = linspace(-1,1,61)
counter = 0

for name in glob.glob('pix/plot_wave*.png'):
    os.remove(name)

for t in tp:
    yp = f(xp, t)
    plot(xp, yp, '-b', axis=[xp[0], xp[-1], -1.5, 1.5], legend='t=%4.2f' % t,\
        title='Evolution of wave over time', savefig='pix/plot_wave%04d.png' \
        % counter)
    counter += 1
    time.sleep(fps)
    
#movie('pix/plot_wave*.png')