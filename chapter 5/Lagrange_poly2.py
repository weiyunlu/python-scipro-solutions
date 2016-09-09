"""
Exercise 5.24: Plot Lagrange's interpolating polynomial
Author: Weiyun Lu
"""

from scitools.std import linspace, sin, pi, plot, array

def L_k(x, k, xp, yp):
    s = 1 #initialize product
    i = 0 #initialize counter
    n = len(xp) - 1
    while i <= n:
        if i != k:
            s *= float(x - xp[i]) / (xp[k] - xp[i])
        i += 1
    return s

def p_L(x, xp, yp):
    s = 0 #initialize sum
    n = len(xp) - 1
    for k in range(n+1):
        s += yp[k] * L_k(x,k,xp,yp)
    return s
    
def test_p_L(xp, yp):
    n = len(xp) - 1
    eps = 10e-12
    count = 0 #count how many answers are not close enough
    for k in range(n+1):
        if abs(p_L(xp[k],xp,yp) - yp[k]) > eps:
            count += 1
    if count == 0:
        print 'Success!  The Lagrange interpolation polynomial indeed passes',\
        'through all the points (xp,yp).'
    else:
        print 'Oh no!  There were %d points where the interpolation polynomial'\
        %(count), 'fails to pass through (xp,yp).'

def graph(f, n, xmin, xmax, resolution=1001):
    Xp = linspace(xmin, xmax, n)
    Yp = f(Xp)
    Xr = linspace(xmin, xmax, resolution) #array of values to plot
    Yr = array([p_L(x,Xp,Yp) for x in Xr]) #get interpolation points
    plot(Xr, Yr, '-r', Xp, Yp, 'bo', title='Lagrange Interpolation')

if __name__ == '__main__':
    XP = linspace(0, pi, 5)
    YP = sin(XP)
    test_p_L(XP, YP)
    graph(sin, 5, 0, pi)