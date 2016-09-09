"""
Exercise 5.23: Implement Lagrange's interpolation formula
Author: Weiyun Lu
"""

from scitools.std import linspace, sin, pi

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
            count +=1
    if count == 0:
        print 'Success!  The Lagrange interpolation polynomial indeed passes',\
        'through all the points (xp,yp).'
    else:
        print 'Oh no!  There were %d points where the interpolation polynomial'\
        %(count), 'fails to pass through (xp,yp).' 

if __name__ == '__main__':
    Xp = linspace(0, pi, 5)
    Yp = sin(Xp)
    test_p_L(Xp, Yp)
    x = Xp[2]-Xp[1]/2.0
    y = sin(x)
    y_inter = p_L(x, Xp, Yp)
    print 'Take the point between Xp[1] and Xp[2].  Evaluating the sin function',\
    'directly yields %.6f, whilst the interpolated value is %.6f.' %(y, y_inter)