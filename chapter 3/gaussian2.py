"""
Exercise 3.16: Implement a Gaussian function
Author: Weiyun Lu
"""

from math import exp, pi, sqrt

gauss = lambda x, m=0, s=1 : (1.0/(sqrt(2*pi)*s)) * exp(-0.5*(float(x-m)/s)**2)

def table(m,s,n):
    h = float((m+5*s) - (m-5*s)) / (n-1) #sizes of subintervals
    print '''The following table gives values of gaussians with mean %.2f and
    standard deviation %.2f. \n''' %(m,s)
    print '%10s %10s' %('x', 'f(x)')
    print '-------------------------------'
    i = 0 #initialize counter
    while i < n:
        x = (m - 5*s) + i*h
        fx = gauss(x,m,s)
        print '%10.6f %10.6f' %(x, fx)
        i+=1
        
table(0,1,9)