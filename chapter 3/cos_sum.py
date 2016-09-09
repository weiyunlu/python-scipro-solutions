"""
Exercise 3.31: Make a table for approximations of cos x
Author: Weiyun Lu
"""

from math import cos, pi

def C(x,n):
    j = 1 #initialize counter; let's start adding at c_1
    c = 1 #initialize c_0 at j=0
    s = 1 #initialize the sum at c_0 = 1
    for j in range(1,n+1):
        c = -c * ( x**2 / float((2*j) * (2*j - 1)) )
        s += c
    return s

X0 = [4*pi, 6*pi, 8*pi, 10*pi]
N0 = [5,25,50,100,200]

def Errors(X,N):
    print '%10s' %('x'), #print "x" and then row of n values
    for n in N:
        print '%10d' %(n),
    print '\n'
    for x in X:
        print '%10.4f' %x, #print x value in first column
        for n in N:
            error = abs(cos(x) - C(x,n)) #compute and print the error
            print '%10.2e' %error,
        print '\n' #line break after each row
        
Errors(X0,N0)