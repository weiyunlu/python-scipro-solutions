"""
Exercise 9.14: Add a new class in a class hierarchy
Author: Weiyun Lu
"""

from integrate import Integrator
import random
import numpy as np

class MonteCarlo(Integrator):
    def construct_method(self):
        a, b, n = self.a, self.b, self.n
        x = np.zeros(n)
        for i in xrange(n):
            x[i] = random.uniform(a, b)
        w = np.zeros(n) + (b-a)*(1/float(n))
        return x, w
        
if __name__ == '__main__':
    n = 100
    a = 0
    b = 10
    f = lambda x : x**2 + np.exp(x) + np.sin(np.pi*x)
    print 'Let f(x) = x^2 + exp(x) + sin(pi*x).  Its definite integral over [0,10] is roughly 22358.799.'
    print 'We test the MonteCarlo integrator 100 times (sampling 100 random points each time):'
    answers = []
    for i in xrange(100):
        Int = MonteCarlo(a,b,n)
        print Int.integrate(f)
        answers.append(Int.integrate(f))
    average = sum(x for x in answers)/float(n)
    error = abs(average - 22358.7991281401)
    print 'The average was %g.' %average
    print 'The error between the average and the true value is %g.' %error