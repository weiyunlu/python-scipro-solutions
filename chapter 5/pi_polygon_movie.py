"""
Exercise 5.35: Animate a sequence of approximations to pi
Author: Weiyun Lu
"""

from numpy import sqrt, pi, sin, cos
import matplotlib.pyplot as plt
import glob
import os

def pathlength(x,y):
    L = 0
    success = len(x)==len(y)
    msg = 'The length of x and y coordinates must be the same!'
    assert success, msg
    for i in range(len(x)-1):
        d = sqrt((x[i+1]-x[i])**2 + (y[i+1]-y[i])**2)
        L += d
    return L

def points_circle(n):
    x=[]; y=[] #initialize empty lists
    for i in range(0,n+1):
        x.append(0.5 * cos((2*pi*i)/n))
        y.append(0.5 * sin((2*pi*i)/n))
    return x, y

def pi_approx(n):
    return pathlength(points_circle(n)[0],points_circle(n)[1])
    
for name in glob.glob('pix/pi_poly*.png'):
    os.remove(name)
    
plt.ion() #draw the first plot
plt.axis([-1.2, 1.2, -1.2, 1.2])
x = points_circle(4)[0]
y = points_circle(4)[1]
lines = plt.plot(x,y)

counter = 0
for s in range(4,100):
    x = points_circle(s)[0]
    y = points_circle(s)[1]
    lines[0].set_xdata(x)
    lines[0].set_ydata(y)
    plt.title('Polygonal approximation to pi')
    plt.legend(['Approximation with k=%d\nApprox pi value = %.10f\nError = %.10f.'\
        %(s, pi_approx(s), abs(pi - pi_approx(s)))])
    plt.draw()
    plt.savefig('pix/pi_poly%4d.png' % counter)
    counter += 1