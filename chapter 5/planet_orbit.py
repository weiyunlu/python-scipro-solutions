"""
Exercise 5.36: Animate a planet's orbit
Author: Weiyun Lu
"""

from scitools.std import pi, sin, cos, sqrt, plot, array, show
import glob
import os

for name in glob.glob('pix/planet*.png'):
    os.remove(name)

n = 100 #we want 100 frames
a = 1 #set parameters for the orbit
b = 1
w = 1
delta_t = (2*pi)/(w*n)
counter = 0
X = []
Y = []

for k in range(n+1):
    tk = k * delta_t #each time through we need to add a new k value
    x = a * cos(w*tk)
    y = b * sin(w*tk)
    X.append(x)
    Y.append(y)
    XP = array(X)
    YP = array(Y)
    XF = array([x])
    YF = array([y])
    velo = w * sqrt(a**2 * sin(w*tk)**2 + b**2 * cos(w*tk)**2)
    plot(XP, YP, '-r', XF, YF, 'bo', axis=[-1.2, 1.2, -1.2, 1.2],
         title='Planetary orbit', legend=(['Instaneous velocity=%6f' % velo,
         'present location']), savefig='pix/planet%4d.png' % counter)
    counter += 1
    show()